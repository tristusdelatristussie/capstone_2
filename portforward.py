import subprocess
import time

# Get the pod name
pod_name = subprocess.check_output(["kubectl", "get", "pods", "-l", "app=front-streamlit", "-o", "jsonpath='{.items[0].metadata.name}'"]).decode().strip("'")

# Function to perform port forwarding
def perform_port_forwarding():
    # Perform port forwarding
    subprocess.call(["kubectl", "port-forward", pod_name, "80:8501"])

# Function to restart port forwarding after 30 seconds
def restart_port_forwarding():
    print("Connection lost. Restarting port forwarding in 30 seconds...")
    time.sleep(30)
    perform_port_forwarding()

# Perform initial port forwarding
perform_port_forwarding()

# Restart port forwarding if the connection is lost
while True:
    try:
        subprocess.check_output(["nc", "-z", "localhost", "80"])
    except subprocess.CalledProcessError:
        restart_port_forwarding()
    time.sleep(1)