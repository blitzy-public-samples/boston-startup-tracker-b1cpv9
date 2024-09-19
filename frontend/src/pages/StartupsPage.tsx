import React from 'react';
import { StartupList } from '../components/StartupList/StartupList';

const StartupsPage: React.FC = () => {
  return (
    <div className="startups-page">
      <h1>Boston Startups</h1>
      
      {/* Render the StartupList component to display the list of startups */}
      <StartupList />

      {/* 
      Human tasks:
      - Consider adding a search bar or filters to allow users to refine the list of startups.
      - Style the startups page according to the application's design specifications.
      */}
    </div>
  );
};

export default StartupsPage;