resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "My_Ways"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "Name"
    type = "S"
  }

  attribute {
    name = "description"
    type = "S"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  tags = {
    Name        = "myways"
    Environment = "production"
  }
}