# 1
FROM python:3.7

# 2
RUN pip install Flask==2.0.1 gunicorn==20.1.0 firebase-admin==5.0.2 PyJWT==2.1.0 pyrebase==3.0.18

# 3
COPY src/ /app
WORKDIR /app

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app