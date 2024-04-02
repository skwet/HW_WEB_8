from models import Contact
from db_connect import connection
from broker_connect import channel

connection()

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects.get(id=contact_id)
    
    if contact:
        contact.message_sent = True
        print(f'Email sending to {contact.email}')
        contact.save()
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
def main():
    channel.queue_declare(queue='email')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='email', on_message_callback=callback)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()

if __name__ == '__main__':
    main()
