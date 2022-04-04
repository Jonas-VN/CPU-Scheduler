from src.functions import calculate_average

def HRRN(data, debug = False):
    jiffy = 0
    scheduled = [
         # [pid, arrival time, service time, waiting time, turnaround time, response ratio]
    ]

    while data != []:
        response_ratios = [
            # [pid, arrival time, service time, response_ratio]
        ]
        for process in data:
            arrival_time = process[1]
            if arrival_time <= jiffy:
                response_ratios.append([process[0], process[1], process[2], (jiffy - arrival_time + process[2]) / process[2]])
            else:
                # data is al gesorteerd op arrival time, dus als er 1 niet voldoet zullen de volgende ook niet voldoen
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

    print(f"=========================== HRRN ({len(scheduled)} processes) ===========================")
    calculate_average(scheduled)

    return scheduled