# Osteoporosis Detection on Knee X-Rays

This project aims to determine osteoporosis on knee X-rays using transfer learning and a tuned convolutional neural network (CNN) model.

## Project Overview

Osteoporosis is a condition characterized by decreased bone density and increased risk of fractures. In this project, we leverage machine learning techniques to analyze knee X-ray images and detect signs of osteoporosis. By employing transfer learning, we utilize a pre-trained CNN model and fine-tune it specifically for osteoporosis detection.

## Data-set  

https://www.kaggle.com/datasets/shashwatwork/knee-osteoarthritis-dataset-with-severity

## Technologies Used

The project extensively utilizes the following technologies:

- **TensorFlow:** An open-source machine learning framework that provides a wide range of tools and libraries for building and training neural networks.

- **Keras:** A high-level neural networks API that runs on top of TensorFlow, simplifying the model building process.

- **TensorFlow Serving API:** A framework for serving TensorFlow models in production environments.

- **Pandas:** A data manipulation and analysis library that provides easy-to-use data structures and data analysis tools.

- **Streamlit:** A Python library for building interactive data applications, which we use for creating a user-friendly front-end interface.

## Kubernetes Services

This project employs a Kubernetes cluster with the following three services:

- **Front Service:** This service handles the user interface and provides an interactive environment for users to upload knee X-ray images.

- **Back Service:** The back-end service processes the uploaded images and applies the trained CNN model for osteoporosis detection.

- **TensorFlow Server:** This service hosts the trained model and provides an API endpoint for inference on the uploaded images.

## Dataset and Training

The CNN model is trained on a dataset consisting of 6000 knee X-ray images. To enhance the model's performance and generalization, data augmentation techniques are applied. Data augmentation involves augmenting the dataset by applying transformations such as rotation, scaling, and flipping, thereby increasing the diversity of the training samples.

## Getting Started

Before running the project, make sure you have the following prerequisites installed:

 - Docker: Install Docker to build and manage containers. Follow the official Docker installation guide for your operating system: https://docs.docker.com/get-docker/.

 - Kubernetes: Install Kubernetes to manage containerized applications. Follow the official Kubernetes installation guide for your platform:   https://kubernetes.io/docs/setup/.

 - Kind: Install Kind (Kubernetes in Docker) to create local Kubernetes clusters. Kind allows for easy cluster creation and management. Follow the official Kind installation guide: https://kind.sigs.k8s.io/docs/user/quick-start/.



To run the project locally, follow these steps:

Clone the repository.

**Executing the Bash Script:**

1. Open a terminal or command line interface.
2. Navigate to the directory where the Bash script is saved.
3. Ensure that the script has executable permissions. If not, run the following command to grant execute permission: `chmod +x script.sh`.
4. Run the script by entering the following command: `./kind-deployment.sh`.
5. The script will start executing the commands sequentially. Wait for each command to complete before proceeding to the next one.
6. If the script prompts for any input or confirmation during execution, provide the necessary input to proceed.
7. Once the script finishes executing all the commands, it will launch the external script `portforward.sh`.

**Executing the Python Script:**

1. Make sure you have Python installed on your system. You can check by running the following command: `python --version`.
2. Open a terminal or command line interface.
3. Navigate to the directory where the Python script is saved.
4. Run the following command to execute the Python script: `python kind-deployment.py`.
5. The script will start executing the commands sequentially. Wait for each command to complete before proceeding to the next one.
6. If the script prompts for any input or confirmation during execution, provide the necessary input to proceed.
7. Once the script finishes executing all the commands, it will launch the external script `portforward.py`.

Please note that both scripts assume that you have the necessary dependencies, such as Kind, Docker (Docker engine must be running), and kubectl, installed and properly configured on your system. Make sure to adjust the file paths and commands within the scripts according to your specific setup.

If you have any further questions or need additional assistance, please don't hesitate to ask.

**How to launch app:**

Access the application in your web browser at : http://localhost:80

## Conclusion

By leveraging transfer learning and a fine-tuned CNN model, this project provides an efficient solution for osteoporosis detection on knee X-ray images. The utilization of Kubernetes services, along with TensorFlow, Keras, TensorFlow Serving API, Pandas, and Streamlit, contributes to the seamless deployment and user-friendly experience.

For more details, please refer to the documentation and code within the repository.

If you have any questions or need further assistance, feel free to reach out.


**Note:** This project is for educational and research purposes only and should not replace professional medical diagnoses.
