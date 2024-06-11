##User Interface
import tkinter as tk
from tkinter import ttk
from data_display import displayData, searchFunction
from PIL import Image, ImageTk
import sqlite3
from tkinter import filedialog
import csv

## Main Window
class main_window(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.master.geometry("1624x768")
        self.master.configure(bg="#e1e114")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        
        icon = tk.PhotoImage(file="Picture1.png")
        self.master.iconphoto(True, icon)

        self.style = ttk.Style()
        self.style.theme_use("classic")
        self.style.configure("pink.TFrame", background="#ee1c25")
        self.style.configure("yellow.TFrame", background="#660033")
        self.style.configure("blue.TFrame", background="blue")

        self.columnconfigure(0, weight=1, uniform = "column")
        self.columnconfigure(1, weight=3, uniform="column")
        self.rowconfigure(0, weight=1, uniform="row")
        self.rowconfigure(1, weight=4, uniform="row")

        bannerImageFrame = ttk.Frame(self, style="yellow.TFrame")
        bannerImageFrame.grid(row=0, column=0, sticky="nsew", columnspan="3")
        self.bannerImageFile = tk.PhotoImage(file="bannerImage.png")
        bannerImage = ttk.Label(bannerImageFrame, image=self.bannerImageFile)
        bannerImage.pack(side="top") 

        navFrame = ttk.Frame(self, style="pink.TFrame")
        navFrame.grid(row=1, column=0, rowspan=1, sticky="nsew")

        style = ttk.Style()
        style.configure("Borderless.TButton", borderwidth=0, font="Impact 40")
        
        self.admin_button = ttk.Button(navFrame, text="Admin Page", style="Borderless.TButton")
        self.admin_button.grid(row=0, column=0, pady=10, padx=10, sticky="ew", ipady=50)
        
        self.standings_button = ttk.Button(navFrame, text="Standings", style="Borderless.TButton")
        self.standings_button.grid(row=1, column=0, pady=10, padx=10, sticky="ew", ipady=50)
        
        self.player_button = ttk.Button(navFrame, text="Players", style="Borderless.TButton")
        self.player_button.grid(row=2, column=0, pady=10, padx=10, sticky="ew", ipady=50)
        
        self.stats_button = ttk.Button(navFrame, text="Stats", style="Borderless.TButton")
        self.stats_button.grid(row=3, column=0, pady=10, padx=10, sticky="ew", ipady=50)
        
        navFrame.columnconfigure(0, weight=1)
        navFrame.rowconfigure(0, weight=1)
        navFrame.rowconfigure(1, weight=1)
        navFrame.rowconfigure(2, weight=1)
        navFrame.rowconfigure(3, weight=1)
        navFrame.rowconfigure(4, weight=1)

## Content Frame with llogin info
        self.contentFrame = ttk.Frame(self)
        self.contentFrame.grid(row=1, column=1, sticky="nsew")
        
        self.username_label = ttk.Label(self, text="Input Username:", font=("Impact", 45))
        self.username_entry = ttk.Entry(self) 
        self.password_label = ttk.Label(self, text="Input Password:", font=("Impact", 45))
        self.password_entry = ttk.Entry(self, show="*")
        self.login_button = ttk.Button(self, text="Login")
        self.signup_button = ttk.Button(self, text="Sign Up")
        
        self.username_label.place(relx=0.49, rely=0.2)
        self.username_entry.place(height=50, width=425, relx=0.49, rely= 0.3)
        self.password_label.place(relx=0.49, rely= 0.37)
        self.password_entry.place(height=50, width=425, relx=0.49 ,rely= 0.465)
        self.login_button.place(height=110, width=250, relx=0.640, rely= 0.55)
        self.signup_button.place(height=110, width=250, relx=0.440, rely= 0.55)

##########################################################################################################################################################################################

class homeFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.HomaPageTitle_label = ttk.Label(self, text="HOME PAGE", font=("Impact", 80))
        self.HomaPageTitle_label.place(relx=0.260, rely=0.0)
        self.prompt_label = ttk.Label(self, text="Select a page to start", font=("Impact", 50))
        self.prompt_label.place(relx=0.320, rely=0.25)
        self.prompt2_label = ttk.Label(self, text="navigating the world of FIFA", font=("Impact", 50))
        self.prompt2_label.place(relx=0.260, rely=0.4)
        
        self.leftarrow = tk.PhotoImage(file="arrowL.png")
        self.leftarrowLabel_S = ttk.Label(self, image=self.leftarrow)
        self.leftarrowLabel_S.place(rely=0.3, relx=0.0)
        self.leftarrowLabel_P = ttk.Label(self, image=self.leftarrow)
        self.leftarrowLabel_P.place(rely=0.55, relx=0.0)     
        self.leftarrowLabel_S = ttk.Label(self, image=self.leftarrow)
        self.leftarrowLabel_S.place(rely=0.8, relx=0.0)   


##########################################################################################################################################################################################

class StandingsFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.titlestandings = ttk.Label(self, text="FIFA STANDINGS PAGE", font=("Impact", 40))
        self.standingsData = displayData(self, db_file= "IA2.db", table_names="tblStandings")
        self.titlestandings.place(rely=0, relx=0.325)
        self.standingsData.place(relx=0.075, rely= 0.17)
        
        self.comment_entry = ttk.Entry(self)
        self.comment_entry.place(relx=0.075, rely=0.55, width=700, height=30)
        
        self.commentData = displayData(self, db_file= "tblUsers.db", table_names="comments")
        self.commentData.place(relx=0.075, rely= 0.62, width=800)
        
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_comment)
        self.submit_button.place(relx=0.7, rely=0.542)
        self.update_button = ttk.Button(self, text="Update", command=self.create_treeview)
        self.update_button.place(relx=0.77, rely=0.542)
        
        self.searchBar = ttk.Entry(self)
        self.searchBar.place(relx=0.075,rely=0.12, width=650)
        self.searchButton = ttk.Button(self, text="Search", style="hum.TButton", command=lambda: searchFunction.search(self,self.searchBar.get(),"tblStandings",self.standingsData.tree, self.searchBar))
        self.searchButton.place(relx=0.63,rely=0.1)

        
    def load_standings_data(self):
        db_file = "IA2.db"
        connect = sqlite3.connect(db_file)
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM tblStandings")  # Replace tblStandings with your actual table name
        standings_data = cursor.fetchall()
        for row in standings_data:
            self.standingsData.insert("", "end", values=row)
        connect.close()
        
        
    def create_treeview(self):
        self.commentData = displayData(self, db_file= "tblUsers.db", table_names="comments")
        self.commentData.place(relx=0.075, rely= 0.6, width=800)
        
    def submit_comment(self):
        comment = self.comment_entry.get()
        if comment:
            # Save comment to the database
            self.save_comment_to_database(comment)
            # Clear the entry field after submission
            self.comment_entry.delete(0, tk.END)
            # Optionally, you can display a message to indicate successful submission
        
    def save_comment_to_database(self, comment):
        db_file = "tblUsers.db"
        connect = sqlite3.connect(db_file)
        cursor = connect.cursor()
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS Comments (id INTEGER PRIMARY KEY AUTOINCREMENT, comment TEXT)")
            cursor.execute("INSERT INTO Comments (comment) VALUES (?)", (comment,))
            connect.commit()
            connect.close()
            print("Comment saved successfully!")
        except Exception as e:
            print("Error occurred while saving comment:", e)
            
    def get_children(self, item=""):
        children = self.get_children(item)
        return children
    
    def search(self, query):
        query = query.lower()
        self.delete(*self.get_children())
        db_file = "IA2.db"
        connect = sqlite3.connect(db_file)
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM tblStandings")
        for row in cursor.fetchall():
            if query in str(row).lower():
                self.insert("", tk.END, values=row)
        connect.close()
            
