# March Madness Coin Flip Bracket
## Do you still need help filling out your bracket this year? Well look no further!

Using this script, you can fill out your bracket using nothing other than a little basketball history and random luck.
To make a bracket, run ```python CoinFlipBracket.py {'historical', 'random'}```

This will fill out one of three brackets for you using different methodologies. Feel free to pick your favorite!

**Option 1:** Historical Data <br>
  This uses empirical data to check all matchups of any pairings of seeds. The "coin" is then weighted with that exact probability to favor the better team. For example, in the first round, the 4 beats the 13 79% of the time. Therefore, this coin is weighted to give the 4 seed the exact same probability of winning.
  
**Option 2:** Pure Chaos <br>
  If these aren't risky enough for you, then let's use pure random chance. Nothing special, every coin is a 50/50 shot.

<br> <br>
#### Have fun and don't blame me when you finish at the bottom of your pool!


<br><br><br>
Data comes from: http://mcubed.net/ncaab/seeds.shtml
- Used historic data to get win percentages in all possible seed matchups
- Most of the Beautiful Soup parsing in this directory comes from ChatGPT
- I did not fit to a distribution, only used empirical totals
- Only need to look for the higher seed in any given pairing
- When no matchups have ever occured and are very unlikely, use 0.5
- When no matchups have ever occured with 1 much higher seed (ie 1v15), use 0.99
- When its historically 100%, change to 99%
- 23-04-01 NOTE: given recent upset history, could be worth re-evaluating these weights


