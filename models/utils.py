import re
import json
import os
from argparse import ArgumentParser
import yaml
from tqdm import tqdm
from requests.auth import HTTPBasicAuth
import json
from nltk.text import sent_tokenize
from nltk import word_tokenize
import requests

def remove_brackets(text:str):
    while re.search(r'{[^{}]*}', text):
        text = re.sub(r'{[^{}]*}', '', text)
    while re.search(r'\([^()]*\)', text):
        text = re.sub(r'\([^()]*\)', '', text)
    while re.search(r'\[[^][]*\]', text):
        text = re.sub(r'\[[^][]*\]', '', text)
    return ' '.join(text.split())


def load_config():
    parser = ArgumentParser()
    parser.add_argument('--config', type=str, default=None, help="The configuration file")
    parser.add_argument('--topics_file', type=str, default=None, help="The json file storing topics")
    parser.add_argument('--topic_content_dir', type=str, default=None, help="The folder where the topic related contents are saved")
    parser.add_argument('--model_type', type=str, default=None, help="The model type to be used: bm25/tfidf/bert")
    parser.add_argument('--query', type=str, default=None, help="The content to be used as query: title/article")

    config = parser.parse_args().config
    with open(config) as f_in:
        config_ = yaml.safe_load(f_in)
        parser.set_defaults(**config_)
        opt = parser.parse_args()
        return opt

def create_dataset(topics_file:str, topic_content_dir:str):
    with open(topics_file) as f_in:
        topics = json.load(f_in)
    dataset = []
    for topic in tqdm(topics):
        data = {}

        topic_content_file = topic_content_dir + 'topic' + topic['topic_id'] + '.md'
        topic_content = []
        with open(topic_content_file, encoding="utf8") as f_in:
            for line in f_in:
                line = line.strip().lower()
                if line:
                    topic_content.append(remove_brackets(line.strip()))
        data['topic_content'] = ' '.join(topic_content)

        data['topic_text'] = topic['topic_text']

        abstract_url = topic['abstract_url']
        resp = requests.get(abstract_url, auth=HTTPBasicAuth('inex', 'qatc2011'), verify=False)
        contents = json.loads(resp.content)
        if not contents['hits']['hits']:
            continue
        abstracts = [hit['_source']['abstract'] for hit in contents['hits']['hits']]
        docs = []
        for abstract in abstracts:
            docs.extend(sent_tokenize(abstract))
        docs = [doc for doc in docs if doc]
        data['docs'] = docs

        dataset.append(data)
    
    return dataset

def load_dataset(opt):
    if os.path.exists(opt.dataset_file):
        return json.load(open(opt.dataset_file))
    else:
        dataset = create_dataset(opt.topics_file, opt.topic_content_dir)
        with open(opt.dataset_file, 'w') as f_out:
            json.dump(dataset, f_out)
        
        return dataset