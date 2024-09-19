// Define the User type representing a user of the application
export type User = {
  // Unique identifier for the user
  id: number;

  // Email address of the user
  email: string;

  // Role of the user in the application (e.g., 'admin', 'user')
  role: string;

  // Flag indicating whether the user account is active
  is_active: boolean;
};