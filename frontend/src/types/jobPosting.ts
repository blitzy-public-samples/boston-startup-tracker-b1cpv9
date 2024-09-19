// Define the JobPosting type representing a job posting by a startup company
export type JobPosting = {
  // Unique identifier for the job posting
  id: number;

  // ID of the startup company that posted the job
  startup_id: number;

  // Title of the job posting
  title: string;

  // Department or team the job is for
  department: string;

  // Detailed description of the job
  description: string;

  // Date when the job was posted
  posted_date: Date;
};