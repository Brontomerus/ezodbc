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
    assert profile.open_profile() == profile
    
def test_query(table: str):
    df = ez(timeout=30).run_query(sql="select * from {table}")
    print(df.head(10))

def test_query_profile(profile: str, table: str):
    sql= f"select * from {table}"
    df = ez(profile_name=profile, timeout=30).run_query(sql=sql)
    print(df.head(10))

test_query_profile('MockAPI', 'LogRequests')
test_base_obj()