##########################################################################################################################################################################################    
    
class PlayersFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.titleplayers = ttk.Label(self, text="FIFA PLAYERS PAGE", font=("Impact", 40))
        self.titleplayers.place(rely=0, relx=0.325)
        self.PlayersData = displayData(self, db_file= "IA2.db", table_names="tblPlayers")
        self.PlayersData.place(relx=0.075, rely= 0.17)
        
        self.comment_entry = ttk.Entry(self)
        self.comment_entry.place(relx=0.075, rely=0.55, width=700, height=30)
        
        self.commentData = displayData(self, db_file= "tblUsers.db", table_names="comments")
        self.commentData.place(relx=0.075, rely= 0.62, width=800)
        
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_comment)
        self.submit_button.place(relx=0.7, rely=0.542)
        self.update_button = ttk.Button(self, text="Update", command=self.create_treeview)
        self.update_button.place(relx=0.77, rely=0.542)
        
        self.searchBar = ttk.Entry(self)
        self.searchBar.place(relx=0.075,rely=0.12, width=650)
        self.searchButton = ttk.Button(self, text="Search", style="hum.TButton", command=lambda: searchFunction.search(self,self.searchBar.get(),"tblPlayers",self.PlayersData.tree, self.searchBar))
        self.searchButton.place(relx=0.63,rely=0.1)
        
        
    def create_treeview(self):
        self.commentData = displayData(self, db_file= "tblUsers.db", table_names="comments")
        self.commentData.place(relx=0.075, rely= 0.6, width=800)
        
    def submit_comment(self):
        comment = self.comment_entry.get()
        if comment:
            # Save comment to the database
            self.save_comment_to_database(comment)
            # Clear the entry field after submission
            self.comment_entry.delete(0, tk.END)
            # Optionally, you can display a message to indicate successful submission
        
    def save_comment_to_database(self, comment):
        db_file = "tblUsers.db"
        connect = sqlite3.connect(db_file)
        cursor = connect.cursor()
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS Comments (id INTEGER PRIMARY KEY AUTOINCREMENT, comment TEXT)")
            cursor.execute("INSERT INTO Comments (comment) VALUES (?)", (comment,))
            connect.commit()
            connect.close()
            print("Comment saved successfully!")
        except Exception as e:
            print("Error occurred while saving comment:", e)
        
