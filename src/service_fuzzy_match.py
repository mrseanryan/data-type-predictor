import Levenshtein
from config_fuzzy_match import FuzzyMatchConfig

def is_fuzzy_match(word1, word2):
    if len(word1) < FuzzyMatchConfig.CalculateMinLength() or len(word2) < FuzzyMatchConfig.CalculateMinLength():
        return word1 == word2
    return Levenshtein.distance(word1, word2, score_cutoff=FuzzyMatchConfig.MAX_DISTANCE) <= FuzzyMatchConfig.MAX_DISTANCE

def is_fuzzy_match_list(word, other_words):
    for other_word in other_words:
        if is_fuzzy_match(word, other_word):
            return True
    return False
