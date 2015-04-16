#Project Description: Tournament Planner

This is a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has three files: 

* `tournament.sql`defining the database schema (SQL table definitions)
* `tournament.py`is the code for the module with different functions.
* `tournament_test.py`is used to test if the module meets the requirement.

##Quick Start

- To run the Vagrant VM, in the terminal ​use the command ​`vagrant up` f​ollowed by`vagrant ssh`.
- To build and access the database we run ​`psql​`followed by `​\i tournament.sql`
- To run the series of tests defined in this test suite, run the program from the command line ​>> `python tournament_test`.​

