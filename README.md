🚗 MLOps Project - Vehicle Insurance Data Pipeline


Welcome to this MLOps project, designed to demonstrate a robust pipeline for managing vehicle insurance data. This project is crafted to impress recruiters and visitors by showcasing end-to-end machine learning operations—from data ingestion to model deployment and CI/CD automation.

📁 Project Setup and Structure

Step 1: Project Template

Run template.py to generate the initial folder structure with all required placeholder files.

Step 2: Package Management

Set up local package imports using setup.py and pyproject.toml.


Step 3: Virtual Environment and Dependencies


bash
Copy
Edit
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list
📊 MongoDB Setup and Data Management

Step 4: MongoDB Atlas Configuration

Sign up at MongoDB Atlas.

Create a project and set up a free M0 cluster.

Configure your DB username/password and whitelist 0.0.0.0/0.

Save your MongoDB connection string (replace <password>).

Step 5: Push Data to MongoDB


Create a notebook folder and add the dataset.

Use mongoDB_demo.ipynb to insert data into MongoDB.

Verify data on MongoDB Atlas → Database → Browse Collections.

📝 Logging, Exception Handling, and EDA


Step 6: Logging and Exception Handling


Implement custom logging.py and exception.py.

Test them via a demo script like demo.py.

Step 7: EDA and Feature Engineering


Perform exploratory data analysis and feature engineering in a Jupyter notebook for pipeline readiness.

📥 Data Ingestion
Step 8: Ingestion Pipeline


Setup MongoDB connection in configuration/mongo_db_connections.py.

Define ingestion logic in data_access and components/data_ingestion.py.

Configure config_entity.py and artifact_entity.py.

Set MongoDB Environment Variable
bash
Copy
Edit
# Bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority"

# PowerShell
$env:MONGODB_URL = "mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority"
🔍 Data Validation, Transformation & Model Training
Step 9: Data Validation


Define schema in config/schema.yaml.

Implement validation in utils/main_utils.py.

Step 10: Data Transformation


Handle transformations in components/data_transformation.py.

Use estimator.py in entity for pipeline configuration.

Step 11: Model Training


Train models via components/model_trainer.py.

🌐 AWS Setup for Deployment
Step 12: AWS Configuration


Create an IAM user in AWS Console.

Grant AdministratorAccess.

bash
Copy
Edit
# Bash
export AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_ACCESS_KEY"
Configure S3 bucket and update access in constants/__init__.py.

Step 13: Push/Pull from S3


Create an S3 bucket: my-model-mlopsproj in us-east-1.

Develop S3 handling logic in src/aws_storage and entity/s3_estimator.py.

🚀 Model Evaluation, Deployment & Prediction Pipeline
Step 14: Model Evaluation & Pusher


Add logic to evaluate and push best model to S3.

Step 15: Prediction Pipeline


Create API endpoints via app.py.

Include templates/ and static/ for web UI.

🔄 CI/CD with Docker, GitHub Actions & AWS
Step 16: Docker & GitHub Actions


Create Dockerfile and .dockerignore.

Set GitHub repository secrets:

nginx
Copy
Edit
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
Step 17: AWS EC2 & ECR Deployment


Launch an EC2 instance.

Install Docker on EC2.

Connect as a GitHub self-hosted runner.

Step 18: Final Steps


Open port 5080 on EC2.

Access app via: http://<your-public-ip>:5080

🛠️ Additional Resources


🔐 GitHub Secrets: Secure CI/CD pipelines using repository secrets.

🎯 Project Workflow Summary
csharp
Copy
Edit
Data Ingestion ➝ Data Validation ➝ Data Transformation ➝
Model Training ➝ Model Evaluation ➝ Model Deployment ➝
CI/CD with GitHub Actions, Docker, AWS EC2 & ECR
💬 Connect


If you found this project helpful or have questions, feel free to connect or raise an issue!
