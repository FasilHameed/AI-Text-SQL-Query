from dotenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Function To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

## Define Your Prompt
## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    Read The Prompt Carefully and try to understand What The User Needs read the input from user and spend good time Understanding that,
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,marks,section, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

## Streamlit App

st.set_page_config(page_title="Gemini SQL Assistant", page_icon=":gemini:")
st.title("🔮 Gemini SQL Assistant 🔍")


st.sidebar.title("🚀 Ask a Question 📝")
question = st.sidebar.text_input("Enter your question here:")

submit = st.sidebar.button("🔎 Get SQL Query")

# Main content area
st.markdown("---")

if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("🔍 Generated SQL Query:")
    st.code(response, language="sql")
    
    # Execute SQL query
    try:
        rows = read_sql_query(response, "student.db")
        if rows:
            st.subheader("📊 Query Result:")
            st.dataframe(rows)
        else:
            st.warning("❗ No results found for this query.")
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")

# Main content area
st.write("""
🎓 **About Gemini SQL Assistant**

Gemini SQL Assistant is an intelligent tool that helps you convert English questions into SQL queries. 
Whether you're a beginner or an expert in SQL, Gemini can assist you in generating SQL queries to retrieve data from the STUDENT database.

Simply enter your question in the sidebar, click on the 'Get SQL Query' button, and Gemini will generate the corresponding SQL query for you. 
You can then execute the query to retrieve the desired data from the database.

🔧 **How to Use**

1. Enter your question in the sidebar.
2. Click on the 'Get SQL Query' button.
3. View the generated SQL query in the main area.
4. Execute the query to retrieve data from the database.
5. Explore the query results and analyze the data as needed.

📊 **Example Questions**

- How many entries of records are present?
- Tell me all the students studying in Data Science class.
- Show me the students with marks above 80.

Feel free to ask any question related to the STUDENT database, and Gemini will assist you in generating the SQL query to retrieve the data.

👩‍💻 **Powered By**

Gemini 💫 - A powerful generative AI model developed by Google.
Streamlit 🚀 - An open-source app framework for Machine Learning and Data Science.

""")

# Footer
footer_with_image_light_blue = """
<style>
.footer {
    background-color: #f0f0f0;
    padding: 20px;
    text-align: center;
    border-top: 1px solid #ccc;
}

.footer img {
    max-width: 100%;
    margin-top: 10px;
}

.footer .connect-text {
    color: #333;
    font-weight: bold;
    margin-bottom: 10px;
}

.footer a {
    margin: 0 10px;
    color: #333;
}

.footer .powered-by {
    color: #333;
    font-size: 14px;
    margin-top: 10px;
}

.bright-text {
    color: #004D40;
}
</style>
<div class="footer">
    <div class="connect-text">Connect with me at</div>
    <a href="https://github.com/FasilHameed" target="_blank"><img src="https://img.icons8.com/plasticine/30/000000/github.png" alt="GitHub"></a>
    <a href="https://www.linkedin.com/in/faisal--hameed/" target="_blank"><img src="https://img.icons8.com/plasticine/30/000000/linkedin.png" alt="LinkedIn"></a>
    <a href="tel:+917006862681"><img src="https://img.icons8.com/plasticine/30/000000/phone.png" alt="Phone"></a>
    <a href="mailto:faisalhameed763@gmail.com"><img src="https://img.icons8.com/plasticine/30/000000/gmail.png" alt="Gmail"></a>
    <div class="powered-by">Powered By <img src="https://img.icons8.com/clouds/30/000000/gemini.png" alt="Gemini"> Gemini 💫 and Streamlit 🚀</div>
</div>
"""

# Render Footer
st.markdown(footer_with_image_light_blue, unsafe_allow_html=True)
