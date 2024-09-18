class CountryDiscountMapper:
    def transform(self, payload):
        return {
            "name": "COUNTRY_DISCOUNT",
            "payload": payload
        }
