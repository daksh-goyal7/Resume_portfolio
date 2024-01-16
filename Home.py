import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2=st.columns(2)
with col1:
    st.image("images/daksh.jpg",width=400)
with col2:
    st.title("Daksh Goyal")
    content=("")
    st.info(f"""Hi, I am Daksh. I am a python programmer and a student. I will graduate in 2025 from Thapar institute of Engineering & Technology. I am currently pursuing my Bachelor's of Engineering degree in field of Electronics & Communication Engineering.Education: Sita Grammar School, Malerkotla : 10th(CBSE board 91.8%) Sohrab Public School, Malerkotla : 12th(CBSE board 87%) Jee Mains Percentile: 93""")
content2="""Below you can find some of the apps I have built in python. Feel free to contact me."""
st.write(content2)

col3,empty_col,col4=st.columns([1.5,0.5,1.5])
df=pandas.read_csv("data.csv",sep=";")

with col3:
    for index,rows in df[:10].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image("images/"+rows["image"])
        st.write("[Source Code](https://pythonhow.com)")

with col4:
    for index,rows in df[10:].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image("images/"+rows["image"])
        st.write("[Source Code](https://pythonhow.com)")
