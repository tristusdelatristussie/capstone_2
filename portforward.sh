#!/bin/bash

# Get the pod name
pod_name=$(kubectl get pods -l app=front-streamlit -o jsonpath="{.items[0].metadata.name}")

# Function to perform port forwarding
perform_port_forwarding() {
    # Perform port forwarding
    kubectl port-forward $pod_name 80:8501
}

# Function to restart port forwarding after 30 seconds
restart_port_forwarding() {
    echo "Connection lost. Restarting port forwarding in 30 seconds..."
    sleep 30
    perform_port_forwarding
}

# Perform initial port forwarding
perform_port_forwarding

# Restart port forwarding if the connection is lost
while true; do
    if ! nc -z localhost 80; then
        restart_port_forwarding
    fi
    sleep 1
done