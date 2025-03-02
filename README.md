# Streaming Setup and Execution Guide

## Kafka Server Setup

### 1. Start ZooKeeper Server
Navigate to the Kafka directory and execute the following command:
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### 2. Start Kafka Server
In the Kafka directory, execute:
```bash
bin/kafka-server-start.sh config/server.properties
```

## Redis Server Setup

### 1. Start Redis Server
Run the following command from any location:
```bash
sudo systemctl start redis
```

### 2. Check Redis Server Status
To verify the server is running:
```bash
sudo systemctl status redis
```

### 3. Connect to Redis CLI
Use the default port 6380:
```bash
redis-cli
```

### 4. Open RedisInsight
Launch RedisInsight to visualize and manage your Redis database.

### 5. Stop Redis Server
To stop the Redis server:
```bash
sudo systemctl stop redis
```
Alternatively, you can shut it down via CLI:
```bash
redis-cli shutdown
```

## Producer and Consumer Scripts

### 1. Run the Producer File
Execute the producer script:
```bash
python3 "/home/jayasurya/Documents/stream_process/producer_kafka.py"
```

### 2. Run the Consumer File
Execute the consumer script:
```bash
python3 "/home/jayasurya/Documents/stream_process/consumer_kafka.py"
```

## Viewing Streamed Data
To see the streamed data in the database, ensure both producer and consumer are running, and verify the data flow using your configured database interface.

---
