import streamlit as st

import bracket


def skip_lines(n_lines: int):
    """Function to space out the st write objects to a desired place."""
    for i in range(n_lines):
        st.write('')


def print_out_first_round():
    """Function to print out the first round matchups of the bracket."""
    first_round_seeds = [
        '1', '16', '8', '9',
        '4', '13', '5', '12',
        '3', '14', '6', '11',
        '7', '10', '2', '15'
    ]
    for i, seed in enumerate(first_round_seeds):
        st.markdown(f":gray-background[{seed}]")
        if i % 2 == 1:
            st.write('')
    st.markdown(':gray[--]')
    for i, seed in enumerate(first_round_seeds):
        st.markdown(f":gray-background[{seed}]")
        if i % 2 == 1:
            st.write('')

def print_second_round(round_of_16: bracket.BracketRound, half: str):
    """Function to print the 2nd round.
    
    We take in a round of 16 because we want to see the winners from the first round.
    """
    if half == 'upper':
        for i, matchup in enumerate(round_of_16.matchups):
            st.markdown(f":gray-background[{matchup.winner}]")
            if i in [0, 3, 5, 7]:
                skip_lines(3)
            elif i == 8:
                skip_lines(0)
            else:
                skip_lines(4)
    elif half == 'lower':
        for i, matchup in enumerate(round_of_16.matchups):
            st.markdown(f":gray-background[{matchup.winner}]")
            if i in [0, 3, 5]:
                skip_lines(3)
            elif i == 8:
                skip_lines(0)
            else:
                skip_lines(4)
    else:
        st.write('ERROR PLEASE USE upper OR lower HALF')


def print_sweet_sixteen(round_of_8: bracket.BracketRound):
    """Function to print the sweet sixteen.
    
    We take in a round of 8 because we want to see the winners from the 2nd round.
    """
    for i, matchup in enumerate(round_of_8.matchups):
        st.markdown(f":gray-background[{matchup.winner}]")
        if i in [0, 2]:
            skip_lines(10)
        elif i == 4:
            skip_lines(0)
        else:
            skip_lines(9)


def print_elite_eight(round_of_4: bracket.BracketRound):
    """Function to print the elite eight.
    
    We take in a round of 4 because we want to see the winners from the 3rd round.
    """
    for i, matchup in enumerate(round_of_4.matchups):
        st.markdown(f":gray-background[{matchup.winner}]")
        if i == 0:
            skip_lines(21)
        else:
            skip_lines(26)


st.header('March Madness Coin Flip Bracket')
st.markdown(
    '### 🏀 Do you still need help filling out your bracket this year? Well look no further! 🏀'
)
st.markdown(
    'Using this script, you can fill out your bracket using nothing other than a little basketball'
    'history and random luck. If you want the odds in your favor, click "Run Weighted Coins'
    'Bracket", which uses historical ranking matchups to flip a biased coin. If you want pure'
    'chaos, click "Run Random Coins Bracket". Either way, do not blame me when you lose!'
)

# user chooses the type of bracket they want to play
button_cols = st.columns(3)
st.divider()
with button_cols[0]:
    run_bracket_weighted = st.button("Run Weighted Coins Bracket")
with button_cols[2]:
    run_bracket_random = st.button("Run Random Coins Bracket")

# once the button is clicked we simluated the bracket
any_button_clicked = run_bracket_random or run_bracket_weighted
if run_bracket_weighted:
    completed_bracket = bracket.play_full_bracket(bracket_method="historical")
if run_bracket_random:
    completed_bracket = bracket.play_full_bracket(bracket_method="random")

