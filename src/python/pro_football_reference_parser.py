import sys
import urllib.request

from bs4 import BeautifulSoup
from nflplayer_passing_stats import nflplayer_passing_stats
from nflplayer_passing_statsDAL import nflplayer_passing_statsDAL
from nflplayerDAL import nflplayerDAL

def getHtmlDoc(html_folderlocation, html_pagename):
    with open(html_pagename, encoding="utf8") as r:
        html_doc = r.read()

    return html_doc

def getHtmlPage(pUrl):
    try:
        html_request = urllib.request.urlopen(pUrl)
        #print(html_request.read())

        html_doc = html_request.read()
 
        return html_doc

    except:
        print("Error retreiving html_page")


def save_result_stat_list(result_stat_list):
    for statline in result_stat_list:
        if statline is not None:
            nflpassingDAL = nflplayer_passing_statsDAL(statline)
            nflpassingDAL.insert()
        

# TO DO - UNIT TESTING, DATA VALIDATION
def pro_football_reference_scrape_passing_tables(html_doc, pNflplayer):

    # INITIALIZE LOCAL VARIABLES
    result_stat_list = []

    try:
        # PARSE THE HTML WITH BEAUTIFUL SOUP
        html_soup = BeautifulSoup(html_doc, 'html.parser')
        #print(html_soup)
        #print(html_soup.prettify())

        # LOOP THROUGH THE FULL TABLES
        nflplayer_full_table_stats = html_soup.find_all(class_='full_table')
		
        # GET ONLY THE ACTUAL PASSING TABLES (NOT THE CLONE TABLES)
        for tr in nflplayer_full_table_stats:

            # GET TABLE ROW ID
            table_row_id = None
            try:
                table_row_id = tr['id']
                print(table_row_id)
            except:
                continue
                #print("Unable to grab table row id")

            # VALIDATE TABLE ROW ID; IGNORE 'CLONE TABLES'
            if table_row_id is not None and 'passing.' in table_row_id and 'clone' not in table_row_id:

                # INITIALIZE NEW PASSING STAT OBJECT
                passing_stat = nflplayer_passing_stats(pNflplayer.nflplayerid) # NFLPLAYERID
                passing_stat.year = table_row_id.replace('passing.','')

                # OBTAIN ALL TD RECORDS
                # POPULATE PASSING STAT RECORD
                tdSoupData = tr.find_all('td')
                passing_stat.populateData(tdSoupData)

                # ADD TO RESULT STAT LIST
                result_stat_list.append(passing_stat)
                passing_stat = None

        return result_stat_list

    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("Error Ocurred")

def pro_football_reference_passing_parser():

    # 1 - GET LIST OF NFL QBs
    myPlayers = nflplayerDAL()
    myPlayers.selectQbs()

    # 2 - for each player, scrape the data
    for myPlayer in myPlayers.nflplayers:
        html_doc = getHtmlPage(myPlayer.url)
        result_stat_list = pro_football_reference_scrape_passing_tables(html_doc, myPlayer)

        # 3 - save result set to database (POSTGRESQL)
        save_result_stat_list(result_stat_list)

if __name__== "__main__":
    print("Hello, world!")
    pro_football_reference_passing_parser()
