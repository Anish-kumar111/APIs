# amqps://lhrmlkwo:tQd4EApZb9qAHGUgRcbFkTU6mp_ZbRGI@puffin.rmq2.cloudamqp.com/lhrmlkwo
import pika , json
params = pika.URLParameters('amqps://lhrmlkwo:tQd4EApZb9qAHGUgRcbFkTU6mp_ZbRGI@puffin.rmq2.cloudamqp.com/lhrmlkwo')


connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body =json.dumps(body), properties=properties)