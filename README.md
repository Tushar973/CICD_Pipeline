# 🚀 Flask App – Automated Testing & CI/CD

A **simple Flask-based project** demonstrating **automated testing**, **Dockerization**, and **CI/CD using GitHub Actions**.

The goal of this project is to show a **basic end-to-end DevOps workflow** for a Python web application.

---

## 🔹 📌 Project Summary

This project includes:
- A minimal **Flask web application**
- Automated testing using **pytest**
- Containerization using **Docker**
- CI/CD pipeline using **GitHub Actions**
- Docker image build & push to **Docker Hub**

It is designed for **learning and demonstration purposes**, especially for beginners in DevOps and backend development.

---

## ❓ Problem Statement

Build a simple Flask application and:
- Automatically test it on every push
- Build a Docker image
- Push the image to Docker Hub using CI/CD

---

## 📂 Project Structure
├── app.py # Flask application
├── test_app.py # Pytest test cases
├── requirements.txt # Python dependencies
├── DockerFile # Docker configuration
├── README.md # Project documentation
├── .github/
│ └── workflows/
│ └── cicd.yml # GitHub Actions CI/CD pipeline

---

## 📂 Dataset / App Details

- **Endpoint:** `/`
- **Response:** `HELLO WORLD!`
- **Port:** `5000`

---

## 🧪 Testing

Tests are written using **pytest**.

Test case validates:
- Status code is `200`
- Response body is `HELLO WORLD!`

Run tests locally:
```bash
pytest
