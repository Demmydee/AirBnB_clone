#!/usr/bin/python3
""" test state module"""
from models.state import State
from tests.test_models.test_base_model import test_basemodel


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.name), str)
