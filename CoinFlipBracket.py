import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
import sys

import bracket


def main():
    bracket_type = sys.argv[1]
    
    bracket_runner = bracket.BracketSimulator(method=bracket_type)
    print(f'Coin Flip Bracket Using {bracket_type} Method')
    regionals = [
        bracket.RegionalBracket(round_w_16=bracket.ROUND_1),
        bracket.RegionalBracket(round_w_16=bracket.ROUND_1),
        bracket.RegionalBracket(round_w_16=bracket.ROUND_1),
        bracket.RegionalBracket(round_w_16=bracket.ROUND_1)
    ]
    for regional in regionals:
        bracket_runner.play_regional_bracket(regional)
    final_four = bracket_runner.play_final_four(regionals[0], regionals[1], regionals[2], regionals[3])
    pprint(regionals)
    pprint(final_four)
    print('')
    
    
    #check law of large numbers for bracket
    num_iter = 10000
    all_winners = np.zeros(num_iter)
    for i in range(num_iter):
        bracket_runner = bracket.BracketSimulator(method=bracket_type)
        regionals = [
            bracket.RegionalBracket(round_w_16=bracket.ROUND_1),
            bracket.RegionalBracket(round_w_16=bracket.ROUND_1),
            bracket.RegionalBracket(round_w_16=bracket.ROUND_1),
            bracket.RegionalBracket(round_w_16=bracket.ROUND_1)
        ]
        for regional in regionals:
            bracket_runner.play_regional_bracket(regional)
        ff = bracket_runner.play_final_four(regionals[0], regionals[1], regionals[2], regionals[3])
        all_winners[i] = ff.finals_matchup.winner

    print("Share of Wins by Seed in",num_iter,"iterations")
    print(np.unique(all_winners, return_counts=True)[1]/num_iter)
    plt.title('Final Four Trips by Seed')
    plt.bar(
        np.unique(all_winners, return_counts=True)[0],
        np.unique(all_winners, return_counts=True)[1]
    )
    plt.xlabel('Seed')
    plt.ylabel('Number of Regional Wins')
    plt.show()
    
    
if __name__ == "__main__":
    main()
