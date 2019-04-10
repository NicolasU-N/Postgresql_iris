from sqlalchemy import create_engine
from sqlalchemy import text
from pandas import DataFrame

class IrisPostgres:

    def getConnection(self):
        # create connection
        engine = create_engine('postgres://iris:iris@localhost:5432/iris',convert_unicode=True)
        return engine
    
    def getDataframe(self):
        # execute query
        sql = text('select sepal_length, sepal_width, petal_length, petal_width, category from iris')
        engine = self.getConnection()
        result = engine.execute(sql)
        # convert sqlalchemy.engine.result to pandas dataframe
        dataframe = DataFrame(result.fetchall())
        dataframe.columns = result.keys()
        print(dataframe.head(5))
        return dataframe