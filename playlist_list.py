import json
from playnaliticsDB import playnaliticsDB

class PlaylistList:

    def __init__(self) -> None:
        self.__db = playnaliticsDB()

    def load_list(self, user_id:str):
        self.db.connect()
        self.__list = self.db.select_playlists(user_id)
        self.db.close()

    @property
    def db(self):
        return self.__db
    
    @property
    def list(self):
        return self.__list

    @property
    def dictionary(self):
        dict = {"items":[]}
        for item in self.list:
            dict["items"].append({"id":item[0], "name":item[1]})
        return dict

    def write_json(self, filename:str):
        with open(filename, 'w') as output_file:
            json.dump(self.dictionary, output_file, indent=4)

