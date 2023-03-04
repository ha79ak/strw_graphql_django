from typing import List

import strawberry

import strawberry_django
import strawberry_django.auth as auth
from strawberry_django import mutations


from .str_graphene_types import (
    Fruit,
    FruitType,
    Color,
    ColorType
)

@strawberry.type
class Mutation:
    createFruit: Fruit = mutations.create()
    createColor: Color = mutations.create()
    
