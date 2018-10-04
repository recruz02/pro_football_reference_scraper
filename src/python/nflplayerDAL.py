from nflplayer import nflplayer
from connect import executeselect
from connect import executesql

class nflplayerDAL(nflplayer):

    def __init__(self):
        self.nflplayers = []

        self.nflplayerid = None
        self.url = None
        self.first_name = None
        self.last_name = None
        self.player_position = None
        self.player_height = None
        self.player_weight = None
        self.birthdate = None
        self.birthplace = None
        self.college = None 

    def selectAll(self):

        self.nflplayers = []
        myPlayer = None

        sql = """
            SELECT 
                nflplayerid, 
                first_name, 
                last_name, 
                player_position, 
                player_height, 
                player_weight, 
                birthdate, 
                birthplace, 
                college, 
                "timestamp", 
                pro_football_reference_url
            FROM 
                nflplayer"""

        args = None

        rows = executeselect(sql, args)

        for row in rows:
            print(row)
            myPlayer = nflplayer()
            myPlayer.nflplayerid = row[0]
            myPlayer.first_name = row[1]
            myPlayer.last_name = row[2]
            myPlayer.player_position = row[3]
            myPlayer.player_height = row[4]
            myPlayer.player_weight = row[5]
            myPlayer.birthdate = row[6]
            myPlayer.birthplace = row[7]
            myPlayer.college = row[8]
            myPlayer.url = row[10]

            self.nflplayers.append(myPlayer)
            myPlayer = None

    def selectQbs(self):

        self.nflplayers = []
        myPlayer = None

        sql = """
            SELECT 
                nflplayerid, 
                first_name, 
                last_name, 
                player_position, 
                player_height, 
                player_weight, 
                birthdate, 
                birthplace, 
                college, 
                "timestamp", 
                pro_football_reference_url
            FROM 
                nflplayer
            WHERE
                player_position LIKE '%QB%'
                and (last_name NOT LIKE 'B%' AND last_name NOT LIKE 'R%')
            """

        args = None

        rows = executeselect(sql, args)

        for row in rows:
            print(row)
            myPlayer = nflplayer()
            myPlayer.nflplayerid = row[0]
            myPlayer.first_name = row[1]
            myPlayer.last_name = row[2]
            myPlayer.player_position = row[3]
            myPlayer.player_height = row[4]
            myPlayer.player_weight = row[5]
            myPlayer.birthdate = row[6]
            myPlayer.birthplace = row[7]
            myPlayer.college = row[8]
            myPlayer.url = row[10]

            self.nflplayers.append(myPlayer)
            myPlayer = None

    def insert(self):
               
            sql = """
                INSERT INTO nflplayer
                ( 
                    first_name, 
                    last_name, 
                    player_position, 
                    player_height, 
                    player_weight, 
                    birthdate, 
                    birthplace, 
                    college, 
                    pro_football_reference_url
                )
                VALUES 
                (
                    %s, %s, %s, %s, %s, 
                    %s, %s, %s, %s
                )
                """

            args = (
                self.first_name,
                self.last_name,
                self.player_position,
                self.player_height,
                self.player_weight,
                self.birthdate,
                self.birthplace,
                self.college,
                self.url)

            executesql(sql, args)
        
if __name__ == '__main__':

    # TEST
    myPlayers = nflplayerDAL()
    myPlayers.selectQbs()

    for myPlayer in myPlayers.nflplayers:
        print(myPlayer.first_name)
        print(myPlayer.url)
