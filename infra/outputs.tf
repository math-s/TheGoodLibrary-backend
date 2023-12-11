

output "lambdas_arns" {
  description = "Lambdas ARNs"
  value       = [for instance in aws_lambda_function.lambdas : instance.invoke_arn]
}
