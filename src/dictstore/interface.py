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

:copyright: (c) 2021 by Sai Sampath Kumar Balivada.
"""


from json.decoder import JSONDecodeError
from typing import Any
import json
from dictstore.exceptions import DataStoreFileCorrupted

from dictstore.file_handler import FileHandler


class DictStore:
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
        self.in_memory_dictionary = {}

        # set default value to None
        self.in_memory_dictionary.setdefault(None)

        # initialize the data file
        self.file_handler = FileHandler(datastore_location)

        # fetch the records from data file
        json_string = self.file_handler.read_from_file()

        # add '{' at the start and '}' at the end
        json_string = '{' + json_string + '}'

        # convert json string to dictionary
        try:
            json_data = json.loads(json_string)
        except JSONDecodeError as json_decode_error:
            raise DataStoreFileCorrupted() from json_decode_error

        # update the in memory dictionary with the JSON data
        self.in_memory_dictionary.update(json_data)

    def __rewrite_data_file(self) -> None:
        """
        converts in memory dictionary to JSON string
        removes the '{' and '}' symbols at the start and end
        asks file handler to write the resulting string
        to the data file.
        """

        json_string = json.dumps(self.in_memory_dictionary, sort_keys=True)

        self.file_handler.rewrite_to_file(json_string[1:-1])

    def __add_record_to_data_file(self, record: dict) -> None:
        """
        converts the given record to JSON string
        removes the '{' and '}' symbols at the start and end
        asks file handler to append the resulting string
        to the end of data file
        """

        json_string = json.dumps(record)

        self.file_handler.append_to_file(', ' + json_string[1:-1])

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

        # if there is no record with the given key
        # update the in memory dictionary and
        # add record to the data file
        if self.get(key) is None:
            self.in_memory_dictionary[key] = value
            self.__add_record_to_data_file({key: value})

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
