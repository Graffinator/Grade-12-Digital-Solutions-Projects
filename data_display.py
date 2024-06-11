#data.display 
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk


class displayData(ttk.Frame):
    def __init__(self, master=None, db_file="IA2.db", table_names="tblStandings"):
        super().__init__(master)
        self.tree = ttk.Treeview(self)
        self.grid(sticky="nsew")
        self.db_file = db_file
        self.table_name = table_names
        connect = sqlite3.connect(self.db_file)

        yscrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="left", fill="y")

        xscrollbar = ttk.Scrollbar(self, orient="horizontal" , command=self.tree.xview)
        self.tree.configure(xscrollcommand=xscrollbar.set)
        xscrollbar.pack(side="bottom", fill="x")

        self.cursor = connect.cursor()
        self.buildTree(self.cursor)
        self.tree.pack(fill=BOTH, expand=1)

        
    def buildTree(self, cursor):
        cursor.execute(f"SELECT * FROM {self.table_name}")
        columns = [description[0] for description in cursor.description]
        self.tree["columns"] = columns
        self.tree['show'] = 'headings'
        for column in columns:
            self.tree.heading(columns, text=columns)
            self.tree.column(column, width=100)
        for row in self.cursor.fetchall():
            self.tree.insert("",'end', values=row)


    def __init__(self, master=None, db_file="IA2.db", table_names="tblPlayers"):
        super().__init__(master)
        self.tree = ttk.Treeview(self)
        self.grid(sticky="nsew")
        self.db_file = db_file
        self.table_name = table_names
        connect = sqlite3.connect(self.db_file)
        self.cursor = connect.cursor()
        self.buildTree(self.cursor)
        self.tree.pack(fill=BOTH, expand=1)

    def buildTree(self, cursor):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        columns = [description[0] for description in self.cursor.description]
        self.tree ["columns"] = columns
        self.tree ['show'] = 'headings'
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=100)
        for row in self.cursor.fetchall():
            self.tree.insert("",'end', values=row)

    def __init__(self, master=None, db_file="IA2.db", table_names="tblPlayerstats"):
        super().__init__(master)
        self.tree = ttk.Treeview(self)
        self.grid(sticky="nsew")
        self.db_file = db_file
        self.table_name = table_names
       

        connect = sqlite3.connect(self.db_file)
        self.cursor = connect.cursor()
        self.buildTree(self.cursor)
        self.tree.pack(fill=BOTH, expand=1)

    def buildTree(self, cursor):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        columns = [description[0] for description in self.cursor.description]
        self.tree ["columns"] = columns
        self.tree ['show'] = 'headings'
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=100)
        for row in self.cursor.fetchall():
            self.tree.insert("",'end', values=row)
            
            
            
            
class searchFunction:
    def __init__(self):
        pass
    
    def search(self, searchQuery, database, tree, entry):
        if searchQuery == "" or searchQuery == "Print...":
            print("null")
        else:
            thing = entry.get()
            print(thing)
            self.db_file = "IA2.db"
            tree.delete(*tree.get_children())
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            print(entry.get())
            if database == "tblStandings":
                cursor.execute("SELECT * FROM tblStandings WHERE nationality LIKE ? OR standing LIKE ?", ('%'+str(thing)+'%', '%'+str(thing)+'%'))
            if database == "tblPlayers":
                cursor.execute("SELECT * FROM tblPlayers WHERE nationality LIKE ? OR ranking LIKE ? OR playerID LIKE ? OR playerFirstName LIKE ?", ('%'+str(entry.get())+'%', '%'+str(entry.get())+'%','%'+str(entry.get())+'%', '%'+str(entry.get())+'%'))
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()

        