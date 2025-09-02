terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.94.1"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

resource "aws_security_group" "my_firewall2" {
    name = "firewall2"
    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}
resource "aws_instance" "myec2" {
    ami = "ami-0e35ddab05955cf57"
    instance_type = "t2.micro"
    vpc_security_group_ids = [aws_security_group.my_firewall2.id]
    key_name = "atharv"
    root_block_device {
        volume_size = 10
        volume_type = "gp3"
    }
    tags = {
        Name=var.instance_name
    }
    user_data = <<-EOF
                #!/bin/bash
                sudo apt update -y
                sudo apt install apache2 -y
                sudo apt install wget -y
                sudo apt install unzip -y
                sudo wget https://www.tooplate.com/zip-templates/2135_mini_finance.zip
                unzip 2135_mini_finance.zip
                sudo cp -r 2135_mini_finance/* /var/www/html
                sudo systemctl start apache2
                sudo systemctl enable apache2
            EOF
}