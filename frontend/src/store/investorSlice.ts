import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { AxiosError } from 'axios';
import { Investor } from '../types/investor';
import { AppDispatch } from './store';
import { api } from '../services/api';

// Define the initial state for the investor slice
const initialState = {
  investors: {
    status: 'idle' as 'idle' | 'loading' | 'succeeded' | 'failed',
    data: [] as Investor[],
    error: null as AxiosError | null,
  },
};

// Create the investor slice
const investorSlice = createSlice({
  name: 'investors',
  initialState,
  reducers: {
    // Action to set the loading state when fetching investors
    getInvestorsStart(state) {
      state.investors.status = 'loading';
    },
    // Action to set the success state and update the investors data
    getInvestorsSuccess(state, action: PayloadAction<Investor[]>) {
      state.investors.status = 'succeeded';
      state.investors.data = action.payload;
      state.investors.error = null;
    },
    // Action to set the failure state and store the error
    getInvestorsFailure(state, action: PayloadAction<AxiosError>) {
      state.investors.status = 'failed';
      state.investors.error = action.payload;
    },
  },
});

// Export the action creators
export const { getInvestorsStart, getInvestorsSuccess, getInvestorsFailure } = investorSlice.actions;

// Async thunk to fetch investor data from the API
export const getInvestors = () => async (dispatch: AppDispatch) => {
  try {
    // Dispatch the start action to indicate that fetching is starting
    dispatch(getInvestorsStart());

    // Send a GET request to the `/investors` endpoint using the `api` service
    const response = await api.get<Investor[]>('/investors');

    // If the request is successful, dispatch the success action with the fetched data
    dispatch(getInvestorsSuccess(response.data));
  } catch (error) {
    // If the request fails, dispatch the failure action with the error object
    dispatch(getInvestorsFailure(error as AxiosError));
  }
};

// Export the reducer
export default investorSlice.reducer;