from src.functions import calculate_mean

def SRT(data, debug = False):
    jiffy = 0
    scheduled = [
        # [pid, arrival time, service time, waiting time, turnaround time, response ratio]
    ]

    # Remaining service time toevoegen
    for process in data:
        process.append(process[2])
    
    while data != []:
        waiting_queue = []
        for process in data:
            arrival_time = process[1]
            if arrival_time <= jiffy:
                waiting_queue.append(process)
            else:
                break

        jiffy += 1
        if waiting_queue != []:
            waiting_queue = sorted(waiting_queue, key=lambda x:x[3])
            process = waiting_queue[0]

            # Laatste cycle voordat het process klaar is
            if process[3] <= 1:
                pid = process[0]
                arrival_time = process[1]
                service_time = process[2]
                waiting_time = jiffy - arrival_time - service_time
                turnaround_time = service_time + waiting_time
                response_ratio = turnaround_time / service_time
                if debug: print(f"PID: {pid}\t Einde: {jiffy}\t Arrival time: {arrival_time}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
                scheduled.append([pid, arrival_time, service_time, waiting_time, turnaround_time, response_ratio])
                data.remove(process)

            else:
                process[3] -= 1

    print(f"=========================== SRT ({len(scheduled)} processes) ===========================")
    calculate_mean(scheduled)

    return scheduled
