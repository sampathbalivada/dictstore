# DictStore

dictstore is a simple local data store for Python that aims to provide an interface similar to a python dictionary.

### Keys

All Hashable Data Types are supported as keys.

#### Hashable Data Types

| Name        | Type        |
| ----------- | ----------- |
| String      | `str`       |
| Integer     | `int`       |
| Float       | `float`     |
| Tuple       | `tuple`     |

### Values

Dictstore uses `ast` package and `ast.literal_eval` under the hood, so currently only the following data types are supported as values. 

strings, bytes, numbers, tuples, lists, dicts, sets, booleans, None and Ellipsis.

For more information about ast.literal_eval visit the following link. 

[https://docs.python.org/3/library/ast.html#ast.literal_eval](https://docs.python.org/3/library/ast.html#ast.literal_eval)


> Exceptions and tests for values are are yet to be added. The above list may be updated depending on various factors.