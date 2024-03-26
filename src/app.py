import streamlit as st

def main():
    tabs = st.tabs(["DALL-E3", "Browsing"])

    with tabs[0]:
        st.header("DALL-E3")

    with tabs[1]:
        st.header("Browsing")

if __name__ == "__main__":
    main()
