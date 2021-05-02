module "lambda_function-create" {
    source = "terraform-aws-modules/lambda/aws"
    function_name = "myways-create"
    description   = "Function for creating dynamodb item"
    handler       = "create.lambda_handler"
    runtime       = "python3.8"
    source_path = "lambda/create.py"
    attach_policies = true
    create_current_version_allowed_triggers = false
    policies = [
        "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",
        "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
    ]
    number_of_policies = 1
    tags = {
        Name = "create"
    }
}
module "lambda_function-search" {
    source = "terraform-aws-modules/lambda/aws"
    function_name = "myways-search"
    description   = "Function for searching"
    handler       = "search.lambda_handler"
    runtime       = "python3.8"
    source_path = "lambda/search.py"
    attach_policies = true
    create_current_version_allowed_triggers = false
    policies = [
        "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",
        "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
    ]
    number_of_policies = 1
    tags = {
        Name = "search"
    }
}
module "lambda_function-delete" {
    source = "terraform-aws-modules/lambda/aws"
    function_name = "myways-delete"
    description   = "Function for deleting dynamodb item"
    handler       = "delete.lambda_handler"
    runtime       = "python3.8"
    source_path = "lambda/delete.py"
    attach_policies = true
    create_current_version_allowed_triggers = false
    policies = [
        "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",
        "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
    ]
    number_of_policies = 1
    tags = {
        Name = "delete"
    }
}
module "dynamodb" {
    source = "./modules/dynamodb"
    
}
module "ec2" {
    source = "./modules/ec2"
}