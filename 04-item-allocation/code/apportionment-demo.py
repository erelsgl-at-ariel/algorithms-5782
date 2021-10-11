#!python3

"""
A demo of apportionment methods.
"""

# from here: https://github.com/martinlackner/apportionment
import apportionment.methods as app

parties = ['A', 'B', 'C']
votes = [40, 135, 325]
seats = 5
app.compute("hamilton", votes, seats, parties, verbose=True)
app.compute("jefferson", votes, seats, parties, verbose=True)

parties = ['A', 'B']
votes = [40, 135]
seats = 2
app.compute("hamilton", votes, seats, parties, verbose=True)
app.compute("jefferson", votes, seats, parties, verbose=True)

parties = ['B', 'C']
votes = [135, 325]
seats = 4
app.compute("hamilton", votes, seats, parties, verbose=True)
app.compute("jefferson", votes, seats, parties, verbose=True)


parties = ['A', 'B', 'C']
votes = [40, 135, 325]
seats = 5
app.compute("hamilton", votes, seats, parties, verbose=True)
app.compute("jefferson", votes, seats, parties, verbose=True)

parties = ['A', 'B']
votes = [160, 340]
seats = 5
app.compute("hamilton", votes, seats, parties, verbose=True)
app.compute("jefferson", votes, seats, parties, verbose=True)
app.compute("webster", votes, seats, parties, verbose=True)
