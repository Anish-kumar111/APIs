 # amqps://lhrmlkwo:tQd4EApZb9qAHGUgRcbFkTU6mp_ZbRGI@puffin.rmq2.cloudamqp.com/lhrmlkwo

from pickle import TRUE
import pika ,json, os , django
os.environ.setdefault("DJANGO_STTINGS_MODULE","admin.settings")
django.setup()
# from products.models import Product

from products.models import Product
params = pika.URLParameters('amqps://lhrmlkwo:tQd4EApZb9qAHGUgRcbFkTU6mp_ZbRGI@puffin.rmq2.cloudamqp.com/lhrmlkwo')


connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch,method,properties,body):
   print('received in admin')
   id = json.loads(body)
   print(id)
   product = Product.objects.get(id=id)
   product.likes = product.likes + 1
   product.save()
   print('Product likes increased! ')


   

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started consuming')
channel.start_consuming()
channel.close()