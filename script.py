import asyncio
from httpx import AsyncClient


async def make_requests():
    async with AsyncClient() as client:
        # Тест 1
        response = await client.post('http://localhost:8000/get_form', data={'email': 'nw007@ya.ru'})
        data = response.json()
        print('Test 1:')
        print(data)
        print('Status Code:', response.status_code)
        print()

        # Тест 2
        response = await client.post('http://localhost:8000/get_form', data={
            'lead_email': 'tester@ya.ru',
            'user_phone': '+7 920 292 42 62',
        })
        data = response.json()
        print('Test 2:')
        print(data)
        print('Status Code:', response.status_code)
        print()

        # Тест 3
        response = await client.post(
            'http://localhost:8000/get_form',
            data={
                'f_name11': '13.12.2024',
                'f_name22': 'text',
            },
        )
        data = response.json()
        print("Test 3:")
        print(data)
        print('Status Code:', response.status_code)
        print()

        # Тест 4
        response = await client.post(
            'http://localhost:8000/get_form',
            data={
                'user_email': 'nw007@ya.ru',
                'user_text': 'hello',
                'user_date': '17.05.1983',
            },
        )
        data = response.json()
        print("Test 4:")
        print(data)
        print('Status Code:', response.status_code)
        print()

if __name__ == "__main__":
    asyncio.run(make_requests())
