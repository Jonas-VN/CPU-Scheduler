from src.functions import calculate_mean

def RR(data, quantum, debug = False):
    jiffy = 0
    scheduled = [
        # [pid, arrival time, service time, waiting time, turnaround time, response ratio]
    ]
    empty_cycle = True

    # Remaining service time toevoegen
    for process in data:
        process.append(process[2])
    
    while data != []:
        empty_cycle = True
        for process in data:
            arrival_time = process[1]
            if arrival_time <= jiffy:
                empty_cycle = False
                # Remaining time is kleiner dan (of gelijk aan) het quantum => process is afgerond na deze quantum cycle
                if process[3] <= quantum:
                    jiffy += process[3]
                    pid = process[0]
                    service_time = process[2]
                    waiting_time = jiffy - arrival_time - service_time
                    turnaround_time = service_time + waiting_time
                    response_ratio = turnaround_time / service_time
                    if debug: print(f"PID: {pid}\t Einde: {jiffy}\t Arrival time: {arrival_time}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
                    scheduled.append([pid, arrival_time, service_time, waiting_time, turnaround_time, response_ratio])
                    data.remove(process)

                # Process is nog niet klaar na deze quantum cycle    
                else:
                    process[3] -= quantum
                    jiffy += quantum
            else:
                # Processen staan geordend volgens arrivale time, als 1 niet gearriveerd is zal de rest ook nog niet gearriveerd zijn
                break
        if empty_cycle: 
            jiffy+= 1
            
    print(f"=========================== RR q={quantum} ({len(scheduled)} processes) ===========================")
    calculate_mean(scheduled)

    return scheduled
