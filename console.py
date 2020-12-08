import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# 1 - Create and Save Artists/Albums
artist_1 = Artist("Arctic Monkeys")
artist_repository.save(artist_1)

album = Album("AM", "Rock", artist_1)
album_repository.save(album)
album = Album("Suck It and See", "Rock", artist_1)
album_repository.save(album)
album = Album("Humbug", "Rock", artist_1)
album_repository.save(album)

#2 - Delete all Artists/Albums
album_repository.delete_all()
artist_repository.delete_all()

#3 - Find Artists/Albums by their ID
album_repository.select(1)
artist_repository.select(1)

#4 - List All Artists/Albums
album_repository.select_all()
artist_repository.select_all()

## EXTENSIONS ##

#1 - List all the albums by an artist
artist_repository.albums(1)

#2 - Edit Artists/Albums
album_repository.update(1)
artist_repository.update(1)

#3 - Delete Artists/Albums
album_repository.delete(1)
artist_repository.delete(1)