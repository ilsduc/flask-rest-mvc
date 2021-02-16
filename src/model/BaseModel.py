from core.Database import Database
from abc import abstractmethod
from core.JsonSerializable import JsonSerializable
from copy import copy

class BaseModel(JsonSerializable):

    db = Database()
        
    def __init__ (that):
        # init with empty object
        for var in that.get_variables():
            that.set(var, None)
        
    @property
    @abstractmethod
    def __key__ (that):
        """ return the id key name """
        
    @property
    @abstractmethod
    def __table__ (that):
        """ return table name """

    @property
    @abstractmethod
    def __variables__ (that):
        """ return model variables """

    def hydrate (that, data, empty_resource_on_fallback=False):
        for column in that.get_variables():
            if data and column in data:
                that.set(column, data[column])
            elif (empty_resource_on_fallback):
                that.set(column, None)

        return that

    def hydrate_collection (that, collection):
        new_collection = []
        for row in collection:
            model = copy(that)
            new_collection.append(model.hydrate(row))
            
        return new_collection

    """
        Save model
    """
    def save (that):
        key = that.get_key()
        key_value = that.get(key)
        table = that.get_table()
        variables, values = that.exclude([key])
        sql_values = that.db.to_sql_values(values)

        if key_value is None:
            # insert
            query = that.db.create_query(
                'INSERT INTO {table} ({columns}) VALUES ({values}) RETURNING {key};',
                table=table,
                columns=", ".join(variables),
                values=", ".join(sql_values),
                key=key
            )

            that.set(key, that.db.safe_exec(query))
        else:
            # update
            setters = [ '{variable}={value}'.format(variable=variables[i], value=sql_values[i]) for i in range(len(variables)) ]
            query = that.db.create_query(
                'UPDATE {table} SET {setters} WHERE {key} = {key_value}',
                table=table,
                setters=', '.join(setters),
                key=key,
                key_value=key_value
            )
            that.db.safe_exec(query)

        return that
    
    """
        Find ONE row based on where clause
        where: dict - Leav blank to get them all
    """
    def findOne(that, where):

        whereKeys = list(where)
        whereValues = that.db.to_sql_values(where.values())
        whereClause = [ '{key}={value}'.format(key=whereKeys[key], value=whereValues[key]) for key in range(len(whereKeys)) ]
        
        query = that.db.create_query('SELECT {variables} FROM {table} WHERE {whereClause};',
            variables=', '.join(["{v} as {v}".format(v=v) for v in that.get_variables()]),
            key=that.get_key(),
            table=that.get_table(),
            key_value=id,
            whereClause=' AND '.join(whereClause)
        )

        row = that.db.safe_fetch('fetchone', query)
        
        return that.hydrate(row)
    
    """
        Find a model based on its key
    """
    def findById (that, id):
        key = that.get_key()
        
        where = {
            key: id 
        }
        
        return that.findOne(where)
    
    """
        Find rows based on where clause
        where: dict - Leav blank to get them all
    """
    def find(that, where = {1:1}, orderBy = {}):
        whereKeys = list(where)
        whereValues = that.db.to_sql_values(where.values())
        whereClause = [ '{key}={value}'.format(key=whereKeys[key], value=whereValues[key]) for key in range(len(whereKeys)) ]

        if (not orderBy):
            orderBy = {
                that.get_key(): 'ASC'
            }

        orderByKeys = list(orderBy)
        orderByDirections = list(orderBy.values())
        orderByClause = [ '{orderBy} {order}'.format(orderBy=orderByKeys[key], order=orderByDirections[key],) for key in range(len(orderByKeys)) ]
        
        query = that.db.create_query(
            'SELECT {variables} FROM {table} WHERE {whereClause} ORDER BY {orderBy};',
            variables=', '.join(that.get_variables()),
            table=that.get_table(),
            whereClause=' AND '.join(whereClause),
            orderBy=', '.join(orderByClause)
        )
        
        rows = that.db.safe_fetch('fetchall', query)

        return that.hydrate_collection(rows)

    def remove (that):
        key = that.get_key()
        key_value = that.get(key)

        query = that.db.create_query(
            'DELETE FROM {table} WHERE {key}={key_value} RETURNING {key};',
            table=that.get_table(),
            key=key,
            key_value=key_value
        )

        res = that.db.safe_exec(query)
        return res

    def is_valid (that):
        return not not that.get(that.get_key())

    def exclude (that, excluded_keys):
        variables = that.get_variables()
        values = that.get_values()
        new_variables = []
        new_values = []
        for i in range(len(variables)):
            if variables[i] in excluded_keys:
                continue
            new_variables.append(variables[i])
            new_values.append(values[i])

        return new_variables, new_values

    """
        Model getter and setter
    """
    def get (that, prop, fallback_value = None):
        if prop in that.get_variables():
            v = getattr(that, prop, fallback_value)
            return v if v is not None else fallback_value
        return fallback_value
    
    def set (that, prop, value):
        if prop in that.get_variables():
            setattr(that, prop, value)

    """
        Base model getter information
    """
    def get_key (that):
        return that.__key__

    def get_table (that):
        return that.__table__

    def get_variables (that):
        return that.__variables__

    def get_values (that):
        values = []
        for k in that.get_variables():
            values.append(that.get(k))
        return values
    
    def get_name (that):
        return that.__class__.__name__