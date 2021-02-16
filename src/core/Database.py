from config import config
import psycopg2
from psycopg2.extras import RealDictCursor

databaseConfig = config(section='database')

class Database:

    connection = None
    allowed_fetch_name = ['fetchone', 'fetchmany', 'fetchall']
    
    def __init__ (that):
        that.connection = None

    def create_cursor (that, **cursor_params):
        if that.connection is None:
            that.connection = psycopg2.connect(**databaseConfig)
            that.connection.autocommit = True

        return that.connection.cursor(**cursor_params)

    def create_query (that, template_string, **params):
        return template_string.format(**params)

    def safe_fetch (that, fetch_name, query, *fetch_params):
        if not fetch_name in that.allowed_fetch_name:
            return
        try:
            cur = that.create_cursor(cursor_factory=RealDictCursor)
            cur.execute(query)
            print('Query executed: ', query)

            # hack the native fetchone method
            if (fetch_name == 'fetchone'):
                res = cur.fetchmany(1)
                if (len(res) > 0):
                    res = res[0]
                else:
                    res = None
            else:
                res = getattr(cur, fetch_name)(*fetch_params)
            
            cur.close()

            return res
        except (Exception, psycopg2.DatabaseError) as error:
            return None, error
        finally:
            that.end()

    # safe execution
    def safe_exec (that, query):
        print(query)
        try:
            cur = that.create_cursor()
            cur.execute(query)
            print('Query executed: ', query)
            res = cur.fetchone()[0]

            return res
        except (Exception, psycopg2.DatabaseError) as error:
            if (isinstance(error, psycopg2.errors.UniqueViolation)):
                raise Exception('Item already exists', 400)
            if (isinstance(error, psycopg2.errors.NotNullViolation)):
                raise Exception('Some fields are missing', 400)    
            return None, error
        finally:
            that.end()

    def to_sql_values (that, values):
        sql_values = []
        for v in values:
            if isinstance(v, (int, float)):
                sql_values.append(str(v))
            elif isinstance(v, (type(None))):
                sql_values.append('NULL')
            else:
                sql_values.append('\'{v}\''.format(v=v))
        return sql_values
            
    
    def end (that):
        if that.connection is not None:
            that.connection.close()
            that.connection = None
