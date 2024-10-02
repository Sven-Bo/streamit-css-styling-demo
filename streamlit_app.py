import streamlit as st
import pathlib


# Function to load CSS from the 'assets' folder
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load the external CSS
css_path = pathlib.Path("assets/styles.css")
load_css(css_path)


st.title("✨ Streamlit CSS Styling Demo")
st.subheader(
    "As of Streamlit **version 1.39**, you can now set CSS classes on elements via the `key` parameter! 🎉"
)
st.code("pip install streamlit --upgrade", language="bash")
st.divider()

# Sytled Button
st.header("Buttons")
st.button("I'm a green button", key="green")
st.button("Click Me!", key="pulse")

# Text Input with Custom Font and Color
st.header("Styled Text Input")
st.text_input("Enter your favorite quote:", key="styledinput")


# Text Area with Custom Font
st.header("Styled Text Area")
st.text_area("Your thoughts:", key="styledtextarea")

# Radio Buttons with Custom Styles
st.header("Styled Radio Buttons")
st.radio("Pick a choice:", ["Choice A", "Choice B", "Choice C"], key="styledradio")

# Markdown with Custom Font and Color
st.header("Styled Markdown")
st.markdown(
    '<p class="custom-markdown">This is <strong>bold text</strong> with a custom font and color.</p>',
    unsafe_allow_html=True,
)
