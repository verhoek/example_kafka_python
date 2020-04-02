Docker Kafka Python Example
=======================

This is a minimal example that runs [Kafka](http://www.confluent.io/)
and two small Python programs, all in a single Docker environment.
The `publisher` program publishes messages into Kafka;
the `consumer` program prints every message it recevies to
its stdout.

Once you've brought it all up, you should see the publisher and
consumer printing messages on their stdout.
