#!/bin/bash

env=${1:-local}
docker_hub_uri='747334718413.dkr.ecr.us-east-1.amazonaws.com'

function tag_push_docker_image(){
    docker tag $1 $docker_hub_uri/$2:$3
    docker push $docker_hub_uri/$2:$3
}

function create_lambda_docker_image() {
    lambda_name=$1
    (
        cd ../src/$lambda_name
        TAG_ID=$(git rev-parse HEAD | cut -c1-15)
        IMAGE_ID=$(docker build --platform linux/amd64 -t $lambda_name:$TAG_ID --quiet . --no-cache | cut -d':' -f2)
        echo $IMAGE_ID
        tag_push_docker_image $IMAGE_ID $lambda_name $TAG_ID
    )
}

# List of lambda names
lambda_names=("book-worker" "book-service" "publishing-service")

# Login to AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $docker_hub_uri

# Call the create_lambda_bucket function for each lambda
for lambda_name in "${lambda_names[@]}"
do
    create_lambda_docker_image $lambda_name
done
