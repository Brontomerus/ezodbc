import tkinter as tk

from tkinter import ttk


class Prompt(tk.Tk):
    def __init__(self):
        self.rdbms: str = ''
        self.domain: str = ''
        self.username: str = ''
        self.password: str = ''
        self.hostip: str = ''
        self.db: str = ''
        self.sql: str = ''
        self.fields = ['Domain', 'Username', 'Password', 'Database Connection String', 'Database Name', 'Copy/Paste SQL Query']
        
        tk.Tk.__init__(self)
        self.chk = DBSelector(self)
        self.chk.pack(side=tk.LEFT,  fill=tk.X)
        self.chk.config(relief=tk.GROOVE, bd=2)
        self.ents = self._makeform()
        self.bind('<Return>', (lambda event, e=self.ents: self._fetch(e))) 
        self.button = tk.Button(self, text='submit', width = 60, fg="white", bg="blue",command=(lambda e=self.ents: self._fetch(e)))
        self.button.pack(padx=5, pady=5)
        self.mainloop()


    def _fetch(self, entries) -> None:
        self.rdbms = self.chk.selection()
        self.domain = entries[0][1].get()
        self.username = entries[1][1].get()
        self.password = entries[2][1].get()
        self.hostip = entries[3][1].get()
        self.db = entries[4][1].get()
        self.sql = entries[5][1].get()
        self.quit()


    def _makeform(self):
        entries = []     
        self.chkstates = self.chk.state()
        # entries.append((chk,ent))
        for field in self.fields:
            row = tk.Frame(self)
            lab = tk.Label(row, width=35, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=35, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))
        return entries
    
    def _close(self) -> None:
        try:
            del self.rdbms
            del self.username
            del self.password
            del self.hostip
            del self.sql
            self.quit()
        except Exception as e:
            pass







class DBSelector(tk.Frame):
    def __init__(self, parent=None, side=tk.LEFT):
        tk.Frame.__init__(self, parent)
        self.rdbms_mapper = {
            1:"pymssql",
            2:"pyodbc",
            3:"mysqldb",
            4:"psycopg2",
            5:"sqlite3"
        }
        self.var = tk.IntVar()
        self.var.set(1)
        self.vars = []
        tk.Radiobutton(self, text = "Microsoft SQL Server FreeTDS - pymssql", variable=self.var, value = 1, command=self.state).grid(row=1, sticky=tk.W)
        tk.Radiobutton(self, text = "Microsoft SQL Server - pyodbc", variable=self.var, value = 2, command=self.state).grid(row=2, sticky=tk.W)
        tk.Radiobutton(self, text = "MySQL - mysqldb", variable=self.var, value = 3, command=self.state).grid(row=3, sticky=tk.W)
        tk.Radiobutton(self, text = "Postgres - psycopg2", variable=self.var, value = 4, command=self.state).grid(row=4, sticky=tk.W)
        tk.Radiobutton(self, text = "Sqlite - sqlite3", variable=self.var, value = 5, command=self.state).grid(row=5, sticky=tk.W)
        self.state()

    def state(self) -> str:
        self.vars.append(self.rdbms_mapper[self.var.get()])
        selection: str = self.rdbms_mapper[self.var.get()]
        return self.var.get()

    def selection(self) -> str:
        return self.vars[-1] # last selection made


