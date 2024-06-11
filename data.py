#data.py
def data_import():
    import sqlite3
    import csv
    #create IA2.db
    conn = sqlite3.connect('IA2.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS tblPlayerstats")
    cursor.execute("DROP TABLE IF EXISTS tblPlayers")
    cursor.execute("DROP TABLE IF EXISTS tblStandings")
    

    #Create tblStandings
    with open('tblStandings.csv', 'r',) as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        columns = ', '.join(headers)
        cursor.execute("""CREATE TABLE tblStandings 
        (nationality TEXT, standing INTEGER, gamesPlayed INTEGER,
        win INTEGER, draw INTEGER, loss INTEGER, goalsFor INTEGER,
        goalsAgainst INTEGER, goalsDifference STRING, Points INTEGER)
        """)
        for row in csv_reader:
            cursor.execute("""INSERT INTO tblStandings 
            (nationality, standing, gamesPlayed, win, draw, loss, goalsFor, goalsAgainst, goalsDifference, points) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, row)
    conn.commit()

    # #Create tblPlayerstats
    with open("tblPlayerstats.csv", 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            columns = ', '.join(headers)
            cursor.execute("""CREATE TABLE tblPlayerstats
            (playerID INTEGER, playername STRING, playerlastname STRING,
            Appearances STRING, goalscored STRING,
            assitsprovided STRING, Dribblesper90 STRING, Interceptionsper90 STRING,
            Tacklesper90 STRING, TotalDuelsWonper90 STRING, Savepercentage STRING, Cleansheets STRING)
            """)
            for row in csv_reader:
                cursor.execute("""INSERT INTO tblPlayerstats
                (playerID, playername, playerlastname, Appearances, goalscored, assitsprovided, Dribblesper90, Interceptionsper90, Tacklesper90, TotalDuelsWonper90, Savepercentage, Cleansheets)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, row)
    conn.commit()

    #Create tblPlayerStats
    with open("tblPlayers.csv", 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        columns = ', '.join(headers)
        cursor.execute("""CREATE TABLE tblPlayers
        (nationality TEXT, playerPositionID STRING, jerseyNumber INTEGER, playerBirthDay STRING, playerBirthYear STRING, club STRING, playerID STRING,
        playerFName STRING, playerLName STRING)
        """)
        for row in csv_reader:
            cursor.execute("""INSERT INTO tblPlayers
            (nationality, playerPositionID, jerseyNumber, playerBirthDay, playerBirthYear,  club, playerID, playerFName, playerLName)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, row)
    conn.commit()

    # Complete
    conn.close()

data_import()