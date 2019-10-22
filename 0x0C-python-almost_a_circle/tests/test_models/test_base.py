#!/usr/bin/python3
"""
Unittest for base.py
"""


import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """tests instances, methods from base class"""
    def setUp(self):
        """sets variable everytime"""
        Base._Base__nb_objects = 0

    def test_type_class(self):
        """tests if class exists"""
        self.assertEqual(str(type(Base())), "<class 'models.base.Base'>")

    def test_create_id_default(self):
        """tests whether id is being created correctly or not"""
        b1 = Base()
        b2 = Base()
        self.assertEqual((b1.id), 1)
        self.assertEqual((b2.id), 2)

    def test_create_id_custom(self):
        """id custom"""
        b1 = Base(14)
        b3 = Base(35)
        self.assertEqual((b1.id), 14)
        self.assertEqual((b3.id), 35)

    def test_args(self):
        with self.assertRaises(TypeError) as e:
            b1 = Base(12, 23)

    def test_negative(self):
        b5 = Base(-5)
        self.assertEqual((b5.id), (-5))

if __name__ == '__main__':
    unittest.main()
