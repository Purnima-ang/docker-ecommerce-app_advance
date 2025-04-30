# E-commerce Multi-Service Application

Dockerized e-commerce storefront with the following services:

- **Web Service:** A frontend application built with Python and Flask.
- **Database Service:** A PostgreSQL database to store application data.
- **Cache Service:** Redis for caching frequently accessed data.

**Prerequisites:**
- Docker Engine (version 20.10 or later)
- Docker Compose (version 1.27 or later)
- Git
- A GitHub account
- A Docker Hub account

**Setup:**

- Clone: `git clone https://github.com/<your_github_username>/<your_repository_name>.git && cd <your_repository_name>`
- Run: `docker compose up -d --build`
- Access: `http://localhost:5000`

**Run Environments:**

- **Dev:** `docker compose up -d --build` (uses `.env` or `.env.development`)
- **Prod:** `docker compose --env-file .env.production up -d --build`

**Docker Hub Images:**
The Docker images for this application are hosted on Docker Hub:

- Web: <your_dockerhub_username>/ecommerce-web
- Database: <your_dockerhub_username>/ecommerce-db
- Cache: <your_dockerhub_username>/ecommerce-cache

**Docker Volumes:**
A named Docker volume db_data is used to persist the PostgreSQL database, ensuring data is retained across container restarts.

**Security Best Practices Implemented:**

**Web Service:**
- Running the application process as a non-root user (appuser).
- Mounting the container's root filesystem as read-only (read_only: true).
- Using tmpfs for temporary file storage (/tmp).
- Preventing privilege escalation using security_opt: no-new-privileges:true.

**Database Service:**
- Limiting resource consumption (CPU and memory) using deploy.resources.limits in docker-compose.yml.

**Cache Service:**
- Running the Redis server as the nobody user.
- Dockerfile Optimizations

**Web Service:**
- Implemented a multi-stage build to reduce the final image size by separating the build environment from the runtime environment. Only necessary artifacts    are copied into the final image.
- Utilized a .dockerignore file to exclude unnecessary files and directories from the build context, leading to faster build times and smaller image sizes.

**Continuous Integration/Continuous Delivery (CI/CD) Pipeline:**

The application leverages GitHub Actions for an automated CI/CD pipeline, defined in `.github/workflows/main.yml`.

**Workflow Trigger:**

- The workflow is automatically triggered on `push` events to the `main` branch and on `pull_request` events targeting the `main` branch.

**Workflow Jobs

- **`build`:**
  -   Checks out the source code.
  -   Sets up `docker/setup-buildx-action` for efficient Docker builds.
  -   Authenticates with Docker Hub using stored secrets (`DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`).
  -   Builds the Docker images for the web, database, and cache services.
  -   Pushes the tagged Docker images to Docker Hub.
- **`deploy`:**
  -   This job depends on the successful completion of the `build` job.
  -   Checks out the source code.
  -   Sets up `docker/compose-action` for interacting with Docker Compose.
  -   **Simulated Deployment:** Currently, this step includes a basic command to simulate deployment to a staging environment by echoing a confirmation message and the newly pushed image digests. In a production setup, this would involve more specific deployment commands tailored to your infrastructure (e.g., deploying to a Kubernetes cluster or a set of virtual machines).

**Running the CI/CD Pipeline:**

To initiate the CI/CD pipeline, simply commit and push your code changes to the `main` branch of your GitHub repository. The progress and results of the workflow can be monitored in the "Actions" tab of your repository on GitHub.

**Docker CLI Commands (Examples):**

- `docker build`: Builds Docker images from Dockerfiles.
- `docker tag`: Tags Docker images with a repository and tag name.
- `docker push`: Pushes Docker images to a Docker registry (Docker Hub).
- `docker ps`: Lists running Docker containers.
- `docker images`: Lists locally available Docker images.
- `docker volume ls`: Lists Docker volumes.
- `docker compose up`: Builds and starts multi-container Docker applications.
- `docker compose down`: Stops and removes containers, networks, volumes, and images created by `up`.
- `docker logs`: Views the logs of Docker containers.
- `docker exec`: Executes commands in a running Docker container.

**Note:** Replace the placeholder links and usernames with your actual information.