import json
import glob
import os
from scipy import spatial
from statistics import mean
from learn import file_to_model_piece
import sys

def read_models(path):
    result = {}
    for file in glob.glob(path):
        category = os.path.basename(file)
        with open(file) as f:
            result[category] = json.load(f)
    return result


def calculate_likeness(tokenized_text, model_record):
    la = []
    lb = []
    for word, freq in tokenized_text.items():
        text_freq = model_record.get(word, 0)
        la.append(freq)
        lb.append(text_freq)
    return 1 - spatial.distance.cosine(la, lb)


def calculate_likeness_all_models(tokenized_text, all_models):
    result = {}
    for category, model in all_models.items():
        score = calculate_likeness(tokenized_text, model)
        result[category] = score
    return result


m = read_models("models/*")

print(calculate_likeness_all_models(file_to_model_piece(sys.argv[1]), m))
