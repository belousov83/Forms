import json
import os
from pathlib import Path

import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db = client.form
forms: motor.motor_asyncio.AsyncIOMotorCollection = db.get_collection("forms")


async def create_data() -> None:
    """Загрузка данных в БД"""
    current_path = Path(os.path.dirname(os.path.realpath(__file__)))
    json_path = os.path.join(current_path, 'fixtures.json')

    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)

    for obj in data:
        await forms.insert_one(obj)
