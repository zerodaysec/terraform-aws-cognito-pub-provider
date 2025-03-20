data "aws_region" "current" {}

locals {
  common_tags = {
    Customer    = var.cust
    Application = var.app
    Environment = var.env
  }
}

resource "aws_sns_topic" "sns_topic" {
  name = var.topic_name

  tags = local.common_tags
}
