import sqlite3


# help from https://medium.com/@keerthanam4141/todo-and-draw-apps-in-python-with-sqlite-database-706e6c687990
def connect():
    conn = sqlite3.connect('bunnyworld.db')
    return conn


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


def add_user(username, password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_exists = cursor.fetchone()
    if not user_exists:
        # print(f'User {username} already exists or password wrong')
        # else:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
    conn.close()


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


def update_highscore(username, score):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET highscore = ? WHERE username = ?', (score, username))
    conn.commit()


def get_highscore(username):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT highscore FROM where username = ?', (username))
    highscore = cursor.fetchone()
    return highscore[0]


def update_level(username, level):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET currentlevel = ? WHERE username = ? ', (level, username))
    conn.commit()


def get_level(username):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT currentlevel FROM where username = ? ', (username))
    currentlevel = cursor.fetchone()
    return currentlevel[0]


def show_all_user_highscore():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT username, highscore FROM users ORDER BY highscore DESC LIMIT 20')
    highscores = cursor.fetchall()
    conn.close()
    return highscores
