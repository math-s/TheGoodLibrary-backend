resource "aws_ecr_repository" "docker_registry" {
  name                 = "good-library"
  image_tag_mutability = "IMMUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

output "aws_ecr_repository_url" {
  value = aws_ecr_repository.docker_registry.repository_url
}
