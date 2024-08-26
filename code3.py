import chess.pgn
import pandas as pd

# Function to extract game data
def extract_game_data(game):
    game_data = {
        "Event": game.headers.get("Event"),
        "Site": game.headers.get("Site"),
        "Date": game.headers.get("Date"),
        "Round": game.headers.get("Round"),
        "White": game.headers.get("White"),
        "Black": game.headers.get("Black"),
        "Result": game.headers.get("Result"),
        "ECO": game.headers.get("ECO"),
        "Moves": game.board().variation_san(game.mainline_moves())
    }
    return game_data

# Load PGN file
pgn_file = open("janu.pgn")

# Parse PGN file
games = []
while True:
    game = chess.pgn.read_game(pgn_file)
    if game is None:
        break
    games.append(extract_game_data(game))

# Convert list of games to DataFrame
df = pd.DataFrame(games)

# Save DataFrame to CSV
df.to_csv("jan.csv", index=False)
#confermation message that pgn file converted into csv file
print("PGN file has been converted to CSV successfully!")
#read the csv file back into data frame and print its content
df_read=pd.read_csv("jan.csv")
print("contents of csv file:")
print(df_read)

