from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ticket_service import (
    get_all_tickets,
    get_ticket,
    update_ticket_status
)

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


class TicketUpdateRequest(BaseModel):
    status: str

@router.get("/")
async def list_tickets():

    tickets = get_all_tickets()

    return tickets

@router.get("/{ticket_id}")
async def get_ticket_by_id(ticket_id: str):

    ticket = get_ticket(ticket_id)

    if not ticket:

        return {
            "message": "Ticket not found"
        }

    return ticket

@router.patch("/{ticket_id}")
async def update_ticket(ticket_id: str, request: TicketUpdateRequest):

    ticket = update_ticket_status(
        ticket_id,
        request.status
    )

    if not ticket:

        return {
            "message": "Ticket not found"
        }

    return {
        "message": "Ticket updated",
        "ticket": ticket
    }