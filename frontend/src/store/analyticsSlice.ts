import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { AxiosError } from 'axios';
import { FundingTrend } from '../types/analytics';
import { AppDispatch } from './store';
import { api } from '../services/api';

// Define the initial state for the analytics slice
const initialState = {
  fundingTrends: {
    status: 'idle' as 'idle' | 'loading' | 'succeeded' | 'failed',
    data: [] as FundingTrend[],
    error: null as AxiosError | null,
  },
  industryBreakdown: {
    status: 'idle' as 'idle' | 'loading' | 'succeeded' | 'failed',
    data: {},
    error: null as AxiosError | null,
  },
  headcountGrowth: {
    status: 'idle' as 'idle' | 'loading' | 'succeeded' | 'failed',
    data: {},
    error: null as AxiosError | null,
  },
};

// Create the analytics slice
const analyticsSlice = createSlice({
  name: 'analytics',
  initialState,
  reducers: {
    // Funding Trends
    getFundingTrendsStart: (state) => {
      state.fundingTrends.status = 'loading';
    },
    getFundingTrendsSuccess: (state, action: PayloadAction<FundingTrend[]>) => {
      state.fundingTrends.status = 'succeeded';
      state.fundingTrends.data = action.payload;
      state.fundingTrends.error = null;
    },
    getFundingTrendsFailure: (state, action: PayloadAction<AxiosError>) => {
      state.fundingTrends.status = 'failed';
      state.fundingTrends.error = action.payload;
    },

    // Industry Breakdown
    getIndustryBreakdownStart: (state) => {
      state.industryBreakdown.status = 'loading';
    },
    getIndustryBreakdownSuccess: (state, action: PayloadAction<any>) => {
      state.industryBreakdown.status = 'succeeded';
      state.industryBreakdown.data = action.payload;
      state.industryBreakdown.error = null;
    },
    getIndustryBreakdownFailure: (state, action: PayloadAction<AxiosError>) => {
      state.industryBreakdown.status = 'failed';
      state.industryBreakdown.error = action.payload;
    },

    // Headcount Growth
    getHeadcountGrowthStart: (state) => {
      state.headcountGrowth.status = 'loading';
    },
    getHeadcountGrowthSuccess: (state, action: PayloadAction<any>) => {
      state.headcountGrowth.status = 'succeeded';
      state.headcountGrowth.data = action.payload;
      state.headcountGrowth.error = null;
    },
    getHeadcountGrowthFailure: (state, action: PayloadAction<AxiosError>) => {
      state.headcountGrowth.status = 'failed';
      state.headcountGrowth.error = action.payload;
    },
  },
});

// Export actions
export const {
  getFundingTrendsStart,
  getFundingTrendsSuccess,
  getFundingTrendsFailure,
  getIndustryBreakdownStart,
  getIndustryBreakdownSuccess,
  getIndustryBreakdownFailure,
  getHeadcountGrowthStart,
  getHeadcountGrowthSuccess,
  getHeadcountGrowthFailure,
} = analyticsSlice.actions;

// Async thunk to fetch funding trend data
export const getFundingTrends = () => async (dispatch: AppDispatch) => {
  try {
    // Dispatch start action
    dispatch(getFundingTrendsStart());

    // Make API call
    const response = await api.get('/analytics/funding-trends');

    // Dispatch success action with fetched data
    dispatch(getFundingTrendsSuccess(response.data));
  } catch (error) {
    // Dispatch failure action with error
    dispatch(getFundingTrendsFailure(error as AxiosError));
  }
};

// Async thunk to fetch industry breakdown data
export const getIndustryBreakdown = () => async (dispatch: AppDispatch) => {
  try {
    // Dispatch start action
    dispatch(getIndustryBreakdownStart());

    // Make API call
    const response = await api.get('/analytics/industry-breakdown');

    // Dispatch success action with fetched data
    dispatch(getIndustryBreakdownSuccess(response.data));
  } catch (error) {
    // Dispatch failure action with error
    dispatch(getIndustryBreakdownFailure(error as AxiosError));
  }
};

// Async thunk to fetch headcount growth data
export const getHeadcountGrowth = () => async (dispatch: AppDispatch) => {
  try {
    // Dispatch start action
    dispatch(getHeadcountGrowthStart());

    // Make API call
    const response = await api.get('/analytics/headcount-growth');

    // Dispatch success action with fetched data
    dispatch(getHeadcountGrowthSuccess(response.data));
  } catch (error) {
    // Dispatch failure action with error
    dispatch(getHeadcountGrowthFailure(error as AxiosError));
  }
};

// Export reducer
export default analyticsSlice.reducer;