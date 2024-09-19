// Import necessary testing libraries
import '@testing-library/jest-dom';
import '@testing-library/jest-dom/extend-expect';

// Configure the testing environment
beforeAll(() => {
  // Add any global setup that needs to be done before all tests
});

afterAll(() => {
  // Add any global cleanup that needs to be done after all tests
});

// Mock any browser APIs that might not be available in the testing environment
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: jest.fn().mockImplementation(query => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    dispatchEvent: jest.fn(),
  })),
});

// Add any custom matchers or extensions to Jest's expect function here

// Human tasks:
// TODO: Mock any external dependencies, such as API calls or browser APIs, that are used in the components being tested.