import streamlit as st

import bracket


# move this all down
br = bracket.BracketSimulator(method='historical')
regionals = [
    bracket.RegionalBracket(round_w_16=bracket.ROUND_1),
    bracket.RegionalBracket(round_w_16=bracket.ROUND_1),
    bracket.RegionalBracket(round_w_16=bracket.ROUND_1),
    bracket.RegionalBracket(round_w_16=bracket.ROUND_1)
]
for regional in regionals:
    br.play_regional_bracket(regional)
br.play_final_four(regionals[0], regionals[1], regionals[2], regionals[3])


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

button_cols = st.columns(3)
st.divider()
with button_cols[0]:
    run_bracket_weighted = st.button("Run Weighted Coins Bracket")
with button_cols[2]:
    run_bracket_random = st.button("Run Random Coins Bracket")

high_level_columns = st.columns(3)
with high_level_columns[0]:
    with st.container():
        lower_level_columns = st.columns(5)
        with lower_level_columns[0]:
            print_out_first_round()
        
        with lower_level_columns[1]:
            # NEED TO TRIM THIS INTO A FUNCTION
            st.write('')
            seed = '1'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(4)
            seed = '8'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(3)
            seed = '4'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(4)
            seed = '5'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(4)
            seed = '3'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(3)
            seed = '6'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(4)
            seed = '7'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(3)
            seed = '2'
            st.markdown(f":gray-background[{seed}]")

            skip_lines(7)
            seed = '1'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(3)
            seed = '8'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(4)
            seed = '4'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(4)
            seed = '5'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(3)
            seed = '3'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(4)
            seed = '6'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(3)
            seed = '7'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(4)
            seed = '2'
            st.markdown(f":gray-background[{seed}]")

        with lower_level_columns[2]:
            # NEED TO TRIM THIS INTO A FUNCTION
            skip_lines(4)
            seed = '1'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(10)
            seed = '4'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(10)
            seed = '3'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(9)
            seed = '2'
            st.markdown(f":gray-background[{seed}]")

            skip_lines(14)
            seed = '1'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(9)
            seed = '4'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(10)
            seed = '3'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(10)
            seed = '2'
            st.markdown(f":gray-background[{seed}]")
        
        with lower_level_columns[3]:
            # NEED TO TRIM THIS INTO A FUNCTION
            skip_lines(10)
            seed = '1'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(23)
            seed = '2'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(25)
            seed = '1'
            st.markdown(f":gray-background[{seed}]")
            skip_lines(23)
            seed = '2'
            st.markdown(f":gray-background[{seed}]")

        with lower_level_columns[4]:
            # NEED TO TRIM THIS INTO A FUNCTION
            skip_lines(23)
            seed = '1'
            st.markdown(f":green-background[{seed}]")
            skip_lines(50)
            seed = '2'
            st.markdown(f":green-background[{seed}]")



with high_level_columns[1]:
    with st.container():
        lower_level_columns = st.columns(3)
        with lower_level_columns[1]:
            skip_lines(38)
            st.markdown('## :green-background[1]')
            skip_lines(6)
    with st.container(border=True):
        lower_level_columns = st.columns(3)
        with lower_level_columns[0]:
            st.markdown('### 1')
        with lower_level_columns[1]:
            st.markdown('#### vs')
        with lower_level_columns[2]:
            st.markdown('### 1')
    with st.container():
        st.write('')

with high_level_columns[2]:
    with st.container():
        lower_level_columns = st.columns(5)
        with lower_level_columns[4]:
            print_out_first_round()
