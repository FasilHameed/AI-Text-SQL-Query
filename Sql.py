import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert records and create table
cursor = connection.cursor()

# Create the table if not exists
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

records = [
    ('Saqib', 'Data Science', 'A', 90),
    ('Subash', 'Data Science', 'B', 100),
    ('Mandeep', 'Data Science', 'A', 86),
    ('Vikash', 'DEVOPS', 'A', 50),
    ('Dipesh', 'DEVOPS', 'A', 35),
    ('Sakshi', 'Class1', 'Section1', 60),
    ('Rajesh', 'Class2', 'Section2', 70),
    ('Amit', 'Class3', 'Section0', 80),
    ('Rahul', 'Class4', 'Section1', 90),
    ('Vivek', 'Class0', 'Section2', 95),
    ('Neha', 'Class1', 'Section0', 99),
    ('Priya', 'Class2', 'Section1', 77),
    ('Deepak', 'Class3', 'Section2', 66),
    ('Pooja', 'Class4', 'Section0', 55),
    ('Ankit', 'Class0', 'Section1', 44),
    ('Ayesha', 'Class1', 'Section2', 33),
    ('Aryan', 'Class2', 'Section0', 22),
    ('Riya', 'Class3', 'Section1', 11),
    ('Sumit', 'Class4', 'Section2', 100),
    ('Meera', 'Class0', 'Section0', 85),
    ('Sachin', 'Class1', 'Section1', 75),
    ('Anjali', 'Class2', 'Section2', 65),
    ('Rahul', 'Class3', 'Section0', 55),
    ('Kritika', 'Class4', 'Section1', 45),
    ('Prateek', 'Class0', 'Section2', 35),
    ('Shreya', 'Class1', 'Section0', 25),
    ('Amit', 'Class2', 'Section1', 15),
    ('Roshni', 'Class3', 'Section2', 5),
    ('Mohit', 'Class4', 'Section0', 95),
    ('Riya', 'Class0', 'Section1', 85),
    ('Ravi', 'Class1', 'Section2', 75),
    ('Anu', 'Class2', 'Section0', 65),
    ('Aman', 'Class3', 'Section1', 55),
    ('Sana', 'Class4', 'Section2', 45),
    ('Raj', 'Class0', 'Section0', 35),
    ('Anushka', 'Class1', 'Section1', 25),
    ('Ajay', 'Class2', 'Section2', 15),
    ('Sanjay', 'Class3', 'Section0', 5),
    ('Shivangi', 'Class4', 'Section1', 99),
    ('Pranav', 'Class0', 'Section2', 77),
    ('Monika', 'Class1', 'Section0', 66),
    ('Sahil', 'Class2', 'Section1', 55),
    ('Riya', 'Class3', 'Section2', 44),
    ('Vikas', 'Class4', 'Section0', 33),
    ('Muskan', 'Class0', 'Section1', 22),
    ('Arjun', 'Class1', 'Section2', 11),
    ('Neha', 'Class2', 'Section0', 100),
    ('Rohit', 'Class3', 'Section1', 85),
    ('Sonia', 'Class4', 'Section2', 75),
    ('Manoj', 'Class0', 'Section0', 65),
    ('Gaurav', 'Class1', 'Section1', 55),
    ('Preeti', 'Class2', 'Section2', 45),
    ('Karan', 'Class3', 'Section0', 35),
    ('Manisha', 'Class4', 'Section1', 25),
    ('Jatin', 'Class0', 'Section2', 15),
    ('Aditi', 'Class1', 'Section0', 5),
    ('Sandeep', 'Class2', 'Section1', 99),
    ('Rajesh', 'Class3', 'Section2', 77),
    ('Tanvi', 'Class4', 'Section0', 66),
    ('Aakash', 'Class0', 'Section1', 55),
    ('Garima', 'Class1', 'Section2', 44),
    ('Harsh', 'Class2', 'Section0', 33),
    ('Shivani', 'Class3', 'Section1', 22),
    ('Rohit', 'Class4', 'Section2', 11),
    ('Sapna', 'Class0', 'Section0', 100),
    ('Rajat', 'Class1', 'Section1', 85),
    ('Sneha', 'Class2', 'Section2', 75),
    ('Vishal', 'Class3', 'Section0', 65),
    ('Pooja', 'Class4', 'Section1', 55),
    ('Akash', 'Class0', 'Section2', 45),
    ('Nisha', 'Class1', 'Section0', 35),
    ('Shubham', 'Class2', 'Section1', 25),
    ('Sakshi', 'Class3', 'Section2', 15),
    ('Gopal', 'Class4', 'Section0', 5),
    ('Shweta', 'Class0', 'Section1', 99),
    ('Mohini', 'Class1', 'Section2', 77),
    ('Vivek', 'Class2', 'Section0', 66),
    ('Aditya', 'Class3', 'Section1', 55),
    ('Tanu', 'Class4', 'Section2', 44),
    ('Aarti', 'Class0', 'Section0', 33),
    ('Rohit', 'Class1', 'Section1', 22),
    ('Pawan', 'Class2', 'Section2', 11),
    ('Ankita', 'Class3', 'Section0', 99),
    ('Komal', 'Class4', 'Section2', 77),
    ('Nidhi', 'Class0', 'Section0', 66),
    ('Abhishek', 'Class1', 'Section1', 55),
    ('Sagar', 'Class2', 'Section2', 44),
    ('Sneha', 'Class3', 'Section0', 33),
    ('Rahul', 'Class4', 'Section1', 22),
    ('Riya', 'Class0', 'Section2', 11)
]


# Add more records to make it 100
for i in range(8, 101):
    records.append(('Student' + str(i), 'Class' + str(i % 5), 'Section' + str(i % 3), i % 101))

# Insert all records
cursor.executemany('INSERT INTO STUDENT VALUES (?,?,?,?)', records)

# Display All the records
print("The inserted records are:")
data = cursor.execute('SELECT * FROM STUDENT')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()
