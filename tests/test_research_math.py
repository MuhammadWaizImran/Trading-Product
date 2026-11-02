"""Arithmetic invariants only. No model imports, fitting, network or orders."""
from decimal import Decimal as D
import unittest
from scripts.research_math import position_size, payoff, orderbook_imbalance, limit_price_rule


class ResearchMathTests(unittest.TestCase):
    def test_limit_price_directions_and_equality(self):
        for fill in ('235', '240', '245'):
            self.assertEqual(limit_price_rule('sell', '240', fill)['price_constraint_satisfied'], D(fill) >= 240)
            self.assertEqual(limit_price_rule('buy', '240', fill)['price_constraint_satisfied'], D(fill) <= 240)
        self.assertFalse(limit_price_rule('sell', 240, 245)['execution_guaranteed'])

    def test_limit_price_decimal_precision_and_invalid_inputs(self):
        self.assertFalse(limit_price_rule('sell', '0.100000000000000001', '0.1')['price_constraint_satisfied'])
        for side,limit,fill in [('unknown',1,1),('sell',0,1),('buy',1,-1),('sell','NaN',1),('buy',True,1)]:
            with self.assertRaises(ValueError): limit_price_rule(side,limit,fill)

    def test_position_budget_and_units(self):
        r = position_size('12000', '0.005', '0.03', '40')
        self.assertEqual((r['risk_budget'], r['notional'], r['quantity']), (D(60), D(2000), D(50)))
        self.assertEqual(r['notional'] * D('.03'), r['risk_budget'])

    def test_missing_stop_abstains(self):
        r = position_size(5000, '.01', entry_price=20)
        self.assertEqual(r['risk_budget'], 50)
        self.assertIsNone(r['quantity'])
        self.assertIsNone(r['notional'])

    def test_missing_entry_and_excess_notional(self):
        r = position_size(1000, '.02', '.01')
        self.assertTrue(r['exceeds_account'])
        self.assertIsNone(r['quantity'])

    def test_payoff_is_not_probability(self):
        r = payoff(4, 1)
        self.assertEqual(r['breakeven_probability'], D('.2'))
        self.assertIsNone(r['expected_r'])
        self.assertFalse(r['actual_probability_known'])
        self.assertEqual(payoff(4, 1, '.2')['expected_r'], 0)

    def test_costs_and_boundary_probabilities(self):
        self.assertEqual(payoff(4, 1, 0, '.1')['expected_r'], D('-1.1'))
        self.assertEqual(payoff(4, 1, 1, '.1')['expected_r'], D('3.9'))
        self.assertEqual(payoff(4, 1, cost_r='.1')['breakeven_probability'], D('.22'))
        self.assertFalse(payoff(1, 1, cost_r=2)['feasible'])

    def test_source_sign_conventions(self):
        self.assertEqual(orderbook_imbalance(60, 100, 'ask_minus_bid')['value'], D('-.25'))
        self.assertEqual(orderbook_imbalance(60, 100, 'bid_minus_ask')['value'], D('.25'))
        self.assertEqual(orderbook_imbalance(60, 100, 'ask_minus_bid')['larger_displayed_side'], 'bid')

    def test_invalid_inputs(self):
        for v in ['NaN', 'Infinity', -1, 0, True]:
            with self.assertRaises(ValueError): position_size(v, '.01', '.02')
        for v in [-1, 0, 2]:
            with self.assertRaises(ValueError): position_size(100, '.01', v)
        with self.assertRaises(ValueError): payoff(4, 1, '1.1')
        with self.assertRaises(ValueError): orderbook_imbalance(0, 0, 'ask_minus_bid')
        with self.assertRaises(ValueError): orderbook_imbalance(1, 2, 'unknown')


if __name__ == '__main__':
    unittest.main()
