from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album


#1 - Create and Save Artists
def save(artist):
    sql =  "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


#2 - Delete all Artists
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)


#3 - Find Artists by their ID
def select(id):
    artist = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist


#4 - List All Artists
def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists


## EXTENSIONS ##


#1 - List all the albums by an artist
def albums(artist):
    albums = []

    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['title'], row['genre'], artist)
        albums.append(album)
    return albums


#2 - Edit Artists
def update(artist):
    sql = "UPDATE artists SET name = %s WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)


# - Delete Artists
def delete(id):
    sql = "DELETE FROM artists WHERE is = %s"
    values = [id]
    run_sql(sql, values)