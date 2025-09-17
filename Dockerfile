# Dockerfile
FROM python:3.12-slim
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "main.py", "--server.port=7860", "--server.address=0.0.0.0"]
