from pydantic import condecimal, BaseModel


class DecimalToFloat(BaseModel):
    original_price: float
    discount: float


def calculate_discount(original_price: condecimal(max_digits=10, decimal_places=2), discount: float)->condecimal(max_digits=10, decimal_places=10):
    data = DecimalToFloat(original_price=original_price, discount=discount)
    if int(discount) == 0:
        return original_price
    discounted_price = data.original_price - ((data.original_price * data.discount) / 100)
    return discounted_price