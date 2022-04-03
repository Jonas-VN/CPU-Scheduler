import numpy as np
import xml.etree.ElementTree as ET


def parse_data(filename):
    tree = ET.parse("./src/Data/" + filename)
    root = tree.getroot()
    data = [
        # [pid, arrivaltime, servicetime] 
    ]

    for process in root:
        data.append([int(process[0].text), int(process[1].text), int(process[2].text)])
    return data


def calc_percentile(scheduled):
    scheduled = sorted(scheduled, key=lambda x: x[2])  # Sorteren op sevice time
    response_ratios = np.array([i[5] for i in scheduled])  # De response ratios die al gesorteerd zijn op service time
    waiting_times = np.array([i[3] for i in scheduled])  # De waiting times      "  "     "        "   "    "      "
    x = range(1, 101)  # array van 1 -> 100 om alle percentielen te berekenen en als x-as op de grafiek
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

    return gemiddelde_response_ratios_per_percentiel, gemiddelde_waiting_times_per_percentiel

    
def calculate_mean(scheduled):
    aantal_processen = len(scheduled)
    gemiddelde_turnaround_time = 0
    gemiddelde_waiting_time = 0
    gemiddelde_response_ratio = 0

    for process in scheduled:
        gemiddelde_waiting_time += process[3]
        gemiddelde_turnaround_time += process[4]
        gemiddelde_response_ratio += process[5]

    gemiddelde_turnaround_time /= aantal_processen
    gemiddelde_waiting_time /= aantal_processen
    gemiddelde_response_ratio /= aantal_processen

    print("Gemiddelde waiting_time: " + str(gemiddelde_waiting_time))
    print("Gemiddelde turnaround_time: " + str(gemiddelde_turnaround_time))
    print("Gemiddelde response_ratio: " + str(gemiddelde_response_ratio))

    return gemiddelde_waiting_time, gemiddelde_turnaround_time, gemiddelde_response_ratio
