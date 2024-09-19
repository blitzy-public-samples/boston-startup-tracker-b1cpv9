import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="header">
      {/* Render the application logo */}
      <div className="logo">
        <Link to="/">
          {/* TODO: Replace with actual logo component or image */}
          <h1>Boston Startup Tracker</h1>
        </Link>
      </div>

      {/* Render navigation links */}
      <nav className="navigation">
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/search">Search</Link></li>
          <li><Link to="/startups">Startups</Link></li>
          <li><Link to="/investors">Investors</Link></li>
          <li><Link to="/jobs">Jobs</Link></li>
          <li><Link to="/news">News</Link></li>
          <li><Link to="/account">Account</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;

// Human tasks:
// TODO: Design and implement the application logo.
// TODO: Style the header and navigation links according to the application's design specifications.