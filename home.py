import backend
import streamlit as st
import pandas as pd

st.set_page_config(initial_sidebar_state="collapsed", layout="wide")


def arrange_data(rows):
    for index, row in rows.iterrows():
        col1, col2, col3, col4 = st.columns([1, 1, 2.5, 0.5])
        with col1:
            st.write(row["title"])
        with col2:
            st.image("images/" + row["images"], width=175)
        with col3:
            st.write(row["description"])
        with col4:
            st.write(f"[Source Code]({row['url']})")
        st.write("_______________________________________")


st.header("Pradiv Gnanaraj")

df = pd.read_csv("data.csv", sep=";")

with st.container():
    col1_main, col2_main = st.columns(2)
    with col1_main:
        st.image("images/self.jpeg", width=300)
    with col2_main:
        st.write(backend.brief_about())
        st.markdown("[LinkedIn](https://www.linkedin.com/in/pradivgnanaraj/)")
        st.markdown("[GitHub](https://github.com/pradivGnanaraj)")


with st.container():
    get_primary_tabs = backend.primary_tabs()
    tab1_py, tab2_ops, tab3_fs = st.tabs(get_primary_tabs)
    with tab1_py:
        get_python_tags = backend.secondary_tabs_py()
        tab1, tab2, tab3, tab4, tab5 = st.tabs(get_python_tags)

        with tab1:
            arrange_data(df[9:])

        with tab2:
            arrange_data(df[2:8])
            arrange_data(df[22:23])
            arrange_data(df[24:25])

        with tab3:
            arrange_data(df[7:10])
            arrange_data(df[14:15])

        with tab4:
            arrange_data(df[:2])
            arrange_data(df[15:16])
            arrange_data(df[19:22])

        with tab5:
            arrange_data(df[12:14])
            arrange_data(df[15:16])
            arrange_data(df[11:12])
            arrange_data(df[15:16])

    with tab2_ops:
        col1_ops, col2_ops, col3_ops = st.columns(3)

        with col1_ops:
            st.write("Vprofile Project Intro & Setup on VM’s")
            st.write("AWS Cloud For Project Set Up Lift & Shift")
            st.write("Re-Architecting Web App on AWS Cloud [PAAS & SAAS]")
            st.write("Continuous Integration Using Jenkins, Nexus, Sonarqube & Slack")
            st.write("Continuous Delivery and Configuration Management [Jenkins plus Ansible]")
        with col2_ops:
            st.write("Vprofile on Beanstalk & RDS")
            st.write("Code Commit, Code Build & Code Pipeline")
            st.write("CI & CD on AWS Cloud for Vprofile Project")
            st.write("Beanstalk, RDS, CodePipeline etc")
            st.write("Vprofile Project deployment on Kubernetes")
        with col3_ops:
            # st.write("Source Code")
            # st.write("Source Code")
            # st.write("Source Code")
            # st.write("Source Code")
            # st.write("Source Code")
            pass

    with tab3_fs:
        arrange_data(df[7:10])
        arrange_data(df[14:15])
