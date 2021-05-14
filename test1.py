##############################################################################
#
# File:         test1.py
# Date:         Thu  6 Oct 2011  15:39
# Author:       Ken Basye
# Description:  
#
##############################################################################

# Note no doctesting in this file; we want to run this as main to play

import games
import mancala
import pandas as pd


def test1():
    game = mancala.MancalaGame()
    named_players = (('MAX', games.query_player_py_exp), ('MIN', games.random_player))
    print(games.play_game2(game, named_players))

def test2():
    game = mancala.MancalaGame()
    named_players = (('MAX', games.query_player_py_exp), ('MIN', games.alphabeta_player))
    print(games.play_game2(game, named_players))

def test3():
    game = mancala.MancalaGame()
    named_players = (('MAX', games.alphabeta_player), ('MIN', games.random_player))
    print(games.play_game2(game, named_players))

def test4():
    game = mancala.MancalaGame()
    named_players = (('MAX', games.alphabeta_full_player), ('MIN', games.alphabeta_player))
    print(games.play_game(game, named_players))

def test4():
    game = mancala.MancalaGame()
    player_fn = lambda g, state: games.alphabeta_player2(game, state, game.evaluate_mancala(game))
    named_players = (('MAX', games.query_player_py_exp), ('MIN', player_fn))
    result=games.play_game2(game, named_players)
    print(result)
    return(result)

def test5(depth = 4):
    game = mancala.MancalaGame()
    player_fn = lambda g, state: games.alphabeta_player2(game, state, game.evaluate_mancala(game))
    # player_fn2 = lambda g, state: games.alphabeta_player2(game, state, game.evaluate_mancala(game))
    named_players = (('MAX', player_fn), ('MIN', games.alphabeta_player))
    result = games.play_game2(game, named_players)
    return (result)



if __name__ == '__main__':
    # test1()
    # test2()
    #   test3()
    # for i in range(10):
    #     test4()
    #     test5()
    max_stats = []
    min_stats = []
    for i in range(10):
        stats = test5()
        max_stats.append(stats['MAX'])
        min_stats.append(stats['MIN'])
    final_stats = {"max_stats":max_stats, "min_stats":min_stats}
    df = pd.DataFrame(final_stats)
    print("max_mean:",df["max_stats"].mean())
    print("min_mean:",df["min_stats"].mean())




