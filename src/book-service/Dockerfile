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

RUN pip install -r requirements-dev.txt

RUN coverage run -m pytest -vvs --junitxml=/report.xml
RUN coverage xml -o /coverage.xml -i

FROM base as final

COPY --from=testing /coverage.xml /
COPY --from=testing /report.xml /

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]