import xml.etree.ElementTree as ET
import matplotlib

def parse_data(filename):
    tree = ET.parse("./Data/" + filename)
    root = tree.getroot()
    data = [
        # [arrivaltime, servicetime] 
    ]

    for process in root:
        data.append([int(process[1].text), int(process[2].text)])
    return data


data = parse_data("processen50000.xml")
jiffy = 0  # 1 jiffy is 1 CPU cycle
finished = False
scheduled = [
    # [arrival time, service time, waiting time, turnaround time, response ratio]
]
index = 0
aantal_processen = len(data)

while not finished:
    if index == aantal_processen:
        break

    arrival_time = data[index][0]
    if arrival_time <= jiffy:
        pid = index + 1
        print(f"Process: {pid}\t Arrival time: {arrival_time}\t Timestamp: {jiffy}")
        service_time = data[index][1]
        waiting_time = jiffy - arrival_time
        turnaround_time = service_time + waiting_time
        response_ratio = turnaround_time / service_time
        scheduled.append([arrival_time, service_time, waiting_time, turnaround_time, response_ratio])
        index += 1
        jiffy += service_time

    jiffy += 1

gemiddelde_turnaround_time = 0
gemiddelde_waiting_time = 0
gemiddelde_response_ratio = 0
for i in scheduled:
    gemiddelde_waiting_time += i[2]
    gemiddelde_turnaround_time += i[3]
    gemiddelde_response_ratio += i[4]

gemiddelde_turnaround_time /= aantal_processen
gemiddelde_waiting_time /= aantal_processen
gemiddelde_response_ratio /= aantal_processen

print("Gemiddelde waiting_time: " + str(gemiddelde_waiting_time))
print("Gemiddelde turnaround_time: " + str(gemiddelde_turnaround_time))
print("Gemiddelde response_ratio: " + str(gemiddelde_response_ratio))