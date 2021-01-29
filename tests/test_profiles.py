from ezodbc import ez
from ezodbc.profiles import Profile
import pandas as pd
import unittest

class TestProfiles(unittest.TestCase):

    def test_profile():
        profile = Profile('sagh://my-connection-string@fancy:database/lol','testing')
        assert profile.open_profile() == profile
        assert profile._check_for_file() == True 
        assert profile._new_profile_dict() == {'testing':{'connection':'sagh://my-connection-string@fancy:database/yolo'}}

    def test_query_connection_str(table: str):
        profile = Profile('sagh://my-connection-string@fancy:database/lol','testing')
        conn_str = ez(profile_name=profile, timeout=30).set_conn_str()
        assert conn_str == 'sagh://my-connection-string@fancy:database/lol'

    def test_query_connection_str(table: str):
        profile = Profile('sagh://my-connection-string@fancy:database/lol','testing')
        conn_str = ez(profile_name=profile, timeout=30).set_conn_str()
        assert conn_str == 'sagh://my-connection-string@fancy:database/lol'

    def test_core_import_profile(table: str):
        profile = Profile('sagh://my-connection-string@fancy:database/lol','testing')
        conn_str = ez(profile_name=profile, timeout=30).import_profile(profile_name=profile)
        assert conn_str == 'sagh://my-connection-string@fancy:database/lol'

    
