// Define the Founder type representing a founder of a startup company
export type Founder = {
    // Unique identifier for the founder
    id: number;

    // ID of the startup the founder is associated with
    startup_id: number;

    // Full name of the founder
    name: string;

    // Title or position of the founder in the startup
    title: string;

    // LinkedIn profile URL of the founder
    linkedin_url: string;
};