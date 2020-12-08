from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository


#1 - Create and Save Albums
def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


#2 - Delete all Albums
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


#3 - Find Albums by their ID
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist.repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist)
    return album


#4 - List All Albums
def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist)
        albums.append(album)
    return albums


## EXTENSIONS ##

#1 (in artist_repository.py)


#2 - Edit Albums
def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.name]
    run_sql(sql, values)


#3 - Delete Albums
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)
