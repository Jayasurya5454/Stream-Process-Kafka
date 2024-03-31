import requests
from confluent_kafka import Producer
import uuid
import schedule
import time

bootstrap_servers = 'localhost:9092'
topic1 = 'topic1'


conf = {
    'bootstrap.servers': bootstrap_servers,
       }


producer = Producer(conf)

def delivery_report(err, msg):
    """Callback function for message delivery report."""
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def send_to_kafka(user_data):
    """Extract name and last name from user data, combine with additional data, and send to Kafka."""
    
    name = user_data['name']['first']
    last_name = user_data['name']['last']
    formatted_data = f"{name} {last_name}"
    
    
    additional_data = {
        'id': uuid.uuid4(),
        'gender': user_data['gender'],
        'address': f"{user_data['location']['street']['number']} {user_data['location']['street']['name']}, "
                   f"{user_data['location']['city']}, {user_data['location']['state']}, {user_data['location']['country']}",
        'post_code': user_data['location']['postcode'],
        'email': user_data['email'],
        'username': user_data['login']['username'],
        'dob': user_data['dob']['date'],
        'registered_date': user_data['registered']['date'],
        'phone': user_data['phone'],
        'picture': user_data['picture']['medium']
    }
    
    
    combined_data = {**additional_data, 'name': formatted_data}
    
    
    producer.produce(topic1, value=str(combined_data).encode('utf-8'), callback=delivery_report)

    
    producer.flush()

def fetch_and_send_to_kafka():

    
    api_url = "https://randomuser.me/api/"

    
    response = requests.get(api_url)

    
    if response.status_code == 200:
        
        data = response.json()

        user_info = data['results'][0]

        send_to_kafka(user_info)
    else:
        print("Error:", response.status_code)

schedule.every(5).seconds.do(fetch_and_send_to_kafka)

while True:
    schedule.run_pending()
    time.sleep(1) 
