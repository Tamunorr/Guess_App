import streamlit as st
import random

st.header("Guessing Game")
st.image("dice-image.gif")

b = st.number_input("Please input a number between 1 and 6")
a = random.randint(1,6)

def game (a,b):
    if b > 6:
        return("Invalid input. Please select a number between 1 and 6")
    else:
        if a == b:
            return("Correct")
        else:
            st.write(f"Your selected number is {b}")
            st.write(f"Random number is {a}")
            return("Wrong, try again")

if st.button("Try your luck"):
    st.write(game(a,b))
