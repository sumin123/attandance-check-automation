import json
import os

def write_score_file(data):
    with open('score.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent='\t')

def read_score_file():
    if os.path.isfile('score.json'):
        with open('score.json', 'r', encoding='utf-8') as f:
            scores = json.load(f)
    else:
        with open('score.json', 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent='\t')
            scores = {}
    return scores