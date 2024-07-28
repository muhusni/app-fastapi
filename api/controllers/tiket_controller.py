from typing import List, Annotated

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc, and_

from api.models.tiket import Tiket, TicketReply
from api.schemas.tiket import TiketResponse
from database import get_db_tiket
import re


class TiketController:
    # @app.get("/tickets/", response_model=List[TiketResponse])
    @staticmethod
    async def get_tickets(db: Annotated[Session, Depends(get_db_tiket)], skip: int = 0, limit: int = 10):
        tickets = db.query(Tiket).options(joinedload(Tiket.ticketReplies), joinedload(Tiket.ticketCategory),
                                          joinedload(Tiket.ticketStatus)).offset(skip).limit(limit).all()
        return tickets

    @staticmethod
    async def get_ticket(ticket_id: int, db: Annotated[Session, Depends(get_db_tiket)]):
        print(ticket_id)
        ticket = db.query(Tiket).options(joinedload(Tiket.ticketReplies), joinedload(Tiket.ticketCategory),
                                         joinedload(Tiket.ticketStatus)).filter(Tiket.ID == ticket_id).first()
        if ticket is None:
            raise HTTPException(status_code=404, detail="Ticket not found")

        # Process the ticket to extract the IKC number
        ticket.ticket_IKC = None
        for reply in ticket.ticketReplies:
            if 'IKC' in reply.body:
                matches = re.findall(r'\b\d{6}\b', reply.body)
                if matches:
                    ticket.ticket_IKC = matches[0]
                    break

        return ticket

    @staticmethod
    async def get_ticket_by_ikc_ticket(nomor_tiket_ikc: int, db: Annotated[Session, Depends(get_db_tiket)]):
        len_nomor = len(str(nomor_tiket_ikc))
        if len_nomor != 6:
            raise HTTPException(status_code=422, detail="Tiket IKC tidak valid")
        # try: 
        ticket = db.query(TicketReply).filter(
            and_(
                TicketReply.body.ilike(f"%IKC%"),
                TicketReply.body.ilike(f"% {nomor_tiket_ikc}%")
                # TicketReply.body.op('regexp')(r"\b\d{6}\b")
            )
        ).options(
            joinedload(TicketReply.ticket)  # Ensure the ticket data is eagerly loaded
        ).first()

        if ticket is None:
            raise HTTPException(status_code=404, detail="not found")

        ticket.ticketIkc = nomor_tiket_ikc

        return ticket
        # except: 
        #     raise HTTPException(status_code=500, detail="error")