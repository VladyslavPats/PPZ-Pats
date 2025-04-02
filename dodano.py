import sqlite3

conn = sqlite3.connect("../../AppData/Roaming/JetBrains/PyCharmCE2023.3/scratches/trains.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS trains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    destination TEXT
)
""")


cursor.execute("INSERT INTO trains (name, destination) VALUES ('Express 101', 'Ivano-Frankivsk')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Fast 202', 'Japan')")


conn.commit()
conn.close()

print("✅ Дані успішно додані!")