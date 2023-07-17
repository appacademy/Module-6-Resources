import sqlite3

DB_FILE = "dev.db"

# with sqlite3.connect(DB_FILE) as conn:
#   curs = conn.cursor()
#   curs.execute("""
#                CREATE TABLE users(
#                  id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  username VARCHAR(50),
#                  email VARCHAR(255),
#                  profile_pic VARCHAR(255)
#                );
#                """)
#   print("user table created")

def create_users(username, email, profile_pic):
  with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute("""
                 INSERT INTO users(username, email, profile_pic)
                 VALUES(:username, :email, :profile_pic)
                 """,
                 {
                   "username": username,
                   "email": email,
                   "profile_pic": profile_pic
                 }
                 )
    print(f"user {username} created")

# create_users("Pip", "pip@pip.pip", "https://pipstagram.s3.amazonaws.com/137336008_406744080656046_3364448327964401597_n.jpg")

def get_all_users():
  with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute("""
                 SELECT *
                 FROM users;
                 """)
    results = curs.fetchall()
    print(results)

get_all_users()