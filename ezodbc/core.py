import sqlalchemy
import pandas as pd 
from ui import Prompt

class Connect:
    def __init__(self, _query_timeout: int = 0) -> None:
        self.connection_string: str = ''
        self.sql: str = ''
        self.engine = engine
        self.query_timeout = _query_timeout

    @property
    def engine(self) -> sqlalchemy.engine:
        return self.engine

    @engine.setter
    def engine(self) -> None:
        self.engine = sqlalchemy.engine(self.connection_string, connect_args={'connect_timeout': self.query_timeout})
    
    @engine.deleter
	def engine(self) -> None:
		del self.engine

    @property
    def connection_string(self) -> str:
        return self.connection_string

    @connection_string.setter
    def _connection_str(self) -> None:
        try:
            propmt = Prompt()
            self.sql = prompt.sql
            self.connection_string = f'mssql+pymssql://{propmt.domain}\{propmt.username}:{propmt.password}@{propmt.hostip}/{propmt.db}
            del prompt
            print(self.connection_string)
        except:
            ValueError("something ain't quite right.")
    
    @connection_string.deleter
	def _connection_str(self) -> None:
		del self._connection_str


    def query(self) -> pd.DataFrame:
        with sqlalchemy.engine.connect(self.connection_string, ):
            df = pd.read_sql(self.sql, connection)

