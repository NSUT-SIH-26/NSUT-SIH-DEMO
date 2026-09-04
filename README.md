# SIH 2026 Demo Submission Repository

This repository demonstrates how a student project can be organised before submitting its GitHub link for SIH 2026.

Replace the sample content with your actual project details.

## Project Information

- **Project Title:** CropGuard – AI Crop Disease Detection
- **PS ID:** SIH2026-DEMO-001
- **PS Title:** AI-based crop disease detection and advisory system
- **Category:** Software
- **Theme:** Smart Agriculture

## Problem Statement

Farmers may have difficulty identifying crop diseases at an early stage. Manual identification can be slow and may depend on access to agricultural experts.

## Proposed Solution

CropGuard allows a user to upload a crop image. The backend processes the image using a machine-learning model, predicts the likely disease, and returns basic advisory information.

## Key Features

- Crop image upload
- Disease prediction
- Confidence score
- Advisory information
- Prediction history

## Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- Machine Learning: TensorFlow, NumPy
- Database: PostgreSQL
- Deployment: Docker / Cloud

## Architecture

See [docs/architecture.md](docs/architecture.md).

```text
User
  |
  v
Frontend
  |
  v
Backend API
  |
  +----> Database
  |
  v
ML Model
  |
  v
Prediction
```

## Repository Structure

```text
NSUT-SIH-DEMO/
├── README.md
├── SUBMISSION_GUIDE.md
├── src/
│   └── main.py
├── docs/
│   └── architecture.md
├── assets/
│   └── screenshots/
│       └── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

The exact folders may differ for your technology stack or hardware project, but keep the repository organised and easy to review.

## Installation

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
pip install -r requirements.txt
```

## Run

```bash
uvicorn src.main:app --reload
```

## Demo

- Live Demo: `<YOUR_LIVE_DEMO_LINK>`
- Demo Video: `<YOUR_DEMO_VIDEO_LINK>`

## Screenshots

Place important screenshots in `assets/screenshots/`.

## Team Members

| Name | Role |
|---|---|
| Student 1 | Team Leader / Backend |
| Student 2 | Machine Learning |
| Student 3 | Frontend |
| Student 4 | Testing / Documentation |

## Future Scope

- Improve prediction accuracy
- Support more crop diseases
- Add multilingual support
- Integrate real-time agricultural advisories

## Important

This is a fictional demo project. Students should replace the sample project details with their own information before submission.
