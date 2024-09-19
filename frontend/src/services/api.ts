import { AxiosInstance, create } from 'axios';
import { Startup } from '../types/startup';

// Create an Axios instance with the base URL for the API
const api: AxiosInstance = create({ baseURL: 'http://localhost:8000/api/v1' });

/**
 * Searches for startups based on a query string.
 * @param query The search query string
 * @returns A promise that resolves to an array of startups matching the query
 */
export async function searchStartups(query: string): Promise<Startup[]> {
  try {
    // Send a GET request to the `/search` endpoint with the query string as a parameter
    const response = await api.get('/search', {
      params: { query },
    });

    // Return the data property of the response, which contains the array of startups
    return response.data;
  } catch (error) {
    // TODO: Handle potential errors from the API request (e.g., network errors, API errors)
    console.error('Error searching startups:', error);
    throw error;
  }
}

// Human tasks:
// - Handle potential errors from the API request (e.g., network errors, API errors)