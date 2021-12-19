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
Helper functions for dictstore
"""


from typing import Any


def is_supported_key_type(key):
    """
    checks if the given key type is supported

    Supported Types:
        - int
        - float
        - str
        - tuple
        - NoneType
    """

    if (
        isinstance(key, (int, float, str, tuple, )) or
        key is None
       ):
        return True

    return False


def is_supported_value_type(value):
    """
    checks if the given value type is supported.

    Supported Types:
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

    if (
        isinstance(value, (str, bytes, int, float, bool)) or
        value is None
       ):
        return True
    if isinstance(value, tuple):
        for sub_value in value:
            if not is_supported_value_type(sub_value):
                return False
        return True
    if isinstance(value, list):
        for sub_value in value:
            if not is_supported_value_type(sub_value):
                return False
        return True
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            if not is_supported_value_type(sub_key):
                return False
            if not is_supported_value_type(sub_value):
                return False
        return True
    if isinstance(value, set):
        for sub_value in value:
            if not is_supported_value_type(sub_value):
                return False
        return True

    return False


def get_escaped_string(var: Any) -> str:
    """
    checks if the given key or value is a string and adds
    quotes around the key if it is.
    """
    if isinstance(var, str):
        return '\'' + var + '\''

    return str(var)
