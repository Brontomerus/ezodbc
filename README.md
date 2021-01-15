# ezodbc

ezodbc is a package built for anyone using pandas with a database. ezodbc aims to make it easier, smoother, and more secure to access databases via python by creating a SQLAlechemy engine object to facilitate the connection. and combining that with a GUI based on the tkinter library to provide a simple and intuitive way to enter the required information. Passwords, usernames, and other sensitive information is not saved anywhere (but potentially your own computer in a future release to bypass having to enter it each time). Below is a list of the databases and connectors supported.


| Database                   |  ODBC Connector  | 
|:---------------------------|:----------------:|
| **Microsoft SQL Server**   | pyodbc, pymssql  |
| **MySQL**                  | MySQLdb          |
| **Postgres**               | psycopg2         |
| **SQLite**                 | sqlite3          |


## Installation

To install, you must have python 3.6+. Particularly, you will also need [Build Tools](https://www.microsoft.com/en-us/download/details.aspx?id=58317) installed for some odbc connector libraries, namely mysqlclient. If this gives you trouble, attempt to install those libraries individually as it may provide you with more context on a given issue.

`pip install ezodbc`




## Getting Started

The purpose of ezodbc is to provide users with a more seamless experience with pandas while using a database connection to pull data, most often using the [pd.read_sql()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html) method to retrieve that data. When you connect to a database that other users are also in, you run the possibility of accidently creating some sort of issue within the database itself as well as accidentally exposing the database to risk by leaving user credentials and hostname information hard-coded. Before the only way to avoid that was with environment variables, which might be confusing to any newer programmers out there - but now there is another... ezodbc!

An example of a simple use case, compared with that of regular useage of the connectors:
```python
import sqlalchemy
import pandas as pd
import ezodbc as ez


# both sql and timeout are optional with ezodbc - see below
def with_ezodbc() -> pd.DataFrame:
    df = ez.data().run_query()
    return df



HOSTNAME = '127.0.0.1:3306' # host:port ... another example would le my.database.local:3306 if there is a DNS
DB = 'myDatabaseName'
USER = 'my_username'
PASSWORD = 'my_password'
SQL = """SELECT * FROM [schema.tablename]"""
TIMEOUT = 60

# This is pretty much the minimum you can get with the connector
def without_ezodbc(user: str, password: str, hostname: str, db_name: str, sql: str, timeout: int = 30) -> pd.DataFrame:
    connection_string = 'mysql://'+user+':'+password+'@'+hostname+'/'+db_name
    engine = sqlalchemy.create_engine(connection_string, connect_args={'connect_timeout': 30}})
    with engine.connect() as connection:
        df = pd.read_sql(sql, connection)
    return df

```

During execution, you'll see a window pop-up for you to then enter the required information. The window looks like this:






## Fields & Their Usage

There are several selections and entries you must make to properly use ezodbc:

__Database Type (buttons on left)__ - This is to select the type of connector you'd like to use. The default is pymssql, which is the only one which requires the user to have a __Domain__ filled in.

1. __Domain__ - This is refering to the domain of a username. An example is CORP\brandon, where CORP\ is the domain. This can be left black in all cases but with the default, Microsoft SQL Server Free TDS.
2. __Username__ - username for access to the database
3. __Password__ - password for the username to authenticate
4. __Database Connection String__ - Host:Port ... in some cases, host will be an IP address, and sometimes it will have a DNS and appear as text. _examples_: 127.0.0.1:3306 and my.database.local:3306
5. __Copy/Paste SQL Query__ - the SQL Query you want to run. This is optional if you provide it in the constructor, ie df = ez.data(sql="give me your data plz, mr. database")


## Query timeouts

You can declare connection timeouts (seconds) for running your query. To do so, simply create the constructor with the optional "timeout=" parameter.

```python
import ezodbc as ez
sql_query = """give me your data plz, mr. database"""
df = ez.data(sql=sql_query, timeout=30).run_query()
```


## Planned Enhancements

1. Ability to save connection "profiles" in user's root directory. ie C:/users/USER_NAME/.ezodbc/connections
2. Ability to declare more kwargs for connections. Currently only able to declare query timeout


