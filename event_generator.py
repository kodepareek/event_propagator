import time

class EventGenerator:
    sampleEvents = [
        {
            "eventType": "price_update",
            "product": "product1",
            "price": 100,
        },
        {
            "eventType": "discount",
            "product": "product1",
            "discount": 10,
            "country": "us"
        },
        {
            "eventType": "discount",
            "product": "product2",
            "discount": 10,
            "country": "esp"
        },
        {
            "eventType": "price_update",
            "product": "product2",
            "price": 101,
        },
        {
            "eventType": "price_update",
            "product": "product1",
            "price": 101,
        },
        {
            "eventType": "discount",
            "product": "product1",
            "discount": 11,
            "country": "us"
        },
        {
            "eventType": "discount",
            "product": "product2",
            "discount": 11,
            "country": "ind"
        }
        ]
    
    def generate(self):
        for event in self.sampleEvents:
            time.sleep(1)
            yield event
