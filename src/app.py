import streamlit as st
from tabs.dalle3 import dalle3

def main():
    tabs = st.tabs(["DALL-E3", "Browsing"])

    with tabs[0]:
        dalle3()

    with tabs[1]:
        st.header("Browsing")


if __name__ == "__main__":
    main()
