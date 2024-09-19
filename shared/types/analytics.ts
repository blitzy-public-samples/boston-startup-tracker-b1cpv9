// Define types for analytics data used in the Boston Startup Tracker application

// Represents a data point for funding trends over time
export class FundingTrend {
    year: number;
    totalFunding: number;
}

// Represents a data point for the breakdown of startups by industry
export class IndustryBreakdown {
    industry: string;
    count: number;
}

// Represents headcount growth statistics
export class HeadcountGrowth {
    average: number;
    median: number;
    percentile75: number;
    percentile90: number;
}