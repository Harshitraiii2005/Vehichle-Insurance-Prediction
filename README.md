🚗 MLOps Project – Vehicle Insurance Data Pipeline

Welcome to this MLOps project built to impress recruiters and showcase real-world skills in:

✅ Data Engineering | ✅ Model Deployment | ✅ CI/CD Automation | ✅ Cloud Integration

📁 Project Structure & Setup

🔧 Step 1: Project Template

Run the project initializer:

bash
Copy
Edit
python template.py
📦 Step 2: Package Management

Ensure local imports work properly:

setup.py

pyproject.toml


🐍 Step 3: Virtual Environment


<details> <summary>🧪 Bash</summary>
  
bash
Copy
Edit
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list
</details> <details> <summary>🧪 PowerShell</summary>
  
powershell
Copy
Edit
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list
</details>
📊 MongoDB Setup & Data Management

🌐 Step 4: MongoDB Atlas



Create a free M0 cluster at MongoDB Atlas

Allow access from 0.0.0.0/0

Create a user & get the Python connection string

🧾 Step 5: Push Data to MongoDB


Add your dataset inside notebook/

Open mongoDB_demo.ipynb and push the data

Verify under: Database → Browse Collections

📝 Logging, Exception Handling & EDA
🛠 Step 6: Logging & Exception Handling


bash
Copy
Edit
src/
  ├── logger.py
  └── exception.py
🧪 Test using:

bash
Copy
Edit
python demo.py
📊 Step 7: EDA + Feature Engineering


Use Jupyter Notebook

Clean and transform data

Prepare features for the pipeline

📥 Data Ingestion
📌 Step 8: Ingestion Pipeline


MongoDB config → configuration/mongo_db_connections.py

Logic → data_access/, components/data_ingestion.py

Configs → entity/config_entity.py, artifact_entity.py

<details> <summary>🧪 Set Environment Variable</summary>
🔵 Bash:

bash
Copy
Edit
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority"
🟣 PowerShell:

powershell
Copy
Edit
$env:MONGODB_URL = "mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority"
</details>
🔍 Data Validation, Transformation & Model Training
✅ Step 9: Data Validation


Schema: config/schema.yaml

Validation: utils/main_utils.py

🔁 Step 10: Data Transformation


Logic: components/data_transformation.py

Configuration: entity/estimator.py

🧠 Step 11: Model Training


Training logic → components/model_trainer.py

🌐 AWS Deployment Setup
☁️ Step 12: AWS IAM Setup


Create IAM user on AWS Console

Attach AdministratorAccess

<details> <summary>🔐 Set AWS Credentials</summary>
🔵 Bash:

bash
Copy
Edit
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
🟣 PowerShell:

powershell
Copy
Edit
$env:AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
$env:AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
</details>
🪣 Step 13: Push Model to S3


S3 bucket: my-model-mlopsproj (Region: us-east-1)

Code: src/aws_storage/, entity/s3_estimator.py

🚀 Model Evaluation, Pusher & Prediction API
📊 Step 14: Evaluation & Pusher


Evaluate models

Push best model to S3

🧪 Step 15: Prediction Pipeline


Build app.py using FastAPI

Add templates/ + static/ for web UI

🔄 CI/CD – Docker + GitHub Actions + AWS
🐳 Step 16: Docker & GitHub Actions


dockerfile
Copy
Edit
# Dockerfile
FROM python:3.10
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
Secrets to add in GitHub repo:

nginx
Copy
Edit
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
☁️ Step 17: Deploy on EC2 + ECR


Launch EC2 instance

Install Docker

Connect EC2 as GitHub self-hosted runner

🔓 Step 18: Final Step


Open port 5080 in EC2 security group

Access app:

cpp
Copy
Edit
http://<your-public-ip>:5080
🛠 Additional Resources
📁 crashcourse.txt – Understand setup.py, pyproject.toml

🔐 GitHub Secrets – Secure your credentials

📦 Docker + FastAPI – Easy containerized API deployment

🎯 Project Workflow Summary
text
Copy
Edit
Data Ingestion ➝ Data Validation ➝ Data Transformation ➝
Model Training ➝ Model Evaluation ➝ Model Deployment ➝
CI/CD (GitHub Actions + Docker + AWS EC2 & ECR)
💬 Connect
Found this useful?
⭐ Star the repo
🐛 Raise an issue
💬 Connect for suggestions or contributions

