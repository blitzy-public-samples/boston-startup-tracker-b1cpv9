``` markdown
# backend/app/api/v1/endpoints/analytics.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/api/v1/endpoints/auth.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/api/v1/endpoints/funding_rounds.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/api/v1/endpoints/investors.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/api/v1/endpoints/jobs.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/api/v1/endpoints/news.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/api/v1/endpoints/search.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/api/v1/endpoints/startups.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/api/v1/endpoints/users.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/core/config.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/core/security.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement database lookup to retrieve user by ID. | Required |
```

``` markdown
# backend/app/db/base_class.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/db/session.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/models/executive.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/models/founder.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/models/funding_round.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/models/investor.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/models/job_posting.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/models/news_article.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/models/startup.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/models/user.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/schemas/executive.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/schemas/founder.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/schemas/funding_round.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/schemas/investor.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/schemas/job_posting.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/schemas/news_article.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/schemas/startup.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/schemas/user.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/services/analytics_service.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement logic to query and aggregate funding round data by year. | Required |
| 2 | Implement logic to query and count startups by industry. | Required |
| 3 | Implement logic to query headcount data and calculate growth statistics. | Required |
```

``` markdown
# backend/app/services/auth_service.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement refresh token generation logic. | Required |
```

``` markdown
# backend/app/services/auth_service.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Query the database for a user with the provided email. | Required |
| 2 | If no user is found, return None. | Required |
| 3 | Verify the provided password against the user's hashed password using `verify_password`. | Required |
| 4 | If the passwords don't match, return None. | Required |
| 5 | Return the authenticated user. | Required |
| 6 | Create the access token data payload with the user ID and expiry time. | Required |
| 7 | Generate the access token using `create_access_token`. | Required |
| 8 | Create a refresh token (implementation not provided). | Required |
| 9 | Return a Token object containing the access token and refresh token. | Required |
| 10 | Implement refresh token generation logic. | Critical |

```

``` markdown
# backend/app/services/crud_founder.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/services/crud_funding_round.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/services/crud_investor.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/services/crud_job_posting.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/services/crud_news_article.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/services/crud_startup.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/services/crud_user.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/services/search_service.py

| Task Number | Description | Severity |
| --- | --- | --- |
| 1 | Implement Elasticsearch query logic. | Required |
| 2 | Implement database lookup to retrieve startup data by ID. | Required |
```

``` markdown
# backend/app/tasks/update_data.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement logic to fetch updated startup data from external sources (e.g., web scraping, API calls). | Required |
| 2 | Implement logic to map external data to the application's data models. | Required |
```

``` markdown
# backend/app/utils/dependencies.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Pass necessary dependencies (e.g., Elasticsearch client) to the SearchService constructor. | Required |
```

``` markdown
# backend/app/utils/logging.py

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/App.tsx

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/components/AnalyticsDashboard/AnalyticsDashboard.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Connect the component to the Redux store to fetch and display other analytics data (e.g., industry breakdown, headcount growth). | Required |
| 2 | Implement interactive features for the charts (e.g., zooming, filtering). | Optional |
```

``` markdown
# frontend/src/components/Dashboard/Dashboard.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Fetch and display key startup ecosystem metrics (e.g., total number of startups, total funding raised, number of active investors). | Required |
| 2 | Implement customizable widgets for personalized data views. | Required |
| 3 | Consider using charts or graphs to visualize the data. | Optional |
```

``` markdown
# frontend/src/components/Footer/Footer.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Populate the footer with actual content, including copyright information, links, and potentially social media icons. | Required |
```

``` markdown
# frontend/src/components/Header/Header.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Design and implement the application logo. | Required |
| 2 | Style the header and navigation links according to the application's design specifications. | Required |
```

``` markdown
# frontend/src/components/InvestorList/InvestorList.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement styling and layout for the investor list. | Required |
| 2 | Consider adding pagination or infinite scrolling if the list of investors is large. | Optional |
| 3 | Add links to individual investor profile pages. | Required |
```

