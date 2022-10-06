import random

import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt
from pyvis.network import Network

from main import get_data
from message import Message, Customer

df = get_data()

customers = []

for i in df.values.tolist():
    known_senders = list(filter(lambda customer: customer.sender == i[0], customers))
    known_recivers = list(filter(lambda customer: customer.sender == i[1], customers))
    if len(known_senders) == 0:
        new_customer = Customer(i[0])
        new_customer.add_message(Message(i[0], i[1], i[2]))
        customers.append(new_customer)
    else:
        known_sender = known_senders[0]
        known_sender.add_message(Message(i[0], i[1], i[2]))
    #     na potrzeby doświadczenia wywalamy nie aktywnych użytkownikó tak zwanych czytajacych bodz w ogóel nic nie robiacych
    if len(known_recivers) == 0:
        new_customer = Customer(i[1])
        customers.append(new_customer)


[i.calculate_propaiblities() for i in customers]

# Day + Night -> max
# max_prop_send_day = max([i.send_night_messages + i.send_message_day for i in customers])
# for i in customers:
#     if max_prop_send_day == i.send_night_messages + i.send_message_day:
#         max_prop_send_day = (i.send_night_messages, i.send_message_day)
# max_prop_send_day = max([i.send_night_messages + i.send_message_day for i in customers])
# for i in customers:
#     if max_prop_send_day == i.send_night_messages + i.send_message_day:
#         max_prop_send_day = (i.send_night_messages, i.send_message_day)

# list(filter(lambda x: (x.send_night_messages is max_prop_send_day[0] and x.send_message_day is max_prop_send_day[1]), customers))[0].is_super_message_recived = True
# print(f'max_prop_send_day: ', max_prop_send_day)

# Random
# customers[random.choice([i for i in range(len(customers))])].is_super_message_recived = True

# Day
# max_prop_send_day = max([i.send_message_day for i in customers])
# list(filter(lambda x: x.send_message_day == max_prop_send_day, customers))[0].is_super_message_recived = True

# Night
# max_prop_send_day = max([i.send_night_messages for i in customers])
# list(filter(lambda x: x.send_night_messages == max_prop_send_day, customers))[0].is_super_message_recived = True
#


# print(f'max_prop_send_day: ', max_prop_send_day)




got_net = Network()

infected_percente = []

G = nx.Graph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
[G.add_node(i.sender) for i in customers]

# for day in range(10000):
#     if day == 180:
#         customers[random.choice([i for i in range(len(customers))])].is_super_message_recived = True
#     if day > 180:
#         for customer in customers:
#             message_day = customer.try_to_send_message_day(day, customers)
#             message_night = customer.try_to_send_message_night(day, customers)
#         infected_percente.append([i.is_super_message_recived for i in customers].count(True) / len(customers))
#     else:
#         for customer in customers:
#             message_day = customer.try_to_send_message_day(day, customers)
#             message_night = customer.try_to_send_message_night(day, customers)
#
#     messages = []
#     [messages.extend(i.messages_send) for i in customers]
#     [G.add_edge(i.sender, i.receiver) for i in messages]
#     print(nx.is_connected(G))
#     print(day)



# Plot graph
for customer in customers:
    if customer.is_super_message_recived:
        got_net.add_node(customer.sender, color='red')
    else:
        got_net.add_node(customer.sender, color='blue')
messages = []
[messages.extend(i.messages_send) for i in customers]
for i in messages:
    # if i.is_super_message is True:
    got_net.add_edge(i.sender, i.receiver)

got_net.show('gameofthrones.html')



messages = []
[messages.extend(i.messages_send) for i in customers]
df = pd.DataFrame(
    [[i.sender for i in messages], [i.receiver for i in messages]]) \
    .transpose() \
    .rename(columns={0: "SRC", 1: "DST"})


print(f'avg messages infected: {[i.is_super_message for i in messages].count(True)}')
print(f'avg customers infected: {[i.is_super_message_recived for i in customers].count(True)}')


fig = plt.figure()
plt.bar([i for i in range(99)], infected_percente)
plt.show()


# G = nx.from_pandas_edgelist(df, "SRC", "DST")
# nx.draw(G)
# plt.show()
