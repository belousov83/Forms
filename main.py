from fastapi import FastAPI

from api.form import router
from db import forms, create_data

app = FastAPI(
    title='Определение форм',
    description='Web-приложение для определения заполненных форм',
)

app.include_router(router)


@app.on_event("startup")
async def app_init() -> None:
    count_forms = await forms.count_documents({})

    if count_forms > 0:
        return
    await create_data()
