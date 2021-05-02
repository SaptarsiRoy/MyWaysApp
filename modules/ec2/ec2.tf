
data "aws_vpc" "default_vpc" {
  default = true
}

data "aws_subnet_ids" "default_subnet" {
  vpc_id = data.aws_vpc.default_vpc.id
}

//Creating Variable for AMI_ID
variable "ami_id" {
  type    = string
  default = "ami-0a9d27a9f4f5c0efc"
}

//Creating Variable for AMI_Type
variable "ami_type" {
  type    = string
  default = "t2.micro"
}


//Creating Key
resource "tls_private_key" "tls_key" {
  algorithm = "RSA"
}


//Generating Key-Value Pair
resource "aws_key_pair" "generated_key" {
  key_name   = "myways-key"
  public_key = tls_private_key.tls_key.public_key_openssh

  depends_on = [
    tls_private_key.tls_key
  ]
}


//Saving Private Key PEM File
resource "local_file" "key-file" {
  content  = tls_private_key.tls_key.private_key_pem
  filename = "./playbooks/myways.pem"

  depends_on = [
    tls_private_key.tls_key
  ]
}


//Creating Security Group for ec2 instance
resource "aws_security_group" "web-SG" {
  name        = "WEB-SG"
  description = "Web Environment Security Group"
  vpc_id      = data.aws_vpc.default_vpc.id


  //Adding Rules to Security Group
  ingress {
    description = "SSH Rule"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }


  ingress {
    description = "HTTP Rule"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
    protocol    = "-1"
  }
  depends_on = [tls_private_key.tls_key]
}

//Launching First ec2 instance
resource "aws_instance" "web_instance" {
  ami             = var.ami_id
  instance_type   = var.ami_type
  key_name        = aws_key_pair.generated_key.key_name
  security_groups = [aws_security_group.web-SG.name]

  //Labelling the Instance
  tags = {
    Name = "webos"
    env  = "Production"
  }
}
