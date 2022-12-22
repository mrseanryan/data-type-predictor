# data-type-predictor README

Given the name of a property or attribute, try to predict a data type like string, bool int...

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

# Dependencies

```
python3 -m pip install --upgrade parameterized=0.7.5
```
