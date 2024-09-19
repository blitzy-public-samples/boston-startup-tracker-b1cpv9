import React from 'react';
import { useSelector } from 'react-redux';
import { NewsArticle } from '../../types/newsArticle';
import { RootState } from '../../store/newsSlice';

const NewsList: React.FC = () => {
  // Fetch the list of news articles from the Redux store using useSelector
  const { articles, loading, error } = useSelector((state: RootState) => state.news);

  if (loading) {
    // Display a loading indicator while data is being fetched
    return <div>Loading news articles...</div>;
  }

  if (error) {
    // Display an error message if there is an error fetching data
    return <div>Error: {error}</div>;
  }

  return (
    <div className="news-list">
      <h2>Latest Startup News</h2>
      {/* Map over the list of news articles and render each article's information */}
      {articles.map((article: NewsArticle) => (
        <div key={article.id} className="news-item">
          <h3>{article.title}</h3>
          <p>Published on: {new Date(article.publishedAt).toLocaleDateString()}</p>
          <p>Source: {article.source}</p>
        </div>
      ))}
    </div>
  );
};

export default NewsList;

// Human tasks:
// TODO: Implement styling and layout for the news article list.
// TODO: Consider adding pagination or infinite scrolling if the list of news articles is large.
// TODO: Make the news article titles clickable links to the original articles.