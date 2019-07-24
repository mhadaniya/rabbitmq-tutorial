#!/user/bin/end python

import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', port='5672'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello',
                    auto_ack=True,
                    on_message_callback=callback)

print(" [*] Waiting for messages. To exist press CTRL+C'")
channel.start_consuming()
