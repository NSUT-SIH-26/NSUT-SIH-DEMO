# SIH 2026 Submission Guide

Use this checklist before sharing your GitHub repository link.

## Required repository content

- Actual source code is present.
- `README.md` explains the project clearly.
- PS ID and PS title are included.
- Problem statement and proposed solution are explained.
- Key features are listed.
- Technology stack is listed.
- Setup and run instructions work.
- Team members and roles are mentioned.
- Important screenshots or hardware/prototype photos are included.
- Final PPT/presentation is placed in `submission/` whenever practical.
- If the PPT is too large for GitHub, an accessible Google Drive/OneDrive viewer link is added to `submission/PRESENTATION.md`.
- Demo video link is added to `submission/DEMO.md` if available. This is optional.
- Repository is accessible to reviewers.

## Recommended structure

```text
YOUR-SIH-PROJECT/
├── README.md
├── SUBMISSION_GUIDE.md
├── submission/
│   ├── PRESENTATION.md
│   └── DEMO.md
├── src/
├── docs/
├── assets/
│   └── screenshots/
└── ...
```

## Presentation

Upload the final PPT/PPTX to the `submission/` folder when the file size is suitable for GitHub. Use a clear filename such as:

`TeamName_SIH2026_Presentation.pptx`

If the PPT is too large, use Google Drive or OneDrive and put the shareable viewer link in `submission/PRESENTATION.md`.

## Demo video

The demo video is optional. If you have one, add its YouTube/Google Drive link to `submission/DEMO.md` and make sure it is accessible without requesting permission.

## Screenshots / hardware photos

Put important screenshots and prototype photos in `assets/screenshots/`. Include the most useful screens/results rather than random development screenshots.

## Do not upload

- Passwords
- API keys
- Access tokens
- `.env` files containing secrets
- Private credentials
- Other confidential information

## README should answer

1. What problem are you solving?
2. What is your proposed solution?
3. How does it work?
4. Which technologies did you use?
5. How can a reviewer run it?
6. What does the final output look like?
7. What are the important features and expected impact?

## Before submission

Open your repository in a private/incognito browser window or while logged out and verify that the reviewer can access the code, PPT, screenshots, documentation and any submitted links that are supposed to be public.
