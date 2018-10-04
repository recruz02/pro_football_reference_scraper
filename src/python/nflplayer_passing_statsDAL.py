from nflplayer_passing_stats import nflplayer_passing_stats
from connect import executesql


def mk_int(s):
    if s is not None:
        s = s.strip()
        return int(s) if s else 0
    else:
        return 0

def mk_float(s):
    if s is not None:
        s = s.strip()
        return float(s) if s else 0.0
    else:
        return 0.0

class nflplayer_passing_statsDAL():

    def __init__(self, pNflplayer_passing_stats):
        self.nflplayer_passing_stats = pNflplayer_passing_stats

    def cleanData(self):
        #self.nflplayer_passing_stats.nflplayerid
        self.nflplayer_passing_stats.year = mk_int(self.nflplayer_passing_stats.year)
        self.nflplayer_passing_stats.age = mk_int(self.nflplayer_passing_stats.age)
        #self.nflplayer_passing_stats.team
        #self.nflplayer_passing_stats.pos
        self.nflplayer_passing_stats.uniform_number = mk_int(self.nflplayer_passing_stats.uniform_number)
        self.nflplayer_passing_stats.g = mk_int(self.nflplayer_passing_stats.g)
        self.nflplayer_passing_stats.gs = mk_int(self.nflplayer_passing_stats.gs)
        #self.nflplayer_passing_stats.qb_rec
        self.nflplayer_passing_stats.pass_cmp = mk_int(self.nflplayer_passing_stats.pass_cmp)
        self.nflplayer_passing_stats.pass_att = mk_int(self.nflplayer_passing_stats.pass_att)
        self.nflplayer_passing_stats.pass_cmp_perc = mk_float(self.nflplayer_passing_stats.pass_cmp_perc)
        self.nflplayer_passing_stats.pass_yds = mk_int(self.nflplayer_passing_stats.pass_yds)
        self.nflplayer_passing_stats.pass_td = mk_int(self.nflplayer_passing_stats.pass_td)                  
        self.nflplayer_passing_stats.pass_td_perc = mk_float(self.nflplayer_passing_stats.pass_td_perc)
        self.nflplayer_passing_stats.pass_int = mk_int(self.nflplayer_passing_stats.pass_int)
        self.nflplayer_passing_stats.pass_int_perc = mk_float(self.nflplayer_passing_stats.pass_int_perc)      
        self.nflplayer_passing_stats.pass_long = mk_int(self.nflplayer_passing_stats.pass_long)
        self.nflplayer_passing_stats.pass_yds_per_att = mk_float(self.nflplayer_passing_stats.pass_yds_per_att)
        self.nflplayer_passing_stats.pass_adj_yds_per_att = mk_float(self.nflplayer_passing_stats.pass_adj_yds_per_att)
        self.nflplayer_passing_stats.pass_yds_per_cmp = mk_float(self.nflplayer_passing_stats.pass_yds_per_cmp)
        self.nflplayer_passing_stats.pass_yds_per_g = mk_float(self.nflplayer_passing_stats.pass_yds_per_g)
        self.nflplayer_passing_stats.pass_rating = mk_float(self.nflplayer_passing_stats.pass_rating)             
        self.nflplayer_passing_stats.qbr = mk_float(self.nflplayer_passing_stats.qbr)
        self.nflplayer_passing_stats.pass_sacked = mk_int(self.nflplayer_passing_stats.pass_sacked)
        self.nflplayer_passing_stats.pass_sacked_yds = mk_int(self.nflplayer_passing_stats.pass_sacked_yds)              
        self.nflplayer_passing_stats.pass_net_yds_per_att = mk_float(self.nflplayer_passing_stats.pass_net_yds_per_att)
        self.nflplayer_passing_stats.pass_adj_net_yds_per_att = mk_float(self.nflplayer_passing_stats.pass_adj_net_yds_per_att)
        self.nflplayer_passing_stats.pass_sacked_perc = mk_float(self.nflplayer_passing_stats.pass_sacked_perc)
        self.nflplayer_passing_stats.comebacks = mk_int(self.nflplayer_passing_stats.comebacks)
        self.nflplayer_passing_stats.gwd = mk_int(self.nflplayer_passing_stats.gwd)
        self.nflplayer_passing_stats.av = mk_int(self.nflplayer_passing_stats.av)

    def insert(self):

        self.cleanData()

        sql = """
            INSERT INTO nflplayer_passing_stats 
            (
                nflplayerid,
                player_year,
                age,
                team,
                player_position,
                player_number,
                games_played,
                games_started,
                qb_record,
                completions,
                attempts,
                completion_percentage,
                yards,
                touchdowns,
                touchdown_percentage,
                interceptions,
                interception_percentage,
                longest_completion,
                yards_per_attempt,
                adjusted_yards_per_attempt,
                yards_per_completion,
                yards_per_game,
                qb_rating,
                qb_rating_espn,
                sacked,
                sacked_yards,
                net_yards_per_pass,
                adjusted_net_yards_per_pass,
                sacked_percentage,
                fourth_quarter_comebacks,
                game_winning_drives,
                approximate_value
            )
            VALUES 
            (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s
            )
            """

        data = (
            self.nflplayer_passing_stats.nflplayerid,
            self.nflplayer_passing_stats.year,
            self.nflplayer_passing_stats.age,
            self.nflplayer_passing_stats.team,
            self.nflplayer_passing_stats.pos,
            self.nflplayer_passing_stats.uniform_number,
            self.nflplayer_passing_stats.g,
            self.nflplayer_passing_stats.gs,
            self.nflplayer_passing_stats.qb_rec,
            self.nflplayer_passing_stats.pass_cmp,
            self.nflplayer_passing_stats.pass_att,
            self.nflplayer_passing_stats.pass_cmp_perc,
            self.nflplayer_passing_stats.pass_yds,
            self.nflplayer_passing_stats.pass_td,                   
            self.nflplayer_passing_stats.pass_td_perc,
            self.nflplayer_passing_stats.pass_int,
            self.nflplayer_passing_stats.pass_int_perc,                   
            self.nflplayer_passing_stats.pass_long,
            self.nflplayer_passing_stats.pass_yds_per_att,
            self.nflplayer_passing_stats.pass_adj_yds_per_att,                    
            self.nflplayer_passing_stats.pass_yds_per_cmp,
            self.nflplayer_passing_stats.pass_yds_per_g,
            self.nflplayer_passing_stats.pass_rating,                    
            self.nflplayer_passing_stats.qbr,
            self.nflplayer_passing_stats.pass_sacked,
            self.nflplayer_passing_stats.pass_sacked_yds,                    
            self.nflplayer_passing_stats.pass_net_yds_per_att,
            self.nflplayer_passing_stats.pass_adj_net_yds_per_att,
            self.nflplayer_passing_stats.pass_sacked_perc,  
            self.nflplayer_passing_stats.comebacks,  
            self.nflplayer_passing_stats.gwd,  
            self.nflplayer_passing_stats.av)

        print(self.nflplayer_passing_stats.toString())
        executesql(sql, data)

    def delete(self, passing_stat_id):
        sql = "DELETE FROM nflplayer_passing_stats where passing_stat_id = %s"
        data = passing_stat_id
        executesql(sql, data)

    def delete_player_stats(self):
        sql = "DELETE FROM nflplayer_passing_stats WHERE nflplayerid = %s"
        data = self.nflplayer_passing_stats.nflplayerid
        executesql(sql, data)
