#!/usr/bin/python3
"""Unittest for db_storage"""
import unittest
import pep8
import sys
import os
import inspect
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
class TestDbStorage(unittest.TestCase):
    """
    Unittest for db_storage
    """
    def testPep8(self):
        """
        Unittest for pep8 complaince
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py',
                                        'tests/test_models/test_engine/\
                                        test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warnings).')
