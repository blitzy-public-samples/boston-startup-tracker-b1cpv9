/// <reference types="react-scripts" />

// This file is used to declare TypeScript definitions for environment variables

declare namespace NodeJS {
  interface ProcessEnv {
    // Add your environment variables here
    // Example:
    // REACT_APP_API_URL: string;
    // REACT_APP_API_KEY: string;
    // REACT_APP_FEATURE_FLAG_EXAMPLE: string;
  }
}

// Human tasks:
// TODO: Declare the specific environment variables used in the application and their corresponding types. For example, you might declare variables for API keys, base URLs, or feature flags.