``` markdown
# frontend/src/components/JobList/JobList.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement styling and layout for the job list. | Required |
| 2 | Consider adding pagination or infinite scrolling if the list of job postings is large. | Optional |
| 3 | Add links to individual job posting pages or external application links. | Required |
```

``` markdown
# frontend/src/components/Layout/Layout.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement styling and layout for the layout container and its components. | Required |
| 2 | Ensure responsiveness across different screen sizes. | Required |
```

``` markdown
# frontend/src/components/NavBar/NavBar.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Style the navigation bar and links according to the application's design specifications. | Required |
| 2 | Consider implementing active link highlighting to indicate the current page. | Optional |
```

``` markdown
# frontend/src/components/NewsList/NewsList.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement styling and layout for the news article list. | Required |
| 2 | Consider adding pagination or infinite scrolling if the list of news articles is large. | Optional |
| 3 | Make the news article titles clickable links to the original articles. | Required |
```

``` markdown
# frontend/src/components/Search/Search.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement input validation and error handling for the search query. | Required |
| 2 | Add more search criteria (e.g., industry, funding stage, location) to the form. | Optional |
| 3 | Style the search component according to the application's design specifications. | Required |
```

``` markdown
# frontend/src/components/StartupList/StartupList.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement styling and layout for the startup list. | Required |
| 2 | Consider adding pagination or infinite scrolling if the list of startups is large. | Optional |
| 3 | Add links to individual startup profile pages. | Required |
```

``` markdown
# frontend/src/components/StartupProfile/StartupProfile.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement styling and layout for the startup profile. | Required |
| 2 | Consider using charts or graphs to visualize data such as funding history or headcount growth. | Optional |
| 3 | Add interactive features such as the ability to follow or unfollow a startup, save a job posting, or share the profile on social media. | Optional |
```

``` markdown
# frontend/src/components/UserAccount/UserAccount.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement functionality to update user profile information (e.g., name, password). | Required |
| 2 | Implement functionality to manage user settings (e.g., notifications, privacy). | Required |
| 3 | Style the user account component according to the application's design specifications. | Required |
```

``` markdown
# frontend/src/pages/HomePage.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Design and implement the hero section with compelling visuals and content. | Required |
| 2 | Consider adding a call to action in the hero section, such as encouraging users to create an account or explore featured startups. | Optional |
| 3 | Style the home page according to the application's design specifications. | Required |
```

``` markdown
# frontend/src/pages/InvestorsPage.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Consider adding a search bar or filters to allow users to refine the list of investors. | Optional |
| 2 | Style the investors page according to the application's design specifications. | Required |
```

``` markdown
# frontend/src/pages/JobsPage.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Consider adding a search bar or filters to allow users to refine the list of job postings. | Optional |
| 2 | Style the job postings page according to the application's design specifications. | Required |
```

``` markdown
# frontend/src/pages/NewsPage.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Consider adding a search bar or filters to allow users to refine the list of news articles. | Optional |
| 2 | Style the news articles page according to the application's design specifications. | Required |
```

``` markdown
# frontend/src/pages/SearchPage.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Display a message if no search results are found. | Required |
| 2 | Style the search results page according to the application's design specifications. | Required |
```

``` markdown
# frontend/src/pages/StartupsPage.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Consider adding a search bar or filters to allow users to refine the list of startups. | Optional |
| 2 | Style the startups page according to the application's design specifications. | Required |
```

``` markdown
# frontend/src/pages/UserAccountPage.tsx

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/services/api.ts

| Task Number | Description | Severity |
| --- | --- | --- |
| 1 | Handle potential errors from the API request (e.g., network errors, API errors). | Required |
```

``` markdown
# frontend/src/store/analyticsSlice.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/store/authSlice.ts

| Task Number | Description | Severity |
|---|---|---|
| 1 | Consider clearing any local storage or cookies related to authentication. | Optional |
```

