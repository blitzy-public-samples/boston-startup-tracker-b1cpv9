// Define the Executive type
export type Executive = {
  // Unique identifier for the executive
  id: number;

  // ID of the startup the executive belongs to
  startup_id: number;

  // Full name of the executive
  name: string;

  // Job title of the executive
  title: string;

  // LinkedIn profile URL of the executive
  linkedin_url: string;
};