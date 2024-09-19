from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.news_article import NewsArticle, NewsArticleCreate, NewsArticleUpdate
from app.services.crud_news_article import CRUDNewsArticle
from app.utils.dependencies import get_news_article_service

router = APIRouter()

@router.get("/", response_model=List[NewsArticle])
def get_news_articles(
    news_article_service: CRUDNewsArticle = Depends(get_news_article_service)
) -> List[NewsArticle]:
    """
    Endpoint to retrieve all news articles.
    """
    # Call the `get_all` function from the `news_article_service` to retrieve all news articles
    news_articles = news_article_service.get_all()
    # Return the list of news articles
    return news_articles

@router.get("/{news_article_id}", response_model=NewsArticle)
def get_news_article(
    news_article_id: int,
    news_article_service: CRUDNewsArticle = Depends(get_news_article_service)
) -> NewsArticle:
    """
    Endpoint to retrieve a specific news article by ID.
    """
    # Call the `get` function from the `news_article_service` to retrieve the news article with the specified ID
    news_article = news_article_service.get(news_article_id)
    # If the news article is not found, raise an HTTPException with status code 404
    if news_article is None:
        raise HTTPException(status_code=404, detail="News article not found")
    # Return the news article
    return news_article

@router.post("/", response_model=NewsArticle, status_code=status.HTTP_201_CREATED)
def create_news_article(
    news_article_in: NewsArticleCreate,
    news_article_service: CRUDNewsArticle = Depends(get_news_article_service)
) -> NewsArticle:
    """
    Endpoint to create a new news article.
    """
    # Call the `create` function from the `news_article_service` to create a new news article with the provided data
    new_news_article = news_article_service.create(news_article_in)
    # Return the newly created news article
    return new_news_article

@router.put("/{news_article_id}", response_model=NewsArticle)
def update_news_article(
    news_article_id: int,
    news_article_in: NewsArticleUpdate,
    news_article_service: CRUDNewsArticle = Depends(get_news_article_service)
) -> NewsArticle:
    """
    Endpoint to update an existing news article.
    """
    # Call the `get` function from the `news_article_service` to retrieve the news article with the specified ID
    existing_news_article = news_article_service.get(news_article_id)
    # If the news article is not found, raise an HTTPException with status code 404
    if existing_news_article is None:
        raise HTTPException(status_code=404, detail="News article not found")
    # Call the `update` function from the `news_article_service` to update the news article with the provided data
    updated_news_article = news_article_service.update(existing_news_article, news_article_in)
    # Return the updated news article
    return updated_news_article

@router.delete("/{news_article_id}", response_model=NewsArticle)
def delete_news_article(
    news_article_id: int,
    news_article_service: CRUDNewsArticle = Depends(get_news_article_service)
) -> NewsArticle:
    """
    Endpoint to delete a news article.
    """
    # Call the `get` function from the `news_article_service` to retrieve the news article with the specified ID
    existing_news_article = news_article_service.get(news_article_id)
    # If the news article is not found, raise an HTTPException with status code 404
    if existing_news_article is None:
        raise HTTPException(status_code=404, detail="News article not found")
    # Call the `remove` function from the `news_article_service` to delete the news article
    deleted_news_article = news_article_service.remove(existing_news_article)
    # Return the deleted news article
    return deleted_news_article