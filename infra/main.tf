terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.16.1"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region                      = var.aws_region
  access_key                  = var.access_key
  secret_key                  = var.secret_key
  skip_credentials_validation = var.skip_credentials_validation
  skip_metadata_api_check     = var.skip_metadata_api_check
  skip_requesting_account_id  = var.skip_requesting_account_id
}


resource "aws_iam_role" "lambda-role" {
  name = "lambda-role"
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

resource "aws_lambda_function" "lambdas" {
  for_each      = toset(var.lambdas)
  function_name = each.key
  package_type  = "Image"
  role          = aws_iam_role.lambda-role.arn
  image_uri     = "${var.account_id}.dkr.ecr.${var.aws_region}.amazonaws.com/${each.key}:${var.docker_image_tag}"

  tags = {
    Name : each.key,
    Version : var.docker_image_tag,
    Type : "Lambda"
  }
}
