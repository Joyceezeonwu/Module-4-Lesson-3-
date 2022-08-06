import sqlite3
# print("Imported successfully!")

#Connect to a database
conn = sqlite3.connect('student_db')
# print("Connected successfully!")

#Create a cursor object
curs = conn.cursor()
# print("Cursor connected successfully!")

#Creating a new table
curs.execute("""CREATE TABLE students_data(
            First TEXT,
            Last TEXT,
            Email TEXT
            )
""")
# print("Table created successfully!")

#Inserting several values to the table
Students_list = [('Will', 'Johnson', 'willjohnson@stutern.com'),
                 ('John', 'Smith', 'johnsmith@stutern.com'),
                 ('Katy', 'Brown', 'katybrown@stutern.com')
                ]
# # print("Student list created successfully!")

curs.executemany("INSERT INTO students_data VALUES (?, ?, ?)", Students_list)

#querying the database
curs.execute("SELECT * FROM students_data")
# print("Query executed successfully!")

#format output to display in a tabular form
items = curs.fetchall()
print("First" + "\t\tLast" + "\t\tEmail \n" f"{'.' * 60}") 

#looping through the items
for item in items:
    First, Last, Email = item
    print(f"{First:16}{Last:16}{Email:30}")

# conn.commit()
# print("Committed successfully!")

#Alter table statement
#Change the table name

curs.execute("ALTER TABLE students_data RENAME TO group_info")
# conn.commit()
# print("Table renamed successfully!")

#Adding a new column
curs.execute("ALTER Table group_info ADD column Age")
# conn.commit()
print("New column added successfully!")

#Updating new column age with details
curs.execute("UPDATE group_info SET Age = '33'")
conn.commit()

curs.execute("SELECT * FROM group_info")
print("Query executed successfully!")

#format output to display in a tabular form
items = curs.fetchall()
print("First" + "\t\tLast" + "\t\tEmail" + "\t\t\t\tAge \n" f"{'.' *  70}") 

#looping through the items
for item in items:
    First, Last, Email, Age = item
    print(f"{First:16}{Last:16}{Email:33}{Age}")
conn.commit()

#Close the connection
conn.close


