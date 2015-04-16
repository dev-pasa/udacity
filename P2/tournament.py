#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def registerPlayer(name):
    conn = connect()
    c = conn.cursor()
    SQL = 'INSERT INTO players (name) VALUES (%s);'
    data = (name,)
    c.execute(SQL, data)
    conn.commit()
    conn.close()

def countPlayers():
    conn = connect()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM players')
    result = c.fetchall()
    for row in result:
        return row[0]
    conn.close()
    
def deletePlayers():
    conn = connect()
    c = conn.cursor()
    c.execute('DELETE FROM players')
    conn.commit()
    conn.close()
    
def deleteMatches():
    conn = connect()
    c = conn.cursor()
    c.execute('DELETE FROM matches')
    conn.commit()
    conn.close()
    
    
def reportMatch(winner, loser):
    conn = connect()
    c = conn.cursor()
    SQL = 'INSERT INTO matches (p1, p2, winner) VALUES (%s, %s, %s);'
    data = (winner, loser, winner,)
    c.execute(SQL, data)
    conn.commit()
    conn.close()
    
def playerStandings():
    conn = connect()
    c = conn.cursor()
    c.execute('SELECT * from playerSTANDINGS')
    result = c.fetchall()
    return [ row for row in result]
    conn.close()
    
def swissPairings():
    conn = connect()
    c = conn.cursor()
    c.execute('SELECT a.id, a.name, b.id, b.name FROM playerSTANDINGS AS a, playerSTANDINGS AS b WHERE a.wins = b.wins and a.id > b.id')
    result = c.fetchall()
    return [ row for row in result]
    conn.close()

