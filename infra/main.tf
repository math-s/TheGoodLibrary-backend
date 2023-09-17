provider "aws" {
  region                      = var.aws_region
  access_key                  = var.access_key
  secret_key                  = var.secret_key
  skip_credentials_validation = var.skip_credentials_validation
  skip_metadata_api_check     = var.skip_metadata_api_check
  skip_requesting_account_id  = var.skip_requesting_account_id

}

# create SQS queue
resource "aws_sqs_queue" "process-book-queue" {
  name = "process-book-queue"
}

# create Lambda function
resource "aws_lambda_function" "book-service" {
  function_name = "book-service"
  package_type  = "Image"
  role          = aws_iam_role.my_role.arn
  handler       = "index.handler"
  runtime       = "python3.11"
  image_uri     = "747334718413.dkr.ecr.us-east-1.amazonaws.com/book-service:9933af6e8c05fbf"
}

resource "aws_lambda_function" "book-worker" {
  function_name = "book-worker"
  package_type  = "Image"
  role          = aws_iam_role.my_role.arn
  handler       = "index.handler"
  runtime       = "python3.11"
  image_uri     = "747334718413.dkr.ecr.us-east-1.amazonaws.com/book-worker:9933af6e8c05fbf"
}

resource "aws_lambda_function" "publishing-service" {
  function_name = "publishing-service"
  package_type  = "Image"
  role          = aws_iam_role.my_role.arn
  handler       = "index.handler"
  runtime       = "python3.11"
  image_uri     = "747334718413.dkr.ecr.us-east-1.amazonaws.com/publishing-service:9933af6e8c05fbf"
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
          "dynamodb:PutItem",
          "dynamodb:UpdateItem",
          "dynamodb:DeleteItem",
        ]
        Effect = "Allow"
        Resource = [
          aws_sqs_queue.process-book-queue.arn,
        ]
      }
    ]
  })
}