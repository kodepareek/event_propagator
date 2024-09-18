
class ProductPriceMapper:
    def transform(self, payload):
        return {
            "name": "PRODUCT_PRICE",
            "payload": payload
        }

