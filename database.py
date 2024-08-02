import sqlite3

conn = sqlite3.connect("form.db")

create_table_query = """
create table form_record(name varchar(40), mail varchar(40), message varchar(120))
"""

cur = conn.cursor()
cur.execute(create_table_query)
print("Table created successfully in database.")

cur.close()
conn.close()
