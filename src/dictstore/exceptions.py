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
defines all the custom exceptions for dictstore.
"""


class InvalidFileExtension(Exception):
    """
    Raised when a path with invalid file extension
    is passed to the FileHandler.
    """
    def __init__(self) -> None:
        self.message = ("Invalid file extension."
                        "Please check if the path ends with a"
                        " '.dictstore' extension"
                        )

        super().__init__(self.message)
