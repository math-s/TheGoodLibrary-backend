FROM python:3.11-slim AS base

COPY src /app
WORKDIR /app

FROM base AS quality
COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
RUN python3 -m coverage run --source=. --omit=tests/* -m unittest discover
RUN coverage report --show-missing


FROM base AS prod
RUN rm -Rf /app/tests
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
