#!/bin/bash

# Boston Startup Tracker - Database Setup Script

# Exit immediately if a command exits with a non-zero status
set -e

# Function to print error messages
error_exit() {
    echo "$1" 1>&2
    exit 1
}

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
    error_exit "PostgreSQL is not installed. Please install PostgreSQL and try again."
fi

# Check if Elasticsearch is installed
if ! command -v elasticsearch &> /dev/null; then
    error_exit "Elasticsearch is not installed. Please install Elasticsearch and try again."
fi

# Check if Alembic is installed
if ! command -v alembic &> /dev/null; then
    error_exit "Alembic is not installed. Please install Alembic and try again."
fi

echo "Starting database setup for Boston Startup Tracker..."

# TODO: Add logic to create the PostgreSQL database
# Example:
# createdb boston_startup_tracker || error_exit "Failed to create PostgreSQL database"

# TODO: Add logic to create the Elasticsearch database
# Example:
# curl -X PUT "localhost:9200/boston_startup_tracker" || error_exit "Failed to create Elasticsearch index"

# TODO: Add logic to apply database migrations using Alembic
# Example:
# alembic upgrade head || error_exit "Failed to apply database migrations"

# TODO: Add logic to create the necessary user accounts for the databases
# Example:
# psql -c "CREATE USER boston_startup_user WITH PASSWORD 'secure_password';" || error_exit "Failed to create PostgreSQL user"

# TODO: Add logic to configure appropriate permissions for the database users
# Example:
# psql -c "GRANT ALL PRIVILEGES ON DATABASE boston_startup_tracker TO boston_startup_user;" || error_exit "Failed to grant permissions to PostgreSQL user"

echo "Database setup completed successfully."

# List of human tasks to be completed:
# - Add logic to create the PostgreSQL database.
# - Add logic to create the Elasticsearch database.
# - Add logic to apply database migrations using Alembic.
# - Add logic to create the necessary user accounts for the databases.
# - Add logic to configure appropriate permissions for the database users.