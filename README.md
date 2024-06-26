# AI-Text-SQL-Query
# Gemini SQL Assistant

Gemini SQL Assistant is an intelligent tool that helps users convert English questions into SQL queries to retrieve data from the STUDENT database. Whether you're a beginner or an expert in SQL, Gemini can assist you in generating SQL queries quickly and efficiently.

![Web APP Link]()

## Features

- **English-to-SQL Conversion:** Enter your question in English, and Gemini will generate the corresponding SQL query for you.
- **Query Execution:** Execute the generated SQL query to retrieve data from the SQLite database.
- **Error Handling:** Robust error handling to handle invalid questions or issues with executing SQL queries.
- **Security:** Measures to prevent SQL injection attacks for enhanced security.
- **Optimization:** Optimized SQL queries for better performance, especially with large databases.
- **User Interface:** Intuitive user interface with clear instructions, error messages, and query result visualization.
- **Documentation:** Provides documentation and tooltips within the app to guide users on effective question asking and understanding query results.

## How to Use

1. Clone this repository.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Run the Streamlit app using the command `streamlit run app.py`.
4. Enter your question in the sidebar and click on the 'Get SQL Query' button.
5. View the generated SQL query and execute it to retrieve data from the database.

## Requirements

- Python 3.x
- Streamlit
- SQLite3
- Google Gemini API Key (Set as an environment variable)

## Configuration

1. Set up a SQLite database with the name `student.db` containing the STUDENT table.
2. Obtain a Google Gemini API key and set it as an environment variable named `GOOGLE_API_KEY`.
3. Configure the Gemini API key in the `get_gemini_response` function in `app.py`.
4. Customize the `prompt` variable in `app.py` to define your prompt for Gemini.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



## Acknowledgments

- Special thanks to Google for developing the Gemini model.
- Thanks to the Streamlit team for providing an excellent app framework.

