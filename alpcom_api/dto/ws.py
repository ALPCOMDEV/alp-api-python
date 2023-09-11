from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Ticker(BaseModel):
    symbol: str
    close: str
    base_vol: str
    quote_vol: str
    change: str
    high: str
    low: str
    bid: str
    ask: str


class Trade(BaseModel):
    date: float
    trade_id: int
    pair: str
    amount: str
    price: str
    direction: str


class Rate(BaseModel):
    rate: str
    base: str
    quote: str


class BookOrder(BaseModel):
    price: str
    amount: str


class Diff(BaseModel):
    symbol: str
    asks: List[BookOrder]
    bids: List[BookOrder]


class Depth(Diff):
    symbol: str
    asks: List[BookOrder]
    bids: List[BookOrder]
    total_asks: str
    total_bids: str


class Wallet(BaseModel):
    code: str
    wallet_type: str
    symbol: Optional[str] = None
    balance: str
    reserve: str


class Order(BaseModel):
    order_id: int
    symbol: str
    side: str
    order_type: str
    base_amount: str
    limit_price: str
    amount_unfilled: str
    amount_filled: str
    amount_cancelled: str
    value_filled: str
    price_avg: Optional[str] = None
    done_at: Optional[float] = None
    status: str
    quote_amount: Optional[str] = None
    wallet_type: str
    stop_price: Optional[str] = None
    stop_operator: str
