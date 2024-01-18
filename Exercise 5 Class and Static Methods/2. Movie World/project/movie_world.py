from project.customer import Customer
from project.dvd import DVD
from typing import List


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next((cust for cust in self.customers if cust.id == customer_id), None)
        dvd = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)

        # if customer is None or dvd is None:
        #     return "Invalid customer ID or DVD ID"
        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next((cust for cust in self.customers if cust.id == customer_id), None)
        dvd = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self) -> str:
        customers = "\n".join(repr(customer) for customer in self.customers)
        dvds = "\n".join(repr(dvd) for dvd in self.dvds).strip()

        return f"{customers}\n"\
               f"{dvds}"
