from sqlalchemy import create_engine
from sqlalchemy.sql.schema import Column, MetaData, Table
from sqlalchemy.sql.sqltypes import Integer, String


engine = create_engine('sqlite:///college.db', echo=True)
meta=MetaData()

students=Table(
    'students',meta,
    Column('id',Integer, primary_key=True),
    Column('first_name',String),
    Column('last_name',String),
)

# st=students.insert().values(first_name='Yan',last_name='Ikimoto')


# print(st)

s=students.select().where(students.c.first_name=='Yan')
print(s)
conn = engine.connect()
result = conn.execute(s)
print(result)
print([row for row in result])
# meta.create_all(engine)