high_level_columns = st.columns(3)
# print the first 2 regionals
with high_level_columns[0]:
    with st.container():
        lower_level_columns = st.columns(5)
        with lower_level_columns[0]:
            print_out_first_round()
        
        if any_button_clicked:
            # Round of 32
            with lower_level_columns[1]:
                skip_lines(1)
                print_second_round(
                    round_of_16=completed_bracket.regionals[0].round_w_16,
                    half='upper'
                )

                skip_lines(4)
                print_second_round(
                    round_of_16=completed_bracket.regionals[1].round_w_16,
                    half='lower'
                )

            # Sweet Sixteen
            with lower_level_columns[2]:
                skip_lines(4)
                print_sweet_sixteen(round_of_8=completed_bracket.regionals[0].round_w_8)
                skip_lines(4)
                print_sweet_sixteen(round_of_8=completed_bracket.regionals[1].round_w_8)
            
            # Elite Eight
            with lower_level_columns[3]:
                skip_lines(10)
                print_elite_eight(round_of_4=completed_bracket.regionals[0].round_w_4)
                print_elite_eight(round_of_4=completed_bracket.regionals[1].round_w_4)

            # Final Four
            with lower_level_columns[4]:
                skip_lines(23)
                regional_champ_1 = completed_bracket.regionals[0].bracket_winner
                st.markdown(f":gray-background[{regional_champ_1}]")
                skip_lines(50)
                regional_champ_2 = completed_bracket.regionals[1].bracket_winner
                st.markdown(f":gray-background[{regional_champ_2}]")


# Print the final four
with high_level_columns[1]:
    if any_button_clicked:
        with st.container():
            lower_level_columns = st.columns(3)
            with lower_level_columns[1]:
                skip_lines(38)
                champion = completed_bracket.final_four.finals_matchup.winner
                tie_breaker = completed_bracket.final_four.finals_matchup.tie_breaker
                st.markdown(f'## :green-background[{champion}]')
                if tie_breaker:
                    st.markdown(f':green-background[{tie_breaker}]')
                skip_lines(6)
        with st.container(border=True):
            lower_level_columns = st.columns(3)
            with lower_level_columns[0]:
                tie_breaker = completed_bracket.final_four.semis_1.tie_breaker
                st.markdown(f'### {completed_bracket.final_four.semis_1.winner}')
                if tie_breaker:
                    st.markdown(f'{tie_breaker}')
            with lower_level_columns[1]:
                st.markdown('#### vs')
            with lower_level_columns[2]:
                tie_breaker = completed_bracket.final_four.semis_2.tie_breaker
                st.markdown(f'### {completed_bracket.final_four.semis_2.winner}')
                if tie_breaker:
                    st.markdown(f'{tie_breaker}')
        with st.container():
            st.write('')

# print the last 2 regionals
with high_level_columns[2]:
    with st.container():
        lower_level_columns = st.columns(5)
        with lower_level_columns[4]:
            print_out_first_round()
        
        if any_button_clicked:
            # Round of 32
            with lower_level_columns[3]:
                skip_lines(1)
                print_second_round(
                    round_of_16=completed_bracket.regionals[2].round_w_16,
                    half='upper'
                )

                skip_lines(5)
                print_second_round(
                    round_of_16=completed_bracket.regionals[3].round_w_16,
                    half='lower'
                )
            
            # Sweet Sixteen
            with lower_level_columns[2]:
                skip_lines(4)
                print_sweet_sixteen(
                    round_of_8=completed_bracket.regionals[2].round_w_8)
                skip_lines(5)
                print_sweet_sixteen(round_of_8=completed_bracket.regionals[3].round_w_8)
            
            # Elite Eight
            with lower_level_columns[1]:
                skip_lines(10)
                print_elite_eight(round_of_4=completed_bracket.regionals[2].round_w_4)
                print_elite_eight(round_of_4=completed_bracket.regionals[3].round_w_4)
            
            # Final Four
            with lower_level_columns[0]:
                skip_lines(23)
                regional_champ_3 = completed_bracket.regionals[2].bracket_winner
                st.markdown(f":gray-background[{regional_champ_3}]")
                skip_lines(50)
                regional_champ_4 = completed_bracket.regionals[3].bracket_winner
                st.markdown(f":gray-background[{regional_champ_4}]")

st.write('Historical data scraped from http://mcubed.net/ncaab/seeds.shtml')
