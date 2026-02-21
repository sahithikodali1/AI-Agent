import sqlite3

DB_NAME = "travelai.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        request TEXT,
        itinerary TEXT,
        content TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_session(request, itinerary, content):
    import json
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO sessions (request,itinerary,content) VALUES (?,?,?)",
              (json.dumps(request), json.dumps(itinerary), json.dumps(content)))
    conn.commit()
    conn.close()

# import sqlite3
# import json

# # Connect to your local SQLite file
# conn = sqlite3.connect("travelai.db")
# c = conn.cursor()

# # Show tables
# c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print("Tables:", c.fetchall())

# # Fetch all sessions
# c.execute("SELECT * FROM sessions")
# rows = c.fetchall()
# for row in rows:
#     session_id = row[0]
#     request = json.loads(row[1])
#     itinerary = json.loads(row[2])
#     content = json.loads(row[3])
#     print(f"Session {session_id}:")
#     print("Request:", request)
#     print("Itinerary:", itinerary)
#     print("Content:", content)
#     print("-"*40)

# conn.close()