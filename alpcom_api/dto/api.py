from datetime import datetime
from typing import List, Optional, Dict

from alpcom_api.dto.constants import ConvertModel, WalletType, OrderSide, OrderStatus, OrderType, TimeInForce, \
    DepositStatus, WithdrawStatus, SideEffect, NEVER, StopOperator, MarginDirection, LoanType

class Currency(ConvertModel):
    short_name: str
    sign: str


class Pair(ConvertModel):
    name: str
    currency1: str
    currency2: str
    amount_precision: int
    price_precision: int
    maximum_order_size: float
    minimum_order_size: float
    minimum_order_value: float


class Ticker(ConvertModel):
    pair: str
    last: float
    vol: float
    buy: float
    sell: float
    high: float
    low: float
    diff: float
    timestamp: float


class OrderbookItem(ConvertModel):
    amount: float
    price: float


class Orderbook(ConvertModel):
    buy: List[OrderbookItem]
    sell: List[OrderbookItem]


class Trade(ConvertModel):
    id: int
    account_id: int
    pair: str
    amount: float
    price: float
    timestamp: float
    type: str


class Candle(ConvertModel):
    open: float
    close: float
    high: float
    low: float
    volume: float
    time: float


class Account(ConvertModel):
    id: int
    email: str
    name: str
    parent_id: Optional[int] = None

    @property
    def is_sub(self) -> bool:
        return bool(self.parent_id)

    @property
    def is_main(self) -> bool:
        return not bool(self.parent_id)


class AccountFee(ConvertModel):
    account_id: int
    active_once: List[datetime]
    taker_fee_rate: float
    maker_fee_rate: float
    fee_currency: str
    priority: int
    currency: str = None
    pair: str = None
    is_active: bool


class Balance(ConvertModel):
    balance: float
    reserve: float
    currency: str
    wallet_type: WalletType
    last_update_at: str
    account_id: int

    @property
    def available(self) -> float:
        return self.balance - self.reserve


class Order(ConvertModel):
    id: int
    account_id: int
    pair: str
    amount: float
    price: float
    side: OrderSide
    status: OrderStatus
    type: OrderType
    wallet_type: WalletType
    amount_canceled: float
    amount_filled: float
    date: datetime
    open_at: datetime
    tif: TimeInForce
    updated_at: datetime
    done_at: datetime = None
    expire_after: datetime = None
    stop_price: float = None


class AccountTrade(ConvertModel):
    account_id: int
    pair: str
    amount: float
    amount_unfilled: float
    price: float
    currency: str
    status: OrderStatus
    date: datetime
    fee_amount: float
    fee_currency: str
    fee_rate: float
    is_maker: bool
    type: OrderType
    wallet_type: WalletType


class WalletMotion(ConvertModel):
    id: int
    account_id: int
    wallet_id: int
    type: str
    balance: float
    balance_delta: float
    balance_end: float
    reserve: float
    reserve_delta: float
    reserve_end: float
    currency: str
    wallet_type: WalletType
    date: datetime


class DepositAttribute(ConvertModel):
    key: str
    value: str


class DepositMethod(ConvertModel):
    network: str
    currency: str
    attributes: List[DepositAttribute]
    confirmations: int
    min_deposit: float
    max_deposit: float
    is_enabled: bool


class WithdrawAttribute(ConvertModel):
    field: str
    regex: Optional[str] = None


class WithdrawMethod(ConvertModel):
    id: int
    network: str
    currency: str
    attributes: List[WithdrawAttribute]
    fee_rate: float
    fee_amount: float
    fee_currency: str
    min_withdraw: float
    max_withdraw: float
    is_enabled: bool


class WithdrawRequest(ConvertModel):
    amount: float
    method: int
    attributes: Dict[str, str]
    client_order_id: str = None


class Deposit(ConvertModel):
    id: int
    amount: float
    currency: str
    status: DepositStatus
    tx_hash: Optional[str] = ''
    date: datetime


class Withdraw(ConvertModel):
    id: int
    amount: float
    fee_amount: float
    currency: str
    fee_currency: str
    status: WithdrawStatus
    tx_hash: Optional[str] = ''
    date: datetime


class BaseOrderRequest(ConvertModel):
    pair: str
    order_side: OrderSide
    client_order_id: str = '1'
    wallet_type: WalletType = WalletType.SPOT
    side_effect: SideEffect = SideEffect.NO_SIDE_EFFECT
    valid_till: datetime = None
    expire_after: datetime = NEVER


class LimitOrderRequest(BaseOrderRequest):
    base_amount: float
    limit_price: float
    order_type: OrderType = OrderType.LIMIT
    tif: TimeInForce = TimeInForce.GOOD_TILL_CANCEL


class MarketOrderRequest(BaseOrderRequest):
    base_amount: float = None
    quote_amount: float = None
    order_type: OrderType = OrderType.MARKET


class StopLimitOrderRequest(BaseOrderRequest):
    base_amount: float
    limit_price: float
    stop_price: float
    stop_operator: StopOperator
    order_type: OrderType = OrderType.STOP_LIMIT
    tif: TimeInForce = TimeInForce.GOOD_TILL_CANCEL


class MarginTransferRequest(ConvertModel):
    account_id: int
    wallet_type: WalletType
    direction: MarginDirection
    amount: float
    currency: str
    pair: str = None
    note: str = None


class BorrowRequest(ConvertModel):
    account_id: int
    borrow: float
    currency: str
    wallet_type: WalletType
    pair: str = None
    type: LoanType = LoanType.MANUAL


class RepayRequest(ConvertModel):
    account_id: int
    amount: float
    currency: str
    wallet_type: WalletType
    pair: str = None
    type: LoanType = LoanType.MANUAL


class Loan(ConvertModel):
    id: int
    account_id: int
    borrowed: float
    interest: float
    currency: str
    wallet_type: WalletType


class MarginTransfer(ConvertModel):
    id: int
    account_id: int
    amount: float
    currency: str
    date: datetime
    direction: MarginDirection
    wallet_type: WalletType
    note: str
    pair: str


class Borrow(ConvertModel):
    id: int
    account_id: int
    borrowed: float
    date: datetime
    interest_accrued: float
    interest_paid: float
    interest_rate: float
    repaid: float
    last_interest_at: datetime = None
    opened_at: datetime
    type: LoanType
    wallet_type: WalletType


class Repay(ConvertModel):
    id: int
    account_id: int
    interest_amount: float
    principal_amount: float
    currency: str
    date: datetime
    type: LoanType
    wallet_type: WalletType


class Interest(ConvertModel):
    id: int
    account_id: int
    borrow_id: int
    currency: str
    interest_accrued: float
    interest_paid: float
    interest_rate: float
    wallet_type: WalletType


class Liquidation(ConvertModel):
    id: int
    account_id: int
    amount: float
    fund_amount: float
    currency: str
    created_at: datetime
    wallet_type: WalletType
    margin_level: float
    closed_at: datetime = None
    pair: str = None
    order_closed: List[int] = None
    order_created: List[int] = None
    borrow_closed: List[int] = None
    repay_created: List[int] = None
