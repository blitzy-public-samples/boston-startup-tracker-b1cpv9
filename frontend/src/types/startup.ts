// Define the Startup type representing a startup company
export type Startup = {
  // Unique identifier for the startup
  id: number;

  // Name of the startup
  name: string;

  // Website URL of the startup
  website: string;

  // Industry in which the startup operates
  industry: string;

  // Sub-sector or specific area within the industry
  sub_sector: string;

  // Total number of employees in the startup
  employee_count: number;

  // Number of employees located in the local area (e.g., Boston)
  local_employee_count: number;

  // Growth rate of the startup's headcount
  headcount_growth: number;

  // Total funding received by the startup (in USD)
  total_funding: number;

  // Date of the most recent funding round
  last_funding_date: Date;

  // Current funding stage of the startup (e.g., Seed, Series A, Series B)
  funding_stage: string;

  // Indicates whether the startup is currently hiring
  is_hiring: boolean;

  // Date when the startup's information was last updated
  last_updated: Date;
};