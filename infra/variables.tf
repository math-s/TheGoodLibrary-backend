variable "access_key" {
  default = "mock_access_key"
}
variable "secret_key" {
  default = "mock_secret_key"
}
variable "aws_region" {
  default = "us-east-1"
}

variable "aws_endpoint" {
  default = null
}

variable "skip_credentials_validation" {
  default = false
}

variable "skip_metadata_api_check" {
  default = false
}

variable "skip_requesting_account_id" {
  default = false
}

variable "docker_host_url" {
  default = "matheusandrade4dev"
}

variable "docker_image_tag" {
  default = "latest"
}
