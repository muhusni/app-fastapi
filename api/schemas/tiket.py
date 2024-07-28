from pydantic import BaseModel
from typing import List, Optional


class TicketReplyResponse(BaseModel):
    ID: int
    ticketid: int
    body: str
    userid: int
    replyid: int
    files: int

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
    ticketReplies: List[TicketReplyResponse] = []
    ticketCategory: Optional[TicketCategoryResponse]
    ticketStatus: Optional[TicketStatusResponse]
    ticket_IKC: str | None

    class Config:
        from_attributes = True

class TiketDuktekResponse(BaseModel):
    ID: int
    title: str
    body: str
    categoryid: Optional[int]
    status: Optional[int]

    class Config:
        from_attributes = True

class TiketIkcResponse(BaseModel):
    ID: int
    ticketid: int
    body: str
    userid: int
    replyid: int
    files: int
    ticketIkc: int
    ticket: TiketDuktekResponse

    class Config:
        from_attributes = True


