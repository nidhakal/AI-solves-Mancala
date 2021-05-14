import games

import cs210_utils

# from games import play_game
import cs210_utils


class MancalaGame(object):

    def __init__(self):
        self.init_state()
        self.init_player()

        self.initial = self.state

    def init_state(self):

        # Index 0 is for Min Mancala
        # Index 7 is for Max Mancala
        self.pits = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
        self.turn = 'max'
        self.state = (self.pits, self.turn)

    def init_player(self):
        self.player1 = 'MAX'
        self.player2 = 'MIN'
        self.player = (self.player1, self.player2)

    def legal_moves(self, state):
        "Return a list of the allowable moves at this point. A state represents the number of stones in each pit on the board."

        legal_moves = []

        pits, turn = state

        if (turn == 'max'):
            for i in range(1, 7):
                if (pits[i] > 0):
                    legal_moves.append(i - 1)
        else:
            for i in range(8, 14):
                if (pits[i] > 0):
                    legal_moves.append(i - 8)

        return legal_moves

    def make_move(self, move, state):
        "Return the state that results from making a move from a state. For Mancala, a move is an integer in the range 0 to 5, inclusive."
        pits, turn = state
        turn_holder = turn

        if (turn == 'max'):
            num_pebbles = pits[move + 1]
            pits[move + 1] = 0
            index = (move + 2) % 14
        else:
            num_pebbles = pits[move + 8]
            pits[move + 8] = 0
            index = (move + 9) % 14

        while (num_pebbles > 0):
            if ((turn_holder == 'max') and (index == 0)):
                index += 1

            elif ((turn_holder == 'min') and (index == 7)):
                index += 1

            if ((num_pebbles == 1) and (turn == 'max')):
                if (pits[(index) % 14] == 0):
                    if ((((index) % 14) < 7) and ((index % 14) > 0)):
                        if (pits[14 - index] > 0):
                            # print('3rd')
                            pits[7] = pits[7] + pits[14 - index] + 1
                            pits[14 - index] = 0
                            pits[index] = 0
                            index = (index + 1) % 14
                            num_pebbles = num_pebbles - 1
                            continue

                if (((index) % 14) == 7):
                    turn = 'max'
                else:
                    turn = 'min'

            elif ((num_pebbles == 1) and (turn == 'min')):
                if (pits[(index) % 14] == 0):
                    if ((((index) % 14) > 7) and ((index) < 14)):
                        if (pits[14 - index] > 0):
                            pits[0] = pits[0] + pits[14 - index] + 1
                            pits[14 - index] = 0
                            pits[index] = 0
                            index = (index + 1) % 14
                            num_pebbles = num_pebbles - 1
                            continue

                if (((index) % 14) == 0):
                    turn = 'min'
                else:
                    turn = 'max'

            pits[index] = pits[index] + 1
            index = (index + 1) % 14
            num_pebbles = num_pebbles - 1

        final_state = True
        if (turn_holder == 'max'):
            for i in range(1, 7):
                if (pits[i] != 0):
                    final_state = False
        else:
            for i in range(8, 14):
                if (pits[i] != 0):
                    final_state = False

        sum_pits = 0
        if (final_state == True):
            if (turn_holder == 'max'):
                for i in range(8, 14):
                    sum_pits += pits[i]

                pits[7] += sum_pits

            else:
                for i in range(1, 7):
                    sum_pits += pits[i]

                pits[0] += sum_pits

        state = pits, turn
        return state

    def utility(self, state, player):
        "Return the value of this final state to player."

        pits, turn = state

        if (player == 'MAX'):
            utility = pits[7] - pits[0]
        else:
            utility = pits[0] - pits[7]

        return utility

    def terminal_test(self, state):
        "Return True if this is a final state for the game."
        pits, turn = state
        final_state_1 = True
        for i in range(1, 7):
            if (pits[i] != 0):
                final_state_1 = False

        final_state_2 = True
        for i in range(8, 14):
            if (pits[i] != 0):
                final_state_2 = False

        if ((final_state_1 == True) or (final_state_2 == True)):
            return True
        else:
            return False

    def to_move(self, state):
        "Return the player whose move it is in this state."
        pits, turn = state

        if (turn == 'max'):
            return 'MAX'

        return 'MIN'

    def max_to_move(self, state):
        "Return True if the player whose move it is in this state is the MAX player, else False."
        pits, turn = state

        pits, turn = state

        if (turn == 'max'):
            return 'MAX'

        return 'MIN'

        return False

    def display(self, state):
        "Print or otherwise display the state."
        pits, turn = state

        print('Maximum Player Mancala: ', pits[7])
        print('Max Player Pits: ', pits[1:7])
        print('Minimum Player Mancala: ', pits[0])
        print('Min Player Pits: ', pits[8:14])

    def evaluate_mancala(self, state):
        "Takes a game and a state and returns a value for that state. Because this function is going to be used in minimax search, we want to have positive values for states that are good for the maximizing player and negative values for states that are good for the minimizer, regardless of who's move it is in the game."
        pits, turn = state

        # evalm = self.utility(player1) - self.utility(player2)
        return 0



    def evaluate_mancala(game, state):

            "Takes a game and a state and returns a value for that state. Because this function is going to be used in minimax search, we want to have positive values for states that are good for the maximizing player and negative values for states that are good for the minimizer, regardless of who's move it is in the game."

            pits, turn = state

            counterMin = 0
            counterMax = 0
            # evalm = 0
            for i in range(0,7):
                counterMin += pits[i]
            # counterMin += game.utility(player=game.player1)
            for j in range(8,14):
                counterMax += pits[j]
            # counterMax += game.utility(player=game.player2)
            if counterMax > counterMin:
                evalm = counterMax - counterMin
            else:
                evalm = counterMin - counterMax

            return evalm
            # return game.utility(state,'Min') - game.utility(state,'Max')
            # pits, turn = state
            # return pits[7] - pits[0]



    def successors(self, state):
        "Return a list of legal (move, state) pairs."
        return [(move, self.make_move(move, state))
                for move in self.legal_moves(state)]

#
# mancala = MancalaGame()
# mancala.pits = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
# mancala.turn = 'max'
# final_pits = mancala.make_move(0, (mancala.pits, mancala.turn))
# print(final_pits)

