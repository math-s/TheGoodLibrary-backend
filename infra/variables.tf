variable "access_key" {
  default = "mock_access_key"
}

variable "secret_key" {
  default = "mock_secret_key"
}

variable "account_id" {
  default = "000000000000"
}

variable "aws_region" {
  default = "us-east-1"
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

variable "docker_image_tag" {
  default = "4c03f4e56e58c50"
}

variable "docker_host_url" {
  default = "747334718413.dkr.ecr.us-east-1.amazonaws.com"
}

variable "lambdas" {
  type    = list(string)
  default = ["book-service", "book-worker", "publishing-service"]
}
