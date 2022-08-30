import glob
import json
import re
import os
import glob
from functools import reduce

from nltk.tokenize import word_tokenize

# import nltk
# nltk.download('punkt')


garden = {"peach": 11, "gherkin": 17, "soil": 33, "tomatoes": 19}
science = {"science": 11, "doctor": 22, "phd": 11, "soil": 11}


def normalize_text(text):
    tokens = word_tokenize(text)
    low = map(lambda t: t.lower(), tokens)
    filtered = filter(lambda t: re.match(r"[a-z]{4,}", t, flags=re.IGNORECASE), low)
    return filtered


def count_tokens(tokens):
    result = {}
    for t in tokens:
        result[t] = result.get(t, 0) + 1
    return result


def list_datasets(path):
    result = {}
    for directory in glob.glob(f"{path}\\*"):
        category = os.path.basename(directory)
        result[category] = glob.glob(f"{path}\\{category}\\*")
    return result


def file_to_model_piece(filename):
    with open(filename, encoding="utf8") as f:
        return count_tokens(normalize_text(f.read()))


def squash_records(model_records):
    result = {}
    for record in model_records:
        for k, v in record.items():
            word_freq = result.get(k, 0)
            result[k] = word_freq + v
    return result


for category, files in list_datasets("data").items():
    path = f"models\\{category}"
    with open(path, "w") as f:
        res = []
        for fl in files:
            res.append(file_to_model_piece(fl))
        f.write(json.dumps(squash_records(res)))
