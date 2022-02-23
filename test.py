import sqlite3

con=sqlite3.connect('test_movies.db')
print("database created")

con.execute('create table Movies(id int primary key not null,name text,actore text,actress text,director text,year of release text)')
print("table created")

con.execute('insert into Movies values(1,"Bachan_pandey","akshay_kumar","kirti_salon","Farhad_Samji","2022")')
print("data insert succesfully")

con.commit()
data=con.execute('select * from Movies')

for row in data:
    print("id:{0},name:{1},actore:{2},actress:{3},director:{4},year of release text:{5}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
