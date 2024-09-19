import React from 'react';
import { useSelector } from 'react-redux';
import { JobPosting } from '../../types/jobPosting';
import { RootState } from '../../store/jobSlice';

const JobList: React.FC = () => {
  // Fetch the list of job postings from the Redux store using useSelector
  const { jobPostings, loading, error } = useSelector((state: RootState) => state.jobs);

  if (loading) {
    // Display a loading indicator while data is being fetched
    return <div>Loading job postings...</div>;
  }

  if (error) {
    // Display an error message if there is an error fetching data
    return <div>Error: {error}</div>;
  }

  return (
    <div className="job-list">
      <h2>Job Postings</h2>
      {jobPostings.map((job: JobPosting) => (
        // Map over the list of job postings and render each job posting's information
        <div key={job.id} className="job-item">
          <h3>{job.title}</h3>
          <p>Company: {job.company}</p>
          <p>Location: {job.location}</p>
          <p>Salary: {job.salary}</p>
          {/* Add more job details as needed */}
        </div>
      ))}
    </div>
  );
};

export default JobList;

// Human tasks:
// - Implement styling and layout for the job list.
// - Consider adding pagination or infinite scrolling if the list of job postings is large.
// - Add links to individual job posting pages or external application links.