from pydantic import BaseModel
from typing import List, Optional


class TicketReplyResponse(BaseModel):
    id: int
    ticketid: int
    reply: str

    class Config:
        from_attributes = True


class TicketCategoryResponse(BaseModel):
    ID: int
    name: str
    description: Optional[str]
    cat_parent: Optional[int]
    image: Optional[str]
    no_tickets: Optional[int]
    auto_assign: Optional[int]

    class Config:
        from_attributes = True


class TicketStatusResponse(BaseModel):
    ID: int
    name: str
    color: Optional[str]
    close: Optional[int]
    text_color: Optional[str]

    class Config:
        from_attributes = True


class TiketResponse(BaseModel):
    ID: int
    title: str
    body: str
    categoryid: Optional[int]
    status: Optional[int]
    ticket_replies: List[TicketReplyResponse] = []
    ticketCategory: Optional[TicketCategoryResponse]
    ticketStatus: Optional[TicketStatusResponse]
    ticket_IKC: str | None

    class Config:
        from_attributes = True
