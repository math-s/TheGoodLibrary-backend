FROM python:3.11-slim AS BASE

COPY src/ /app
WORKDIR /app

FROM BASE AS QUALITY
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
RUN python3 -m coverage run --source=. --omit=tests/* -m unittest discover
RUN coverage report --show-missing


FROM BASE AS PROD
RUN rm -Rf /app/tests
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
