// Define the FundingRound type
export type FundingRound = {
  // Unique identifier for the funding round
  id: number;

  // ID of the startup that received this funding round
  startup_id: number;

  // Amount of funding received in this round
  amount: number;

  // Date when the funding round occurred
  date: Date;

  // Type of funding round (e.g., Seed, Series A, Series B, etc.)
  round_type: string;
};