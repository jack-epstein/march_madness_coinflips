# March Madness Coin Flip Bracket
## Do you still need help filling out your bracket this year? Well look no further!

Using this script, you can fill out your bracket using nothing other than a little basketball history and random luck.
To make a bracket, run ```python CoinFlipBracket.py```

This will fill out three brackets for you using three different methodologies. Feel free to pick your favorite!

**Option 1:** Historical Data <br>
  This uses empirical data to check all matchups of any pairings of seeds. The "coin" is then weighted with that exact probability to favor the better team. For example, in the first round, the 4 beats the 13 79% of the time. Therefore, this coin is weighted to give the 4 seed the exact same probability of winning.
  
**Option 2:** Manually Weighted Coin <br>
  This option will make a weighted coin based stricly of the numbers of the seeds. Again, in our 4 vs 13 matchup, we will combine the totals of these seeds and then weight positively towards to stronger team. In this case, we'd give the 4 seed a 13/17 (76%) chance of winning.
  
**Option 3:** Pure Chaos <br>
  If these aren't risky enough for you, then let's use pure random chance. Nothing special, every coin is a 50/50 shot.

<br> <br>
#### Have fun and don't blame me when you finish at the bottom of your pool!




<br><br><br><br>
Data comes from: http://mcubed.net/ncaab/seeds.shtml


