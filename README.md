# DictStore

dictstore is a simple local data store for Python that aims to provide an interface similar to a python dictionary.

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


### TODO for Initial Release:

- Tests for different types of values to be added