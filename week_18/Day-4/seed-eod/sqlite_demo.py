import sqlite3 


DB_FILE = "dev.db"

# with sqlite3.connect(DB_FILE) as conn:
#     curs = conn.cursor()
#     curs.execute(
#         """
#         CREATE TABLE users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username VARCHAR(250),
#         email VARCHAR(250),
#         profile_pic VARCHAR(250)    
#         );
#         """
#     )

# print("Users table created!")


def create_user(username, email, profile_pic):
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            """
            INSERT INTO users(username, email, profile_pic)
            VALUES (:username, :email, :profile_pic);
            """,
            {
                "username": username,
                "email": email,
                "profile_pic": profile_pic
            }
        )
        print(f"User {username} created!")


# create_user("Patchenator", 
#     "patch_the_cat@gmail.com", 
#     "https://res.cloudinary.com/app-academy4/image/upload/v1647912257/Patchstagram/IMG_3074_ubqe1e.jpg"
# )


def get_all_users():
  with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            """
            SELECT *
            FROM users;
            """
        )
        results = curs.fetchone()
        print(results)
        return results


get_all_users()
