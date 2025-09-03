from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import asyncio
import os


KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")


async def get_producer():
    p = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP)
    await p.start()
    return p


async def get_consumer(topic, group_id="gesture-ai-group"):
    c = AIOKafkaConsumer(topic, bootstrap_servers=KAFKA_BOOTSTRAP, group_id=group_id)
    await c.start()
    return c
