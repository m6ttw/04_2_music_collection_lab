import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.album = Album("AM", "Rock", "Arctic Monkeys")

    def test_album_has_title(self):
        self.assertEqual("AM", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("Rock", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("Arctic Monkeys", self.album.artist)