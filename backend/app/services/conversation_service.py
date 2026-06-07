from app.core.database import get_connection


def save_message(session_id: str, role: str, content: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO conversations(
            session_id
        )
        VALUES(?)
        """,
        (session_id,)
    )

    cursor.execute(
        """
        INSERT INTO messages(
            session_id,
            role,
            content
        )
        VALUES(?, ?, ?)
        """,
        (
            session_id,
            role,
            content
        )
    )

    conn.commit()

    conn.close()


def get_conversation_history(session_id: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, content
        FROM messages
        WHERE session_id = ?
        ORDER BY id DESC
        LIMIT 10
        """,
        (session_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    history = ""

    for row in rows:

        history += (
            f"{row['role']}: {row['content']}\n"
        )

    return history