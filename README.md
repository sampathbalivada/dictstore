# dictstore

dictstore is a simple local data store for Python that aims to provide an interface similar to a python dictionary.

<hr/>

### Getting Started

##### Installation

```bash
pip install dictstore
```

##### Usage
```python3
# file: sample_1.py

from dictstore import DictStore

data = DictStore()

d[1] = 45
```

```python3
# file: sample_2.py

from dictstore import DictStore

data = DictStore()

print(d[1])

# output: 45
```

<hr/>

### Considerations

- dictstore uses an in memory dictionary to support fast reads so using multiple DictStore instances for the same data file is not supported.

- dictstore is best suited for CLIs or similar applications where values have to be remembered accross multiple runs. 

- The data file is a plain readable text file and no encryption is offered by dictstore.

- dictstore might not be the fastest datastore in the market, its promise is to get the work done and nothing else.

- dictstore will evaluate the type of value for all the nested objects in a given value, this is done using a Tree.

### Keys

All Hashable Data Types are supported as keys.

##### Hashable Data Types

| Name        | Type        |
| ----------- | ----------- |
| String      | `str`       |
| Integer     | `int`       |
| Float       | `float`     |
| Tuple       | `tuple`     |

### Values

Dictstore uses `ast` package and `ast.literal_eval` under the hood, so currently all the data types supported by `ast.literal_eval` except Ellipsis are supported as values. 

strings, bytes, numbers, tuples, lists, dicts, sets, booleans, None.

For more information about ast.literal_eval visit the following link. 

[https://docs.python.org/3/library/ast.html#ast.literal_eval](https://docs.python.org/3/library/ast.html#ast.literal_eval)

<hr>

### To-Do:

- Tests for different types of values to be added
- Raise exception when creating multiple instances for the same data file 