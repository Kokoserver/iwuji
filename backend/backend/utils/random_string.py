from datetime import datetime
import random
import string
import uuid


def random_str(size=7) -> str:
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))
    return ran


def generate_orderId() -> str:
    return f"IW-{random_str(10)}"


def generate_pay_ref() -> str:
    return f"IW-{random_str(15)}"


def generate_uuid(make_string: bool = False):
    return uuid.uuid4 if not make_string else uuid.uuid4().hex
