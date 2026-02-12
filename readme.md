# Product Management Application

This repository contains a **Product Management application** built using:

- **Frontend**: React (served via a Node Backend-for-Frontend)
- **Backend**: FastAPI (Python)
- **Architecture**: Backend-for-Frontend (BFF) pattern

The application allows creating, updating, deleting, and viewing products.

---

## 🚀 Running the Frontend (React + Node BFF)

The frontend is served using a **Node BFF (Backend-for-Frontend)** server.  
This server:
- Serves the React build files
- Proxies API requests to the FastAPI backend

### Steps

1. Navigate to the frontend directory:
   ```bash
   cd frontend

1. Install frontend dependencies:
   ```bash
   npm install

2. Build the React application:
   ```bash
   npm run build


3. Start the frontend server (BFF):
   ```bash
   node bff.js

4. Build the React application:
   ```bash
   npm run build

5. Open the application in the browser:
   ```bash
   https://<frontend-port-url>



## 🚀 Running the Backend (FastAPI)

The backend is a FastAPI application that exposes REST APIs for product management.
### Steps

1. Navigate to the backend directory:
   ```bash
   cd backend

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate

3. Install backend dependencies:
   ```bash
   pip install -r requirements.txt

4. Create a .env file (refer to .env.example):
   ```bash
   DB_URL=sqlite:///./products.db
   ALLOWED_ORIGINS=http://localhost:3000

5. Run the FastAPI server:
   ```bash
   uvicorn main:server --reload

6. Backend API will be available at:
   ```bash
   http://localhost:8000

   
   


## 📘 API Documentation (Swagger)

FastAPI automatically generates interactive API documentation.
Once the backend is running, access:
### Steps

1. Swagger UI
   ```bash
   http://localhost:8000/docs

