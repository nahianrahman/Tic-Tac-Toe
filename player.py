import math
import random

class Player:
    def __init__(self,letter):
        # assign whther x or o will represent this player
        self.letter = letter


    def get_move(self, game):
        # all players must get their move given a game
        pass


class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)


    def get_move(self, game):
        # select a random empty square for next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        # keep asking user to selct a square until a valid move is made
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{self.letter}\'s turn. Input move (0-8):')
            # check if input is a valid integer
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # choose randomly at beginning
            square = random.choice(game.available_moves())
        else:
            # get square based off minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square


    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # first check if previous move is a winner (base case)
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}

        # no empty squares
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf} # score should be larger
        else:
            best = {'position': None, 'score': math.inf} # score should be smaller

        for possible_move in state.available_moves():
            # step 1: try a spot to make a move
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player) # alternate players

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best