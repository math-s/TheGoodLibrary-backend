FROM public.ecr.aws/lambda/python:3.11 AS base

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Copy function code
COPY app/ ${LAMBDA_TASK_ROOT}/app

# Install the specified packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM base as testing

COPY tests/ ${LAMBDA_TASK_ROOT}/tests

COPY requirements-dev.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements-dev.txt
RUN pip install pytest

FROM base as final

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]