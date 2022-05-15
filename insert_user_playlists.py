import pymysql

#will be loaded from a json
playlist_list = [{"ID":"4XTcm8oG4wHKwFWCQ0eLw4", "title":"Italian Synthwave"}]
#this is my ID
userID = 'spotify:user:1167306845'

sql = """INSERT INTO playlists VALUES(%s, %s, %s, %b)"""
hostname = 'localhost'
username = 'root'
password = ''
database = 'playnaliticsDB'

playnaliticsDB_connection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
playnaliticsDB_cursor = playnaliticsDB_connection.cursor()

for playlist in playlist_list:
    playnaliticsDB_cursor.execute(sql,(playlist["ID"],userID,playlist["title"],False))

playnaliticsDB_connection.commit()
playnaliticsDB_connection.close()
