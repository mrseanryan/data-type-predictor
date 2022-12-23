import Levenshtein

MAX_DISTANCE = 5
MIN_LENGTH = min(3, MAX_DISTANCE)

def is_fuzzy_match(word1, word2):
    if len(word1) < MIN_LENGTH or len(word2) < MIN_LENGTH:
        return word1 == word2
    return Levenshtein.distance(word1, word2, score_cutoff=MAX_DISTANCE) <= MAX_DISTANCE

def is_fuzzy_match_list(word, other_words):
    for other_word in other_words:
        if is_fuzzy_match(word, other_word):
            return True
    return False
