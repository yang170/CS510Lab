import requests
from rank_bm25 import BM25Okapi, BM25Plus, BM25L
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import BertModel, BertTokenizer
from tqdm import tqdm
from zmq import device
from models.utils import load_config, load_dataset
from nltk import word_tokenize
from nltk.text import sent_tokenize
import numpy as np
import torch


# disable warnings related to verify
requests.urllib3.disable_warnings()

# Load config file
opt = load_config()

# Load dataset
print('Loading dataset')
dataset = load_dataset(opt)

# Generate target sentence
print('Collect target passage')
with open('target.txt', 'w', encoding='utf8') as f_out:
    f_out.write('\n'.join([data['topic_text'] for data in dataset]))

if opt.model_type == 'bert':
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    bert = BertModel.from_pretrained('bert-base-uncased')
    bert.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    bert.to(device)

# Apply model to each data sample
print('Collecting passage')
results = []
for i, data in enumerate(tqdm(dataset)):
    if opt.model_type.startswith('bm25'):
        tokenized_corpus = [word_tokenize(doc.lower()) for doc in data['docs']]
        if opt.model_type == 'bm25okapi':
            bm25 = BM25Okapi(tokenized_corpus)
        elif opt.model_type == 'bm25plus':
            bm25 = BM25Plus(tokenized_corpus)
        elif opt.model_type == 'bm25l':
            bm25 = BM25L(tokenized_corpus)
        else:
            raise NotImplementedError
        
        query_text = word_tokenize(data['topic_text'].lower() if opt.query == 'title' else data['topic_content'])
        query_scores = bm25.get_scores(query_text)
        results.append(data['docs'][query_scores.argmax()])

    elif opt.model_type == 'tfidf':
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(data['docs']).toarray()
        query_matrix = vectorizer.transform([data['topic_text'], data['topic_content']]).toarray()
        scores:np.ndarray = np.matmul(query_matrix, X.T)
        best_idx = scores.argmax(axis=1)
        results.append(data['docs'][best_idx[0 if opt.query == 'title' else 1]])
    
    elif opt.model_type == 'bert':
        with torch.no_grad():
            doc_tokens = tokenizer.batch_encode_plus(data['docs'], padding=True, return_tensors='pt').to(device)
            cls_embs = bert(**doc_tokens)['last_hidden_state'][:, 0, :]
            if opt.query == 'title':
                topic_text = data['topic_text']
                doc_tokens = tokenizer.encode(topic_text, padding=True, return_tensors='pt').to(device)
                query_embs = bert(doc_tokens)['last_hidden_state'][:, 0, :]
            else:
                topic_text = sent_tokenize(data['topic_content'].replace('---', '.').replace('# ', ''))
                doc_tokens = tokenizer.batch_encode_plus(topic_text, padding='longest', return_tensors='pt', truncation='longest_first').to(device)
                query_embs = bert(**doc_tokens)['last_hidden_state'][:, 0, :]
            query_scores = torch.matmul(cls_embs, query_embs.T).sum(dim=1).cpu().numpy()
        results.append(data['docs'][query_scores.argmax()])

with open(opt.output_file, 'w', encoding='utf8') as f_out:
    f_out.write('\n'.join(results))