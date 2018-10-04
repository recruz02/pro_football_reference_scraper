#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()
        
        # EXAMPLE:
        # >>> cur.execute("INSERT INTO foo VALUES (%s)", "bar")    # WRONG
        # >>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar"))  # WRONG
        # >>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar",)) # correct
        # >>> cur.execute("INSERT INTO foo VALUES (%s)", ["bar"])  # correct

		# EXAMPLE: select from nflplayer table
        print('nflplayer table:')
        sql = 'SELECT nflplayerid, first_name, last_name, player_position, pro_football_reference_url FROM nflplayer where player_position = %s'
        args= ["QB"]
        cur.execute(sql, args)

        
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def executeselect(sql, args):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        # print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()

		# execute sql
        cur.execute(sql, args)
		
		# retrieve database
        rows = cur.fetchall()
        #rows.append(cur.fetchone())

        # close the communication with the PostgreSQL
        cur.close()
		
        # return dataset
        return rows

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def executesql(sql, args):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        # print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()

		# execute sql
        cur.execute(sql, args)
		
        # save data to postgresql database
        conn.commit()

        # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
def executesql_many(sql, args):
    #insert multiple vendors into the vendors table
    #sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,args)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
def test_insert():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
        # create a cursor
        cur = conn.cursor()
        
        # EXAMPLE:
        # >>> cur.execute("INSERT INTO foo VALUES (%s)", "bar")    # WRONG
        # >>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar"))  # WRONG
        # >>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar",)) # correct
        # >>> cur.execute("INSERT INTO foo VALUES (%s)", ["bar"])  # correct

		# EXAMPLE: select from nflplayer table
        sql = """                
            insert into nflplayer_passing_stats
            (
            nflplayerid, age, team, player_position, player_number,
            games_played, games_started, qb_record, completions, attempts, completion_percentage, yards, 
            touchdowns, touchdown_percentage, interceptions, interception_percentage, longest_completion, 
            yards_per_attempt, adjusted_yards_per_attempt, yards_per_completion, yards_per_game, qb_rating, 
            qb_rating_espn, sacked, sacked_yards, net_yards_per_pass, adjusted_net_yards_per_pass, sacked_percentage, 
            fourth_quarter_comebacks, game_winning_drives, approximate_value

            )
            values
            (
            'c4bfef6c-7932-4f54-9685-63d3d0136b04','32','SDG','QB','0','2','2','1-1','30','43','69.8',
            '345','3','7.0','0','0.0','49','8.0','9.4','11.5','172.5','116.9',
            '0.0','5','29','6.58','7.83','10.4','0','0','0'
            )
            """
        args = None
        cur.execute(sql, args)    

        conn.commit()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

#TO TEST LATER
"""

if __name__ == '__main__':
    # insert one vendor
    insert_vendor("3M Co.")
    # insert multiple vendors
    insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])
"""
 
# TO IMPLEMENT:
"""
connection = psycopg.connect('dbname=Birds', 'user=robert')
mark = connection.cursor()
statement = 'INSERT INTO ' + table + ' (' + columns + ') VALUES (' + values + ')'
mark.execute(statement)
connection.commit()  
"""


# TO IMPLEMENT
"""
UNIT TESTS
"""


# TO IMPLEMENT: INSERT INTO POSTGRESQL AS JSON DATA
"""
cursor.execute("
    INSERT INTO MyTable (channel, report_id, report_data)
    SELECT 
      src.MyJSON->'account_id',
      src.MyJSON->'id',
      src.MyJSON
    FROM (
      SELECT %s AS MyJSON
    ) src
  ",
  (data2,)
)
"""

# SAMPLE 3
"""
population = 10008
 
data = [
('city 1', 'MAC', 'distrct 1', 16822),
('city 2', 'PSE', 'distrct 2', 15642),
('city 3', 'ZWE', 'distrct 3', 11642),
('city 4', 'USA', 'distrct 4', 14612),
('city 5', 'USA', 'distrct 5', 17672),
]
 
sql = "insert into city(name, countrycode, district, population) 
VALUES(%s, %s, %s, %s)"
 
number_of_rows = cursor.executemany(sql, data)
db.commit()
 
db.close()
"""

# SAMPLE 4
"""
    query =  "INSERT INTO items (info, city, price) VALUES (%s, %s, %s);"
    data = (info, city, price)
"""


 
 
if __name__ == '__main__':
    connect()
    #test_insert()
