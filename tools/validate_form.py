import re
from collections import defaultdict

DATE_REGEX = r"^([0-3][0-9].[0-1][0-9].[0-9]{4}|[0-9]{4}-[0-1][0-9]-[0-3][0-9])$"
PHONE_REGEX = r"^(\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}|\+7\d{10})$"
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$"


async def get_field_type(value: str) -> str:
    """Определяем тип поля на основе его значения"""
    if re.match(DATE_REGEX, value):
        return "date"
    elif re.match(PHONE_REGEX, value):
        return "phone"
    elif re.match(EMAIL_REGEX, value):
        return "email"
    else:
        return "text"


async def find_matching_form(results: list[dict], data: dict) -> dict:
    """
    Поиск среди шаблонов форм по совпадению имен полей и типу значения
    Если совпадений несколько возвращается шаблон с макс. кол-вом совпадений
    Если совпадений не найдено, возвращаются валидированные данные
    """
    matching_forms = defaultdict(int)
    for result in results:
        match_fields = set(result.keys() & data.keys())
        for field in match_fields:
            field_type_db = result.get(field)
            field_type_prediction = await get_field_type(data.get(field))
            if field_type_db == field_type_prediction:
                field_name = result.get('name')
                matching_forms[field_name] += 1
    if matching_forms:
        field_name = max(matching_forms, key=matching_forms.get)
        return {'name': field_name}
    for key, value in data.items():
        data[key] = await get_field_type(value)
    return data
