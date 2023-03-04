import strawberry
from strawberry import auto
from typing import List
from ..models import Fruit, Color
import strawberry_django


@strawberry.django.type(Fruit)
class FruitType:
    id: auto
    name: auto
    color: 'ColorType'

@strawberry.django.type(Color)
class ColorType:
    id: auto
    name: auto
    fruits: List[FruitType]


@strawberry_django.input(Fruit)
class Fruitinput:
    id: auto
    name: auto
    color: auto

@strawberry_django.input(Color)
class Colorinput:
    id: auto
    name: auto
    fruits: auto
