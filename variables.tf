variable "cust" {
  type        = string
  description = "A unique identifier to differentiate this deployment."
}

variable "app" {
  type        = string
  description = "A unique identifier to differentiate this deployment."
}

variable "env" {
  type        = string
  description = "Environment name, such as 'dev', 'Test', or 'Production'"
}

variable "topic_name" {
  type        = string
  description = "The name of the SNS topic to be created."
}

variable "service_identifiers" {
  type        = list(string)
  description = "List of services allowed to publish to this SNS topic."
}