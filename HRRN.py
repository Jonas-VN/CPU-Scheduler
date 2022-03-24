from src.functions import parse_data, visualize_data


def HRRN(data, debug = False):
    jiffy = 0
    scheduled = [
         # [pid, arrival time, service time, waiting time, turnaround time, response ratio]
    ]
    aantal_processen = len(data)
    while data != []:
        response_ratios = [
            # [pid, arrival time, service time, respond_ratio]
        ]
        for process in data:
            arrival_time = process[1]
            if arrival_time <= jiffy:
                response_ratios.append([process[0], process[1], process[2], (jiffy - arrival_time + process[2]) / process[2]])
            else:
                break

        if response_ratios != []:
            response_ratios = sorted(response_ratios, key=lambda x: x[3], reverse = True)  # sorteren op hoogste response ratios
            data.remove(response_ratios[0][:3])
            pid = response_ratios[0][0]
            arrival_time = response_ratios[0][1]
            service_time = response_ratios[0][2]
            waiting_time = jiffy - arrival_time
            turnaround_time = waiting_time + service_time
            response_ratio = response_ratios[0][3]
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

    print("=========================== HRRN ===========================")
    print("Gemiddelde waiting_time: " + str(gemiddelde_waiting_time))
    print("Gemiddelde turnaround_time: " + str(gemiddelde_turnaround_time))
    print("Gemiddelde response_ratio: " + str(gemiddelde_response_ratio))

    return scheduled







#data = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5], [5, 8, 2]]  # zelfde data als op ppt, mean R is idd gelijk, dus onze berkeningen kloppen

data = parse_data("processen10000.xml")
scheduled = HRRN(data, True)
visualize_data(scheduled)