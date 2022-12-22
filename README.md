# data-type-predictor README

Given the name of a property or attribute, try to predict a data type like string, bool int...

# Usage

```
python3 ./src/predict-type-from-name.py <name>
```

## Example

```
python3 ./src/predict-type-from-name.py IsOk
```

Output:

```
Boolean
```

# Dependencies

```
python3 -m pip install --upgrade parameterized=0.7.5
```
