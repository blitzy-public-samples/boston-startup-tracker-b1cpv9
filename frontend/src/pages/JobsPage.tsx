import React from 'react';
import { JobList } from '../components/JobList/JobList';

const JobsPage: React.FC = () => {
  return (
    <div className="jobs-page">
      <h1>Job Postings</h1>
      
      {/* Render the JobList component to display the list of job postings */}
      <JobList />
      
      {/* 
      Human tasks:
      - Consider adding a search bar or filters to allow users to refine the list of job postings.
      - Style the job postings page according to the application's design specifications.
      */}
    </div>
  );
};

export default JobsPage;