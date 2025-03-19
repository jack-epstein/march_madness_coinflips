#USED HISTORIC DATA TO GET WIN PERCENTAGES IN ALL POSSIBLE SEED MATCHUPS (http://mcubed.net/ncaab/seeds.shtml)
    #did not fit to a distribution, only used empirical totals
    #only need to look for the higher seed in any given pairing
    #when no matchups have ever occured and are exponentially unlikely, use 0.5
    #when no matchups have ever occured with 1 much higher seed (ie 1v15), use 0.99
    #when its historically 100%, change to 99%
    #23-04-01 NOTE: given recent upset history, could be worth re-evaluating these weights

# GOAL: SCRAPE THIS WEBSITE WITH BEAUTIFUL SOUP AND MAKE THE DICTIONARY DYNAMIC
empirical_dict = {}
empirical_dict[1] = {1:0.5,2:0.551,3:0.643,4:0.691,5:0.803,6:0.706,7:0.857,8:0.787,9:0.909,
                     10:0.875,11:0.6,12:0.99,13:0.99,14:0.99,15:0.99,16:0.987}
empirical_dict[2] = {2:0.5,3:0.603,4:0.5,5:0.25,6:0.703,7:0.705,8:0.4,9:0.667,
                     10:0.646,11:0.8,12:0.99,13:0.99,14:0.99,15:0.929,16:0.99}
empirical_dict[3] = {3:0.5,4:0.556,5:0.5,6:0.577,7:0.632,8:0.99,9:0.75,
                     10:0.692,11:0.677,12:0.99,13:0.99,14:0.853,15:0.667,16:0.99}
empirical_dict[4] = {4:0.5,5:0.567,6:0.429,7:0.383,8:0.335,9:0.4,
                     10:0.99,11:0.99,12:0.717,13:0.788,14:0.99,15:0.99,16:0.99}
empirical_dict[5] = {5:0.5,6:0.667,7:0.5,8:0.25,9:0.4,
                     10:0.99,11:0.5,12:0.667,13:0.857,14:0.99,15:0.99,16:0.99}
empirical_dict[6] = {6:0.5,7:0.667,8:0.25,9:0.5,10:0.6,11:0.619,12:0.5,13:0.99,
                     14:0.875,15:0.99,16:0.99}
empirical_dict[7] = {7:0.5,8:0.5,9:0.5,10:0.609,11:0.01,12:0.5,13:0.5,14:0.99,15:0.33,16:0.99}
empirical_dict[8] = {8:0.5,9:0.506,10:0.5,11:0.99,12:0.01,13:0.99,14:0.99,15:0.99,16:0.99}
empirical_dict[9] = {9:0.5,10:0.99,11:0.5,12:0.5,13:0.99,14:0.99,15:0.99,16:0.99}
empirical_dict[10] = {10:0.5,11:0.5,12:0.5,13:0.5,14:0.99,15:0.99,16:0.99}
empirical_dict[11] = {11:0.5,12:0.5,13:0.5,14:0.99,15:0.5,16:0.5}
empirical_dict[12] = {12:0.5,13:0.75,14:0.5,15:0.5,16:0.5}
empirical_dict[13] = {13:0.5,14:0.5,15:0.5,16:0.5}
empirical_dict[14] = {14:0.5,15:0.5,16:0.5}
empirical_dict[15] = {15:0.5,16:0.5}
empirical_dict[16] = {16:0.5}
