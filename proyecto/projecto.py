import ciw
import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt

N = ciw.create_network(
    Arrival_distributions=[['Exponential', 40]],
    Service_distributions=[['Exponential', 20]],
    Number_of_servers=[3]
)

ciw.seed(1)
Q = ciw.Simulation(N)

Q.simulate_until_max_time(2)

recs = Q.get_all_records()
recs.sort()
t = PrettyTable([
    'id',
    'arrival',
    'service start',
    'waiting time',
    'service end',
    'exit',
    'queue arrival',
    'queue departure'
])


for record in recs:
    t.add_row([
        record.id_number,
        format(record.arrival_date, '.4f'),
        format(record.service_start_date, '.4f'),
        format(record.waiting_time, '.4f'),
        format(record.service_end_date, '.4f'),
        format(record.exit_date, '.4f'),
        record.queue_size_at_arrival,
        record.queue_size_at_departure
    ])

print(t)

waits = [r.waiting_time for r in recs]
arrival = [r.service_start_date for r in recs]
qArrival = [r.queue_size_at_arrival for r in recs]
qDeparture = [r.queue_size_at_departure for r in recs]

arrivalPlot, = plt.plot(arrival, qArrival)
departurePlot, = plt.plot(arrival, qDeparture, label='line 2')

plt.title('Queue Arrival Vs Departure')
plt.xlabel('Arrival time')
plt.ylabel('Queue')
plt.legend([arrivalPlot, departurePlot], ['Arrival Queue', 'Departure Queue'], loc=1)
plt.show()
