from faker import Faker
from models import Contact
from db_connect import connection
from broker_connect import channel

def fake_contacts():
    fake = Faker()
    contacts = []
    for _ in range(50):
        full_name = fake.name()
        email = full_name.lower().replace(" ", "_") + '@gmail.com'
        contact = Contact(
            full_name = full_name,
            email = email,
        )
        contact.save()
        contacts.append(contact)
    
    return contacts

def contacts_to_rmq(contacts):
    channel.queue_declare(queue='email')

    for contact in contacts:
        channel.basic_publish(exchange='', routing_key='email', body=str(contact.id).encode())

    channel.close()

if __name__ == '__main__':
    connection()
    Contact.objects().delete()
    contacts = fake_contacts()
    contacts_to_rmq(contacts)

    