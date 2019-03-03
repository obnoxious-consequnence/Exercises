import re
from collections import Counter

def word_count(phrase):
    words = re.split(r"'?\s+'?|[_,!&@$%^.:]+", phrase)
    counter = Counter((word.lower() for word in words if word))
    return counter