import React from 'react';
import { NewsList } from '../components/NewsList/NewsList';

const NewsPage: React.FC = () => {
  return (
    <div className="news-page">
      <h1>Boston Startup News</h1>
      {/* Render the NewsList component to display the list of news articles */}
      <NewsList />
    </div>
  );
};

export default NewsPage;

// Human tasks:
// TODO: Consider adding a search bar or filters to allow users to refine the list of news articles.
// TODO: Style the news articles page according to the application's design specifications.