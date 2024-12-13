from pydantic import BaseModel, ConfigDict


class ExampleForm(BaseModel):
    model_config = ConfigDict(
        extra="allow",
        json_schema_extra={
            "example": {
                "field_name_1": "phone",
                "field_name_2": "date",
            }
        },
    )
