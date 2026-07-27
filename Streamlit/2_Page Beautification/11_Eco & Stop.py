import streamlit as st

# Writing single line of code 
# It will not be executeable
st.markdown("# 1. 'st.code()' function")
st.code("st.write('This is code inside the write statement.')")

# Writing multiple line of code + it is executable
st.markdown("# 2. 'st.eco()' function")
st.markdown("## Example 1: ")
with st.echo():
    st.write("This is code inside the write statement.")

st.markdown("## Example 2: ")

def get_username():
    return 'Toshak'

with st.echo():
    def get_punc():
        return "!!!"
    greating = "Hi there, "

    st.write(greating, get_username(), get_punc())


# STOP: use to pause the code
st.markdown("# 3. 'st.stop()' function")
first_name = st.text_input('Enter your first name: ')
if not first_name:
    st.warning("Please enter your first name!!")
    st.stop()

last_name = st.text_input('Enter your last name: ')
if not last_name:
    st.warning("Please enter your last name!!")
    st.stop()

st.success('Thank you for writing your name.')