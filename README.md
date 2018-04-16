# cs336-AMQP

- These two programs are part of a simple logging system, and are meant
  to be used alongside one another. In this logging system, every running 
  copy of the receiver program (receive_logs.py) will get the messages sent 
  by the sender program (emit_log.py). Essentially, published log messages 
  are going to be broadcast to all the receivers.
  
- Requires installing RabbitMQ and running it on "localhost" on standard
  port(5672).
  
- Code inspired by this source:
	https://www.rabbitmq.com/tutorials/tutorial-three-python.html
