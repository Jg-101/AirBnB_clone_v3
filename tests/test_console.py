#!/usr/bin/python3
""" Test for console """
import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test Suite for the console"""

    @classmethod
    def set_up_class(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def tear_down(cls):
        """at the end of the test this will tear it down"""
        del cls.consol

    def tear_down(self):
        """Remove temporary file (file.json) created as a result"""
        if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
            try:
                os.remove("file.json")
            except Exception:
                pass

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_empty_line(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())


if __name__ == "__main__":
    unittest.main()
