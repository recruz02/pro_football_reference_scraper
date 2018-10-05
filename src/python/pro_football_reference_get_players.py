from nflplayerDAL import nflplayerDAL
from bs4 import BeautifulSoup
import urllib.request
import string

"""
Pro Football Reference Last Name "R": https://www.pro-football-reference.com/players/R/
e.g.:
<p><a href="/players/R/RodgAa00.htm">Aaron Rodgers</a> (QB)</b> 2005-2018</p>
<p><a href="/players/R/RivePh00.htm">Philip Rivers</a> (QB)</b> 2004-2018</p>
<p><a href="/players/R/RiveRe00.htm">Reggie Rivers</a> (RB) 1991-1996</p>

FOR EACH A RECORD:
    1) RETRIEVE URL
    2) RETRIEVE FIRST NAME
    3) RETRIEVE LAST NAME
    4) RETRIEVE PLAYER POSITION
    5) SAVE DATA TO POSTGRESQL
"""

def removeParenthesis(str):
    return str.replace('(','').replace(')','')


def pro_football_reference_get_players():

    # LOOP THROUGH EVERY LETTER OF ALPHABET
    for letter in list(string.ascii_uppercase):

        try:
            url = "https://www.pro-football-reference.com/players/" + letter + "/"
            html_request = urllib.request.urlopen(url)
            #print(html_request.read())
            html_doc = html_request.read()
            html_soup = BeautifulSoup(html_doc, 'html.parser')
            #print(html_soup)

            # Example: <div class="section_content" id="div_players">
            nflplayer_containers = html_soup.find('div', id="div_players")
            #print(nflplayer_containers)

            players_container = nflplayer_containers.find_all('p')
            for player in players_container:
                try:
                    print(player)

                    href_tags = player.find(href=True)
                    player_url = "https://pro-football-reference.com" + href_tags['href']
                    player_info = player.text.split(' ')
                    player_first_name = player_info[0]
                    player_last_name = player_info[1]
                    player_position = removeParenthesis(player_info[2])

                    print(player_url)
                    print(player_first_name)
                    print(player_last_name)
                    print(player_position)

                    myPlayer = nflplayerDAL()
                    myPlayer.first_name = player_first_name
                    myPlayer.last_name = player_last_name
                    myPlayer.player_position = player_position
                    myPlayer.url = player_url
                    myPlayer.insert()
                
                except:
                    print("Error Adding Player:" + player)

        except:
            print("Error navigating to Pro-Football-Reference URL")




if __name__ == '__main__':
    pro_football_reference_get_players()