``` markdown
# frontend/src/store/investorSlice.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/store/jobSlice.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/store/newsSlice.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/store/searchSlice.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/store/startupSlice.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/store/store.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/store/userSlice.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/types/analytics.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/types/executive.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/types/founder.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/types/fundingRound.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/types/investor.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/types/jobPosting.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/types/newsArticle.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/types/startup.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/types/user.ts

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/main.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/app/main.py

TABLE COLUMNS: Task Number, Description, Severity (Critical, Required, or Optional)

| Task Number | Description | Severity |
|---|---|---|
| 1 | Add necessary imports: `fastapi`, `app.api.v1.api`, `app.core.config`, `fastapi.middleware.cors`. | Required |
| 2 | Initialize the FastAPI app with the title "Boston Startup Tracker API" and set the openapi_url to `f\"{settings.API_PREFIX}/openapi.json\"`. | Required |

```

``` markdown
# backend/alembic.ini

| Task Number | Description | Severity |
|---|---|---|
| 1 | Populate the `sqlalchemy.url` variable with the actual database connection URL. | Critical |
```

``` markdown
# backend/requirements.txt

| Task Number | Description | Severity |
|---|---|---|
| 1 | Populate this file with the specific versions of the required Python packages. | Required |
```

``` markdown
# frontend/Dockerfile

| Task Number | Description | Severity |
|---|---|---|
| 1 | Specify the appropriate base image (e.g., `node:18-alpine`) for the frontend application. | Required |
| 2 | Replace `<source_directory>` with the actual directory containing the frontend code. | Required |
| 3 | Replace `<build_directory>` with the desired directory for the built frontend assets. | Required |
| 4 | Replace `<port>` with the port on which the frontend application will run (e.g., `3000`). | Required |
```

``` markdown
# frontend/package.json

| Task Number | Description | Severity |
|---|---|---|
| 1 | Populate the `name`, `version`, `description`, `author`, and other relevant fields with appropriate values. | Required |
| 2 | Add the necessary dependencies for the frontend application, including React, Redux, and other libraries. | Required |
| 3 | Define scripts for common tasks such as starting the development server, building the production application, and running tests. | Required |
```

``` markdown
# frontend/src/index.tsx

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/tailwind.config.js

| Task Number | Description | Severity |
|---|---|---|
| 1 | Populate the `content` array with the paths to all template files that use Tailwind CSS classes. | Required |
| 2 | Define custom colors, fonts, and other design elements according to the application's design specifications. | Required |
```

``` markdown
# frontend/tsconfig.json

| Task Number | Description | Severity |
|---|---|---|
| 1 | Configure the compiler options, include and exclude paths, and other settings according to the project requirements and coding conventions. | Required |
```

``` markdown
# frontend/tsconfig.json

| Task Number | Description | Severity |
|---|---|---|
| 1 | Configure the compiler options, include and exclude paths, and other settings according to the project requirements and coding conventions. | Required |

```

``` markdown
# frontend/tsconfig.json

| Task Number | Description | Severity |
|---|---|---|
| 1 | Configure the compiler options, include and exclude paths, and other settings according to the project requirements and coding conventions. | Required |

```

``` markdown
# scripts/run_crawlers.sh

| Task Number | Description | Severity |
|---|---|---|
| 1 | Implement the logic to run the web crawlers, potentially using tools like Scrapy. | Required |
| 2 | Set up scheduling for the crawlers to run at regular intervals (e.g., daily, weekly). | Required |
| 3 | Implement logging to track the progress and results of the crawling process. | Required |
| 4 | Add error handling and notifications for any issues encountered during crawling. | Required |
```

``` markdown
# scripts/setup_database.sh

| Task Number | Description | Severity |
|---|---|---|
| 1 | Add logic to create the PostgreSQL database. | Required |
| 2 | Add logic to create the Elasticsearch database. | Required |
| 3 | Add logic to apply database migrations using Alembic. | Required |
| 4 | Add logic to create the necessary user accounts for the databases. | Required |
| 5 | Add logic to configure appropriate permissions for the database users. | Required |
```

``` markdown
# shared/types/analytics.ts

