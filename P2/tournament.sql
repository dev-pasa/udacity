-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
--
-- Create database in tournament.sql



CREATE DATABASE tournament;
\c tournament;
--
--Players table have a name and id set up.
CREATE TABLE players (id SERIAL PRIMARY KEY, name TEXT);
--
--Matches table have p1 and p2 for the 2 players and a winner column which references the id in players.
CREATE TABLE matches (p1 INTEGER, p2 INTEGER, winner INTEGER);
--
--The number of wins for each player.
CREATE VIEW countWIN AS SELECT id, COUNT(winner) AS wins FROM players LEFT JOIN matches on winner = id GROUP BY id;
--
--Finding the number of matches each player has played.
CREATE VIEW countMATCHES AS SELECT id, count(winner) AS matches FROM players LEFT JOIN matches ON p1 = id or p2 =id GROUP BY id;
--
--The player standings.
CREATE VIEW playerSTANDINGS AS SELECT players.id, name, wins, matches FROM players JOIN countWIN ON players.id = countWIN.id JOIN countMATCHES ON players.id = countMATCHES.id ORDER BY wins DESC;



