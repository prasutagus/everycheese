import pytest

pytestmark = pytest.mark.django_db

from everycheese.cheeses.models import Cheese

from .factories import CheeseFactory

def test___str__():
    cheese = CheeseFactory()

    assert cheese.__str__() == cheese.name

