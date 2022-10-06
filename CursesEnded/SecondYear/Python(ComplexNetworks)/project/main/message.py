import random as random
from datetime import datetime

import pytz

warsaw = pytz.timezone('Europe/Warsaw')


# 7-18 day
# 19-7 night


class Message:

    def __init__(self, sender, receiver, send_time):
        self.sender = sender
        self.receiver = receiver
        self.send_time = send_time.astimezone(warsaw)
        self.is_super_message = False


class Customer:

    def __init__(self, id):
        self.sender = id
        self.messages_send = []
        self.send_message_day = None
        self.send_night_messages = None
        self.is_super_message_recived = False
        self.days_without_new_contact = 0
        self.days_without_message_to_contact = 0

    def add_message(self, message):
        self.messages_send.append(message)

    def calculate_propaiblities(self, day=0):
        hours_messages_send = [i.send_time.hour for i in self.messages_send]
        message_friends = set([i.receiver for i in self.messages_send])
        day_messages = 0
        night_messages = 0
        for i in hours_messages_send:
            if 7 <= i < 18:
                day_messages += 1
            elif i >= 18 or i <= 7:
                night_messages += 1

        self.send_message_day = day_messages / (193 + day)
        self.send_night_messages = night_messages / (193 + day)
        self.get_new_contact = len(message_friends) / (193 + day)
        self.send_messages_to_new_contact = sum(set([i.receiver for i in self.messages_send])) / (193 + day)
        self.days_without_new_contact = 1
        self.days_without_message_to_contact = 1

    def try_to_send_message_day(self, day, customers):
        return self.try_to_send_message(customers, day, self.send_message_day)

    def try_to_send_message_night(self, day, customers):
        new_message = self.try_to_send_message(customers, day, self.send_night_messages)

        self.days_without_message_to_contact += 1
        self.days_without_new_contact += 1
        return new_message

    def try_to_send_message(self, customers, day, prop_send):
        counted_messages_to_send = prop_send * self.days_without_message_to_contact

        while counted_messages_to_send >= 1:
            if self.send_messages_to_new_contact * self.days_without_new_contact:
                self.send_to_new_contact(customers, day)
                counted_messages_to_send -= 1
            if counted_messages_to_send >= 1:
                self.send_to_existing_contact(customers, day)
                counted_messages_to_send -= 1

    def send_to_existing_contact(self, customers, day):
        new_message_customer_id = random.choice([i.receiver for i in self.messages_send])
        customers = list(filter(lambda x: x.sender == new_message_customer_id, customers))
        if len(customers) > 0:
            self.infect_or_leve(customers[0])
            new_message = Message(self.sender, new_message_customer_id, datetime.now())
            new_message.is_super_message = self.is_super_message_recived

            self.messages_send.append(
                new_message)
            self.calculate_propaiblities(day)

    def send_to_new_contact(self, customers, day):
        new_conntact = random.choice(customers)
        self.infect_or_leve(new_conntact)
        new_message = Message(self.sender, new_conntact.sender, datetime.now())
        new_message.is_super_message = self.is_super_message_recived
        self.messages_send.append(new_message)
        self.calculate_propaiblities(day)

    def infect_or_leve(self, customer):
        if self.is_super_message_recived:
            customer.is_super_message_recived = True
