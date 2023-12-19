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

variable "lambdas" {
  type    = list(string)
  default = ["good-library-api"]
}
