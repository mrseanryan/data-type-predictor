# data-type-predictor README

Given the name of a property or attribute like 'BrandName' or 'AmountReceived', try to predict a data type like String, Boolean, Integer...

# Dependencies

```
python3 -m pip install --upgrade parameterized==0.7.5 levenshtein==0.20.8
```

# Usage

```
python3 ./src/predict-type-from-name.py <name>
```

## Example - REPL to try it out

```
python3 ./src/predict-type-from-name-repl.py
```
Output:

```
Enter a property name like 'Color' or 'BrandName' or 'CreatedOn' (just press ENTER to exit) ->ExportedOn
ExportedOn=Date
Enter a property name like 'Color' or 'BrandName' or 'CreatedOn' (just press ENTER to exit) ->ItemWidth
ItemWidth=Integer
```

## Example - passing a property name on the command line

```
python3 ./src/predict-type-from-name.py IsOk
```

Output:

```
Boolean
```

# Approach

1. The property name (the word) is stemmed into smaller tokens, assuming camelCase or PascalCase
2. Heuristics are run to try and recognise the first or last token. Example: `is` or `can` indicates `Boolean`. If match is found, exit.
3. Levenshtein distance is then allowed on longer tokens, to try to get a fuzzy match.
