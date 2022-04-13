import re

def remove_brackets(text:str):
    while re.search(r'{[^{}]*}', text):
        text = re.sub(r'{[^{}]*}', '', text)
    while re.search(r'\([^()]*\)', text):
        text = re.sub(r'\([^()]*\)', '', text)
    while re.search(r'\[[^][]*\]', text):
        text = re.sub(r'\[[^][]*\]', '', text)
    return ' '.join(text.split())