#!/usr/bin/python3
"""
Contains the TestAmenityDocs classes
"""

from datetime import datetime
import inspect
import models
from models import amenity
from models.base_model import BaseModel
from models import user
import pep8
import unittest
Amenity = amenity.Amenity

User = user.User


class TestAmenityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Amenity class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """Test for the amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test for the presence of docstrings in Amenity methods"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

        def test_email_attr(self):
            """Test that User has attr email, and it's an empty string"""
            user = User()
            self.assertTrue(hasattr(user, "email"))
            self.assertEqual(user.email, None)
            self.assertEqual(user.email, "")

        def test_password_attr(self):
            """Test that User has attr password, and it's an empty string"""
            user = User()
            self.assertTrue(hasattr(user, "password"))
            self.assertEqual(user.password, None)
            self.assertEqual(user.password, "")

        def test_first_name_attr(self):
            """Test that User has attr first_name, and it's an empty string"""
            user = User()
            self.assertTrue(hasattr(user, "first_name"))
            self.assertEqual(user.first_name, None)
            self.assertEqual(user.first_name, "")

        def test_last_name_attr(self):
            """Test that User has attr last_name, and it's an empty string"""
            user = User()
            self.assertTrue(hasattr(user, "last_name"))
            self.assertEqual(user.last_name, None)
            self.assertEqual(user.last_name, "")
