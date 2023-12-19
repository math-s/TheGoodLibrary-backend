resource "aws_dynamodb_table" "authors" {
  name         = "Authors"
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "name"

  attribute {
    name = "name"
    type = "S"
  }

  attribute {
    name = "country"
    type = "S"
  }

  global_secondary_index {
    name            = "GSI1"
    hash_key        = "name"
    range_key       = "country"
    projection_type = "ALL"
  }

  tags = {
    Name = "Authors"
  }
}
