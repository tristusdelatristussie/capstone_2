#!/bin/bash

# Create Kind cluster
kind create cluster

# Build Docker image for the model
cd tf_server
docker build -t model:v001 .
kind load docker-image model:v001

# Apply deployments and services for the model
kubectl apply -f ./model-deployment.yaml
kubectl apply -f ./model-service.yaml

# Wait for model deployment to finish
kubectl rollout status deployment/model-deployment

# Build Docker image for the backend
cd ../back
docker build -t back:v001 .
kind load docker-image back:v001

# Apply deployments and services for the backend
kubectl apply -f ./back-deployment.yaml
kubectl apply -f ./back-service.yaml

# Wait for backend deployment to finish
kubectl rollout status deployment/back-deployment

# Build Docker image for the frontend
cd ../front
docker build -t front:v001 .
kind load docker-image front:v001

# Apply deployments and services for the frontend
kubectl apply -f ./front-deployment.yaml
kubectl apply -f ./front-service.yaml

# Wait for frontend deployment to finish
kubectl rollout status deployment/front-deployment

cd ..

# Run the external script portforward.sh
./portforward.sh