No pending human tasks have been identified for this file.
```

``` markdown
# shared/types/executive.ts

No pending human tasks have been identified for this file.
```

``` markdown
# shared/types/founder.ts

No pending human tasks have been identified for this file.
```

``` markdown
# shared/types/fundingRound.ts

No pending human tasks have been identified for this file.
```

``` markdown
# shared/types/investor.ts

No pending human tasks have been identified for this file.
```

``` markdown
# shared/types/jobPosting.ts

No pending human tasks have been identified for this file.
```

``` markdown
# shared/types/newsArticle.ts

No pending human tasks have been identified for this file.
```

``` markdown
# shared/types/startup.ts

No pending human tasks have been identified for this file.
```

``` markdown
# shared/types/user.ts

No pending human tasks have been identified for this file.
```

``` markdown
# tests/backend/conftest.py

No pending human tasks have been identified for this file.
```

``` markdown
# tests/backend/test_analytics.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Add assertions to verify the structure and content of the funding trend data. | Required |
| 2 | Add assertions to verify the structure and content of the industry breakdown data. | Required |
| 3 | Add assertions to verify the structure and content of the headcount growth data. | Required |
```

``` markdown
# tests/backend/test_auth.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Retrieve a test user from the database or create one if it doesn't exist. | Required |
| 2 | Replace the placeholder test credentials with the actual test user's credentials. | Required | 
```

``` markdown
# tests/backend/test_funding_rounds.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Add assertions to verify the structure and content of the funding round data. | Required |
| 2 | Retrieve a valid funding round ID from the database. | Required | 
| 3 | Add assertions to verify the structure and content of the created funding round data. | Required |
| 4 | Retrieve a valid funding round ID from the database. | Required |
| 5 | Add assertions to verify the structure and content of the updated funding round data. | Required |
| 6 | Retrieve a valid funding round ID from the database. | Required | 
```

``` markdown
# tests/backend/test_investors.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Add assertions to verify the structure and content of the investor data. | Required |
| 2 | Retrieve a valid investor ID from the database. | Required |
| 3 | Add assertions to verify the structure and content of the created investor data. | Required |
| 4 | Retrieve a valid investor ID from the database. | Required |
| 5 | Add assertions to verify the structure and content of the updated investor data. | Required |
| 6 | Retrieve a valid investor ID from the database. | Required |

```

``` markdown
# tests/backend/test_jobs.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Add assertions to verify the structure and content of the job posting data. | Required |
| 2 | Retrieve a valid job posting ID from the database. | Required |
| 3 | Add assertions to verify the structure and content of the created job posting data. | Required |
| 4 | Retrieve a valid job posting ID from the database. | Required |
| 5 | Add assertions to verify the structure and content of the updated job posting data. | Required |
| 6 | Retrieve a valid job posting ID from the database. | Required |

```

``` markdown
# tests/backend/test_news.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Add assertions to verify the structure and content of the news article data. | Required |
| 2 | Retrieve a valid news article ID from the database. | Required |
| 3 | Add assertions to verify the structure and content of the created news article data. | Required |
| 4 | Retrieve a valid news article ID from the database. | Required |
| 5 | Add assertions to verify the structure and content of the updated news article data. | Required |
| 6 | Retrieve a valid news article ID from the database. | Required |

```

``` markdown
# tests/backend/test_search.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Populate the database with test startup data. | Required |
| 2 | Add assertions to verify that the returned startups match the search query. | Required |
```

``` markdown
# tests/backend/test_startups.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Add assertions to verify the structure and content of the startup data. | Required |
| 2 | Retrieve a valid startup ID from the database. | Required |
| 3 | Add assertions to verify the structure and content of the created startup data. | Required |
| 4 | Retrieve a valid startup ID from the database. | Required |
| 5 | Add assertions to verify the structure and content of the updated startup data. | Required |
| 6 | Retrieve a valid startup ID from the database. | Required |

```

``` markdown
# tests/backend/test_users.py

