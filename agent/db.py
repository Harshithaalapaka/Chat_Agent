import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    message TEXT
)
""")
conn.commit()

# Function to save a message
def save_conversation(role, message):
    cursor.execute(
        "INSERT INTO chat_memory (role, message) VALUES (?, ?)",
        (role, message)
    )
    conn.commit()

# Function to get all previous messages
def get_conversation_history():
    cursor.execute("SELECT role, message FROM chat_memory")
    rows = cursor.fetchall()
    history = ""
    for role, message in rows:
        history += f"{role}: {message}\n"
    return history
