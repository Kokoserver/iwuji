import enum


class CartStatus(str, enum.Enum):
    ordered = "ordered"
    abandoned = "abandoned"
