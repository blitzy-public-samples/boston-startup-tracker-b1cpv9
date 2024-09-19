import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { User } from '../../types/user';
import { RootState } from '../../store/userSlice';
import { logout } from '../../store/authSlice';

const UserAccount: React.FC = () => {
  // Fetch user data from the Redux store
  const user = useSelector((state: RootState) => state.user.data);
  const loading = useSelector((state: RootState) => state.user.loading);
  const error = useSelector((state: RootState) => state.user.error);

  // Get the dispatch function from Redux
  const dispatch = useDispatch();

  // Define a function to handle user logout
  const handleLogout = () => {
    dispatch(logout());
  };

  // Display a loading indicator while user data is being fetched
  if (loading) {
    return <div>Loading user data...</div>;
  }

  // Display an error message if there is an error fetching user data
  if (error) {
    return <div>Error: {error}</div>;
  }

  // Render user information and logout button
  return (
    <div className="user-account">
      <h2>User Account</h2>
      {user ? (
        <>
          <p>Email: {user.email}</p>
          <p>Role: {user.role}</p>
          <button onClick={handleLogout}>Logout</button>
        </>
      ) : (
        <p>No user data available</p>
      )}
    </div>
  );
};

export default UserAccount;

// Human tasks:
// TODO: Implement functionality to update user profile information (e.g., name, password).
// TODO: Implement functionality to manage user settings (e.g., notifications, privacy).
// TODO: Style the user account component according to the application's design specifications.