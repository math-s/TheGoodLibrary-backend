# output resources
output "s3_bucket_name" {
  value = aws_s3_bucket.my_bucket.id
}

output "sqs_queue_url" {
  value = aws_sqs_queue.process-book-queue.id
}
