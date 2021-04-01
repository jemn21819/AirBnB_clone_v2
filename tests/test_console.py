#!/usr/bin/python3
"""Unittests for console.py"""
import unittest
import pep8
import sys
import os
import console
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Test console with unit test
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup for unittest
        """
        cls.console = HBNBCommand()

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass

    def testPep8(self):
        """
        Testing pep8 validation for console
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style error (and wanrnings).')

    def testPep8Unittest(self):
        """
        Testing pep8 validation for unittest
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style error (and wanrnings).')

    def testDocstring(self):
        """
        Test docstring model for console
        """
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring.")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring.")

    def testDocClass(self):
        """
        Testing for class docstring documentation
        """
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring.")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring.")
