# Live Video Chat Dating App Backend

This is the backend API for the Live Video Chat Dating App built using FastAPI and Firestore.

## **Table of Contents**

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Deployment](#deployment)

## **Getting Started**

This guide will help you set up and run the backend application on your local machine for development and testing purposes.

## **Project Structure**

backend/ ├── app/ │ ├── main.py │ ├── models/ │ ├── routers/ │ ├── services/ │ ├── schemas/ │ ├── utils/ │ └── init.py ├── tests/ ├── Dockerfile ├── requirements.txt └── README.md



## **Setup**

### **Prerequisites**

- Python 3.8 or higher
- Google Cloud SDK (for Firestore)
- Docker (optional, for containerization)

### **Install Dependencies**

1. **Create a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
    ```