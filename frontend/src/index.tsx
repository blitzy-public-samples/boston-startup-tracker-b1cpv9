import React from 'react';
import { createRoot } from 'react-dom/client';
import { App } from './App';
import { reportWebVitals } from './reportWebVitals';
import { store } from './store/store';
import { Provider } from 'react-redux';

// Get the root element from the DOM
const rootElement = document.getElementById('root');

// Ensure the root element exists
if (!rootElement) {
  throw new Error('Root element not found');
}

// Create a root using createRoot from react-dom
const root = createRoot(rootElement);

// Render the App component wrapped in Redux Provider
root.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();