# from ezodbc import core
# from ezodbc import ui

# # p = ui.Prompt()

# test = core.data()


import ezodbc
import pandas as pd
df = ezodbc.data()
print(df.head(10))