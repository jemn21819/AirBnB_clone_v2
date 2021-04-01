#!/usr/bin/python3
"""Unittest for db_storage"""
import unittest
import pep8
import sys
import os
from models import storage
from models.engine import db_storage


class TestDbStorage(unittest.TestCase):
    """
    Unittest for db_storae
    """
    def testPep8(self):
        """
        Unittest for pep8 complaince
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style error (and warnings).')

    def testPep8(self):
        """
        Unittest for pep8 complaince
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_engine/\
                                        test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style error (and warnings).')
