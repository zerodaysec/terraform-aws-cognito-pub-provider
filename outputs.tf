output "topic_arn" {
  description = "The ARN of the SNS topic. Notifications will be sent to this."
  value       = aws_sns_topic.sns_topic.arn
}