import React from 'react';
import { useSelector } from 'react-redux';
import { Startup } from '../../types/startup';
import { RootState } from '../../store/startupSlice';

const StartupList: React.FC = () => {
  // Fetch the list of startups from the Redux store using useSelector
  const { startups, loading, error } = useSelector((state: RootState) => state.startups);

  // Display a loading indicator while data is being fetched
  if (loading) {
    return <div>Loading...</div>;
  }

  // Display an error message if there is an error fetching data
  if (error) {
    return <div>Error: {error}</div>;
  }

  // Map over the list of startups and render each startup's information
  return (
    <div className="startup-list">
      {startups.map((startup: Startup) => (
        <div key={startup.id} className="startup-item">
          <h2>{startup.name}</h2>
          <p>{startup.description}</p>
          <p>Founded: {startup.foundedYear}</p>
          <p>Funding: ${startup.totalFunding.toLocaleString()}</p>
          {/* Add more startup details as needed */}
        </div>
      ))}
    </div>
  );
};

export default StartupList;

// Human tasks:
// TODO: Implement styling and layout for the startup list.
// TODO: Consider adding pagination or infinite scrolling if the list of startups is large.
// TODO: Add links to individual startup profile pages.