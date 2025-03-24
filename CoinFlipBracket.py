#!/usr/bin/env python
# coding: utf-8
import json
import numpy as np
import matplotlib.pyplot as plt
import random
import sys


class Bracket():
    def __init__(self, method: str ='random', verbose: bool = True):
        self.method = method  # method can be ['random', 'historical']
        self.verbose = verbose  # print out all rounds
        with open("empirical_history_dict.json") as f:
            self.game_probability_dict = json.load(f)

    def picker(self, seed_1: int, seed_2: int) -> int:
        """method to pick a winner between 2 seeds
        inputs: seed_1, seed_2 the seeds of both teams competing
        outputs: seed -- the winner of the matchups"""
        
        if self.method == 'random':
            check = random.random()
            # need to handle even seeds in semis or finals
            if seed_1 == seed_2:
                if check < 0.5:
                    if self.verbose == True:
                        print("first team wins")
                    return seed_1
                else:
                    if self.verbose == True:
                        print("second team wins")
                    return seed_2
            
            if check < 0.5:
                return seed_1
            else:
                return seed_2
        elif self.method == 'historical':
            #draw random number
            check = random.random()
            #need to handle even seeds in semis or finals
            if seed_1 == seed_2:
                if check < 0.5:
                    if self.verbose == True:
                        print("first team wins")
                    return seed_1
                else:
                    if self.verbose == True:
                        print("second team wins")
                    return seed_2
            
            # get better seed
            if seed_1 <= seed_2:
                # get prob of seed 1 winning
                prob_seed_1 = self.game_probability_dict[str(seed_1)][str(seed_2)] / 100
            else:
                # get prob of seed 2 winning
                prob_seed_1 = 1 - self.game_probability_dict[str(seed_2)][str(seed_1)] / 100
                
            #compare random number to probability of seed 1 winning
            if check <= prob_seed_1:
                return seed_1
            else:
                return seed_2
        else:
            return "Need proper picking method: select from ['random', 'historical']"
        
        
    def play_round(self, matchup_list: list) -> list:
        '''method to play a round of matchups
        inputs: matchup_list (list of tuples) -- the matchups of all the seeds
        outputs: winners list (list of tuples) -- the winners of each matchup'''
        
        #if we are down to 2 teams, produce a winner
        if len(matchup_list) == 1:
            winner_list = []
            winner_list.append(self.picker(matchup_list[0][0],matchup_list[0][1]))
            return winner_list

        #initaite list to store new rounds
        next_round_list = []
        #giong 2 at a time, find winners and create next round matchups
        for i in range(0,len(matchup_list),2):

            #get the teams to match up
            team_1a, team_1b = matchup_list[i]
            team_2a, team_2b = matchup_list[i+1]

            #flip the coins and store winners in new list
            new_tuple = (self.picker(team_1a, team_1b), self.picker(team_2a, team_2b))
            next_round_list.append(new_tuple)    
        return next_round_list
    
    def play_bracket(self) -> int:
        regional_winners = np.zeros(4)
        for i in range(4):
            #try and save results and run 4 times to get all first round predictions
            round_1_matchups = [(1,16),(8,9),(4,13),(5,12),(3,14),(6,11),(7,10),(2,15)]

            #play each round
            round_2_matchups = self.play_round(round_1_matchups)
            sweet_16_matchups = self.play_round(round_2_matchups)
            elite_8_matchup = self.play_round(sweet_16_matchups)
            regional_champ = self.play_round(elite_8_matchup)
            regional_winners[i] = regional_champ[0]
            
            if self.verbose == True:
                print("regional results")
                print(round_2_matchups)
                print(sweet_16_matchups)
                print(elite_8_matchup)
                print(regional_champ)
                print("")
                

        #play semis -- need to do all separate print statements in case of equal seeds
        if self.verbose == True:
            print("final four results")
        regional_winners = regional_winners.astype(int)
        semis = [(regional_winners[0],regional_winners[2]),
                 (regional_winners[1],regional_winners[3])]
        if self.verbose == True:
            print(semis)
        finals = self.play_round(semis)
        if self.verbose == True:
            print(finals)
        champ = self.play_round(finals)
        if self.verbose == True:
            print(champ)
        
        return champ


def main():
    bracket_type = sys.argv[1]
    
    bracket = Bracket(method=bracket_type)
    print(f'Coin Flip Bracket Using {bracket_type} Method')
    bracket.play_bracket()     
    print('')
    
    
    #check law of large numbers for bracket
    num_iter = 10000
    all_winners = np.zeros(num_iter)
    for i in range(num_iter):

        bracket = Bracket(method=bracket_type, verbose=False)
        winner = bracket.play_bracket()

        all_winners[i]=winner[0]

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
