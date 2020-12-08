import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    
    def setUp(self):
        self.artist = Artist("Arctic Monkeys")

    def test_artist_has_name(self):
        self.assertEqual("Arctic Monkeys", self.artist.name)