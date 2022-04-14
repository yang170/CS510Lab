import requests
from rank_bm25 import BM25Okapi, BM25Plus, BM25L
from sklearn.feature_extraction.text import TfidfVectorizer
from tqdm import tqdm
from models.utils import load_config, load_dataset
from nltk import word_tokenize
import numpy as np


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
        title_as_query_scores = bm25.get_scores(word_tokenize(data['topic_text'].lower()))
        article_as_query_scores = bm25.get_scores(word_tokenize(data['topic_content']))
        results.append(data['docs'][title_as_query_scores.argmax()])

    elif opt.model_type == 'tfidf':
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(data['docs']).toarray()
        query_matrix = vectorizer.transform([data['topic_text'], data['topic_content']]).toarray()
        scores:np.ndarray = np.matmul(query_matrix, X.T)
        best_idx = scores.argmax(1)
        results.append(data['docs'][best_idx[0]])

with open(opt.output_file, 'w', encoding='utf8') as f_out:
    f_out.write('\n'.join(results))