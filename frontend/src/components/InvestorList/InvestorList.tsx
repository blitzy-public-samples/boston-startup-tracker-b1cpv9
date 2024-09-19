import React from 'react';
import { useSelector } from 'react-redux';
import { Investor } from '../../types/investor';
import { RootState } from '../../store/investorSlice';

const InvestorList: React.FC = () => {
  // Fetch the list of investors from the Redux store
  const { investors, loading, error } = useSelector((state: RootState) => state.investors);

  // Display a loading indicator while data is being fetched
  if (loading) {
    return <div>Loading investors...</div>;
  }

  // Display an error message if there is an error fetching data
  if (error) {
    return <div>Error: {error}</div>;
  }

  // Map over the list of investors and render each investor's information
  return (
    <div className="investor-list">
      <h2>Investors</h2>
      {investors.map((investor: Investor) => (
        <div key={investor.id} className="investor-item">
          <h3>{investor.name}</h3>
          <p>Company: {investor.company}</p>
          <p>Investment Focus: {investor.investmentFocus}</p>
          {/* Add more investor details as needed */}
        </div>
      ))}
    </div>
  );
};

export default InvestorList;

// Human tasks:
// TODO: Implement styling and layout for the investor list.
// TODO: Consider adding pagination or infinite scrolling if the list of investors is large.
// TODO: Add links to individual investor profile pages.