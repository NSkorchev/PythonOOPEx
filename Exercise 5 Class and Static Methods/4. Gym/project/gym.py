from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)
        return

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)
        return

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)
        return

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)
        return

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
        return

    def subscription_info(self, subscription_id: int) -> str:
        subscription = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        customer = [cus for cus in self.customers if cus.id == subscription.customer_id][0]
        trainer = [tr for tr in self.trainers if tr.id == subscription.trainer_id][0]
        plan = [pl for pl in self.plans if pl.id == subscription.exercise_id][0]
        equipment = [eq for eq in self.equipment if eq.id == plan.equipment_id][0]

        return f"{subscription}\n" \
               f"{customer}\n" \
               f"{trainer}\n" \
               f"{equipment}\n" \
               f"{plan}\n"
