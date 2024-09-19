import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { AxiosError } from 'axios';
import { User } from '../types/user';
import { AppDispatch } from './store';
import { api } from '../services/api';

// Define the initial state for the authentication slice
const initialState = {
  user: null as User | null,
  token: null as string | null,
  status: 'idle' as 'idle' | 'loading' | 'succeeded' | 'failed',
  error: null as AxiosError | null,
};

// Create the authentication slice
const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    // Action to set the login process as started
    loginStart: (state) => {
      state.status = 'loading';
      state.error = null;
    },
    // Action to handle successful login
    loginSuccess: (state, action: PayloadAction<{ user: User; token: string }>) => {
      state.status = 'succeeded';
      state.user = action.payload.user;
      state.token = action.payload.token;
    },
    // Action to handle login failure
    loginFailure: (state, action: PayloadAction<AxiosError>) => {
      state.status = 'failed';
      state.error = action.payload;
    },
    // Action to log the user out
    logout: (state) => {
      state.user = null;
      state.token = null;
      state.status = 'idle';
      // Human task: Consider clearing any local storage or cookies related to authentication.
    },
  },
});

// Export the action creators
export const { loginStart, loginSuccess, loginFailure, logout } = authSlice.actions;

// Async thunk to handle user login
export const login = (credentials: { username: string; password: string }) => async (dispatch: AppDispatch) => {
  try {
    // Dispatch the loginStart action to indicate that login is starting
    dispatch(loginStart());

    // Send a POST request to the /auth/token endpoint using the api service with the user's credentials
    const response = await api.post('/auth/token', credentials);

    // If the request is successful, dispatch the loginSuccess action with the received user data and token
    dispatch(loginSuccess({ user: response.data.user, token: response.data.token }));
  } catch (error) {
    // If the request fails, dispatch the loginFailure action with the error object
    dispatch(loginFailure(error as AxiosError));
  }
};

// Export the reducer
export default authSlice.reducer;