import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { AxiosError } from 'axios';
import { Startup } from '../types/startup';
import { AppDispatch } from './store';
import { api } from '../services/api';

// Define the initial state for the startup slice
const initialState = {
  startups: {
    status: 'idle' as 'idle' | 'loading' | 'succeeded' | 'failed',
    data: [] as Startup[],
    error: null as AxiosError | null,
  },
};

// Create the startup slice
const startupSlice = createSlice({
  name: 'startups',
  initialState,
  reducers: {
    // Action to set the loading state when fetching startups
    getStartupsStart(state) {
      state.startups.status = 'loading';
    },
    // Action to update the state with fetched startups data
    getStartupsSuccess(state, action: PayloadAction<Startup[]>) {
      state.startups.status = 'succeeded';
      state.startups.data = action.payload;
      state.startups.error = null;
    },
    // Action to handle errors when fetching startups fails
    getStartupsFailure(state, action: PayloadAction<AxiosError>) {
      state.startups.status = 'failed';
      state.startups.error = action.payload;
    },
  },
});

// Export the action creators
export const { getStartupsStart, getStartupsSuccess, getStartupsFailure } = startupSlice.actions;

// Async thunk to fetch startup data from the API
export const getStartups = () => async (dispatch: AppDispatch) => {
  try {
    // Dispatch the start action to indicate fetching is starting
    dispatch(getStartupsStart());

    // Send a GET request to the /startups endpoint
    const response = await api.get<Startup[]>('/startups');

    // Dispatch the success action with the fetched data
    dispatch(getStartupsSuccess(response.data));
  } catch (error) {
    // Dispatch the failure action with the error object
    dispatch(getStartupsFailure(error as AxiosError));
  }
};

// Export the reducer
export default startupSlice.reducer;