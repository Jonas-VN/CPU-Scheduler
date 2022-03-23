from src.functions import parse_data, visualize_data


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



#data = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5], [5, 8, 2]]  # zelfde data als op ppt, mean R is idd gelijk, dus onze berkeningen kloppen

data = parse_data("processen20000.xml")
scheduled = FCFS(data)
visualize_data(scheduled)