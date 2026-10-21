🚀 CI/CD Pipeline Using GitHub Actions and Docker

<p align="center">
<img src="https://img.shields.io/badge/CI%2FCD-Automation-blue?style=for-the-badge" alt="CI/CD Automation">
<img src="https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/GitHub%20Actions-Workflow-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

📌 Project Overview

This project demonstrates the implementation of a Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions and Docker.

The pipeline automates application testing, Docker image building, and image publishing to Docker Hub. The application is deployed using Render and verified through its deployment URL.

🎯 Main Goal: To understand DevOps practices, workflow automation, containerization, and application deployment.

🎯 Objectives
⚙️ Automate application testing using GitHub Actions.
🐳 Build a Docker image using a Dockerfile.
📦 Push the Docker image to Docker Hub.
🌐 Deploy the application using Render.
✅ Verify the application after deployment.
🔄 Understand CI/CD workflow automation.
🛠️ Technologies Used
Technology	Purpose
🐙 Git & GitHub	Version control and source code management
⚙️ GitHub Actions	CI/CD workflow automation
🐳 Docker	Application containerization
📦 Docker Hub	Docker image storage and distribution
🔧 Docker Compose	Application service configuration
🌐 Render	Application deployment and hosting
🐍 Python & Flask	Sample web application
💻 VS Code / GitHub Codespaces	Development environment
🔄 Project Architecture
👨‍💻 Developer
      |
      v
🐙 GitHub Repository
      |
      v
⚙️ GitHub Actions Workflow
      |
      v
🧪 Automated Testing
      |
      v
🐳 Build Docker Image
      |
      v
📦 Push Image to Docker Hub
      |
      v
🌐 Deploy Application on Render
      |
      v
✅ Verify Deployed Application

📁 Project Structure
cicd-project/
├── 📄 app.py
├── 📄 test_app.py
├── 📄 requirements.txt
├── 🐳 Dockerfile
├── 📄 docker-compose.yml
├── 📄 .dockerignore
├── 📂 .github/
│   └── 📂 workflows/
│       └── ⚙️ ci-cd.yml
└── 📄 README.md

📋 Prerequisites

Before running this project, make sure you have:

✅ Git installed
✅ Docker installed
✅ A GitHub account
✅ A Docker Hub account
✅ A Render account
✅ Python installed for local testing
🚀 Setup and Execution
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY


Replace the placeholders with your actual GitHub username and repository name.

2️⃣ Install Dependencies
python -m pip install -r requirements.txt

3️⃣ Run Automated Tests
python -m pytest -q


✅ This command runs the automated tests to check whether the application is working correctly.

4️⃣ Build the Docker Image
docker build -t YOUR_DOCKERHUB_USERNAME/cicd-project:latest .

5️⃣ Run the Application Locally
docker run --rm -p 5000:5000 YOUR_DOCKERHUB_USERNAME/cicd-project:latest


🌍 Open your browser and visit:

http://localhost:5000

6️⃣ Configure GitHub Actions

The workflow configuration is located at:

.github/workflows/ci-cd.yml

The workflow runs automated tests and builds and pushes the Docker image when code is pushed to the main branch.

🔐 Configure the following under GitHub Repository → Settings → Secrets and variables → Actions:

DOCKERHUB_USERNAME — Docker Hub username (repository variable).
DOCKERHUB_TOKEN — Docker Hub access token (repository secret).

⚠️ Security Note: Never commit access tokens, passwords, or other sensitive credentials to your repository.

7️⃣ Deploy Using Render
🌐 Sign in to Render.
🔗 Connect your GitHub repository.
⚙️ Configure the deployment method and required build/start settings.
🚀 Deploy the application.
✅ Open the Render-provided URL and verify the application.
📊 Expected Results
✅ Automated tests execute successfully.
🐳 Docker image builds successfully.
📦 Docker image is published to Docker Hub.
⚙️ GitHub Actions workflow completes successfully.
🌐 Application is accessible through the Render deployment URL.
📸 Project Deliverables
🐙 GitHub repository containing source code and workflow configuration.
🐳 Docker Hub repository and published image link.
⚙️ Screenshots of successful GitHub Actions workflow runs.
📦 Screenshot of the Docker Hub image.
🌐 Render deployment URL and application screenshot.
📝 Project report documenting implementation and validation.
🎓 Learning Outcomes

Through this project, I gained practical experience with:

🔄 CI/CD workflow automation
🐳 Docker image creation and containerization
🧪 Automated application testing
📦 Docker image publishing
🌐 Application deployment
🔐 Secure management of deployment credentials

🏁 Conclusion

This project demonstrates how GitHub Actions, Docker, and Docker Hub can automate application testing and container image publishing. Render provides an environment for deploying and accessing the application.

Overall, this internship mini project provides practical knowledge of DevOps automation, version control, containerization, and application deployment.

👩‍💻 Author

Snehal Kute

🌟 Internship Mini Project — DevOps & CI/CD
