# data-type-predictor README

Given the name of a property or attribute like 'BrandName' or 'AmountReceived', try to predict a data type like String, Boolean, Integer...

# Dependencies

```
python3 -m pip install --upgrade parameterized==0.7.5 levenshtein==0.20.8 Flask==2.2.2
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

## Example - running as a REST API

```
./go.api.sh
```

Open a URL with a property-name at the end:

```
http://127.0.0.1:5000/predict_type/Branded
```

Output:
```
property_name: Branded -> predicted type=Boolean
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

# Usage - Training

A small element of Machine Learning is used to optimize the parameters used to predict, for a given data set.

The Accuracy measure is used (TP/(TP+FP)). The Cost function is defined simply to maximise the accuracy.

## Example

```
python3 ./src/train.py ./data/ip-xxx-big.json
Training...
[done]
Optimal config:
is_fuzzy=False, max_distance=0, min_length=2, cost=29, accuracy=71
```

Unfortunately, Machine Learning indicates that the optimal configuration can be acheived WITHOUT fuzzy matching!
However, for UX reasons, fuzzy matching still seems useful, given the accuracy against data is the same.

# Approach

1. The property name (the word) is stemmed into smaller tokens, assuming camelCase or PascalCase
2. Heuristics are run to try and recognise the first or last token. Example: `is` or `can` indicates `Boolean`. If match is found, exit.
3. [If fuzzy matching is enabled] Levenshtein distance is then allowed on the longer tokens, to try to get a fuzzy match.

# Evaluation (Validation)

## Data set: 66 words

| Approach                                                    | Accuracy | Correctly predicted | Incorrectly predicated | Not predicted | Data set                                                                                | Comment                                                                                           |
| ----------------------------------------------------------- | -------- | ------------------- | ---------------------- | ------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Heuristics, no fuzzy match                                  | -        | 45%                 | 5%                     | 50%           | 66 words                                                                                | 'Safe' predications                                                                               |
| Heuristics, with fuzzy match (min length 3, max distance 5) | -        | 47%                 | 48%                    | 5%            | 66 words                                                                                | 'Unsafe' fuzzy predications: small gain in true positives with cost of much more false positives. |
| Heuristics, with fuzzy match (min length 2, max distance 2) | -        | 50%                 | 14%                    | 36%           | 66 words                                                                                | 'Safer' fuzzy predications.                                                                       |
| Heuristics, with fuzzy match (min length 5, max distance 2) | 91%      | 47%                 | 5%                     | 48%           | 66 words                                                                                | 'Safer' fuzzy predications.                                                                       |
| *ML Optimized* Heuristics, with NO fuzzy match (min length 2)              | 91%      | 45%                 | 5%                     | 50%           | _Machine Learning optimized the 5600 item data set_ -> Fuzzy is OFF. |

## Data set: 5640 words

| Approach                                                    | Accuracy | Correctly predicted | Incorrectly predicated | Not predicted | Data set                                                                       | Comment              |
| ----------------------------------------------------------- | -------- | ------------------- | ---------------------- | ------------- | ------------------------------------------------------------------------------ | -------------------- |
| Heuristics, no fuzzy match                                  | -        | 16%                 | 7%                     | 77%           | 5640 words                                                                     | 'Safe' predications. |
| Heuristics, with fuzzy match (min length 2, max distance 2) | -        | 24%                 | 30%                    | 46%           | 5640 words                                                                     | Fuzzy predications.  |
| Heuristics, with fuzzy match (min length 2, max distance 2) | -        | 24%                 | 30%                    | 46%           | 5640 words                                                                     | Fuzzy predications.  |
| Heuristics, with fuzzy match (min length 5, max distance 2) | 68%      | 17%                 | 8%                     | 75%           | 5640 words                                                                     | Fuzzy predications.  |
| *ML Optimized* Heuristics, with forced fuzzy match (min length 6, max distance 1)              | 71%      | 16%                 | 7%                     | 77%     | 5640       | _Machine Learning optimized THIS data set_ Fuzzy is forced ON, learned optimal token length. |
| *ML Optimized* Heuristics, with NO fuzzy match               | 71%      | 16%                 | 7%                     | 77%     | 5640       | _Machine Learning optimized THIS data set_ -> Fuzzy is OFF. |
