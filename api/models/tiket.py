from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class TicketReply(Base):
    __tablename__ = 'ticket_replies'

    ID = Column(Integer, primary_key=True, index=True)
    ticketid = Column(Integer, ForeignKey('tickets.ID'))
    userid = Column(Integer, nullable=False)
    body = Column(String, nullable=False)
    replyid = Column(Boolean, nullable=False)
    files = Column(Integer, nullable=True)
    # Add other fields as needed

    ticket = relationship("Tiket", back_populates="ticketReplies")


class TicketCategory(Base):
    __tablename__ = 'ticket_categories'
    # __table_args__ = {'schema': 'mysql_tiket'}  # Set the connection schema if needed

    ID = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    cat_parent = Column(Integer, nullable=True)
    image = Column(String, nullable=True)
    no_tickets = Column(Integer, nullable=True)
    auto_assign = Column(Integer, nullable=True)

    tickets = relationship("Tiket", back_populates="ticketCategory")


class TicketStatus(Base):
    __tablename__ = 'custom_statuses'
    # __table_args__ = {'schema': 'mysql_tiket'}  # Set the connection schema if needed

    ID = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=True)
    close = Column(Integer, nullable=True)
    text_color = Column(String, nullable=True)

    tickets = relationship("Tiket", back_populates="ticketStatus")


class Tiket(Base):
    __tablename__ = 'tickets'
    # __table_args__ = {'schema': 'mysql_tiket'}  # Set the connection schema if needed

    ID = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    categoryid = Column(Integer, ForeignKey('ticket_categories.ID'))
    status = Column(Integer, ForeignKey('custom_statuses.ID'))

    ticketReplies = relationship("TicketReply", back_populates="ticket", cascade="all, delete-orphan")
    ticketCategory = relationship("TicketCategory", uselist=False)
    ticketStatus = relationship("TicketStatus", uselist=False)
