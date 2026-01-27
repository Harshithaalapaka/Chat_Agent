import sqlite3
connection = sqlite3.connect("memory.db", check_same_thread=False)
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    message TEXT
)
""")
connection.commit()
def save_conversation(role, message):
    cursor.execute(
        "INSERT INTO chat_memory (role, message) VALUES (?, ?)",
        (role, message)
    )
    connection.commit()

def get_conversation_history():
    cursor.execute("SELECT role, message FROM chat_memory")
    rows = cursor.fetchall()
    history = ""
    for role, message in rows:
        history += f"{role}: {message}\n"
    return history
