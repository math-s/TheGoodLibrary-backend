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
