# from ezodbc import core
# from ezodbc import ui

# # p = ui.Prompt()

# test = core.data()


from ezodbc import ez
import pandas as pd


def test_base_obj():
    d = ez(timeout=30)

def test_profile(profile: str):
    profile = Profile('sagh://my-connection-string@fancy:database/lol','testing', append_new=False)
    print(profile.open_profile())
    # assert profile.open_profile() == profile
    
def test_query(table: str):
    sql= f"select * from {table}"
    df = ez(timeout=30).run_query(sql=sql)
    # assert df is not None
    print(df.head(10))

def test_query_profile(profile: str, table: str):
    sql= f"select * from {table}"
    df = ez(profile_name=profile, timeout=30).run_query(sql=sql)
    # assert df is not None
    print(df.head(10))


# test_query_profile('MockAPI', 'LogRequests')
test_query('LogRequests')



