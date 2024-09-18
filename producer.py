from kafka import KafkaProducer
import json
from event_generator import EventGenerator
from data_mappers.product_price_mapper import ProductPriceMapper
from data_mappers.country_discount_mapper import CountryDiscountMapper

producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
generator =  EventGenerator()
priceMapper = ProductPriceMapper()
discountMapper = CountryDiscountMapper()

class WriteToKafka:
    def transform(self, event):
        eventType = event["eventType"]
        match eventType:
            case "price_update":
                return priceMapper.transform(event)
            case "discount":
                return discountMapper.transform(event)
            case _:
                return Exception("invalid event found")            
    
    def write(self):
        for event in generator.generate():
            transformedEvent = self.transform(event)
            producer.send(transformedEvent["name"], transformedEvent)            

if __name__ == "__main__":
    kafkaProducer = WriteToKafka()
    kafkaProducer.write()
