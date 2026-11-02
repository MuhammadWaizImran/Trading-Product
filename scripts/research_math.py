"""Exact arithmetic for hypothetical research scenarios. No fitting or order execution."""
from decimal import Decimal, InvalidOperation


def number(value):
    if isinstance(value, bool):
        raise ValueError('Boolean is not a numeric input')
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError('Expected a finite decimal number') from None
    if not result.is_finite():
        raise ValueError('Expected a finite decimal number')
    return result


def limit_price_rule(side, limit_price, hypothetical_fill_price):
    """Check a hypothetical price constraint only; never submit or simulate an order."""
    if side not in ('buy', 'sell'):
        raise ValueError('Explicit buy or sell side required')
    limit, fill = number(limit_price), number(hypothetical_fill_price)
    if limit <= 0 or fill <= 0:
        raise ValueError('Positive limit and hypothetical fill prices required')
    return {'price_constraint_satisfied': fill <= limit if side == 'buy' else fill >= limit,
            'side': side, 'limit_price': limit, 'hypothetical_fill_price': fill,
            'constraint': 'fill <= limit' if side == 'buy' else 'fill >= limit',
            'execution_guaranteed': False,
            'scope': 'Gross price comparison only; no fees, liquidity, venue rules or actual execution assessed.'}


def position_size(account, risk_fraction, stop_fraction=None, entry_price=None):
    """Linear spot notional under exact stop execution, excluding costs and leverage."""
    account, risk = number(account), number(risk_fraction)
    if account <= 0 or not Decimal(0) < risk <= Decimal(1):
        raise ValueError('Positive account and risk fraction in (0,1] required')
    budget = account * risk
    if stop_fraction is None:
        return {'status': 'insufficient_information', 'risk_budget': budget,
                'missing': 'entry-to-stop fractional loss', 'notional': None, 'quantity': None}
    stop = number(stop_fraction)
    if not Decimal(0) < stop <= Decimal(1):
        raise ValueError('Spot stop fraction must be in (0,1]')
    notional = budget / stop
    quantity = None
    if entry_price is not None:
        entry = number(entry_price)
        if entry <= 0:
            raise ValueError('Positive entry price required')
        quantity = notional / entry
    return {'status': 'calculated', 'risk_budget': budget, 'notional': notional,
            'quantity': quantity, 'exceeds_account': notional > account,
            'assumptions': 'Linear spot; exact stop execution; no costs. Not an order.'}


def payoff(win_r, loss_r, probability=None, cost_r=0):
    """Loss is a positive magnitude; constant per-outcome costs in risk units."""
    win, loss, cost = map(number, (win_r, loss_r, cost_r))
    if win <= 0 or loss <= 0 or cost < 0:
        raise ValueError('Positive win/loss magnitudes and nonnegative costs required')
    breakeven = (loss + cost) / (win + loss)
    expected = None
    if probability is not None:
        p = number(probability)
        if not Decimal(0) <= p <= Decimal(1):
            raise ValueError('Probability must be in [0,1]')
        expected = p * win - (1-p) * loss - cost
    return {'breakeven_probability': breakeven, 'feasible': breakeven <= 1,
            'expected_r': expected, 'actual_probability_known': probability is not None}


def orderbook_imbalance(ask_depth, bid_depth, convention):
    """Require explicit sign convention; never infer a paper's definition."""
    ask, bid = number(ask_depth), number(bid_depth)
    if ask < 0 or bid < 0 or ask + bid == 0:
        raise ValueError('Nonnegative comparable depths with positive total required')
    if convention not in ('ask_minus_bid', 'bid_minus_ask'):
        raise ValueError('Explicit ask_minus_bid or bid_minus_ask convention required')
    result = (ask-bid)/(ask+bid)
    if convention == 'bid_minus_ask':
        result = -result
    return {'value': result, 'convention': convention,
            'larger_displayed_side': 'bid' if bid > ask else 'ask' if ask > bid else 'equal',
            'predictive_claim': None}
