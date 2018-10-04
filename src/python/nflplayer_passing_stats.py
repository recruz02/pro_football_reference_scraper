from bs4 import BeautifulSoup

def xstr(s):
    return '' if s is None else str(s)

# CREATE CLASS OBJECT
class nflplayer_passing_stats:

    def __init__(self, pNflplayerid):
        self.nflplayerid = pNflplayerid
        self.year = None
        self.age = None
        self.team = None
        self.pos = None
        self.uniform_number = None
        self.g = None
        self.gs = None
        self.qb_rec = None
        self.pass_cmp = None
        self.pass_att = None
        self.pass_cmp_perc = None
        self.pass_yds = None
        self.pass_td = None                   
        self.pass_td_perc = None
        self.pass_int = None
        self.pass_int_perc = None                   
        self.pass_long = None
        self.pass_yds_per_att = None
        self.pass_adj_yds_per_att = None                    
        self.pass_yds_per_cmp = None
        self.pass_yds_per_g = None
        self.pass_rating = None                    
        self.qbr = None
        self.pass_sacked = None
        self.pass_sacked_yds = None                    
        self.pass_net_yds_per_att = None
        self.pass_adj_net_yds_per_att = None
        self.pass_sacked_perc = None  
        self.comebacks = None  
        self.gwd = None  
        self.av = None  

    def toString(self):
        return "\"" + xstr(self.nflplayerid) + "\"" + ",\"" + xstr(self.age) + "\"" + ",\"" + xstr(self.team) + "\"" + ",\"" + xstr(self.pos) + "\"" + ",\"" + xstr(self.uniform_number) + "\"" + ",\"" + xstr(self.g) + "\"" + ",\"" + xstr(self.gs) + "\"" + ",\"" + xstr(self.qb_rec) + "\"" + ",\"" + xstr(self.pass_cmp) + "\"" + ",\"" + xstr(self.pass_att) + "\"" + ",\"" + xstr(self.pass_cmp_perc) + "\"" + ",\"" + xstr(self.pass_yds) + "\"" + ",\"" + xstr(self.pass_td) + "\"" + ",\"" + xstr(self.pass_td_perc) + "\"" + ",\"" + xstr(self.pass_int) + "\"" + ",\"" + xstr(self.pass_int_perc) + "\"" + ",\"" + xstr(self.pass_long) + "\"" + ",\"" + xstr(self.pass_yds_per_att) + "\"" + ",\"" + xstr(self.pass_adj_yds_per_att) + "\"" + ",\"" + xstr(self.pass_yds_per_cmp) + "\"" + ",\"" + xstr(self.pass_yds_per_g) + "\"" + ",\"" + xstr(self.pass_rating) + "\"" + ",\"" + xstr(self.qbr) + "\"" + ",\"" + xstr(self.pass_sacked) + "\"" + ",\"" + xstr(self.pass_sacked_yds) + "\"" + ",\"" + xstr(self.pass_net_yds_per_att) + "\"" + ",\"" + xstr(self.pass_adj_net_yds_per_att) + "\"" + ",\"" + xstr(self.pass_sacked_perc) + "\"" + ",\"" + xstr(self.comebacks) + "\"" + ",\"" + xstr(self.gwd) + "\"" + ",\"" + xstr(self.av) + "\"" + "\n"
		
    def toJSON(self):
        return None

    def populateData(self, pBeautifulSoupData):

        for data in pBeautifulSoupData:
            #print(data)                     # TABLE DATA
            #print(data["data-stat"])        # COLUMN NAME
            #print(data.text)                # ACTUAL DATA
            
            #self.year = td.replace('passing.','')
            if data["data-stat"] == "age": self.age = data.text
            if data["data-stat"] == "team": self.team = data.text
            if data["data-stat"] == "pos": self.pos = data.text
            if data["data-stat"] == "uniform_number": self.uniform_number = data.text
            if data["data-stat"] == "g": self.g = data.text
            if data["data-stat"] == "gs": self.gs = data.text
            if data["data-stat"] == "qb_rec": self.qb_rec = data.text
            if data["data-stat"] == "pass_cmp": self.pass_cmp = data.text
            if data["data-stat"] == "pass_att": self.pass_att = data.text
            if data["data-stat"] == "pass_cmp_perc": self.pass_cmp_perc = data.text
            if data["data-stat"] == "pass_yds": self.pass_yds = data.text
            if data["data-stat"] == "pass_td": self.pass_td = data.text                   
            if data["data-stat"] == "pass_td_perc": self.pass_td_perc = data.text
            if data["data-stat"] == "pass_int": self.pass_int = data.text
            if data["data-stat"] == "pass_int_perc": self.pass_int_perc = data.text                   
            if data["data-stat"] == "pass_long": self.pass_long = data.text
            if data["data-stat"] == "pass_yds_per_att": self.pass_yds_per_att = data.text
            if data["data-stat"] == "pass_adj_yds_per_att": self.pass_adj_yds_per_att = data.text                    
            if data["data-stat"] == "pass_yds_per_cmp": self.pass_yds_per_cmp = data.text
            if data["data-stat"] == "pass_yds_per_g": self.pass_yds_per_g = data.text
            if data["data-stat"] == "pass_rating": self.pass_rating = data.text                    
            if data["data-stat"] == "qbr": self.qbr = data.text
            if data["data-stat"] == "pass_sacked": self.pass_sacked = data.text
            if data["data-stat"] == "pass_sacked_yds": self.pass_sacked_yds = data.text                    
            if data["data-stat"] == "pass_net_yds_per_att": self.pass_net_yds_per_att = data.text
            if data["data-stat"] == "pass_adj_net_yds_per_att": self.pass_adj_net_yds_per_att = data.text
            if data["data-stat"] == "pass_sacked_perc": self.pass_sacked_perc = data.text  
            if data["data-stat"] == "comebacks": self.comebacks = data.text  
            if data["data-stat"] == "gwd": self.gwd = data.text  
            if data["data-stat"] == "av": self.av = data.text          

