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
