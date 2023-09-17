# output resources
output "sqs_queue_url" {
  value = aws_sqs_queue.process-book-queue.id
}

output "lambda-book-service-uri" {
  value = aws_lambda_function.book-service.invoke_arn
}

output "lambda-book-worker-uri" {
  value = aws_lambda_function.book-worker.invoke_arn
}

output "lambda-publishing-service-uri" {
  value = aws_lambda_function.publishing-service.invoke_arn
}