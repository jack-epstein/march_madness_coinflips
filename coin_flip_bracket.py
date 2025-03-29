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


st.header('March Madness')

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
                for i, matchup in enumerate(completed_bracket.regionals[0].round_w_16.matchups):
                    st.markdown(f":gray-background[{matchup.winner}]")
                    if i in [0, 2, 3, 5, 7]:
                        skip_lines(3)
                    elif i == 8:
                        skip_lines(0)
                    else:
                        skip_lines(4)

                skip_lines(5)
                for i, matchup in enumerate(completed_bracket.regionals[1].round_w_16.matchups):
                    st.markdown(f":gray-background[{matchup.winner}]")
                    if i in [0, 3, 5]:
                        skip_lines(3)
                    elif i == 8:
                        skip_lines(0)
                    else:
                        skip_lines(4)

            # Sweet Sixteen
            with lower_level_columns[2]:
                skip_lines(4)
                for i, matchup in enumerate(completed_bracket.regionals[0].round_w_8.matchups):
                    st.markdown(f":gray-background[{matchup.winner}]")
                    if i in [0]:
                        skip_lines(10)
                    elif i == 4:
                        skip_lines(0)
                    else:
                        skip_lines(9)

                skip_lines(5)
                for i, matchup in enumerate(completed_bracket.regionals[1].round_w_8.matchups):
                    st.markdown(f":gray-background[{matchup.winner}]")
                    if i in [0, 2]:
                        skip_lines(10)
                    elif i == 4:
                        skip_lines(0)
                    else:
                        skip_lines(9)
            
            # Elite Eight
            with lower_level_columns[3]:
                skip_lines(10)
                for i, matchup in enumerate(completed_bracket.regionals[0].round_w_4.matchups):
                    st.markdown(f":gray-background[{matchup.winner}]")
                    if i == 0:
                        skip_lines(21)
                    else:
                        skip_lines(26)
                for i, matchup in enumerate(completed_bracket.regionals[1].round_w_4.matchups):
                    st.markdown(f":gray-background[{matchup.winner}]")
                    skip_lines(23)

            # Final Four
            with lower_level_columns[4]:
                skip_lines(23)
                regional_champ_1 = completed_bracket.regionals[0].round_w_2.matchups[0].winner
                st.markdown(f":gray-background[{regional_champ_1}]")
                skip_lines(50)
                regional_champ_2 = completed_bracket.regionals[1].round_w_2.matchups[0].winner
                st.markdown(f":gray-background[{regional_champ_2}]")


# print the final four
# JE NEED TO HANDLE THE CASE OF THE SAME SEED MATCHUP
with high_level_columns[1]:
    with st.container():
        lower_level_columns = st.columns(3)
        with lower_level_columns[1]:
            skip_lines(38)
            champion = completed_bracket.final_four.finals_matchup.winner
            st.markdown(f'## :green-background[{champion}]')
            skip_lines(6)
    with st.container(border=True):
        lower_level_columns = st.columns(3)
        with lower_level_columns[0]:
            st.markdown(f'### {completed_bracket.regionals[0].bracket_winner}')
        with lower_level_columns[1]:
            st.markdown('#### vs')
        with lower_level_columns[2]:
            st.markdown(f'### {completed_bracket.regionals[1].bracket_winner}')
    with st.container():
        st.write('')

with high_level_columns[2]:
    with st.container():
        lower_level_columns = st.columns(5)
        with lower_level_columns[4]:
            print_out_first_round()
