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
tests module for dictstore
"""

import unittest
import os
from dictstore import file_handler
from dictstore.exceptions import (
    InvalidFileExtension,
    DataStoreFileCorrupted,
    UnsupportedValueType
)
from dictstore.interface import DictStore


def clean_temp_files(file_name):
    """
    remove data file if already exists
    """
    try:
        os.remove(file_name)
    except OSError:
        pass


class Test:
    """Test Class for Testing Key and Values Types"""
    count = 0

    def __init__(self) -> None:
        self.message = 'Test Class'

    def __hash__(self) -> int:
        """hash function"""
        Test.count += 1
        return Test.count


class TestFileHandler(unittest.TestCase):
    """
    Unit tests for FileHandler class
    """
    def test_invalid_filename(self):
        """
        checks if an invalid filename raises
        the InvalidFileExtension exception.
        """
        with self.assertRaises(InvalidFileExtension):
            file_handler.FileHandler('file_name_without_dictstore_extension')

    def test_invalid_file_contents(self):
        """
        checks if invalid file contents raise
        DataStoreFileCorrupted exception.
        """

        data_file_name = 'tests/test_invalid_file_contents.dictstore'

        clean_temp_files(data_file_name)

        # create the data file
        file_handler.FileHandler(data_file_name)

        with open(data_file_name, 'a', encoding='utf-8') as data_file:
            data_file.writelines('abcd')

        with self.assertRaises(DataStoreFileCorrupted):
            DictStore(data_file_name)


class TestDictStoreKeys(unittest.TestCase):
    """
    checks if all types of hashable keys are
        being accepted and retrieved correctly

            Key Types:
                Integer
                Float/Decimal
                String
                Integer Tuple
                String Tuple
    """

    def test_integer_key(self):
        """
        checks if integer keys are working correctly
        """

        data_file_name = 'tests/test_integer_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], 45, "Integer Key")

    def test_float_key(self):
        """
        checks if floating point keys are working correctly
        """

        data_file_name = 'tests/test_float_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1.2] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1.2], 45, "Floating Point Key")

    def test_char_string_key(self):
        """
        checks if character string keys are working correctly
        """

        data_file_name = 'tests/test_char_string_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store['str'] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store['str'], 45, "Character String Key")

    def test_integer_string_key(self):
        """
        checks if integer string keys are working correctly
        """

        data_file_name = 'tests/test_integer_string_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store['2'] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store['2'], 45, "Integer String Key")

    def test_integer_tuple_key(self):
        """
        checks if integer tuple keys are working correctly
        """

        data_file_name = 'tests/test_integer_tuple_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[(1, 2)] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[(1, 2)], 45, "Integer Tuple Key")

    def test_string_tuple_key(self):
        """
        checks if integer tuple keys are working correctly
        """

        data_file_name = 'tests/test_string_tuple_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[('1', '2')] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[('1', '2')], 45, "String Tuple Key")


class TestDictStoreValues(unittest.TestCase):
    """
    checks if all types of storable values are
    being accepted and retrieved correctly

        Values Types:
            - strings
            - bytes
            - numbers
            - tuples
            - lists
            - dicts
            - sets
            - booleans
            - None
    """

    def test_if_unsupported_type_expection_raised(self):
        """
        checks if UnsupportedValueType is raised.
        """

        test_class_instance = Test()

        data_file_name = ('tests/test_if_unsupported_'
                          'type_expection_raised.dictstore'
                          )

        clean_temp_files(data_file_name)

        with self.assertRaises(UnsupportedValueType):
            dict_store = DictStore(data_file_name)
            dict_store['Hi'] = test_class_instance

    def test_if_unsupported_type_expection_raised_nested_list(self):
        """
        checks if UnsupportedValueType is raised
        for nested values
        """

        test_value = [Test(), Test()]

        data_file_name = ('tests/test_if_unsupported_'
                          'type_expection_raised_nested_list.dictstore'
                          )

        clean_temp_files(data_file_name)

        with self.assertRaises(UnsupportedValueType):
            dict_store = DictStore(data_file_name)
            dict_store['Hi'] = test_value

    def test_if_unsupported_type_expection_raised_nested_set(self):
        """
        checks if UnsupportedValueType is raised
        for nested values
        """

        test_value = set([Test(), Test()])

        data_file_name = ('tests/test_if_unsupported_'
                          'type_expection_raised_nested_set.dictstore'
                          )

        clean_temp_files(data_file_name)

        with self.assertRaises(UnsupportedValueType):
            dict_store = DictStore(data_file_name)
            dict_store['Hi'] = test_value


if __name__ == '__main__':
    unittest.main()
