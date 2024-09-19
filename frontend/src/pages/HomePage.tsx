import React from 'react';
import Dashboard from '../components/Dashboard/Dashboard';
import Search from '../components/Search/Search';

const HomePage: React.FC = () => {
  return (
    <div className="home-page">
      {/* Hero section */}
      <section className="hero">
        <h1>Welcome to Boston Startup Tracker</h1>
        <p>Discover and explore the vibrant startup ecosystem in Boston</p>
        {/* TODO: Add compelling visuals for the hero section */}
        {/* TODO: Consider adding a call-to-action button */}
      </section>

      {/* Search component */}
      <section className="search-section">
        <h2>Find Startups</h2>
        <Search />
      </section>

      {/* Dashboard component */}
      <section className="dashboard-section">
        <h2>Boston Startup Ecosystem Overview</h2>
        <Dashboard />
      </section>

      {/* TODO: Style the home page according to the application's design specifications */}
    </div>
  );
};

export default HomePage;

// Human tasks:
// - Design and implement the hero section with compelling visuals and content.
// - Consider adding a call to action in the hero section, such as encouraging users to create an account or explore featured startups.
// - Style the home page according to the application's design specifications.