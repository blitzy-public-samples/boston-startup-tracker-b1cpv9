import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { AxiosError } from 'axios';
import { JobPosting } from '../types/jobPosting';
import { AppDispatch } from './store';
import { api } from '../services/api';

// Define the initial state for the job slice
const initialState = {
  jobs: {
    status: 'idle' as 'idle' | 'loading' | 'succeeded' | 'failed',
    data: [] as JobPosting[],
    error: null as AxiosError | null,
  },
};

// Create the job slice using createSlice from Redux Toolkit
const jobSlice = createSlice({
  name: 'jobs',
  initialState,
  reducers: {
    getJobPostingsStart: (state) => {
      state.jobs.status = 'loading';
    },
    getJobPostingsSuccess: (state, action: PayloadAction<JobPosting[]>) => {
      state.jobs.status = 'succeeded';
      state.jobs.data = action.payload;
      state.jobs.error = null;
    },
    getJobPostingsFailure: (state, action: PayloadAction<AxiosError>) => {
      state.jobs.status = 'failed';
      state.jobs.error = action.payload;
    },
  },
});

// Export the action creators
export const { getJobPostingsStart, getJobPostingsSuccess, getJobPostingsFailure } = jobSlice.actions;

// Define the async thunk to fetch job posting data
export const getJobPostings = () => async (dispatch: AppDispatch) => {
  try {
    // Dispatch the start action to indicate that fetching is starting
    dispatch(getJobPostingsStart());

    // Send a GET request to the /jobs endpoint using the api service
    const response = await api.get<JobPosting[]>('/jobs');

    // If the request is successful, dispatch the success action with the fetched data
    dispatch(getJobPostingsSuccess(response.data));
  } catch (error) {
    // If the request fails, dispatch the failure action with the error object
    dispatch(getJobPostingsFailure(error as AxiosError));
  }
};

// Export the reducer
export default jobSlice.reducer;