# 🦉 Video Quiz Generator
This is a simple web app that let you generate quizzes❓ from given video to check your understanding after watching the video. This app is a combination of [🔥 Streamlit UI](https://streamlit.io/) + [⚡️ FastAPI ](https://fastapi.tiangolo.com/) + [💬 Faster Whisper](https://github.com/guillaumekln/faster-whisper) + 🦜 Large Language Model (LLM) API ([Google Bard](https://github.com/dsdanielpark/Bard-API), [OpenAIGPT](https://platform.openai.com/account/api-keys)).

## 1. Technical
The application is divided into 2 separate parts: frontend and backend. So you need to run both at the same time.
- Frontend: Using Streamlit.
- Backend: Using FastAPI.
    - Speech recognition: Using Faster Whisper, a reimplementation of OpenAI's Whisper, with faster inference and approximate accuracy but using less memory.
    - Quizzes generation: Using available APIs. Note that bard's API has not been released yet. So we use an [Bard-API](https://github.com/dsdanielpark/Bard-API) ("unofficial python package that returns response of Google Bard through cookie value").


## 2. Setup
First, you need rename the `.env.example` files in `fastapi` and `streamlit` folder to `.env`.

Install requirements:
```
pip install -r fastapi/requirements.txt
pip install -r streamlit/requirements.txt
```

### Backend
```
python fastapi/src/main.py
```

### Frontend
```
python streamlit/src/main.py
```

### Notes:
- This repo is built and tested on python `3.10`.
- Faster Whisper model is being run on CPU with Float32. You can change the config in file `fastapi/src/speech_rec/service.py` (See more config in the [Faster Whisper repo](https://github.com/guillaumekln/faster-whisper)).
- Quizzes generated with OpenAPI GPT is better and more consistent between different times than Bard. But due to OpenAI API Key issue, this app has not been tested much on OpenAI config. So if you find any bugs while testing with your API Key, please create an issue. We really appreciate that.
- Currently, I am only testing on English language. If there are any problems when you try with another language, don't hesitate to create an issue.
- Note that you need to double-check the generated quizzes.

## 3. Docker
This repo provides quickstart support with Docker (remember to rename the `.env.example` file first):
```
docker compose up -d
```
Go to http://localhost:8501 and enjoy 😎

## 4. Usage
[video](https://drive.google.com/file/d/1_RnZG-8mxDWCPZokdJVrKJoXSALxp3HU/view?usp=sharing)