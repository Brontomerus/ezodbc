import sqlalchemy
import pandas as pd 
from ezodbc.ui import Prompt

class data:
    def __init__(self, _query_timeout: int = 0) -> None:
        self.query_timeout = _query_timeout
        self.sql: str = "select 'Im a teapot'"

        try:
            self.prompt = Prompt()
            self.sql = self.prompt.sql
            self.connection_string: str = self.set_conn_str()
            self.engine = self.set_engine()
        except Exception as e:
            print('oh shit')
        finally:
            self.prompt.assure_close()
        
        self._query()
        

    def set_engine(self) -> None:
        self.engine = sqlalchemy.engine(self.connection_string, connect_args={'connect_timeout': self.query_timeout})
    

    def set_conn_str(self) -> None:
        rdbms_mapper = { # defined in https://docs.sqlalchemy.org/en/13/core/engines.html
            "pyodbc":"mssql+pyodbc://",
            "pymyssql":"mssql+pymssql://",
            "mysqldb":"mysql+mysqldb://",
            "psycopg2":"postgresql+psycopg2://",
            "sqlite3":"sqlite:///" # needs //// (4 slashes for mac/linux 'sqlite:///C:\\path\\to\\foo.db')
        }
        try:
            self.rdbms = rdbms_mapper[self.prompt.rdbms]
            conn_str =  f'{self.rdbms}{self.prompt.domain}\{self.prompt.username}:{self.prompt.password}@{self.prompt.hostip}/{self.prompt.db}'
            print(conn_str)
        except Exception as e:
            ValueError("something ain't quite right.")
        return conn_str

    def _query(self) -> pd.DataFrame:
        with self.engine.connect() as connection:
            df = pd.read_sql(self.sql, connection)
        return df


