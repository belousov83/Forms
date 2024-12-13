from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from tools.validate_form import find_matching_form
from db import forms
from schemas.form import ExampleForm

router = APIRouter()


@router.get("/", include_in_schema=False)
async def index():
    return RedirectResponse("/docs")


@router.post(
    "/get_form",
    summary="Поиск среди шаблонов форм",
    description="Выводит имя шаблона, если шаблон найден по совпадениям"
                "если нет, тогда выводит словарь, где ключ - имя поля, а значение - тип данных"
                "в этом поле",
    response_model=ExampleForm
)
async def get_form(request: Request):
    """
    Поддерживаются типы:
    - **email**
    - **телефон**
    - **дата**
    - **текст**
    """
    form_data = await request.form()
    data = {**form_data}
    or_conditions = []
    for field_name in data.keys():
        or_conditions.append(
            {field_name: {'$exists': True}}
        )

    # Ищем все совпадения по названиям полей
    cursor = forms.find(
        {
            "$or": or_conditions
        }
    )
    results = [obj async for obj in cursor]
    data = await find_matching_form(results, data)
    return data


@router.get(
    "/forms",
    summary='Список всех шаблонов форм'
)
async def get_all_forms() -> list[dict]:
    cursor = forms.find()
    form_list = await cursor.to_list(length=None)
    forms_without_id = [
        {k: v for k, v in form.items() if k != '_id'} for form in form_list
    ]
    return forms_without_id
