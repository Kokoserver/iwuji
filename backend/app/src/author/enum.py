import enum


class AuthorTitle(str, enum.Enum):
    MR = "mr"
    MRS = "mrs"
    DR = "dr"
    MISS = "miss"
    PROF = "prof"