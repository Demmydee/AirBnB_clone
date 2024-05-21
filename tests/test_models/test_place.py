#!/usr/bin/python3
"""test place module """
from models.place import Place
from tests.test_models.test_base_model import test_basemodel


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.description), str)

    def test_numRooms(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.numRooms), int)

    def test_numBath(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.numBath), int)

    def test_maxGuest(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.maxGuest), int)

    def test_nightPrice(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.nightPrice), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)
