from confluent_kafka import Consumer, KafkaError
import redis

bootstrap_servers = 'localhost:9092'
topic = 'topic1'

conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my_consumer_group',  
    'auto.offset.reset': 'earliest'   
}

consumer = Consumer(conf)

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

consumer.subscribe([topic])

try:
    while True:
        message = consumer.poll(timeout=1.0)

        if message is None:
            continue
        
        if message.error():
            if message.error().code() == KafkaError._PARTITION_EOF:
                print('%% %s [%d] reached end at offset %d\n' %
                      (message.topic(), message.partition(), message.offset()))
            elif message.error():
                raise KafkaException(message.error())
        else:
            decoded_message = message.value().decode('utf-8')
            print(f"Received message: {decoded_message}")

            # Store message in Redis
            r.rpush(topic, decoded_message)
            print(f"Message stored in Redis: {decoded_message}")

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
