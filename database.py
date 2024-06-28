import sqlite3


# connect to database
# help from https://medium.com/@keerthanam4141/todo-and-draw-apps-in-python-with-sqlite-database-706e6c687990
def connect():
    conn = sqlite3.connect('bunnyworld.db')
    return conn


# initialize db if it doesn't exists
def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        highscore INTEGER DEFAULT 0,
        currentlevel INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()


# Create new user with password
def add_user(username, password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_exists = cursor.fetchone()
    if not user_exists:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
    conn.close()


# get the user, wenn wenn username and password are correct
def get_user(username, password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user_data = cursor.fetchone()

    if user_data and user_data[2] == password:
        return {
            'username': user_data[1],
            'password': user_data[2],
            'highscore': user_data[3],
            'currentlevel': user_data[4]
        }
    else:
        return None


# update user with new highscore and level
def update_user(username, highscore, currentlevel):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? ', (username,))
    cursor.execute('UPDATE users SET highscore = ?, currentlevel = ? WHERE username = ?',
                   (highscore, currentlevel, username))
    conn.commit()
    conn.close()


# update only the highscore, when username is known
def update_highscore(username, score):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET highscore = ? WHERE username = ?', (score, username))
    conn.commit()


# getting the highscore, when the username is known
def get_highscore(username):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT highscore FROM users where username = ?', (username,))
    highscore = cursor.fetchone()
    return highscore[0]


# update only the level, when username is known
def update_level(username, level):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET currentlevel = ? WHERE username = ? ', (level, username))
    conn.commit()


# getting the level, when the username is known
def get_level(username):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT currentlevel FROM users where username = ? ', (username,))
    currentlevel = cursor.fetchone()
    return currentlevel[0]


# creating a list of all users and sort with the highest score but limit it to 10
def show_all_user_highscore():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT username, highscore FROM users ORDER BY highscore DESC LIMIT 10')
    highscores = cursor.fetchall()
    conn.close()
    return highscores


# reset highscore to default 0 and level to default 1
def reset_highscore_level(user_data):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET highscore = ?, currentlevel = ? WHERE username = ?', (0, 1, user_data['username']))
    conn.commit()
    conn.close()
