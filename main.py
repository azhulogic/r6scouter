#TODO: error checking

import json
import requests

username_url = "https://r6tab.com/api/search.php?platform=uplay&search="#+{name}
player_id_url = "https://r6tab.com/api/player.php?p_id="#+{id}
ranks = {
    "21": "Champion",
    "20": "Diamond",
    "19": "Platinum I",
    "18": "Platinum II",
    "17": "Platinum III",
    "16": "Gold I",
    "15": "Gold II",
    "14": "Gold III",
    #let's not even consider stuff below
}

class playerClass(object):
    def __init__(self, name):
        #default constructor
        self.name = name

    def setPlayerName(self, name):
        #sets player name (i.e. in case constructed incorrectly)
        self.name = name

    def getPlayerID(self):
        #gets player_id based on provided username in constructor
        #needs error checking
        response = requests.get(username_url + self.name)
        if response.status_code == 200:
            content = json.loads(response.content.decode('utf-8'))
            self.p_id = content["results"][0]["p_id"]
            return
        else:
            print("no player found, double check .name attribute")
            return None

    def getTabData(self):
        #gets data from R6Tab API based on p_id retrieved from getPlayerID()
        #TODO: check content["playerFound"] (boolean)
        if self.p_id:
            response = requests.get(player_id_url + self.p_id)
            if response.status_code == 200:
                content = json.loads(response.content.decode('utf-8'))

                #TODO: display formatted json, delete l8er
                print(json.dumps(content, indent=4, sort_keys=True))

                #for now just load all the info into this var for breakdown
                #maybe streamline later
                self.playerData = content
                return
        else:
            print("no ID found, have you called getPlayerID?")
            return



    def setStats(self, rank, seasKD, seasWL, ovrKD, ovrWL):
        #sets all pertinent stats into local vars
        #current season (Ember Rise) is season14
        if self.playerData:
            data = self.playerData
            #seasonal rank & mmr:
            self.seasRank = data["p_currentrank"]
            self.seasMMR = data["p_currentmmr"]
            #seasonal max rank & mmr:
            self.seasMaxRank = data["p_maxrank"]
            self.seasMaxMMR = data["p_maxmmr"]
            #seasonal ranked KD and WL:
            self.seasKD = data["seasonal"]["total_rankedkills"]/data["seasonal"]["total_rankeddeaths"]
            self.seasWL = data["seasonal"]["total_rankedwins"]/data["seasonal"]["total_rankedtotal"]
            #overall KD & WL
            self.ovrKD = data["kd"]
            self.ovrWL = data["data"][21]/(data["data"][21]+data["data"][22])
            
            #TODO: the rest of these
            # self.playerData["favattacker"]
            # self.playerData["favdefender"]
            return
        else:
            print("no player data found, have you retrieved it yet?")
            return

#testing
player = playerClass("SirPivinton")
player.getPlayerID()
player.getTabData()
