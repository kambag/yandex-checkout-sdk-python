# -*- coding: utf-8 -*-
import unittest

from yandex_checkout.domain.models.amount import Amount
from yandex_checkout.domain.models.currency import Currency
from yandex_checkout.domain.models.refund_source import RefundSource


class TestRefundSource(unittest.TestCase):

    def test_refund_source_cast(self):
        self.maxDiff = None
        src = RefundSource()
        src.account_id = '79990000000'
        src.amount = Amount({
            "value": '100.01',
            "currency": Currency.RUB
        })

        self.assertEqual({
            'account_id': '79990000000',
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            }
        }, dict(src))

        self.assertEqual('79990000000', src.account_id)

        self.assertEqual({"value": 100.01, "currency": Currency.RUB}, dict(src.amount))
        self.assertEqual(src.amount.value, 100.01)

        with self.assertRaises(TypeError):
            src.amount = 'invalid type'
