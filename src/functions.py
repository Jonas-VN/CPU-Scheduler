from cProfile import label
import numpy as np
from matplotlib import pyplot as plt
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


def visualize_data(scheduled, color, label):
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

    plt.plot(x, gemiddelde_response_ratios_per_percentiel, color=color, label=label)
    #plt.plot(x, gemiddelde_waiting_times_per_percentiel, color=color)
    #plt.show()