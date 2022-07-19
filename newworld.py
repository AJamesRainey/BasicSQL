# %%
import sqlite3

connection = sqlite3.connect('newworld.db')

cursor = connection.cursor()

'''Create table'''

c1 = """CREATE TABLE IF NOT EXISTS stores(store_id INTEGER PRIMARY KEY, location TEXT)"""
cursor.execute(c1)

# %%
'''Insert into table'''
c2 = "INSERT INTO stores VALUES (1, 'Rexburg, ID')"
c3 = "INSERT INTO stores VALUES (2, 'Logan, UT')"


cursor.execute(c2)
cursor.execute(c3)

# %%

'''Function to select all entries from table'''
def select_all():
    c4 = "SELECT * FROM stores"
    cursor.execute(c4)
    results = cursor.fetchall()
    print(results)
select_all()
# %%

'''Assign variables for multiple insertions into database at once'''
store_ids = [(3, 4, 5, 6, 7, 8, 9, 10)]
locations = [
("American Falls, ID"), 
("Boise, ID"),
("Idaho Falls, ID"),
("Rigby, ID"),
("Pocatello, ID"),
("Mountain Home, ID"),
("Jackson Hole, WY"),
("Salt Lake City, UT")
]


#First attempt at mass insertion(failed)
'''command4 = "INSERT INTO stores (store_id, location) VALUES (%s, %s)"'''

#second attempt at mass insertion(failed)
''' cursor.execute("INSERT INTO stores (store_id, location) VALUES (:store_id, :location)", [store_ids , locations])'''
# %%
'''Modify Data'''
#Sqlite does not support boolean datatypes. So assign a new in_idaho column as int'''
c5 = "ALTER table stores ADD in_idaho INTEGER"
cursor.execute(c5)
results = cursor.fetchall()
print(results)
# %%
'''Query database to check if new column exists '''
select_all()
# %%
#Query subset of data when 
c6 = "SELECT * FROM stores WHERE location LIKE '%ID%'"
cursor.execute(c6)
results = cursor.fetchall()
print(results)


#First attempt to insert 1 into 1st in_idaho entry(failed)
c7 = "INSERT INTO stores(in_idaho) VALUES (1)"
cursor.execute(c7)

# %% 
#Second attempt: to insert 1 when select statement is true, elsewise insert 0(Failed)
'''
c7 = "INSERT INTO stores(location)
SELECT case
    WHEN location like '%sID%' then 1
    else 
from data;
"
'''
# %%
select_all()
# %%

'''Delete from table'''

#Delete results of failed entry into in_idaho
c8 = "DELETE FROM stores WHERE store_id=3;"
cursor.execute(c8)

#check results
select_all()

# %%
