import tkinter as tk

class Prompt(tk.Tk):
    def __init__(self):
        self.fields = ['Domain', 'Username', 'Password', 'Database Connection String', 'Database Name', 'Copy/Paste SQL Query']
        tk.Tk.__init__(self)
        self.ents = self._makeform()
        self.bind('<Return>', (lambda event, e=self.ents: self._fetch(e))) 
        self.button = tk.Button(self, text='submit', command=(lambda e=self.ents: self._fetch(e)))
        self.button.pack(side=tk.LEFT, padx=5, pady=5)
        self.mainloop()
        

    def _fetch(self, entries):
        self.domain = entries[0][1].get()
        self.username = entries[1][1].get()
        self.password = entries[2][1].get()
        self.hostip = entries[3][1].get()
        self.db = entries[4][1].get()
        self.sql = entries[5][1].get()
        self.quit()

    def _makeform(self):
        entries = []
        for field in self.fields:
            row = tk.Frame(self)
            lab = tk.Label(row, width=35, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=35, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))
        return entries