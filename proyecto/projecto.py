import ciw
import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt

lamda = float(input("Escribe el valor de Lambda: "))
mu = float(input("Escribe el valor de mu: "))
s = int(input("Escribe el valor de s (número de servidores): "))
n = int(input("Num de clientes a simular: "))

N = ciw.create_network(
    Arrival_distributions=[['Exponential', lamda]],
    Service_distributions=[['Exponential', mu]],
    Number_of_servers=[s]
)

ciw.seed(1)
Q = ciw.Simulation(N)

Q.simulate_until_max_customers(n, progress_bar=True)

recs = Q.get_all_records()
recs.sort()
t = PrettyTable([
    'id',
    'arrival',
    'waiting time',
    'service start',
    'service end',
    'exit',
    'queue arrival',
    'queue departure'
])

for record in recs:
    t.add_row([
        record.id_number,
        format(record.arrival_date, '.4f'),
        format(record.waiting_time, '.4f'),
        format(record.service_start_date, '.4f'),
        format(record.service_end_date, '.4f'),
        format(record.exit_date, '.4f'),
        record.queue_size_at_arrival,
        record.queue_size_at_departure
    ])

p = lamda / (s * mu)
helper = lamda / mu
aux1 = 0
for n in range(s):
    aux1 += pow(helper, n) / math.factorial(n)
aux2 = pow(helper, s) / (math.factorial(s) * (1 - p))

p0 = 1 / (aux1 + aux2)
lq = (pow(helper, s) * p0 * p) / (math.factorial(s) * pow(1 - p, 2))
wq = lq / lamda
ws = wq + 1 / mu
ls = lamda * ws


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

plt.title('Waiting time of customers')
plt.ylabel('Number of customers')
plt.xlabel('Waiting time')
plt.hist(waits)
plt.show()

print(t)

print("Estadisticas Teorico")
print("λ=%f  μ=%f  s=%d" % (lamda, mu, s))
print("p=%f  p0=%f  Ls=%f  Lq=%f  Ws=%f  Wq=%f\n" % (p, p0, ls, lq, ws, wq))


print("Estadisticas Simulacion")
sim = PrettyTable([
    'id',
    'lqR',
    'lsR',
    'wsR',
    'wqR'
])
i = 0
for a in qArrival:
    lqR = a
    wqR = lqR / lamda
    wsR = wqR + 1 / mu
    lsR = lamda * wsR
    i += 1

    sim.add_row([
        i,
        format(lqR, '.4f'),
        format(lsR, '.4f'),
        format(wsR, '.4f'),
        format(wqR, '.4f'),
    ])
    # print("id:", i, "\tlqR:", round(lqR, 3), "\tlsR:", round(lsR, 3), "\t\twsR:", round(wsR, 3), "\t\twqR:", round(wqR, 3))

print(sim)
servicetimes = [r.service_time for r in recs]
wait = [r.waiting_time for r in recs]
mean_service_time = sum(servicetimes) / len(servicetimes)
mean_waiting_time = sum(wait) / len(wait)
mean_queue = sum(qDeparture) / len(qDeparture)
print("Media de tiempo de servicio: %f ; Media de tiempo de espera: %f" % (mean_service_time, mean_waiting_time))
print()
print("Media de fila: %f" % mean_queue)
