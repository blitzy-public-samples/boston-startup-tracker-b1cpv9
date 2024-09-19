import React from 'react';
import { useSelector } from 'react-redux';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { FundingTrend } from '../../types/analytics';
import { RootState } from '../../store/analyticsSlice';

const AnalyticsDashboard: React.FC = () => {
  // Fetch funding trend data from the Redux store using useSelector
  const fundingTrends = useSelector((state: RootState) => state.analytics.fundingTrends);
  const loading = useSelector((state: RootState) => state.analytics.loading);
  const error = useSelector((state: RootState) => state.analytics.error);

  // Display a loading indicator while data is being fetched
  if (loading) {
    return <div>Loading analytics data...</div>;
  }

  // Display an error message if there is an error fetching data
  if (error) {
    return <div>Error: {error}</div>;
  }

  // Render a LineChart from the recharts library to visualize the funding trends
  return (
    <div className="analytics-dashboard">
      <h2>Startup Funding Trends</h2>
      <LineChart
        width={800}
        height={400}
        data={fundingTrends}
        margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
      >
        {/* Configure the LineChart with XAxis, YAxis, CartesianGrid, Tooltip, and Legend components */}
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="amount" stroke="#8884d8" activeDot={{ r: 8 }} />
      </LineChart>
    </div>
  );
};

export default AnalyticsDashboard;

// Human tasks:
// TODO: Connect the component to the Redux store to fetch and display other analytics data (e.g., industry breakdown, headcount growth).
// TODO: Implement interactive features for the charts (e.g., zooming, filtering).