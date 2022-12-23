# data-type-predictor README

Given the name of a property or attribute like 'BrandName' or 'AmountReceived', try to predict a data type like String, Boolean, Integer...

# Dependencies

```
python3 -m pip install --upgrade parameterized==0.7.5 levenshtein==0.20.8
```

# Usage - Prediction

```
python3 ./src/predict-type-from-name.py <name> [--help --fuzzy]
```

## Example - passing a property name on the command line

```
python3 ./src/predict-type-from-name.py Actve --fuzzy
```

Output:

```
Actve=Boolean
```

## Example - REPL to try it out

```
python3 ./src/predict-type-from-name-repl.py
```
Output:

```
Enter a property name like 'Color' or 'BrandName' or 'CreatedOn'
(just press ENTER to exit) ->ExportedOn
ExportedOn=Date
(just press ENTER to exit) ->ItemWidth
ItemWidth=Integer
```

# Usage - Evaluation

```
python3 ./src/evaluate.py <path or glob to JSON data file(s)> [--help --fuzzy]
```

## Example

```
python3 ./src/evaluate.py ./data/names-and-types.small.1.json
```

Output:
```
# Accuracy:

45% correctly predicted
5% incorrectly predicted
50% not predicted
Data set size: 66 words
```

# Approach

1. The property name (the word) is stemmed into smaller tokens, assuming camelCase or PascalCase
2. Heuristics are run to try and recognise the first or last token. Example: `is` or `can` indicates `Boolean`. If match is found, exit.
3. [If fuzzy matching is enabled] Levenshtein distance is then allowed on the longer tokens, to try to get a fuzzy match.

# Evaluation (Validation)

## Data set: 66 words

| Approach | Correctly predicted | Incorrectly predicated | Not predicted | Data set | Comment |
|---|---|---|---|---|---|
| Heuristics, no fuzzy match | 45% | 5% | 50% | 66 words | 'Safe' predications |
| Heuristics, with fuzzy match (min length 3, max distance 5) | 47% | 48% | 5% | 66 words | 'Unsafe' fuzzy predications: small gain in true positives with cost of much more false positives. |
| Heuristics, with fuzzy match (min length 2, max distance 2) | 50% | 14% | 36% | 66 words | 'Safer' fuzzy predications. |
| Heuristics, with fuzzy match (min length 5, max distance 2) | 47% | 5% | 48% | 66 words | 'Safer' fuzzy predications. |

## Data set: 5640 words

| Approach | Correctly predicted | Incorrectly predicated | Not predicted | Data set | Comment |
|---|---|---|---|---|---|
| Heuristics, no fuzzy match | 16% | 7% | 77% | 5640 words | 'Safe' predications. |
| Heuristics, with fuzzy match (min length 2, max distance 2) | 24% | 30% | 46% | 5640 words | Fuzzy predications. |
| Heuristics, with fuzzy match (min length 2, max distance 2) | 24% | 30% | 46% | 5640 words | Fuzzy predications. |
| Heuristics, with fuzzy match (min length 5, max distance 2) | 17% | 8% | 75% | 5640 words | Fuzzy predications. |
