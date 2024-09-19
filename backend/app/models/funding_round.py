from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from app.db.base_class import Base

class FundingRound(Base):
    """Model representing a funding round for a startup company."""

    # Define the table name
    __tablename__ = "funding_rounds"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to link the funding round to a specific startup
    startup_id = Column(Integer, ForeignKey("startups.id"), nullable=False)

    # Amount of funding received in this round
    amount = Column(Float, nullable=False)

    # Date of the funding round
    date = Column(Date, nullable=False)

    # Type of funding round (e.g., Seed, Series A, Series B, etc.)
    round_type = Column(String, nullable=False)

    def __init__(self, startup_id: int, amount: float, date: Date, round_type: str):
        """
        Initialize a new FundingRound instance.

        Args:
            startup_id (int): The ID of the startup that received the funding.
            amount (float): The amount of funding received.
            date (Date): The date of the funding round.
            round_type (str): The type of funding round.
        """
        self.startup_id = startup_id
        self.amount = amount
        self.date = date
        self.round_type = round_type

    def __repr__(self):
        """
        Return a string representation of the FundingRound instance.
        """
        return f"<FundingRound(id={self.id}, startup_id={self.startup_id}, amount={self.amount}, date={self.date}, round_type={self.round_type})>"