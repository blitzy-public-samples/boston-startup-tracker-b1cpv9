// Import necessary dependencies and slices
import { configureStore } from '@reduxjs/toolkit';
import { analyticsSlice } from './analyticsSlice';
import { authSlice } from './authSlice';
import { investorSlice } from './investorSlice';
import { jobSlice } from './jobSlice';
import { newsSlice } from './newsSlice';
import { searchSlice } from './searchSlice';
import { startupSlice } from './startupSlice';

// Configure the Redux store with all the slices
export const store = configureStore({
  reducer: {
    analytics: analyticsSlice.reducer,
    auth: authSlice.reducer,
    investors: investorSlice.reducer,
    jobs: jobSlice.reducer,
    news: newsSlice.reducer,
    search: searchSlice.reducer,
    startups: startupSlice.reducer,
  },
});

// Define RootState type for use in selectors and components
export type RootState = ReturnType<typeof store.getState>;

// Define AppDispatch type for use in async actions
export type AppDispatch = typeof store.dispatch;