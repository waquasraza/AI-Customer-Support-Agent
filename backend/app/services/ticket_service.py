import json
import uuid
import os

from app.core.database import get_connection


def create_ticket(question: str, category: str ):

    conn = get_connection()

    cursor = conn.cursor()

    ticket = {
        "ticket_id": str(uuid.uuid4())[:8],
        "category": category,
        "question": question,
        "status": "open"
    }

    cursor.execute(
            """
            INSERT INTO tickets(
                ticket_id,
                category,
                question,
                status
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                ticket["ticket_id"],
                ticket["category"],
                ticket["question"],
                ticket["status"]
            )
        )

    conn.commit()

    conn.close()

    return ticket


def get_all_tickets():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tickets"
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        dict(row)
        for row in rows
    ]


def get_ticket(ticket_id: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM tickets
        WHERE ticket_id = ?
        """,
        (ticket_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return dict(row)

    return None


def update_ticket_status(ticket_id: str, status: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tickets
        SET status = ?
        WHERE ticket_id = ?
        """,
        (
            status,
            ticket_id
        )
    )

    conn.commit()

    ticket = get_ticket(
        ticket_id
    )

    conn.close()

    return ticket