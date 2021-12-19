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
file handler reads and writes datastore entries to and from the disk.
file paths are case sensitive.
"""

import os.path
import datetime

from pathlib import Path

from dictstore.exceptions import InvalidFileExtension


def generate_file_header_string() -> str:
    """Generates file header string for the data file"""
    header = '// Python Dictstore File\n'
    date_string = str(datetime.datetime.now())
    header += '// Last Rewrite: ' + date_string + '\n'
    return header


class FileHandler:
    """
    handles the dictstore datastore file(s)
    """

    def __has_valid_file_extension(self):
        """Checks if the given file path ends with .dictstore"""
        if self.file_path.endswith('.dictstore'):
            return True
        return False

    def __init__(self, file_path) -> None:
        """
        creates a file handler for the datastore file.
                Exceptions:
                    OSError
                    InvalidFileExtension
        """

        # store the given file path
        self.file_path = file_path

        # check if the filename is valid
        if not self.__has_valid_file_extension():
            raise InvalidFileExtension()

        # check if file exists at path
        # and create a datastore file if it doesn't exist
        if not os.path.exists(self.file_path):
            Path(os.path.dirname(self.file_path)).mkdir(
                parents=True,
                exist_ok=True
                )
            with open(self.file_path, 'w', encoding='utf-8') as data_file:
                data_file.write(generate_file_header_string())

        # open the file and read its contents
        with open(self.file_path, 'r', encoding='utf-8') as data_file:
            self.file_contents = data_file.read()

    def rewrite_to_file(self, lines) -> None:
        """Writes the given lines to data file"""
        with open(self.file_path, 'w', encoding='utf-8') as data_file:
            data_file.write(generate_file_header_string())
            data_file.writelines(lines)

    def append_to_file(self, string: str) -> None:
        """Appends the given string to data file"""
        with open(self.file_path, 'a', encoding='utf-8') as data_file:
            data_file.write(string)

    def read_from_file(self) -> str:
        """
        Reads the contents of data file and
        returns all the contents of file
        without the first two lines
        """
        with open(self.file_path, 'r', encoding='utf-8') as data_file:
            data_file.readline()
            data_file.readline()
            return data_file.readlines()
