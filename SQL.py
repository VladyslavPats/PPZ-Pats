import sqlite3

def fetch_all_data(db_name):

   conn = sqlite3.connect(db_name)
   cursor = conn.cursor()

   cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
   tables = cursor.fetchall()


   print("Таблиці в базі даних:")
   for table in tables:
       table_name = table[0]
       print(f"\nТаблиця: {table_name}")


       cursor.execute(f"SELECT * FROM {table_name}")
       rows = cursor.fetchall()


       cursor.execute(f"PRAGMA table_info({table_name})")
       columns = [col[1] for col in cursor.fetchall()]
       print(" | ".join(columns))


       for row in rows:
           print(row)



   conn.close()



fetch_all_data("trains.db")