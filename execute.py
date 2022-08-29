import json
import glob
import os
from scipy import spatial
from functools import reduce

def read_models(path):
    result = {}
    for file in glob.glob(path):
        category = os.path.basename(file)
        with open(file) as f:
            result[category] = json.load(f)
    return result


def calculate_likeness(tokenized_text, model_record):
    diff_list = []
    la = []
    lb = []
    for word, freq in model_record.items():
        text_freq = tokenized_text.get(word, 0)
        la.append(freq)
        lb.append(text_freq)
        if text_freq != 0:
            diff_freq_pc = text_freq / freq if freq > text_freq else freq / text_freq
            diff_list.append(diff_freq_pc)
    return 1 - spatial.distance.cosine(la, lb)


def calculate_likeness_all_models(tokenized_text, all_models):
    result = {}
    for category, models in all_models.items():
        for model in models:
            score = calculate_likeness(tokenized_text, model)
            cat_score = result.get(category, score)
            result[category] = (score + cat_score) / 2
    return result

m = read_models("models/*")


print(calculate_likeness_all_models(m['scientific'][0], m))
print(calculate_likeness_all_models(m['scientific'][1], m))
print(calculate_likeness_all_models(m['gardening'][1], m))
print(calculate_likeness_all_models(m['gardening'][0], m))
# print(calculate_likeness(models['gardening'][0], models['gardening'][1]))
# print(calculate_likeness(models['scientific'][0], models['scientific'][1]))
