# output resources
output "sqs_queue_url" {
  value = aws_sqs_queue.process-book-queue.id
}

output "lambdas_arns" {
  description = "Lambdas ARNs"
  value       = [for instance in aws_lambda_function.lambdas : instance.invoke_arn]
}
