import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt
import numpy as np

def parse_data(filename):
    tree = ET.parse("./Data/" + filename)
    root = tree.getroot()
    data = [
        # [pid, arrivaltime, servicetime] 
    ]

    for process in root:
        data.append([int(process[0].text), int(process[1].text), int(process[2].text)])
    return data


def FCFS(data):
    jiffy = 0  # 1 jiffy is 1 CPU cycle
    index = 0
    aantal_processen = len(data)
    scheduled = [
        # [pid, arrival time, service time, waiting time, turnaround time, response ratio]
    ]

    while index < aantal_processen:
        arrival_time = data[index][1]
        if arrival_time <= jiffy:
            pid = index + 1
            service_time = data[index][2]
            waiting_time = jiffy - arrival_time
            turnaround_time = service_time + waiting_time
            response_ratio = turnaround_time / service_time
            print(f"PID: {pid}\t Start: {jiffy}\t Arrival time: {arrival_time}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
            scheduled.append([pid, arrival_time, service_time, waiting_time, turnaround_time, response_ratio])
            index += 1
            jiffy += service_time
        else:
            jiffy += 1

    gemiddelde_turnaround_time = 0
    gemiddelde_waiting_time = 0
    gemiddelde_response_ratio = 0
    for i in scheduled:
        gemiddelde_waiting_time += i[3]
        gemiddelde_turnaround_time += i[4]
        gemiddelde_response_ratio += i[5]
    gemiddelde_turnaround_time /= aantal_processen
    gemiddelde_waiting_time /= aantal_processen
    gemiddelde_response_ratio /= aantal_processen

    print("=========================== FCFS ===========================")
    print("Gemiddelde waiting_time: " + str(gemiddelde_waiting_time))
    print("Gemiddelde turnaround_time: " + str(gemiddelde_turnaround_time))
    print("Gemiddelde response_ratio: " + str(gemiddelde_response_ratio))

    return scheduled


def visualize_FCFS(scheduled):
    scheduled = sorted(scheduled, key=lambda x: x[2])  # Sorteren op sevice time
    response_ratios = np.array([i[5] for i in scheduled])  # De response ratios die al gesorteerd zijn op service time
    waiting_times = np.array([i[3] for i in scheduled])  # De waiting times      "  "     "        "   "    "      "
    x = [i for i in range(1, 101)]  # array van 1 -> 100 om alle percentielen te berekenen en als x-as op de grafiek
    step = len(scheduled) // len(x)  # stap per percentiel, voor 10_000 processen: 10_000 // 100 = 100 processen per percentiel

    gemiddelde_response_ratios_per_percentiel = []
    gemiddelde_waiting_times_per_percentiel = []
    for percentiel in x:
        response_ratios_per_percentiel = []
        waiting_times_per_percentiel = []  # rt: response ratio; wt: waiting time
        for j in range((percentiel - 1) * step, percentiel * step):  # range voor i = 1 => 0 -> 100; i = 100 => 9900 -> 10_000 
            response_ratios_per_percentiel.append(response_ratios[j])
            waiting_times_per_percentiel.append(waiting_times[j])

        gemiddelde_response_ratios_per_percentiel.append(sum(response_ratios_per_percentiel) / len(response_ratios_per_percentiel))  # gemiddelde toevoegen
        gemiddelde_waiting_times_per_percentiel.append(sum(waiting_times_per_percentiel) / len(waiting_times_per_percentiel))  # gemiddelde toevoegen

    plt.plot(x, gemiddelde_response_ratios_per_percentiel, color='red')
    plt.plot(x, gemiddelde_waiting_times_per_percentiel, color='blue')
    plt.show()


#data = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5], [5, 8, 2]]  # zelfde data als op ppt, mean R is idd gelijk, dus onze berkeningen kloppen

data = parse_data("processen20000.xml")
scheduled = FCFS(data)
visualize_FCFS(scheduled)
