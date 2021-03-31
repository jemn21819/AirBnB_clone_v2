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

    def testPep8Unittest(self):
        """
        Testing pep8 validation for unittest
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_console.py'])

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

    def test_help_help(self):
        """tests if the f of help command is correct"""
        line1 = "Documented commands (type help <topic>):"
        line2 = "========================================"
        line3 = "Amenity    City  Place   State  all    create   help  show"
        line4 = "BaseModel  EOF   Review  User   count  destroy  quit  update"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        line = f.getvalue()
        self.assertIn(line1, line)
        self.assertIn(line2, line)
        self.assertIn(line3, line)
        self.assertIn(line4, line)

    def test_prompt(self):
        """Tests if the prompt is the correct"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())
