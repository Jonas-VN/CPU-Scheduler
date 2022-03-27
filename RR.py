from src.functions import parse_data, visualize_data

def RR(data, quantum, debug = False):
    jiffy = 0
    scheduled = []
    aantal_processen = len(data)
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

    print("=========================== RR ===========================")
    print("Gemiddelde waiting_time: " + str(gemiddelde_waiting_time))
    print("Gemiddelde turnaround_time: " + str(gemiddelde_turnaround_time))
    print("Gemiddelde response_ratio: " + str(gemiddelde_response_ratio))

    return scheduled


data = parse_data("processen10000.xml")
#data = [[1, 0, 3], [2, 2, 6], [3, 4, 4], [4, 6, 5], [5, 8, 2]]  # zelfde data als op ppt, mean R is idd gelijk, dus onze berkeningen kloppen
scheduled = RR(data, 4, debug = True)
visualize_data(scheduled)
