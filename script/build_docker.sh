#!/bin/bash

env=${1:-local}


if [ $env == "local" ]; then
    docker_hub_uri="localhost:5000"
else
    aws_account_id=$AWS_ACCOUNT_ID # get account id from env var
    aws_region=$AWS_REGION # get region from env var
    docker_hub_uri="$aws_account_id.dkr.ecr.$aws_region.amazonaws.com"
fi 


function create_lambda_docker_image() {
    lambda_name=$1
    (
        cd ../src/$lambda_name
        TAG_ID=$(git rev-parse HEAD | cut -c1-15)
        docker build --platform linux/amd64 -t $lambda_name:$TAG_ID . --no-cache
        docker tag $lambda_name:$TAG_ID $lambda_name:latest
        docker push $docker_hub_uri/$lambda_name:$TAG_ID 
    )
}

# List of lambda names
lambda_names=("book-worker" "book-service" "publishing-service")

# Call the create_lambda_bucket function for each lambda
for lambda_name in "${lambda_names[@]}"
do
    create_lambda_docker_image $lambda_name
done
