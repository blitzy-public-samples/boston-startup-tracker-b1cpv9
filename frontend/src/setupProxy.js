const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  // Create a proxy middleware for requests to the '/api' path
  const apiProxy = createProxyMiddleware('/api', {
    // Configure the target URL for the backend API
    target: 'http://localhost:8000',
    // Change the origin of the host header to the target URL
    changeOrigin: true,
    // Rewrite the path by removing the '/api' prefix
    pathRewrite: {
      '^/api': '',
    },
  });

  // Apply the proxy middleware to the development server
  app.use(apiProxy);
};

// Human tasks:
// - Adjust the target URL ('http://localhost:8000') to match the actual URL of the backend API.