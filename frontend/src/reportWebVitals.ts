import { ReportHandler } from 'web-vitals';
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

const reportWebVitals = (onPerfEntry?: ReportHandler): void => {
  // Check if the onPerfEntry callback is provided
  if (onPerfEntry && onPerfEntry instanceof Function) {
    // Measure various web vitals metrics using functions from the web-vitals library
    getCLS(onPerfEntry); // Cumulative Layout Shift
    getFID(onPerfEntry); // First Input Delay
    getFCP(onPerfEntry); // First Contentful Paint
    getLCP(onPerfEntry); // Largest Contentful Paint
    getTTFB(onPerfEntry); // Time to First Byte
  }
};

export default reportWebVitals;