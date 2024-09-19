import React from 'react';
import { Link } from 'react-router-dom';

const NavBar: React.FC = () => {
  return (
    <nav className="navbar">
      {/* Render navigation links */}
      <ul className="nav-list">
        <li className="nav-item">
          <Link to="/" className="nav-link">Home</Link>
        </li>
        <li className="nav-item">
          <Link to="/search" className="nav-link">Search</Link>
        </li>
        <li className="nav-item">
          <Link to="/startups" className="nav-link">Startups</Link>
        </li>
        <li className="nav-item">
          <Link to="/investors" className="nav-link">Investors</Link>
        </li>
        <li className="nav-item">
          <Link to="/jobs" className="nav-link">Jobs</Link>
        </li>
        <li className="nav-item">
          <Link to="/news" className="nav-link">News</Link>
        </li>
        <li className="nav-item">
          <Link to="/account" className="nav-link">Account</Link>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;

// Human tasks:
// TODO: Style the navigation bar and links according to the application's design specifications.
// TODO: Consider implementing active link highlighting to indicate the current page.