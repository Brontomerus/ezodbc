import sqlalchemy
import pandas as pd 
from ezodbc.ui import Prompt, Profile_Prompt

class ez:
    def __init__(self, timeout: int = 0, profile_name: str = None) -> None:
        self.query_timeout = timeout
        self.sql: str = None
        self.profile_name = profile_name
        if self.profile_name is None:
            try:
                self.prompt = Prompt()
                self.sql = self.prompt.sql or ''
                self.connection_string: str = self.set_conn_str()
                if self.prompt.save_profile:
                    p = Profile_Prompt()
                    self.profile_name = p.profile_name
                    if self.profile_name is None or self.profile_name == '':
                        raise ValueError('Profile must have a valid name!')
                    self._add_profile_if_works()
            except Exception as e:
                print(str(e))
                print('Error!')
        else:
            self.connection_string: str = self.import_profile(self.profile_name)
        self.engine = self.start_engine(timeout=self.query_timeout)


    def start_engine(self, timeout: int = 0) -> sqlalchemy.engine:
        if "pymssql" in self.connection_string:
            engine = sqlalchemy.create_engine(self.connection_string, connect_args={'timeout': timeout})
        else:
            engine = sqlalchemy.create_engine(self.connection_string, connect_args={'connect_timeout': timeout})
        return engine
    

    def set_conn_str(self) -> None:
        rdbms_mapper = { # defined in https://docs.sqlalchemy.org/en/13/core/engines.html
            "pyodbc":"mssql+pyodbc://",
            "pymssql":"mssql+pymssql://",
            "mysqldb":"mysql://",
            "psycopg2":"postgresql+psycopg2://",
            "sqlite3":"sqlite:///" # needs //// (4 slashes for mac/linux 'sqlite:///C:\\path\\to\\foo.db')
        }
        try:
            self.rdbms = rdbms_mapper[self.prompt.rdbms]
            if self.prompt.domain is None or self.prompt.domain == '':
                conn_str =  f'{self.rdbms}{self.prompt.username}:{self.prompt.password}@{self.prompt.hostip}/{self.prompt.db}'
            else:    
                conn_str =  f'{self.rdbms}{self.prompt.domain}\{self.prompt.username}:{self.prompt.password}@{self.prompt.hostip}/{self.prompt.db}'
        except Exception as e:
            ValueError("something ain't quite right with the entered information.")

        return conn_str


    def import_profile(self, profile_name: str) -> str:
        from ezodbc.profiles import Profile
        profile = Profile(profile_name=profile_name)
        return profile.open_profile()

    def _add_profile_if_works(self) -> None:
        from ezodbc.profiles import Profile
        temp_engine = self.start_engine(timeout=15)
        print(self.connection_string)
        print(self.profile_name)
        # try:
        with temp_engine.connect() as connection:
            pass    
        Profile(profile_name=self.profile_name, connection_string=self.connection_string)
        # except Exception as e:
        #     print("Was not able to connect using this profile - it will not be saved.")


    def run_query(self, **kwargs) -> pd.DataFrame:
        if kwargs.get("sql") is not None:
            self.sql = kwargs.get("sql")
        with self.engine.connect() as connection:
            df = pd.read_sql(self.sql, connection)
        return df


