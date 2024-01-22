import subprocess
import time

def run_command(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()

# Create Kind cluster
run_command('kind create cluster')

# Build Docker image for the model
run_command('cd tf_server && docker build -t model:v001 . && kind load docker-image model:v001')

# Apply deployments and services for the model
run_command('cd tf_server && kubectl apply -f ./model-deployment.yaml')
run_command('cd tf_server && kubectl apply -f ./model-service.yaml')

# Wait for model deployment to finish
run_command('kubectl rollout status deployment/model-deployment')

# Build Docker image for the backend
run_command('cd back && docker build -t back:v001 . && kind load docker-image back:v001')

# Apply deployments and services for the backend
run_command('cd back && kubectl apply -f ./back-deployment.yaml')
run_command('cd back && kubectl apply -f ./back-service.yaml')

# Wait for backend deployment to finish
run_command('kubectl rollout status deployment/back-deployment')

# Build Docker image for the frontend
run_command('cd front && docker build -t front:v001 . && kind load docker-image front:v001')
# Apply deployments and services for the frontend
run_command('cd front && kubectl apply -f ./front-deployment.yaml')
run_command('cd front && kubectl apply -f ./front-service.yaml')

# Wait for frontend deployment to finish
run_command('kubectl rollout status deployment/front-deployment')

# Run the external script portforward
run_command('python portforward.py')
