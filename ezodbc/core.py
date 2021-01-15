import sqlalchemy
import pandas as pd 
from ezodbc.ui import Prompt

class data:
    def __init__(self, _query_timeout: int = 0) -> None:
        self.query_timeout = _query_timeout
        self.sql: str = "select 'Im a teapot'"

        try:
            self.prompt = Prompt()
            self.sql = self.prompt.sql or ''
            self.connection_string: str = self.set_conn_str()
            self.engine = self.start_engine()
        except Exception as e:
            print(str(e))
            print('Error!')
               

    def start_engine(self) -> sqlalchemy.engine:
        if self.prompt.rdbms in('pymssql'):
            engine = sqlalchemy.create_engine(self.connection_string, connect_args={'timeout': self.query_timeout})
        else:
            engine = sqlalchemy.create_engine(self.connection_string, connect_args={'connect_timeout': self.query_timeout})
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


    def run_query(self, **kwargs) -> pd.DataFrame:
        if kwargs.get("sql") is not None:
            self.sql = kwargs.get("sql")
        with self.engine.connect() as connection:
            df = pd.read_sql(self.sql, connection)
        return df


