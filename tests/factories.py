import factory
from faker import Faker
from myapp.models import Product

fake = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n + 1)
    name = factory.LazyAttribute(lambda _: fake.word())
    category = factory.LazyAttribute(lambda _: fake.word())
    price = factory.LazyAttribute(lambda _: round(fake.pyfloat(min_value=1, max_value=1000), 2))
    available = factory.LazyAttribute(lambda _: fake.boolean())
