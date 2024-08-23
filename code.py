import chess.pgn
import io
# PGN data as a string
pgn_data = """[Event "Rated Classical game"]
[Site "https://lichess.org/j1dkb5dw"]
[White "BFG9k"]
[Black "mamalak"]
[Result "1-0"]
[UTCDate "2012.12.31"]
[UTCTime "23:01:03"]
[WhiteElo "1639"]
[BlackElo "1403"]
[WhiteRatingDiff "+5"]
[BlackRatingDiff "-8"]
[ECO "C00"]
[Opening "French Defense: Normal Variation"]
[TimeControl "600+8"]
[Termination "Normal"]"""

# Use a StringIO object to simulate a file
pgn = io.StringIO(pgn_data)

# Load the game
game = chess.pgn.read_game(pgn)

# Display some basic information
print("Event:", game.headers["Event"])
print("Site:", game.headers["Site"])
print("White:", game.headers["White"])
print("Black:", game.headers["Black"])
print("Result:", game.headers["Result"])