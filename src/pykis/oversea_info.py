from enum import Enum, auto
import math


class Country(Enum):
    USA = 0
    HK = 1
    JP = 2
    CN_SHA = 3
    CN_SZX = 4
    VN = 5

    @classmethod
    def get_all(cls):
        return [e.name for e in cls]


class Market(Enum):
    NASD = 0
    NYSE = 1
    AMEX = 2

    SEHK = 10

    TKSE = 20

    SHAA = 30
    SZAA = 40

    HASE = 50
    VNSE = 51

    @classmethod
    def get_all(cls):
        return [e.name for e in cls]


def get_country_by_market_code(code):
    val = Market[code].value
    country_val = Market[code].value // 10
    return Country(country_val).name