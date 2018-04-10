#!/usr/bin/env python

""" emit_log.py

- Author: Anthony Panisales

- This program emits log messages and is meant to be used alongside
  receive_logs.py, as part of a simple logging system. In this logging
  system, every running copy of the receiver program (receive_logs.py)
  will get the messages sent by the sender program (emit_log.py). 
  Essentially, published log messages are going to be broadcast to all
  the receivers.

- The default message is "info: Hello World!"

- Example usage: python emit_log.py [message]

- Code inspired by this source:
		https://www.rabbitmq.com/tutorials/tutorial-three-python.html

"""

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()