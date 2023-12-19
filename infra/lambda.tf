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
  image_uri     = "${aws_ecr_repository.docker_registry.repository_url}:${each.key}"

  tags = {
    Name : each.key,
    Type : "Lambda"
  }
}
