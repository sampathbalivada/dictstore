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

        data_file_name = 'tests/test_data/test_invalid_file_contents.dictstore'

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

        data_file_name = 'tests/test_data/test_integer_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], 45, "Integer Key")

    def test_float_key(self):
        """
        checks if floating point keys are working correctly
        """

        data_file_name = 'tests/test_data/test_float_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1.2] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1.2], 45, "Floating Point Key")

    def test_char_string_key(self):
        """
        checks if character string keys are working correctly
        """

        data_file_name = 'tests/test_data/test_char_string_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store['str'] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store['str'], 45, "Character String Key")

    def test_integer_string_key(self):
        """
        checks if integer string keys are working correctly
        """

        data_file_name = 'tests/test_data/test_integer_string_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store['2'] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store['2'], 45, "Integer String Key")

    def test_integer_tuple_key(self):
        """
        checks if integer tuple keys are working correctly
        """

        data_file_name = 'tests/test_data/test_integer_tuple_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[(1, 2)] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[(1, 2)], 45, "Integer Tuple Key")

    def test_string_tuple_key(self):
        """
        checks if integer tuple keys are working correctly
        """

        data_file_name = 'tests/test_data/test_string_tuple_key.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[('1', '2')] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[('1', '2')], 45, "String Tuple Key")

    def test_unsupproted_key_type(self):
        """
        checks if using an unsupported key type raises an exception
        """

        data_file_name = 'tests/test_data/test_unsupproted_key_type.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        with self.assertRaises(KeyError):
            dict_store[Test()] = 45


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

    def test_string_value(self):
        """
        checks if string values are
        accepted and retrieved correctly
        """

        data_file_name = 'tests/test_data/test_string_value.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = 'abc'

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], 'abc')

    def test_bytes_value(self):
        """
        checks if bytes values are
        accepted and retrieved correctly
        """

        data_file_name = 'tests/test_data/test_bytes_value.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = bytes('abc', 'utf-8')

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], bytes('abc', 'utf-8'))

    def test_int_value(self):
        """
        checks if int values are
        accepted and retrieved correctly
        """

        data_file_name = 'tests/test_data/test_int_value.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = 45

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], 45)

    def test_float_value(self):
        """
        checks if float values are
        accepted and retrieved correctly
        """

        data_file_name = 'tests/test_data/test_float_value.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = 1.2

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], 1.2)

    def test_tuple_value(self):
        """
        checks if tuple values are
        accepted and retrieved correctly
        """

        data_file_name = 'tests/test_data/test_tuple_value.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = (1, '2', 1.2)

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], (1, '2', 1.2))

    def test_list_value(self):
        """
        checks if list values are
        accepted and retrieved correctly
        """

        data_file_name = 'tests/test_data/test_list_value.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = [1, '2', 1.2, {1: 2, '1': '2'}]

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], [1, '2', 1.2, {1: 2, '1': '2'}])

    def test_dict_value(self):
        """
        checks if dict values are
        accepted and retrieved correctly
        """

        data_file_name = 'tests/test_data/test_dict_value.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = {1: 2, '1': '2', 1.2: 2.4}

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], {1: 2, '1': '2', 1.2: 2.4})

    def test_set_value(self):
        """
        checks if set values are
        accepted and retrieved correctly
        """

        data_file_name = 'tests/test_data/test_set_value.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        value = set([1, 2, 3, 3, 4])
        dict_store[1] = value

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], value)

    def test_bool_value(self):
        """
        checks if bool values are
        accepted and retrieved correctly
        """

        data_file_name = 'tests/test_data/test_bool_value.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = True
        dict_store[2] = False

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], True)
        self.assertEqual(dict_store[2], False)

    def test_none_value(self):
        """
        checks if None value is
        accepted and retrieved correctly
        """

        data_file_name = 'tests/test_data/test_bool_value.dictstore'

        clean_temp_files(data_file_name)

        dict_store = DictStore(data_file_name)
        dict_store[1] = None

        dict_store = DictStore(data_file_name)
        self.assertEqual(dict_store[1], None)

    def test_if_unsupported_type_expection_raised(self):
        """
        checks if UnsupportedValueType is raised.
        """

        test_class_instance = Test()

        data_file_name = ('tests/test_data/test_if_unsupported_'
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

        data_file_name = ('tests/test_data/test_if_unsupported_'
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

        data_file_name = ('tests/test_data/test_if_unsupported_'
                          'type_expection_raised_nested_set.dictstore'
                          )

        clean_temp_files(data_file_name)

        with self.assertRaises(UnsupportedValueType):
            dict_store = DictStore(data_file_name)
            dict_store['Hi'] = test_value


class CheckSingletonBehavior(unittest.TestCase):
    """
    checks if the Singleton behavior of the
    DictStore class is behaving correctly
    """

    def test_singleton_behavior_same_filename(self):
        """
        initializes two DictStore objects with the same filename
        and verifies if the references are same
        """

        data_file_name = ('tests/test_data/'
                          'test_singleton_behavior_same_filename'
                          '.dictstore'
                          )

        self.assertEqual(
            DictStore(data_file_name) is DictStore(data_file_name),
            True
            )

    def test_singleton_behavior_different_filename(self):
        """
        initializes two DictStore objects with the same filename
        and verifies if the references are same
        """

        data_file_name_1 = ('tests/test_data/'
                            'test_singleton_behavior_different_filename_1'
                            '.dictstore'
                            )

        data_file_name_2 = ('tests/test_data/'
                            'test_singleton_behavior_different_filename_2'
                            '.dictstore'
                            )

        self.assertEqual(
            DictStore(data_file_name_1) is DictStore(data_file_name_2),
            False
            )


if __name__ == '__main__':
    unittest.main()
