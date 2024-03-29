#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import norm
import sys

#USED HISTORIC DATA TO GET WIN PERCENTAGES IN ALL POSSIBLE SEED MATCHUPS (http://mcubed.net/ncaab/seeds.shtml)
    #did not fit to a distribution, only used empirical totals
    #only need to look for the higher seed in any given pairing
    #when no matchups have ever occured and are exponentially unlikely, use 0.5
    #when no matchups have ever occured with 1 much higher seed (ie 1v15), use 0.99
    #when its historically 100%, change to 99%
    #23-04-01 NOTE: given recent upset history, could be worth re-evaluating these weights
empirical_dict = {}
empirical_dict[1] = {1:0.5,2:0.545,3:0.634,4:0.705,5:0.826,6:0.706,7:0.857,8:0.795,9:0.905,
                     10:0.857,11:0.556,12:0.99,13:0.99,14:0.99,15:0.99,16:0.987}
empirical_dict[2] = {2:0.5,3:0.609,4:0.5,5:0.286,6:0.722,7:0.7,8:0.4,9:0.667,
                     10:0.635,11:0.842,12:0.99,13:0.99,14:0.99,15:0.932,16:0.99}
empirical_dict[3] = {3:0.5,4:0.625,5:0.5,6:0.581,7:0.611,8:0.99,9:0.99,
                     10:0.692,11:0.661,12:0.99,13:0.99,14:0.857,15:0.667,16:0.99}
empirical_dict[4] = {4:0.5,5:0.561,6:0.333,7:0.333,8:0.333,9:0.5,
                     10:0.99,11:0.99,12:0.705,13:0.791,14:0.99,15:0.99,16:0.99}
empirical_dict[5] = {5:0.5,6:0.99,7:0.5,8:0.25,9:0.25,
                     10:0.99,11:0.5,12:0.667,13:0.842,14:0.99,15:0.99,16:0.99}
empirical_dict[6] = {6:0.5,7:0.667,8:0.25,9:0.5,10:0.6,11:0.625,12:0.5,13:0.99,14:0.875,15:0.99,16:0.99}
empirical_dict[7] = {7:0.5,8:0.5,9:0.5,10:0.602,11:0.01,12:0.5,13:0.5,14:0.99,15:0.4,16:0.99}
empirical_dict[8] = {8:0.5,9:0.512,10:0.5,11:0.99,12:0.01,13:0.99,14:0.99,15:0.99,16:0.99}
empirical_dict[9] = {9:0.5,10:0.99,11:0.5,12:0.5,13:0.99,14:0.99,15:0.99,16:0.99}
empirical_dict[10] = {10:0.5,11:0.5,12:0.5,13:0.5,14:0.99,15:0.99,16:0.99}
empirical_dict[11] = {11:0.5,12:0.5,13:0.5,14:0.99,15:0.5,16:0.5}
empirical_dict[12] = {12:0.5,13:0.75,14:0.5,15:0.5,16:0.5}
empirical_dict[13] = {13:0.5,14:0.5,15:0.5,16:0.5}
empirical_dict[14] = {14:0.5,15:0.5,16:0.5}
empirical_dict[15] = {15:0.5,16:0.5}
empirical_dict[16] = {16:0.5}



class Bracket():
    def __init__(self, method='fifty', verbose=True):
        self.method = method #method can be ['fifty','historical','weighted']
        self.verbose = verbose #print out all rounds
    
    def picker(self, seed_1, seed_2):
        '''method to pick a winner between 2 seeds
        inputs: seed_1, seed_2 (int) the seeds of both teams competing
        outputs: seed (int) -- the winner of the matchups'''
        
        if self.method == 'random':
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
            
            #get better seed
            if seed_1 <= seed_2:
                prob_seed_1 = empirical_dict[seed_1][seed_2] #get probability of seed 1 winning
            else:
                prob_seed_1 = 1 - empirical_dict[seed_2][seed_1] #get probability of seed 1 winning
                
            #compare random number to probability of seed 1 winning
            if check <= prob_seed_1:
                return seed_1
            else:
                return seed_2
        else:
            return "Need proper picking method: select from ['random','historical']"
        
        
    def play_round(self, matchup_list):
        '''method to play a round of matchups
        inputs: matchup_list (list of tuples) -- the matchups of all the seeds
        outputs: winners list (list of tuples) -- the winners of each matchupt'''
        
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
    
    def play_bracket(self):
        
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
        semis = [(regional_winners[0],regional_winners[2]),(regional_winners[1],regional_winners[3])]
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
    plt.bar(np.unique(all_winners, return_counts=True)[0], np.unique(all_winners, return_counts=True)[1])
    plt.xlabel('Seed')
    plt.ylabel('Number of Regional Wins')
    plt.show()
    
    
if __name__ == "__main__":
    main()
