# Use an appropriate base image for the frontend application
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application
RUN npm run build

# Expose the port on which the frontend application will run
EXPOSE 3000

# Start the application
CMD ["npm", "start"]

# Human tasks:
# TODO: Specify the appropriate base image (e.g., `node:18-alpine`) for the frontend application.
# TODO: Replace `<source_directory>` with the actual directory containing the frontend code.
# TODO: Replace `<build_directory>` with the desired directory for the built frontend assets.
# TODO: Replace `<port>` with the port on which the frontend application will run (e.g., `3000`).