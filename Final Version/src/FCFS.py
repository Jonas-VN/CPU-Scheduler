from src.functions import calculate_average

def FCFS(data, debug = False):
    jiffy = 0  # 1 jiffy is 1 CPU cycle
    scheduled = [
        # [pid, arrival time, service time, waiting time, turnaround time, response ratio]
    ]

    while data != []:
        arrival_time = data[0][1]
        if arrival_time <= jiffy:
            pid = data[0][0]
            service_time = data[0][2]
            waiting_time = jiffy - arrival_time
            turnaround_time = service_time + waiting_time
            response_ratio = turnaround_time / service_time
            if debug: print(f"PID: {pid}\t Start: {jiffy}\t Arrival time: {arrival_time}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
            scheduled.append([pid, arrival_time, service_time, waiting_time, turnaround_time, response_ratio])
            jiffy += service_time
            data.remove(data[0])
        else:
            jiffy += 1

    print(f"=========================== FCFS ({len(scheduled)} processes) ===========================")
    calculate_average(scheduled)

    return scheduled