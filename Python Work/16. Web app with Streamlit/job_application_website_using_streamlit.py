import streamlit as st
import datetime
import pandas as pd
st.title("TaskLyft Summer Internship 2025")
st.text("This internship is for Fresh Graduates and University students to gain Industry Experience.")
fullname=st.text_input("Full Name")
email=st.text_input("Email")
gender=st.radio("Gender",['Male','Female'])
birth_date=st.date_input("Date of Birth",min_value=datetime.date(1950,1,1),max_value=datetime.date(2007,1,1))
positions=['MERN Stack','ML','Flutter Developement','ODOO','Desktop App Development']
interested_positions=st.multiselect("Which position(s) are you interested in?",positions)
university=st.text_input("University")
currsemester=st.selectbox("Current Semester",[1,2,3,4,5,6,7,8])
cgpa=st.slider("Current CGPA",1.0,4.0,3.2)
cv=st.file_uploader("Upload your CV",type="pdf")
col1,col2,col3,col4,col5,col6=st.columns(6)

with col1:
    review_clicked = st.button("Review")

with col6:
    submit_clicked = st.button("Submit")
info_dict={'Full Name':fullname,'Email':email,'Gender':gender,'Birth Date':birth_date,
               'Interested Poisitions':interested_positions,'University':university,'Current Semester':currsemester,
               'CGPA':cgpa}
info_df=pd.DataFrame(info_dict)


if submit_clicked:
    info_df.to_csv(f"{fullname}_application")
    st.write("Form Submitted Successfully. Our Hiring team will review your application and contact you soon.")
if review_clicked:
    st.write(info_df)