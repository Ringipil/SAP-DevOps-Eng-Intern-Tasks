import random

# Define the possible moves and rules for determining the winner
moves = ['R', 'P', 'S']
rules = {
    ('R', 'S'): 'Player1',  # Rock beats Scissors
    ('S', 'R'): 'Player2',  # Scissors lose to Rock
    ('P', 'R'): 'Player1',  # Paper beats Rock
    ('R', 'P'): 'Player2',  # Rock loses to Paper
    ('S', 'P'): 'Player1',  # Scissors beat Paper
    ('P', 'S'): 'Player2'   # Paper loses to Scissors
}

def generate_moves():
    """Generate random moves for both players."""
    player1_moves = [random.choice(moves) for _ in range(100)]
    player2_moves = [random.choice(moves) for _ in range(100)]
    return player1_moves, player2_moves

def write_moves_to_file(filename, moves):
    """Write the list of moves to a file."""
    try:
        with open(filename, 'w') as f:
            f.write('\n'.join(moves))
    except IOError as e:
        print(f"Error writing to {filename}: {e}")

def read_moves_from_file(filename):
    """Read the list of moves from a file."""
    try:
        with open(filename, 'r') as f:
            moves = f.read().splitlines()
        return moves
    except IOError as e:
        print(f"Error reading from {filename}: {e}")
        return []

def compare_moves(player1_moves, player2_moves):
    """Compare moves and count the results."""
    player1_wins = 0
    player2_wins = 0
    draws = 0

    for move1, move2 in zip(player1_moves, player2_moves):
        if move1 == move2:
            draws += 1
        else:
            winner = rules.get((move1, move2))
            if winner == 'Player1':
                player1_wins += 1
            elif winner == 'Player2':
                player2_wins += 1

    return player1_wins, player2_wins, draws

def main():
    # Generate random moves for both players
    player1_moves, player2_moves = generate_moves()

    # Write moves to files
    write_moves_to_file('player1.txt', player1_moves)
    write_moves_to_file('player2.txt', player2_moves)

    # Read moves from files
    player1_moves = read_moves_from_file('player1.txt')
    player2_moves = read_moves_from_file('player2.txt')

    # Ensure both files are read correctly and have 100 moves
    if len(player1_moves) != 100 or len(player2_moves) != 100:
        print("Error: Each player must have exactly 100 moves.")
        return

    # Compare moves and get results
    player1_wins, player2_wins, draws = compare_moves(player1_moves, player2_moves)

    # Display the results
    print(f"Player1 wins: {player1_wins}")
    print(f"Player2 wins: {player2_wins}")
    print(f"Draws: {draws}")

    # Write results to result.txt
    try:
        with open('result.txt', 'w') as result_file:
            result_file.write(f"Player1 wins: {player1_wins}\n")
            result_file.write(f"Player2 wins: {player2_wins}\n")
            result_file.write(f"Draws: {draws}\n")
    except IOError as e:
        print(f"Error writing to result.txt: {e}")

if __name__ == "__main__":
    main()