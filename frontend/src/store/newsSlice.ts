import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { AxiosError } from 'axios';
import { NewsArticle } from '../types/newsArticle';
import { AppDispatch } from './store';
import { api } from '../services/api';

// Define the initial state for the news slice
const initialState = {
  news: {
    status: 'idle' as 'idle' | 'loading' | 'succeeded' | 'failed',
    data: [] as NewsArticle[],
    error: null as AxiosError | null,
  },
};

// Create the news slice
const newsSlice = createSlice({
  name: 'news',
  initialState,
  reducers: {
    getNewsArticlesStart: (state) => {
      state.news.status = 'loading';
    },
    getNewsArticlesSuccess: (state, action: PayloadAction<NewsArticle[]>) => {
      state.news.status = 'succeeded';
      state.news.data = action.payload;
      state.news.error = null;
    },
    getNewsArticlesFailure: (state, action: PayloadAction<AxiosError>) => {
      state.news.status = 'failed';
      state.news.error = action.payload;
    },
  },
});

// Export the action creators
export const {
  getNewsArticlesStart,
  getNewsArticlesSuccess,
  getNewsArticlesFailure,
} = newsSlice.actions;

// Async thunk to fetch news article data from the API
export const getNewsArticles = () => async (dispatch: AppDispatch) => {
  try {
    // Dispatch the start action to indicate that fetching is starting
    dispatch(getNewsArticlesStart());

    // Send a GET request to the /news endpoint using the api service
    const response = await api.get<NewsArticle[]>('/news');

    // If the request is successful, dispatch the success action with the fetched data
    dispatch(getNewsArticlesSuccess(response.data));
  } catch (error) {
    // If the request fails, dispatch the failure action with the error object
    dispatch(getNewsArticlesFailure(error as AxiosError));
  }
};

// Export the reducer
export default newsSlice.reducer;