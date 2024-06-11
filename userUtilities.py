##User Utilities
import sqlite3

class Login:
    def __init__(self):
        self.db_file = "tblUsers.db"
        
        connect = sqlite3.connect(self.db_file)
        cursor = connect.cursor()
        connect.execute('''CREATE TABLE IF NOT EXISTS users
        (username TEXT PRIMARY KEY UNIQUE, password TEXT, is_admin INTEGER DEFAULT 0)''')
        try:
            cursor.execute("INSERT INTO users (username, password, is_admin) VALUES ('ajman0', 'booksbooksbooks', 1)")
            print("User Database Loaded")
            cursor.execute("INSERT INTO users (username, password, is_admin) VALUES ('a', 'a', 1)")
            print("User Database Loaded")
        except:
            print("User Database Loaded")
        connect.commit()

    def check_Login(self, username, password):
        self.db_file = "tblUsers.db"
        connect = sqlite3.connect(self.db_file)
        cursor = connect.cursor()

        cursor.execute('''SELECT COUNT(*) FROM users
            where username = ? AND password= ?''', (username, password))
        result = cursor.fetchone()
        if result and result[0] > 0:
            cursor.execute('''SELECT username, is_admin FROM users
                            where username = ? and password= ?''', (username, password))
            result = cursor.fetchone()
            if result:
                self.is_admin = bool(result[1])
                connect.close()
                return True
            connect.close()
            return False
        
class Register:
    def __init__(self):
        self.db_file = "tblUsers.db"
  
    def register_user(self, username, password):
        with sqlite3.connect(self.db_file) as conn:
            c = conn.cursor()
            try:
                c.execute('''INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)''', (username, password, 0))
                conn.commit()
                print("User registered successfully")
                return True
            except sqlite3.IntegrityError:
                print("User already exists.")
                return False
            
            
# class comments:
#     def __init__(self):
#         db_file = "tblUsers.db"
#         connect = sqlite3.connect(db_file)
#         cursor = connect.cursor()
#         try:
#             cursor.execute("CREATE TABLE IF NOT EXISTS Comments (id INTEGER PRIMARY KEY AUTOINCREMENT, comment TEXT)")
#             cursor.execute("INSERT INTO Comments (comment) VALUES (?)", (comment,))
#             connect.commit()
#             connect.close()
#             print("Comment saved successfully!")
#         except Exception as e:
#             print("Error occurred while saving comment:", e)