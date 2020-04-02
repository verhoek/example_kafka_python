#!/usr/bin/env python

import time
from confluent_kafka import Producer


p = Producer({'bootstrap.servers': 'kafka:19092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print(f'Message {msg.value().decode()} delivered to topic {msg.topic()} partition [{msg.partition()}]')


i = 0
while True:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    if i % 10000 == 0:
        time.sleep(10)

    i = i+1
    msg = f'message {i}'
    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('mytopic', msg.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()