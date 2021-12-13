"""
tests module for dictstore
"""

import unittest
from dictstore import file_handler
import dictstore.exceptions

# TODO: Move each class to a separate module for better maintainability


class TestFileHandler(unittest.TestCase):
    """
    Unit tests for FileHandler class
    """
    def test_invalid_filename(self):
        """
        checks if an invalid filename raises
        the InvalidFileExtension exception.
        """
        with self.assertRaises(dictstore.exceptions.InvalidFileExtension):
            file_handler.FileHandler('file_name_without_dictstore_extension')


if __name__ == '__main__':
    unittest.main()
