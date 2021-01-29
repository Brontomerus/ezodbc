from ezodbc import ez
import pandas as pd
import unittest

# class TestCore(unittest.TestCase):

def test_base_obj():
    d = ez(timeout=30)

def test_query(table: str):
    sql= f"select * from {table}"
    df = ez(timeout=30).run_query(sql=sql)
    assert isinstance(df, pd.DataFrame)

def test_query_profile(profile: str, table: str):
    sql= f"select * from {table}"
    df = ez(profile_name=profile, timeout=30).run_query(sql=sql)
    # assert df is not None
    print(df.head(10))


# this test is run manually due to the user interface being difficult to test in an automated manner
if __name__ == "__main__":
    test_base_obj()

    table = input("Enter a name of a testing table in your database:    ")
    test_query(table)

    table = input("Enter a profile of a testing table in your database:    ")
    test_query_profile(profile=profile, table=table)

    
