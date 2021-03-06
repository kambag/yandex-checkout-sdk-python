# -*- coding: utf-8 -*-
import unittest

from yandex_checkout.domain.models.amount import Amount
from yandex_checkout.domain.models.currency import Currency
from yandex_checkout.domain.response.transfer_response import TransferResponse, TransferStatus


class TestTransferResponse(unittest.TestCase):

    def test_transfer_cast(self):
        self.maxDiff = None
        transfer = TransferResponse()
        transfer.status = TransferStatus.SUCCEEDED
        transfer.account_id = '79990000000'
        transfer.amount = Amount({
            "value": '100.01',
            "currency": Currency.RUB
        })

        self.assertEqual({
            "account_id": "79990000000",
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            },
            "status": TransferStatus.SUCCEEDED
        }, dict(transfer))

        self.assertEqual('79990000000', transfer.account_id)
        self.assertEqual(TransferStatus.SUCCEEDED, transfer.status)

        self.assertEqual({"value": 100.01, "currency": Currency.RUB}, dict(transfer.amount))
        self.assertEqual(transfer.amount.value, 100.01)

        with self.assertRaises(TypeError):
            transfer.amount = 'invalid type'

    def test_transfer_value(self):
        self.maxDiff = None
        transfer = TransferResponse({
            "account_id": "79990000000",
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            },
            "status": TransferStatus.SUCCEEDED
        })

        self.assertEqual({
            "account_id": "79990000000",
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            },
            "status": TransferStatus.SUCCEEDED
        }, dict(transfer))

        self.assertEqual('79990000000', transfer.account_id)
        self.assertEqual(TransferStatus.SUCCEEDED, transfer.status)

        self.assertEqual({"value": 100.01, "currency": Currency.RUB}, dict(transfer.amount))
        self.assertEqual(transfer.amount.value, 100.01)
