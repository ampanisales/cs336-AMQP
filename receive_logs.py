#!/usr/bin/env python

""" receive_logs.py

- Author: Anthony Panisales

- This program receives log messages and prints them. It is meant to
  be used alongside emit_log.py as part of a simple logging system.
  In this logging system, every running copy of the receiver program
  (receive_logs.py) will get the messages sent by the sender program 
  (emit_log.py). Essentially, published log messages are going to be 
  broadcast to all the receivers.

- Example usage: python receive_logs.py

- Code inspired by this source:
		https://www.rabbitmq.com/tutorials/tutorial-three-python.html

"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

try:
	channel.start_consuming()
except KeyboardInterrupt:
	print(" Exiting...")
