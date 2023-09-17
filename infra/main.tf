provider "aws" {
  region                      = var.aws_region
  access_key                  = var.access_key
  secret_key                  = var.secret_key
  skip_credentials_validation = var.skip_credentials_validation
  skip_metadata_api_check     = var.skip_metadata_api_check
  skip_requesting_account_id  = var.skip_requesting_account_id

}

# create S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-bucket"
}

# create SQS queue
resource "aws_sqs_queue" "process-book-queue" {
  name = "process-book-queue"
}

# create Lambda function
resource "aws_lambda_function" "book-service" {
  function_name = "book-service"
  handler       = "index.handler"
  runtime       = "python3.11"
  role          = aws_iam_role.my_role.arn
  image_uri     = "${var.docker_host_url}/book-service:${var.docker_image_tag}"
}

resource "aws_lambda_function" "book-worker" {
  function_name = "book-worker"
  handler       = "index.handler"
  runtime       = "python3.11"
  role          = aws_iam_role.my_role.arn
  image_uri     = "${var.docker_host_url}/book-worker:${var.docker_image_tag}"
}

resource "aws_lambda_function" "publishing-service" {
  function_name = "publishing-service"
  handler       = "index.handler"
  runtime       = "python3.11"
  role          = aws_iam_role.my_role.arn
  image_uri     = "${var.docker_host_url}/publishing-service:${var.docker_image_tag}"
}

# create IAM role for Lambda function
resource "aws_iam_role" "my_role" {
  name = "my-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# create IAM policy for Lambda function
resource "aws_iam_policy" "my_policy" {
  name = "my-policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "sqs:SendMessage",
          "dynamodb:GetItem",
          "dynamodb:PutItem"
        ]
        Effect = "Allow"
        Resource = [
          aws_sqs_queue.process-book-queue.arn,
        ]
      }
    ]
  })
}