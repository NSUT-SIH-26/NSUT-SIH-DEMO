# SIH 2026 Project Repository Template

This repository is a **reference template for SIH 2026 teams**. Students can use this structure for their own project repository before submitting the GitHub link.

Replace all sample content with your actual project information.

## 1. Project Information

- **Project Title:** CropGuard – AI Crop Disease Detection
- **PS ID:** SIH2026-DEMO-001
- **PS Title:** AI-based crop disease detection and advisory system
- **Category:** Software
- **Theme:** Smart Agriculture

## 2. Problem Statement

Farmers may have difficulty identifying crop diseases at an early stage. Manual identification can be slow and may depend on access to agricultural experts.

## 3. Proposed Solution

CropGuard allows a user to upload a crop image. The backend processes the image using a machine-learning model, predicts the likely disease, and returns basic advisory information.

## 4. Key Features

- Crop image upload
- Disease prediction
- Confidence score
- Advisory information
- Prediction history

## 5. Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- Machine Learning: TensorFlow, NumPy
- Database: PostgreSQL
- Deployment: Docker / Cloud

## 6. Architecture

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

## 7. Repository Structure

```text
YOUR-SIH-PROJECT/
├── README.md
├── SUBMISSION_GUIDE.md
├── submission/
│   ├── PRESENTATION.md
│   └── DEMO.md
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

### What goes where?

| Item | Location |
|---|---|
| Source code | `src/` or your normal project folders |
| Architecture / technical documentation | `docs/` |
| Project screenshots / hardware photos | `assets/screenshots/` |
| Final PPT / presentation | `submission/` |
| Demo video link | `submission/DEMO.md` |
| Project overview | `README.md` |

## 8. Final Presentation

Keep your final SIH presentation in the repository whenever the file size allows it.

See [submission/PRESENTATION.md](submission/PRESENTATION.md) for the required format.

If the PPT is too large for GitHub, use Google Drive/OneDrive and put the accessible viewer link in `submission/PRESENTATION.md`.

## 9. Demo Video

A demo video is **optional**, but recommended.

Add the YouTube/Google Drive link in [submission/DEMO.md](submission/DEMO.md).

## 10. Screenshots / Prototype Photos

Add important screenshots or hardware/prototype photos to:

`assets/screenshots/`

See [assets/screenshots/README.md](assets/screenshots/README.md) for examples and naming conventions.

## 11. Installation

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
pip install -r requirements.txt
```

## 12. Run

```bash
uvicorn src.main:app --reload
```

Replace these commands with the actual setup and run instructions for your project.


## 13. Future Scope

Describe realistic improvements or extensions that can be made to the project.

## Important

Before submission, make sure the repository is accessible to reviewers. Do **not** upload passwords, API keys, access tokens, `.env` files containing secrets, or other confidential credentials.