| Task Number | Description | Severity |
|---|---|---|
| 1 | Add assertions to verify the structure and content of the user data. | Required |
| 2 | Populate the database with test user data. | Required |
| 3 | Retrieve a valid user ID from the database. | Required |
| 4 | Add assertions to verify the structure and content of the created user data. | Required |
| 5 | Retrieve a valid user ID from the database. | Required |
| 6 | Add assertions to verify the structure and content of the updated user data. | Required |
| 7 | Retrieve a valid user ID from the database. | Required |

```

``` markdown
# tests/frontend/App.test.tsx

| Task Number | Description | Severity |
|---|---|---|
| 1 | Add more specific assertions to verify that the App component renders the expected content, such as the header, navigation bar, and footer. | Required |
| 2 | Consider using `screen.getByText` or other query functions from `@testing-library/react` to locate specific elements in the rendered output. | Optional |
```

``` markdown
# tests/frontend/setupTests.ts

| Task Number | Description | Severity |
|---|---|---|
| 1 | Mock any external dependencies, such as API calls or browser APIs, that are used in the components being tested. | Required |
```

``` markdown
# backend/alembic/env.py

No pending human tasks have been identified for this file.
```

``` markdown
# backend/alembic/script.py.mako

No pending human tasks have been identified for this file.
```

``` markdown
# backend/alembic/versions/000000000000_initial_migration.py

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/public/favicon.ico

| Task Number | Description | Severity |
|---|---|---|
| 1 | Replace this placeholder file with the actual favicon for the application. | Required |
```

``` markdown
# frontend/public/index.html

| Task Number | Description | Severity |
|---|---|---|
| 1 | Populate the `<title>` tag with the application's title. | Required |
| 2 | Add a `<meta name=\"description\" ...>` tag with a brief description of the application. | Required |
| 3 | Customize the `<link rel=\"icon\" ...>` tag to point to the actual favicon file. | Required |
| 4 | Add any additional `<meta>` tags for SEO or social media sharing. | Optional |
| 5 | Include links to external CSS files or CDN links for libraries like Bootstrap or Tailwind CSS. | Required |
| 6 | Add any necessary JavaScript code for analytics or other third-party services. | Optional |
```

``` markdown
# frontend/public/logo192.png

| Task Number | Description | Severity |
|---|---|---|
| 1 | Replace this placeholder file with the actual logo image for the application. | Required |
```

``` markdown
# frontend/public/logo512.png

| Task Number | Description | Severity |
|---|---|---|
| 1 | Replace this placeholder file with the actual logo image for the application. | Required |
```

``` markdown
# frontend/public/manifest.json

| Task Number | Description | Severity |
| :----------- | :----------- | :----------- |
| 1 | Replace placeholders for `short_name`, `name`, `icons`, and `theme_color` with actual content. | Required |
```

``` markdown
# frontend/public/robots.txt

| Task Number | Description | Severity |
|---|---|---|
| 1 | Define the rules for search engine crawlers. For example, you can allow all crawlers to access all pages, or you can disallow certain crawlers from accessing specific pages or directories. | Required |
```

``` markdown
# frontend/src/main.tsx

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/react-app-env.d.ts

| Task Number | Description | Severity |
|---|---|---|
| 1 | Declare the specific environment variables used in the application and their corresponding types. For example, you might declare variables for API keys, base URLs, or feature flags. | Required |
```

``` markdown
# frontend/src/reportWebVitals.ts

No pending human tasks have been identified for this file.
```

``` markdown
# frontend/src/setupProxy.js

| Task Number | Description | Severity |
|---|---|---|
| 1 | Adjust the target URL (`http://localhost:8000`) to match the actual URL of the backend API. | Required |
```

``` markdown
# .github/workflows/backend.yml

