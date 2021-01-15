# from ezodbc import core
# from ezodbc import ui

# # p = ui.Prompt()

# test = core.data()


from ezodbc import data
import pandas as pd
df = data().run_query(sql="select * from LogRequests")
print(df.head(10))
# , connect_args={'connect_timeout': self.query_timeout}
