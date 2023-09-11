from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict

from pydantic import BaseModel

DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
NEVER = datetime(year=3000, month=1, day=1, tzinfo=timezone.utc)


def convert_datetime(d: datetime):
    return d.strftime(DATE_FORMAT)


class ConvertModel(BaseModel):
    class Config:
        json_encoders = {datetime: convert_datetime}


class WalletType(str, Enum):
    SPOT = 'SPOT'
    MARGIN_CROSS = 'CROSS_MARGIN'
    MARGIN_ISOLATED = 'ISOLATED_MARGIN'
    FUNDING = 'FUNDING'


class OrderSide(str, Enum):
    BUY = 'BID'
    SELL = 'ASK'


class OrderType(str, Enum):
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'
    STOP_LIMIT = 'STOP_LIMIT'
    STOP_MARKET = 'STOP_MARKET'


class OrderStatus(str, Enum):
    UNDEFINED = 'UNDEFINED'
    PENDING = 'PENDING'
    OPEN = 'OPEN'
    CANCELLED = 'CANCELLED'
    PARTIAL_CANCELLED = 'PARTIAL_CANCELLED'
    PARTIAL_FILLED = 'PARTIAL_FILLED'
    FILLED = 'FILLED'
    EXPIRED = 'EXPIRED'
    FAILED = 'FAILED'


class TimeInForce(str, Enum):
    GOOD_TILL_CANCEL = 'GTC'
    IMMEDIATE_OR_CANCEL = 'IOC'
    ALL_OR_NONE = 'AON'
    FILL_OR_KILL = 'FOK'
    UNDEFINED = 'UNDEFINED_TIME_IN_FORCE'


class SideEffect(str, Enum):
    NO_SIDE_EFFECT = 'NO_SIDE_EFFECT'
    AUTO_BORROW = 'AUTO_BORROW'
    AUTO_REPLAY = 'AUTO_REPLAY'


class StopOperator(str, Enum):
    GTE = "GTE"
    LTE = "LTE"


class LoanType(str, Enum):
    AUTO = "LOAN_AUTO"
    MANUAL = "LOAN_MANUAL"


class MarginDirection(str, Enum):
    ADD = "ADD"
    SUB = "SUB"


class DepositStatus(str, Enum):
    PENDING = "PENDING"
    MODERATION = "MODERATION"
    CONFIRMED = "CONFIRMED"
    REJECTED = "REJECTED"


class WithdrawStatus(str, Enum):
    NEW = "NEW"
    CONFIRMED = "CONFIRMED"
    VERIFIED = "VERIFIED"
    MODERATION = "MODERATION"
    APPROVED = "APPROVED"
    SUSPENDED = "SUSPENDED"
    DONE = "DONE"
    REFUSED = "REFUSED"
    CANCELED = "CANCELED"


class ChartInterval(int, Enum):
    FIVE_MIN = 5
    FIFTEEN_MINS = 15
    HALF_HOUR = 30
    HOUR = 60
    FOUR_HOURS = 60 * 4
    DAY = 60 * 24