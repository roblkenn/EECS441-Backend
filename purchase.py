class Purchase(object):

    def __init__(self, transaction_id, product_id, quantity, purchased_at, response=None):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.quantity = quantity
        self.purchased_at = purchased_at
        self.response = response

    @classmethod
    def from_app_store_receipt(cls, receipt, response):
        purchase = {
            'transaction_id': receipt['transaction_id'],
            'product_id': receipt['product_id'],
            'quantity': receipt['quantity'],
            'purchased_at': receipt['purchase_date'],
            'response': response,
        }
        return cls(**purchase)
        