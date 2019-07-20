'''
Declares a class for generating various test data to represent a person's personal information
'''
from faker import Faker

class person_data:
    '''
    Class for generating various test data to represent a person's personal information
    '''
    def __init__(self, first_name, last_name, address, date_of_birth, phone, country, postcode):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.country = country
        self.postcode = postcode

    def gen_first_name():
        '''
        generates a fake first name for class person_data
        '''
        fake = Faker()
        first_name = fake.first_name()
        return first_name

    def gen_last_name():
        '''
        generates a fake last name for class person_data
        '''
        fake = Faker()
        last_name = fake.last_name()
        return last_name

    def gen_address():
        '''
        generates a fake address for class person_data
        '''
        fake = Faker()
        address = fake.address()
        return address

    def gen_date_of_birth():
        '''
        generates a fake date of birth for class person_data
        '''
        fake = Faker()
        date_of_birth = fake.date_of_birth()
        return date_of_birth

    def gen_phone_number():
        '''
        generates a fake phone number for class person_data
        '''
        fake = Faker()
        phone_number = fake.phone_number()
        return phone_number

    def gen_country():
        '''
        generates a fake country for class person_data
        '''
        fake = Faker()
        country = fake.country()
        return country

    def gen_postcode():
        '''
        generates a fake postcode for class person_data
        '''
        fake = Faker()
        postcode = fake.postcode()
        return postcode

    def gen_all():
        '''
        calls all functions in class person_data and returns all the generated data
        '''
        return(gen_first_name(), gen_last_name(), gen)
