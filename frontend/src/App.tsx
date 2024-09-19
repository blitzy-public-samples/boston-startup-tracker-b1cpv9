import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import SearchPage from './pages/SearchPage';
import StartupsPage from './pages/StartupsPage';
import InvestorsPage from './pages/InvestorsPage';
import JobsPage from './pages/JobsPage';
import NewsPage from './pages/NewsPage';
import UserAccountPage from './pages/UserAccountPage';
import Layout from './components/Layout/Layout';

const App: React.FC = () => {
  return (
    // Render the application within a BrowserRouter to enable routing
    <BrowserRouter>
      {/* Render the Layout component to provide a consistent structure for all pages */}
      <Layout>
        {/* Define the application's routes using Routes and Route components */}
        <Routes>
          {/* Render the corresponding page component for each route */}
          <Route path="/" element={<HomePage />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/startups" element={<StartupsPage />} />
          <Route path="/investors" element={<InvestorsPage />} />
          <Route path="/jobs" element={<JobsPage />} />
          <Route path="/news" element={<NewsPage />} />
          <Route path="/account" element={<UserAccountPage />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
};

export default App;