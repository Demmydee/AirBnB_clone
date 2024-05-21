#!/usr/bin/python3
"""test amenity module """
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel


class test_Amenity(test_basemodel):
    """ test amenity class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.name), str)
