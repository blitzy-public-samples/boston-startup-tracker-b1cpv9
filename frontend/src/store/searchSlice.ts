import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { AxiosError } from 'axios';
import { Startup } from '../types/startup';

// Define the initial state for the search slice
const initialState = {
  searchResults: {
    status: 'idle' as 'idle' | 'loading' | 'succeeded' | 'failed',
    data: [] as Startup[],
    error: null as AxiosError | null,
  },
};

// Create the search slice
const searchSlice = createSlice({
  name: 'search',
  initialState,
  reducers: {
    // Action to set the search results
    setSearchResults: (state, action: PayloadAction<Startup[]>) => {
      // Set the `data` property of the `searchResults` state to the payload of the action
      state.searchResults.data = action.payload;
      // Set the `status` property of the `searchResults` state to 'succeeded'
      state.searchResults.status = 'succeeded';
    },
    // Add more actions as needed, such as setLoading, setError, etc.
  },
});

// Export the actions
export const { setSearchResults } = searchSlice.actions;

// Export the reducer
export default searchSlice.reducer;