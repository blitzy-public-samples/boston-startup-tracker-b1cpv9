import React from 'react';
import { useLocation } from 'react-router-dom';
import { StartupList } from '../../components/StartupList/StartupList';

const SearchPage: React.FC = () => {
  // Retrieve the search results from the location state using useLocation
  const location = useLocation();
  const searchResults = location.state?.searchResults || [];

  return (
    <div className="search-page">
      <h1>Search Results</h1>
      {searchResults.length > 0 ? (
        // Render the StartupList component, passing the search results as a prop
        <StartupList startups={searchResults} />
      ) : (
        // Display a message if no search results are found
        <p>No startups found matching your search criteria.</p>
      )}
    </div>
  );
};

export default SearchPage;

// Human tasks:
// TODO: Display a message if no search results are found.
// TODO: Style the search results page according to the application's design specifications.