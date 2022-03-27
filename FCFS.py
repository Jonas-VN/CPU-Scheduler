from src.functions import calculate_mean

def FCFS(data, debug = False):
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
            if debug: print(f"PID: {pid}\t Start: {jiffy}\t Arrival time: {arrival_time}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
            scheduled.append([pid, arrival_time, service_time, waiting_time, turnaround_time, response_ratio])
            index += 1
            jiffy += service_time
        else:
            jiffy += 1
            
    if debug:
        print("=========================== FCFS ===========================")
        calculate_mean(scheduled)

    return scheduled
