import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { searchStartups } from '../../services/api';
import { Startup } from '../../types/startup';

const Search: React.FC = () => {
  // Initialize state variables for search query and results
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState<Startup[]>([]);

  // Initialize the navigate function from react-router-dom
  const navigate = useNavigate();

  // Handle the search form submission
  const handleSearch = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      // Call the searchStartups function from the API service
      const results = await searchStartups(searchQuery);

      // Update the search results state
      setSearchResults(results);

      // Redirect to the search results page with the results as state
      navigate('/search-results', { state: { results } });
    } catch (error) {
      console.error('Error searching startups:', error);
      // TODO: Implement error handling and user feedback
    }
  };

  return (
    <div className="search-container">
      <h2>Search Startups</h2>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="Enter startup name or keyword"
          required
        />
        <button type="submit">Search</button>
      </form>
    </div>
  );
};

export default Search;

// TODO: Human tasks
// - Implement input validation and error handling for the search query.
// - Add more search criteria (e.g., industry, funding stage, location) to the form.
// - Style the search component according to the application's design specifications.