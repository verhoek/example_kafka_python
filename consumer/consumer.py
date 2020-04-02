# #!/usr/bin/env python

from confluent_kafka import Consumer, KafkaError

def on_error(kafka_error):
    print(kafka_error)

c = Consumer({
    'bootstrap.servers': 'kafka:19092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest',
    'error_cb': on_error,
})



c.subscribe(['mytopic'])

while True:
    print('polling')
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()