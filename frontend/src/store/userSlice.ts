import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { AxiosError } from 'axios';
import { User } from '../types/user';
import { AppDispatch } from './store';
import { api } from '../services/api';

// Define the initial state for the user slice
const initialState = {
  user: {
    status: 'idle' as 'idle' | 'loading' | 'succeeded' | 'failed',
    data: null as User | null,
    error: null as AxiosError | null,
  },
};

// Create the user slice
const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    getUserStart: (state) => {
      state.user.status = 'loading';
    },
    getUserSuccess: (state, action: PayloadAction<User>) => {
      state.user.status = 'succeeded';
      state.user.data = action.payload;
      state.user.error = null;
    },
    getUserFailure: (state, action: PayloadAction<AxiosError>) => {
      state.user.status = 'failed';
      state.user.data = null;
      state.user.error = action.payload;
    },
  },
});

// Export the action creators
export const { getUserStart, getUserSuccess, getUserFailure } = userSlice.actions;

// Define the async thunk to fetch user data
export const getUser = (userId: number) => async (dispatch: AppDispatch) => {
  try {
    // Dispatch the getUserStart action to indicate that fetching is starting
    dispatch(getUserStart());

    // Send a GET request to the /users/${userId} endpoint using the api service
    const response = await api.get<User>(`/users/${userId}`);

    // If the request is successful, dispatch the getUserSuccess action with the fetched data
    dispatch(getUserSuccess(response.data));
  } catch (error) {
    // If the request fails, dispatch the getUserFailure action with the error object
    dispatch(getUserFailure(error as AxiosError));
  }
};

// Export the reducer
export default userSlice.reducer;