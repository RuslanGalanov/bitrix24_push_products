from pydantic import BaseModel


stops = [
    'Лист1',
    'Лист3',
    'Лист2',
    'ФИЛЬТРЫ',
    'SANIFLOOR+',
    'SANICUBIC R2 (Dom. - Coll.)'
]


class Spare(BaseModel):
    refference: str
    position: list[str] | None
    ru_name: str
    en_name: str
    price: int | None
    group: list[str]