| Task Number | Description | Severity |
|---|---|---|
| 1 | Replace `<docker_username>` with your Docker Hub username. | Required |
| 2 | Replace `<docker_password>` with your Docker Hub password or access token. | Required |
| 3 | Replace `<aws_access_key_id>` with your AWS access key ID. | Required |
| 4 | Replace `<aws_secret_access_key>` with your AWS secret access key. | Required |
| 5 | Replace `<aws_region>` with the AWS region where you want to deploy the application. | Required |
| 6 | Replace `<ecr_repository_name>` with the name of your ECR repository. | Required |
| 7 | Replace `<ecs_cluster_name>` with the name of your ECS cluster. | Required |
| 8 | Replace `<ecs_service_name>` with the name of your ECS service. | Required |
| 9 | Specify the appropriate Dockerfile path for the backend application. | Required |
| 10 | Define the necessary steps for building and pushing the Docker image to ECR. | Required |
| 11 | Define the necessary steps for deploying the application to ECS. | Required |
```

``` markdown
# .github/workflows/frontend.yml

| Task Number | Description | Severity |
|---|---|---|
| 1 | Replace `<docker_username>` with your Docker Hub username. | Required |
| 2 | Replace `<docker_password>` with your Docker Hub password or access token. | Required |
| 3 | Replace `<aws_access_key_id>` with your AWS access key ID. | Required |
| 4 | Replace `<aws_secret_access_key>` with your AWS secret access key. | Required |
| 5 | Replace `<aws_region>` with the AWS region where you want to deploy the application. | Required |
| 6 | Replace `<ecr_repository_name>` with the name of your ECR repository. | Required |
| 7 | Replace `<s3_bucket_name>` with the name of your S3 bucket. | Required |
| 8 | Replace `<cloudfront_distribution_id>` with the ID of your CloudFront distribution. | Required |
| 9 | Specify the appropriate Dockerfile path for the frontend application. | Required |
| 10 | Define the necessary steps for building and pushing the Docker image to ECR. | Required |
| 11 | Define the necessary steps for deploying the application to S3 and invalidating the CloudFront cache. | Required |
```

``` markdown
# .github/workflows/frontend.yml

| Task Number | Description | Severity |
|---|---|---|
| 1 | Replace `<docker_username>` with your Docker Hub username. | Required |
| 2 | Replace `<docker_password>` with your Docker Hub password or access token. | Required |
| 3 | Replace `<aws_access_key_id>` with your AWS access key ID. | Required |
| 4 | Replace `<aws_secret_access_key>` with your AWS secret access key. | Required |
| 5 | Replace `<aws_region>` with the AWS region where you want to deploy the application. | Required |
| 6 | Replace `<ecr_repository_name>` with the name of your ECR repository. | Required |
| 7 | Replace `<s3_bucket_name>` with the name of your S3 bucket. | Required |
| 8 | Replace `<cloudfront_distribution_id>` with the ID of your CloudFront distribution. | Required |
| 9 | Specify the appropriate Dockerfile path for the frontend application. | Required |
| 10 | Define the necessary steps for building and pushing the Docker image to ECR. | Required |
| 11 | Define the necessary steps for deploying the application to S3 and invalidating the CloudFront cache. | Required |

```

``` markdown
# README.md

| Task Number | Description | Severity |
|---|---|---|
| 1 | Provide a detailed overview of the Boston Startup Tracker project, including its purpose, features, and target audience. | Required |
| 2 | Include instructions for setting up the development environment, including installing dependencies, configuring the database, and running the application locally. | Required |
| 3 | Provide instructions for deploying the application to a production environment. | Required |
| 4 | Add information on how to contribute to the project, including coding conventions, testing procedures, and submitting pull requests. | Optional |
| 5 | Include a license for the project (e.g., MIT License). | Required |
```

``` markdown
# docker-compose.yml

| Task Number | Description | Severity |
|---|---|---|
| 1 | Replace the image placeholders with the actual image names and tags for the backend and frontend services. | Required |
| 2 | Specify the necessary environment variables for each service, such as database connection URLs, API keys, and other configuration settings. | Required |
| 3 | Configure the ports for each service to expose them to the host machine or other services. | Required |
| 4 | Define volumes to persist data for the database, search engine, and cache. | Required |
| 5 | Consider adding a service for the message broker (Apache Kafka) if needed. | Optional |
```

