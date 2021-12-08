"""
dictstore is a simple local data store
for Python that aims to provide an interface
similar to a python dictionary.

:copyright: (c) 2021 by Sai Sampath Kumar Balivada.
"""


class DictStore:
    """
    A class that initializes the database into the memory
    and provides functions to manipulate it.
    """

    def __init__(self) -> None:
        """
        Initializes the in memory dictionary and
        copies all the records from the database file to memory
        """
        self.in_memory_dictionary = {}

    def __len__(self) -> int:
        """returns the number of records in the database"""
        return self.in_memory_dictionary.__len__()

    def get(self, key):
        """
        takes a key and returns the value if it exists.
        returns None if the key does not exist.
        """
        return self.in_memory_dictionary.get(key)

    def keys(self):
        """returns a list of all the keys in the datastore"""
        return self.in_memory_dictionary.keys()

    def values(self):
        """returns a list of all the values in the datastore"""
        return self.in_memory_dictionary.values()

    def set_default_value(self):
        """
        sets the default value to be returned by get()
        if the key doesnot exist in the datastore
        """
        print("ERROR: Unable to change default value.")
        print("Default value is currently set to None.")

    def upsert_record(self, key, value):
        """takes a key and value objects and stores them in the datastore"""
        self.in_memory_dictionary[key] = value


if __name__ == '__main__':
    # TODO: Setup testing and move tests to the tests directory
    # TODO: add LICENSE prompt here

    # intiialize a dictstore
    dict_store = DictStore()

    # add values to the dictstore
    dict_store.upsert_record(1, "Hi")

    print(dict_store.keys())
    print(dict_store.values())
    dict_store.set_default_value()
