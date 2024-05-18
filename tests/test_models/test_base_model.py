#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        x = self.value()
        self.assertEqual(type(x), self.value)

    def test_kwargs(self):
        """ """
        x = self.value()
        copy = x.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is x)

    def test_kwargs_int(self):
        """ """
        x = self.value()
        copy = x.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        x = self.value()
        x.save()
        i = self.name + "." + x.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[i], x.to_dict())

    def test_str(self):
        """ """
        x = self.value()
        self.assertEqual(str(x), '[{}] ({}) {}'.format(self.name, x.id,
                         x.__dict__))

    def test_todict(self):
        """ """
        x = self.value()
        n = x.to_dict()
        self.assertEqual(x.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertNotEqual(new.created_at, new.updated_at)
