import React from 'react';
import { useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { Startup } from '../../types/startup';
import { RootState } from '../../store/startupSlice';

const StartupProfile: React.FC = () => {
  // Retrieve the startup ID from the URL parameters
  const { id } = useParams<{ id: string }>();

  // Fetch the startup data from the Redux store
  const startup = useSelector((state: RootState) =>
    state.startups.startups.find((s: Startup) => s.id === id)
  );

  // Display a loading indicator while data is being fetched
  if (!startup) {
    return <div>Loading...</div>;
  }

  // Render the startup profile
  return (
    <div className="startup-profile">
      <h1>{startup.name}</h1>
      <p>Website: <a href={startup.website} target="_blank" rel="noopener noreferrer">{startup.website}</a></p>
      <p>Industry: {startup.industry}</p>
      <h2>Description</h2>
      <p>{startup.description}</p>

      <h2>Team Members</h2>
      <ul>
        {startup.teamMembers.map((member, index) => (
          <li key={index}>{member.name} - {member.role}</li>
        ))}
      </ul>

      <h2>Funding History</h2>
      <ul>
        {startup.fundingHistory.map((funding, index) => (
          <li key={index}>
            {funding.date}: ${funding.amount} ({funding.round})
          </li>
        ))}
      </ul>

      <h2>News Articles</h2>
      <ul>
        {startup.newsArticles.map((article, index) => (
          <li key={index}>
            <a href={article.url} target="_blank" rel="noopener noreferrer">{article.title}</a>
            <p>{article.date}</p>
          </li>
        ))}
      </ul>

      <h2>Job Postings</h2>
      <ul>
        {startup.jobPostings.map((job, index) => (
          <li key={index}>
            <h3>{job.title}</h3>
            <p>{job.description}</p>
            <p>Location: {job.location}</p>
            <p>Salary Range: ${job.salaryRange.min} - ${job.salaryRange.max}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default StartupProfile;

// Human tasks:
// - Implement styling and layout for the startup profile.
// - Consider using charts or graphs to visualize data such as funding history or headcount growth.
// - Add interactive features such as the ability to follow or unfollow a startup, save a job posting, or share the profile on social media.