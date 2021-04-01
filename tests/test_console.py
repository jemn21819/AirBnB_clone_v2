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


class Test_HBNBCommand(unittest.TestCase):
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

    def test_create(self):
        """Test create with space notation"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            test_value = f.getvalue().strip()
        msg = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")

    def test_create_dot_notation(self):
        """Test create with dot notation"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
            test_value = f.getvalue().strip()

    def test_show(self):
        """Test show with space notation"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj_test = storage.all()["BaseModel.{}".format(test_value)]
            command = "show BaseModel {}".format(test_value)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj_test.__str__(), f.getvalue().strip())
        msg = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(msg, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
        self.assertEqual(msg, f.getvalue().strip())

    def test_show_dot_notation(self):
        """Test show with dot notation"""
        msg = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        self.assertEqual(msg, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
        self.assertEqual(msg, f.getvalue().strip())
        msg = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(6767)")
        self.assertEqual(msg, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 35353")
        self.assertEqual(msg, f.getvalue().strip())
        msg = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(4544)")
        self.assertEqual(msg, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(5667)")
        self.assertEqual(msg, f.getvalue().strip())
        msg = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(msg, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(msg, f.getvalue().strip())

    def test_destroy(self):
        """Test destroy with space notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["BaseModel.{}".format(obj_id)]
            command = "destroy BaseModel {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["User.{}".format(obj_id)]
            command = "destroy User {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        msg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(msg, f.getvalue().strip())
