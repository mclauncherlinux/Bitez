FROM python:3.6
ADD . ./app
WORKDIR /app
RUN pip install requirements.txt
EXPOSE 8000
CMD ["gunicorn", "main:app"]
