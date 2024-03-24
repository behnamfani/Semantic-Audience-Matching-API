FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt uvicorn
WORKDIR /app/scripts
CMD ["uvicorn", "API:app", "--reload", "--host", "0.0.0.0"]
