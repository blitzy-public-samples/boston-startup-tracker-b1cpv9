import React from 'react';
import { UserAccount } from '../components/UserAccount/UserAccount';

// UserAccountPage component: Renders the user account page content
const UserAccountPage: React.FC = () => {
  return (
    <div className="user-account-page">
      {/* Render the UserAccount component */}
      <UserAccount />
    </div>
  );
};

export default UserAccountPage;