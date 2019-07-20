'''
Declares a class for generating various test data to represent transaction data
'''
from faker import Faker

class transaction_data:
    '''
    class for generating various test data to represent transaction data
    '''
    def __init__(self, date_time, customer, card_number, card_provider, card_expire, card_code, description, product_code):
        self.date_time = date_time
        self.customer = customer
        self.card_number = card_number
        self.card_provider = card_provider
        self.card_expire = card_expire
        self.card_code = card_code
        self.description = description
        self.product_code = product_code

    def gen_date_time():
        '''
        generates a fake date and time for class transaction_data
        '''
        fake = Faker()
        date_time = fake.date_time()
        return date_time

    def gen_customer():
        '''
        generates a fake customer name for class transaction_data
        '''
        fake = Faker()
        customer = fake.name()
        return customer

    def gen_card_number():
        '''
        generates a fake credit card number for class transaction_data
        '''
        fake = Faker()
        card_number = fake.credit_card_number()
        return card_number

    def gen_card_provider():
        '''
        generate a fake credit card provider for class transaction_data
        '''
        fake = Faker()
        card_provider = fake.credit_card_provider()
        return card_provider

    def gen_card_expire():
        '''
        generates a fake credit card expiry data for class transaction_data
        '''
        fake = Faker()
        card_expire = fake.credit_card_expire()
        return card_expire

    def gen_card_code():
        '''
        generates a fake credit card security code data for class transaction_data
        '''
        fake = Faker()
        card_code = fake.credit_card_security_code()
        return card_code

    def gen_description():
        '''
        generates a fake description for class transaction_data
        '''
        fake = Faker()
        description = fake.lorem()
        return description

    def gen_product_code():
        '''
        generates a fake product code data for class transaction_data
        '''
        fake = Faker()
        product_code = fake.ean8()
        return product_code