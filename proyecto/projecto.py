import ciw
from prettytable import PrettyTable
import matplotlib

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
    'queue size '
])


for record in recs:
    t.add_row([
        record.id_number,
        format(record.arrival_date, '.4f'),
        format(record.service_start_date, '.4f'),
        format(record.waiting_time, '.4f'),
        format(record.service_end_date, '.4f'),
        format(record.exit_date, '.4f'),
        record.queue_size_at_arrival
    ])

print(t)
