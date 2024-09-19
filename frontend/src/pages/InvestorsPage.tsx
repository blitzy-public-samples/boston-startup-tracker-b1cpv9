import React from 'react';
import { InvestorList } from '../components/InvestorList/InvestorList';

const InvestorsPage: React.FC = () => {
  return (
    <div className="investors-page">
      <h1>Boston Startup Investors</h1>
      
      {/* Render the InvestorList component to display the list of investors */}
      <InvestorList />

      {/* 
        Human tasks:
        - Consider adding a search bar or filters to allow users to refine the list of investors.
        - Style the investors page according to the application's design specifications.
      */}
    </div>
  );
};

export default InvestorsPage;