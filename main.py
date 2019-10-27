import json
import requests

username_url = "https://r6tab.com/api/search.php?platform=uplay&search="#+{name}
player_id_url = "https://r6tab.com/api/player.php?p_id="#+{id}

class playerClass(object):
    def __init__(self, name):
        self.name = name

    def getPlayerID(self):
        response = requests.get(username_url + self.name)
        if response.status_code == 200:
            content = json.loads(response.content.decode('utf-8'))
            self.p_id = content["results"][0]["p_id"]
            return
        else:
            print("no player found")
            return None

    def getTabData(self):
        if self.p_id:
            response = requests.get(player_id_url + self.p_id)
            if response.status_code == 200:
                content = json.loads(response.content.decode('utf-8'))

                #display formatted json, delete l8er
                print(json.dumps(content, indent=4, sort_keys=True))
                return
        else:
            print("no ID found")
            return


    def setStats(self, rank, seasKD, seasWL, ovrKD, ovrWL):
        self.rank = rank
        self.seasKD = seasKD
        self.seasWL = seasWL
        self.ovrKD = ovrKD
        self.ovrWL = ovrWL



# ranks = ("bronze/silver", "gold III", "gold II", "gold I", "plat III", "plat II",
#             "plat I", "diamond", "champion")

player = playerClass("SirPivinton")
player.getPlayerID()
player.getDetails()
