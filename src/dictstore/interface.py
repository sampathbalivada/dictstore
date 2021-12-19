# Copyright 2021 Sai Sampath Kumar Balivada

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
dictstore is a simple local data store
for Python that aims to provide an interface
similar to a python dictionary.
"""


from typing import Any, DefaultDict
from pathlib import Path
import ast
import dictstore.helpers as helpers

from dictstore.exceptions import DataStoreFileCorrupted, UnsupportedValueType
from dictstore.file_handler import FileHandler


class DictStoreSingleton(type):
    """
    metaclass to implement singleton behavior for DictStore class
    """
    _instances = DefaultDict(None)

    def __call__(cls, datastore_location='./default.dictstore') -> Any:
        if datastore_location in cls._instances:
            return cls._instances[datastore_location]

        instance = super(DictStoreSingleton, cls).__call__(datastore_location)
        cls._instances[datastore_location] = instance
        return instance


class DictStore(metaclass=DictStoreSingleton):
    """
    A class that initializes the datastore into the memory
    and provides functions to manipulate it.
    """

    def __init__(self, datastore_location='./default.dictstore') -> None:
        """
        Initializes the in memory dictionary and
        copies all the records from the database file to memory
        """

        # create an in memory dictionary to store the value
        # and set default value to None
        self.in_memory_dictionary = {}

        self.in_memory_dictionary.setdefault(None)

        # check if the datafile is already opened and return
        # the object already opened else continue creating a new object

        self.datastore_location = Path(datastore_location).resolve().__str__()

        self.file_handler = FileHandler(self.datastore_location)

        # fetch the file contents and parse accordingly
        # parse key and value as JSON objects

        data = self.file_handler.read_from_file()

        # check if the number of lines are even

        if len(data) % 2 != 0:
            raise DataStoreFileCorrupted()

        for line_number_of_key in range(0, len(data), 2):
            key = data[line_number_of_key]
            key_parsed = ast.literal_eval(key)
            value = data[line_number_of_key + 1]
            value_parsed = ast.literal_eval(value)
            self.in_memory_dictionary[key_parsed] = value_parsed

    def __rewrite_data_file(self) -> None:
        """
        converts in memory dictionary to string
        asks file handler to write the resulting string
        to the data file.
        """

        # convert each record into the desired format
        # Format:
        # key \n
        # json(value) \n

        data_file_cache = []

        for key, value in self.in_memory_dictionary.items():
            print(key, '|', value)
            data_file_cache.append(helpers.get_escaped_string(key) + '\n')
            data_file_cache.append(helpers.get_escaped_string(value) + '\n')

        self.file_handler.rewrite_to_file(data_file_cache)

    def __add_record_to_data_file(self, key, value) -> None:
        """
        converts the given record to string
        asks file handler to append the resulting string
        to the end of data file
        """

        data_record_cache = helpers.get_escaped_string(key) + '\n'
        data_record_cache += helpers.get_escaped_string(value) + '\n'

        self.file_handler.append_to_file(data_record_cache)

    # -----------------
    # Read Operations
    # -----------------
    # All read operation are performed on the in memory dictionary
    # -----------------

    def keys(self) -> list:
        """returns a list of all the keys in the datastore"""
        return list(self.in_memory_dictionary.keys())

    def values(self) -> list:
        """returns a list of all the values in the datastore"""
        return list(self.in_memory_dictionary.values())

    def get(self, key: Any) -> Any:
        """
        takes a key and returns the value if it exists.
        returns None if the key does not exist.
        """

        return self.in_memory_dictionary.get(key)

    # -----------------
    # Write Operations
    # -----------------
    # All write operations are performed with a write through approach
    #
    # Write operations are first performed on the in memory dictionary
    # and updated on the data file
    # -----------------

    def upsert_record(self, key: Any, value: Any) -> None:
        """
        takes a key value pair
        and updates the value if it already exists
        creates a new record otherwise
        """

        if not helpers.is_supported_key_type(key):
            message = ('Supported key types are '
                       'int, float, str, tuple and NoneType'
                       )
            raise KeyError(message)

        if not helpers.is_supported_value_type(value):
            raise UnsupportedValueType()

        # if there is no record with the given key
        # update the in memory dictionary and
        # add record to the data file
        if self.get(key) is None:
            self.in_memory_dictionary[key] = value
            self.__add_record_to_data_file(key, value)

        # if a record exists with the given key
        # add new key-value pair to in memory dictionary
        # and rewrite the data file
        else:
            self.in_memory_dictionary[key] = value
            self.__rewrite_data_file()

    def remove(self, key):
        """
        takes a key
        and removes the record if it exists
        """

        # if a record exists with the given key
        # remove it from the in memory dictionary
        # and rewrite the data file
        if self.get(key) is not None:
            del self.in_memory_dictionary[key]
            self.__rewrite_data_file()

    def __len__(self) -> int:
        """returns the number of records in the database"""
        return self.in_memory_dictionary.__len__()

    def __delitem__(self, key):
        """delete key value pair from the datastore"""
        self.remove(key)

    def __getitem__(self, key):
        """perform get operation with the given key"""
        return self.get(key)

    def __setitem__(self, key, value):
        """perform upsert operation with the given key and value"""
        self.upsert_record(key, value)
