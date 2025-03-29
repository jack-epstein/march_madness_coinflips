from dataclasses import dataclass
from copy import deepcopy
import json
import random


@dataclass
class Matchup:
    team_1: int
    team_2: int
    winner: int | None = None
    tie_breaker: str | None = None


@dataclass
class BracketRound:
    matchups: list[Matchup]


@dataclass
class RegionalBracket:
    round_w_16: BracketRound | None = None
    round_w_8: BracketRound | None = None
    round_w_4: BracketRound | None = None
    round_w_2: BracketRound | None = None
    bracket_winner: int | None = None


@dataclass
class FinalFour:
    semis_1: Matchup
    semis_2: Matchup
    finals_matchup: Matchup | None = None

@dataclass
class FullBracket:
    regionals: list[RegionalBracket]
    final_four: FinalFour | None = None


ROUND_1 = BracketRound(
    matchups=[
        Matchup(team_1=1, team_2=16),
        Matchup(team_1=8, team_2=9),
        Matchup(team_1=4, team_2=13),
        Matchup(team_1=5, team_2=12),
        Matchup(team_1=3, team_2=14),
        Matchup(team_1=6, team_2=11),
        Matchup(team_1=7, team_2=10),
        Matchup(team_1=2, team_2=15)
    ]
)

REGIONALS = [
    RegionalBracket(round_w_16=deepcopy(ROUND_1)),
    RegionalBracket(round_w_16=deepcopy(ROUND_1)),
    RegionalBracket(round_w_16=deepcopy(ROUND_1)),
    RegionalBracket(round_w_16=deepcopy(ROUND_1))
]


class BracketSimulator():
    """Object that picks and plays a full bracket based on weighted or unweighted coins."""
    def __init__(self, method: str ='historical'):
        if method not in {'historical', 'random'}:
            raise ValueError("Need proper picking method: select from ['random', 'historical']")
        self.method = method  # method can be ['random', 'historical']
        with open("empirical_history_dict.json") as f:
            self.game_probability_dict = json.load(f)
    
    def picker(self, seed_1: int, seed_2: int):  # -> int:
        # need to handle even seeds in semis or finals
        if seed_1 == seed_2:
            return seed_1

        #draw random number
        check = random.random()

        if self.method == 'historical':
            # get better seed
            if seed_1 <= seed_2:
                # get prob of seed 1 winning
                prob_seed_1 = self.game_probability_dict[str(seed_1)][str(seed_2)] / 100
            else:
                # get prob of seed 2 winning
                prob_seed_1 = 1 - self.game_probability_dict[str(seed_2)][str(seed_1)] / 100
                
            #compare random number to probability of seed 1 winning
            return seed_1 if check <= prob_seed_1 else seed_2
        else:
            return seed_1 if check < 0.5 else seed_2  
    
    def play_matchup(self, matchup: Matchup): # -> Matchup:
        matchup.winner = self.picker(seed_1=matchup.team_1, seed_2=matchup.team_2)
        if matchup.team_1 == matchup.team_2:
            check = random.random()
            matchup.tie_breaker = "first" if check < 0.5 else "second"
        return matchup

    def play_round(self, bracket_round: BracketRound): # -> BracketRound | int:
        [self.play_matchup(matchup) for matchup in bracket_round.matchups]

        if len(bracket_round.matchups) == 1:
            return bracket_round.matchups[0].winner
        
        next_round = BracketRound(matchups=[])
        for i in range(0, len(bracket_round.matchups), 2):
            next_round.matchups.append(
                Matchup(
                    team_1=bracket_round.matchups[i].winner,
                    team_2=bracket_round.matchups[i+1].winner
                )
            )
        return next_round
    
    def play_regional_bracket(self, full_bracket: RegionalBracket): # -> RegionalBracket:
        full_bracket.round_w_8 = self.play_round(full_bracket.round_w_16)
        full_bracket.round_w_4 = self.play_round(full_bracket.round_w_8)
        full_bracket.round_w_2 = self.play_round(full_bracket.round_w_4)
        full_bracket.bracket_winner = self.play_round(full_bracket.round_w_2)
        return full_bracket
    
    def play_final_four(
            self,
            regional_1: RegionalBracket,
            regional_2: RegionalBracket,
            regional_3: RegionalBracket,
            regional_4: RegionalBracket
        ):
        final_four = FinalFour(
            semis_1=Matchup(team_1=regional_1.bracket_winner, team_2=regional_2.bracket_winner),
            semis_2=Matchup(team_1=regional_3.bracket_winner, team_2=regional_4.bracket_winner)
        )
        self.play_matchup(matchup=final_four.semis_1)
        self.play_matchup(matchup=final_four.semis_2)
        final_four.finals_matchup = Matchup(
            team_1=final_four.semis_1.winner,
            team_2=final_four.semis_2.winner,
        )
        self.play_matchup(matchup=final_four.finals_matchup)
        return final_four


def play_full_bracket(bracket_method: str) -> FullBracket:
    """Randomly run a full bracket, including regionals and final four."""
    bracket_simulator = BracketSimulator(method=bracket_method)
    full_bracket = FullBracket(regionals=REGIONALS)

    for regional in full_bracket.regionals:
        bracket_simulator.play_regional_bracket(regional)
    final_four = bracket_simulator.play_final_four(
        regional_1=full_bracket.regionals[0],
        regional_2=full_bracket.regionals[1],
        regional_3=full_bracket.regionals[2],
        regional_4=full_bracket.regionals[3],
    )
    full_bracket.final_four = final_four
    return full_bracket