########################################################################################################################################################################################## 
        
class statsFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.titlestats = ttk.Label(self, text="FIFA STATS PAGE", font=("Impact", 40))
        self.StatsData = displayData(self, db_file= "IA2.db", table_names="tblPlayerstats")
        self.titlestats.place(rely=0, relx=0.325)
        self.StatsData.place(relx=0, rely= 0.17)
        
        self.comment_entry = ttk.Entry(self)
        self.comment_entry.place(relx=0.075, rely=0.55, width=700, height=30)
        
        self.commentData = displayData(self, db_file= "tblUsers.db", table_names="comments")
        self.commentData.place(relx=0.075, rely= 0.62, width=800)
        
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_comment)
        self.submit_button.place(relx=0.7, rely=0.542)
        self.update_button = ttk.Button(self, text="Update", command=self.create_treeview)
        self.update_button.place(relx=0.77, rely=0.542)

        self.searchBar = ttk.Entry(self)
        self.searchBar.place(relx=0.075,rely=0.12, width=650)
        self.searchButton = ttk.Button(self, text="Search", style="hum.TButton", command=lambda: searchFunction.search(self,self.searchBar.get(),"tblStats",self.StatsData.tree, self.searchBar))
        self.searchButton.place(relx=0.63,rely=0.1)
        
    def create_treeview(self):
        self.commentData = displayData(self, db_file= "tblUsers.db", table_names="comments")
        self.commentData.place(relx=0.075, rely= 0.6, width=800)
        
    def submit_comment(self):
        comment = self.comment_entry.get()
        if comment:
            # Save comment to the database
            self.save_comment_to_database(comment)
            # Clear the entry field after submission
            self.comment_entry.delete(0, tk.END)
            # Optionally, you can display a message to indicate successful submission
        
    def save_comment_to_database(self, comment):
        db_file = "tblUsers.db"
        connect = sqlite3.connect(db_file)
        cursor = connect.cursor()
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS Comments (id INTEGER PRIMARY KEY AUTOINCREMENT, comment TEXT)")
            cursor.execute("INSERT INTO Comments (comment) VALUES (?)", (comment,))
            connect.commit()
            connect.close()
            print("Comment saved successfully!")
        except Exception as e:
            print("Error occurred while saving comment:", e)

##########################################################################################################################################################################################        
        
class adminFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.titleadmin = ttk.Label(self, text="Admin Only Page", font=("Impact", 40))
        self.titleadmin.place(rely=0, relx=0.325)
        
        self.comment_tree = ttk.Treeview(self, columns=("ID", "Comment"), selectmode="extended")
        self.comment_tree.heading("#0", text="ID")
        self.comment_tree.column("#0", width=50)
        self.comment_tree.heading("ID", text="ID")
        self.comment_tree.column("ID", width=50)
        self.comment_tree.heading("Comment", text="Comment")
        self.comment_tree.column("Comment", width=300)
        self.comment_tree.place(relx=0.065, rely= 0.6)
        
        self.delete_button = ttk.Button(self, text="Delete Selected Comments", command=self.delete_selected_comments)
        self.delete_button.place(relx=0.065, rely= 0.52)
        
        # self.userlist = displayData(self, db_file= "tblUsers.db", table_names="users")
        # self.userlist.place(relx=0.065, rely= 0.15, width=400)
        
   
        
        self.user_tree = ttk.Treeview(self, columns=("Username", "Password", "Is_Admin"), selectmode="extended")
        self.user_tree.heading("#0", text="ID")  # Placeholder for the ID column
        self.user_tree.column("#0", width=50)
        self.user_tree.heading("Username", text="Username")
        self.user_tree.column("Username", width=150)
        self.user_tree.heading("Password", text="Password")
        self.user_tree.column("Password", width=150)
        self.user_tree.heading("Is_Admin", text="Is Admin")
        self.user_tree.column("Is_Admin", width=50)
        self.user_tree.place(relx=0.065, rely= 0.13)
        
        self.delete_user_button = ttk.Button(self, text="Delete Selected User(s)", command=self.delete_selected_users)
        self.delete_user_button.place(relx=0.23, rely= 0.52)
        
        self.open_file_button = ttk.Button(self, text="Open CSV File", command=self.open_csv_file)
        self.open_file_button.place(relx=0.5, rely=0.5, width=150, height=100)
        
        self.load_comments()
        self.load_users()
        
        
    def open_csv_file(self):
        # Open file explorer dialog
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        
        if file_path:
            # Read data from CSV file and insert into database
            self.insert_csv_data(file_path)
            
    def insert_csv_data(self, file_path):
        # Connect to the database
        db_file = "IA2.db"
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        try:
            # Open CSV file and insert data into the database
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                # Assuming the first row of the CSV file contains column headers
                headers = next(csv_reader)
                for row in csv_reader:
                    cursor.execute(f"INSERT INTO tblStandings ({', '.join(headers)}) VALUES ({', '.join(['?' for _ in headers])})", row)
            # Commit changes to the database
            conn.commit()
            tk.messagebox.showinfo("Success", "Data inserted successfully.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            # Close database connection
            conn.close()
        
    def delete_selected_users(self):
        # Get selected items
        selection = self.user_tree.selection()
        if selection:
            # Ask for confirmation before deleting
            if tk.messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected user(s)?"):
                db_file = "tblUsers.db"
                connect = sqlite3.connect(db_file)
                cursor = connect.cursor()
                # Delete selected users from the database
                for item in selection:
                    # Assuming "Username" is unique and using it to identify the user
                    username = self.user_tree.item(item, "values")[0]
                    cursor.execute("DELETE FROM Users WHERE username=?", (username,))
                connect.commit()
                connect.close()
                # Refresh the user treeview
                self.user_tree.delete(*self.user_tree.get_children())
                self.load_users()
                tk.messagebox.showinfo("Success", "Selected user(s) deleted successfully.")
        else:
            tk.messagebox.showwarning("Warning", "Please select one or more users to delete.")
        
    def load_users(self):
        db_file = "tblUsers.db"
        connect = sqlite3.connect(db_file)
        cursor = connect.cursor()
        cursor.execute("SELECT username, password, is_admin FROM Users")
        users = cursor.fetchall()
        for user in users:
            self.user_tree.insert("", tk.END, values=user)
        connect.close()
        

        
    def load_comments(self):
        db_file = "tblUsers.db"
        connect = sqlite3.connect(db_file)
        cursor = connect.cursor()
        cursor.execute("SELECT id, comment FROM Comments")
        comments = cursor.fetchall()
        for comment in comments:
            self.comment_tree.insert("", tk.END, values=comment)
        connect.close()
        
    def delete_selected_comments(self):
        # Get selected items
        selection = self.comment_tree.selection()
        if selection:
            # Ask for confirmation before deleting
            if tk.messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected comments?"):
                db_file = "tblUsers.db"
                connect = sqlite3.connect(db_file)
                cursor = connect.cursor()
                # Delete selected comments from the database
                for item in selection:
                    comment_id = self.comment_tree.item(item, "values")[0]
                    cursor.execute("DELETE FROM Comments WHERE id=?", (comment_id,))
                connect.commit()
                connect.close()
                # Refresh the comment treeview
                self.comment_tree.delete(*self.comment_tree.get_children())
                self.load_comments()
                tk.messagebox.showinfo("Success", "Selected comments deleted successfully.")
        else:
            tk.messagebox.showwarning("Warning", "Please select one or more comments to delete.")
        
        