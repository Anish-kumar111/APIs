 # amqps://lhrmlkwo:tQd4EApZb9qAHGUgRcbFkTU6mp_ZbRGI@puffin.rmq2.cloudamqp.com/lhrmlkwo

import pika ,json

# from products.models import Product

from main import app,db,Product
params = pika.URLParameters('amqps://lhrmlkwo:tQd4EApZb9qAHGUgRcbFkTU6mp_ZbRGI@puffin.rmq2.cloudamqp.com/lhrmlkwo')


connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='flask')


def callback(ch,method,properties,body):
   print('received in flask db')
   data = json.loads(body)
   print(data)
   

 


channel.basic_consume(queue='flask', on_message_callback=callback, auto_ack=True)

print('started consuming')
channel.start_consuming()
channel.close()