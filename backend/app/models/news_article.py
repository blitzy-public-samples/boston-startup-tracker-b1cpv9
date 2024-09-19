from sqlalchemy import Column, ForeignKey, Integer, String, Date
from app.db.base_class import Base

class NewsArticle(Base):
    """Model representing a news article related to a startup company."""

    # Define the table name
    __tablename__ = "news_articles"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to link the news article to a startup
    startup_id = Column(Integer, ForeignKey("startups.id"), nullable=False)

    # Title of the news article
    title = Column(String, nullable=False)

    # URL of the news article
    url = Column(String, nullable=False)

    # Published date of the news article
    published_date = Column(Date, nullable=False)

    def __init__(self, startup_id: int, title: str, url: str, published_date: Date):
        """
        Initialize a new NewsArticle instance.

        Args:
            startup_id (int): The ID of the startup associated with this news article.
            title (str): The title of the news article.
            url (str): The URL of the news article.
            published_date (Date): The date when the article was published.
        """
        self.startup_id = startup_id
        self.title = title
        self.url = url
        self.published_date = published_date

    def __repr__(self):
        """
        Return a string representation of the NewsArticle instance.
        """
        return f"<NewsArticle(id={self.id}, startup_id={self.startup_id}, title='{self.title}')>"