from src.functions import parse_data, visualize_data

def SJF(data, debug = False):
    jiffy = 0  # 1 jiffy is 1 CPU cycle
    aantal_processen = len(data)
    scheduled = [
        # [pid, arrival time, service time, waiting time, turnaround time, response ratio]
    ]

    while data != []:
        waiting_queue = []
        for process in data:
            if process[1] <= jiffy:
                waiting_queue.append(process)
            else:
                # Processen staan goed georderd, dus vanaf dat 1 process niet voldoet zal de rest ook niet voldoen. Anders is het veel te traag
                break

        if waiting_queue != []:
            waiting_queue = sorted(waiting_queue, key=lambda x: x[2])
            data.remove(waiting_queue[0])
            pid = waiting_queue[0][0]
            arrival_time = waiting_queue[0][1]
            service_time = waiting_queue[0][2]
            waiting_time = jiffy - arrival_time
            turnaround_time = service_time + waiting_time
            response_ratio = turnaround_time / service_time
            if debug: print(f"PID: {pid}\t Start: {jiffy}\t Arrival time: {arrival_time}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
            scheduled.append([pid, arrival_time, service_time, waiting_time, turnaround_time, response_ratio])
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

    print("=========================== SJF ===========================")
    print("Gemiddelde waiting_time: " + str(gemiddelde_waiting_time))
    print("Gemiddelde turnaround_time: " + str(gemiddelde_turnaround_time))
    print("Gemiddelde response_ratio: " + str(gemiddelde_response_ratio))

    return scheduled

#data = parse_data("processen50000.xml")
#scheduled = SJF(data)
#visualize_data(scheduled)