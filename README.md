# Lambda_DynamoDB_visitor_counter
Lambda function coupled with a DynamoDB table serving as a visitor counter

This Lambda function is triggered by API gateway. In each run, it increases the value in the DynamoDB table by 1 and then returns the current value.

DynamoDB table layout:<br>
**table name:** visitor_counter<br>
**primary key:** type (String)<br>
**column:** count (Number)
