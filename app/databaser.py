import sqlite3
import datetime
 
def open_connection():
    connection = sqlite3.connect("app/database.db", check_same_thread=False)
    connection.row_factory = sqlite3.Row
    return connection.cursor(), connection

cursor, connection = open_connection()
cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                username TEXT,
                text TEXT,
                date DATETIME)''')
connection.commit()

def create_message(name,text):
    cursor, connection = open_connection()

    cursor.execute('''INSERT INTO messages (username, text,date) 
    VALUES (?, ?, ?)''', (name, text, datetime.datetime.now()))

    connection.commit()

def get_messages():
    cursor, connection = open_connection()
        
    cursor.execute('SELECT * FROM messages')
    messages = cursor.fetchall()
    messages = list(map(dict, messages))
    for i in range(len(messages)):
        msgDate = datetime.datetime.strptime(messages[i]['date'],'%Y-%m-%d %H:%M:%S.%f')
        if msgDate.day >=  10 :
            day = msgDate.day
        else:
            day = f"0{msgDate.day}"            
        if msgDate.month >= 10 :
            month = msgDate.month
        else:
            month = f"0{msgDate.month}"              
        if msgDate.hour >= 10 :
            hour = msgDate.hour
        else:
            hour = f"0{msgDate.hour}"
        if msgDate.minute >= 10 :
            minute = msgDate.minute
        else:
            minute = f"0{msgDate.minute}"

        messages[i]['date'] = f"{day}.{month} at {hour}:{minute}"

    connection.commit()
    return messages