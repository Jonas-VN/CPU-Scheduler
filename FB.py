from src.functions import calculate_mean
import random

def FB(data, quanta, debug = False):
    waiting_queue1 = [quanta[0], 1/6, []]
    waiting_queue2 = [quanta[1], 2/6, []]
    waiting_queue3 = [quanta[2], 3/6, []]
    waiting_queue4 = [quanta[3], 4/6, []]
    waiting_queue5 = [quanta[4], 5/6, []]

    jiffy = 0
    scheduled = [
        # [pid, arrival time, service time, waiting time, turnaround time, response ratio]
    ]

    # Remaining service time toevoegen
    for process in data:
        process.append(process[2])

    # Zolang de data niet leeg is en de queues ook niet leeg zijn moet er gewerkt worden
    while data != [] or (waiting_queue1[2] != [] or waiting_queue2[2] != [] or waiting_queue3[2] != [] or waiting_queue4[2] != [] or waiting_queue5[2] != []):
        # Checken ofdat er een nieuw process moet worden toegevoegd
        for process in data:
            if process[1] <= jiffy:
                # Elk process begint standaard in de hoogste priority queue
                waiting_queue5[2].append(process)
                data.remove(process)
            else:
                break

        if waiting_queue1[2] != []:
            for process in waiting_queue1[2]:
                if process[3] <= waiting_queue1[0]:
                    # Process zal klaar zijn na deze cycle (geen rekening gehouden dat voor deze quantum cycle ook geyield kan worden, 
                    # maar dat is niet belangrijk omdat ze toch klaar zullen zijn en dus niks meer hebben aan een eventuele promotie/demotie)
                    jiffy += process[3]
                    pid = process[0]
                    service_time = process[2]
                    waiting_time = jiffy - process[1] - service_time
                    turnaround_time = service_time + waiting_time
                    response_ratio = turnaround_time / service_time
                    if debug: print(f"PID: {pid}\t Einde: {jiffy}\t Arrival time: {process[1]}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
                    scheduled.append([pid, process[1], service_time, waiting_time, turnaround_time, response_ratio])
                    waiting_queue1[2].remove(process)
                else:
                    # Process zal nog niet klaar zijn na deze cycle
                    if (random.random() <= waiting_queue1[1]):
                        # Process zal yielden en dus indien mogelijk een promotie ontvangen, 
                        # omdat het hier alreeds in de hoogste priority queue staat is dit niet mogelijk maar houdt het zijn plek in de hoogste priority queue
                        lenght = random.randint(1, waiting_queue1[0])  # Random lengte van de quantum cycle (nooit de volledige quantum cycle)
                        jiffy += lenght
                        process[3] -= lenght
                    else:
                        # Process zal niet yielden en dus een demotie ontvangen
                        process[3] -= waiting_queue1[0]
                        jiffy += waiting_queue1[0]
                        waiting_queue1[2].remove(process)
                        waiting_queue2[2].append(process)

        elif waiting_queue2[2] != []:
            for process in waiting_queue2[2]:
                if process[3] <= waiting_queue2[0]:
                    # Process zal klaar zijn na deze cycle (geen rekening gehouden dat voor deze quantum cycle ook geyield kan worden, 
                    # maar dat is niet belangrijk omdat ze toch klaar zullen zijn en dus niks meer hebben aan een eventuele promotie/demotie)
                    jiffy += process[3]
                    pid = process[0]
                    service_time = process[2]
                    waiting_time = jiffy - process[1] - service_time
                    turnaround_time = service_time + waiting_time
                    response_ratio = turnaround_time / service_time
                    if debug: print(f"PID: {pid}\t Einde: {jiffy}\t Arrival time: {process[1]}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
                    scheduled.append([pid, process[1], service_time, waiting_time, turnaround_time, response_ratio])
                    waiting_queue2[2].remove(process)
                else:
                    # Process zal nog niet klaar zijn na deze cycle
                    if (random.random() <= waiting_queue2[1]):
                        # Process zal yielden en dus indien mogelijk een promotie ontvangen
                        lenght = random.randint(1, waiting_queue2[0])  # Random lengte van de quantum cycle (nooit de volledige quantum cycle)
                        jiffy += lenght
                        process[3] -= lenght
                        waiting_queue2[2].remove(process)
                        waiting_queue1[2].append(process)
                    else:
                        # Process zal niet yielden en dus een demotie ontvangen
                        process[3] -= waiting_queue2[0]
                        jiffy += waiting_queue2[0]
                        waiting_queue2[2].remove(process)
                        waiting_queue3[2].append(process)

        elif waiting_queue3[2] != []:
            for process in waiting_queue3[2]:
                if process[3] <= waiting_queue3[0]:
                    # Process zal klaar zijn na deze cycle (geen rekening gehouden dat voor deze quantum cycle ook geyield kan worden, 
                    # maar dat is niet belangrijk omdat ze toch klaar zullen zijn en dus niks meer hebben aan een eventuele promotie/demotie)
                    jiffy += process[3]
                    pid = process[0]
                    service_time = process[2]
                    waiting_time = jiffy - process[1] - service_time
                    turnaround_time = service_time + waiting_time
                    response_ratio = turnaround_time / service_time
                    if debug: print(f"PID: {pid}\t Einde: {jiffy}\t Arrival time: {process[1]}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
                    scheduled.append([pid, process[1], service_time, waiting_time, turnaround_time, response_ratio])
                    waiting_queue3[2].remove(process)
                else:
                    # Process zal nog niet klaar zijn na deze cycle
                    if (random.random() <= waiting_queue3[1]):
                        # Process zal yielden en dus indien mogelijk een promotie ontvangen
                        lenght = random.randint(1, waiting_queue3[0])  # Random lengte van de quantum cycle (nooit de volledige quantum cycle)
                        jiffy += lenght
                        process[3] -= lenght
                        waiting_queue3[2].remove(process)
                        waiting_queue2[2].append(process)
                    else:
                        # Process zal niet yielden en dus een demotie ontvangen
                        process[3] -= waiting_queue3[0]
                        jiffy += waiting_queue3[0]
                        waiting_queue3[2].remove(process)
                        waiting_queue4[2].append(process)

        elif waiting_queue4[2] != []:
            for process in waiting_queue4[2]:
                if process[3] <= waiting_queue4[0]:
                    # Process zal klaar zijn na deze cycle (geen rekening gehouden dat voor deze quantum cycle ook geyield kan worden, 
                    # maar dat is niet belangrijk omdat ze toch klaar zullen zijn en dus niks meer hebben aan een eventuele promotie/demotie)
                    jiffy += process[3]
                    pid = process[0]
                    service_time = process[2]
                    waiting_time = jiffy - process[1] - service_time
                    turnaround_time = service_time + waiting_time
                    response_ratio = turnaround_time / service_time
                    if debug: print(f"PID: {pid}\t Einde: {jiffy}\t Arrival time: {process[1]}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
                    scheduled.append([pid, process[1], service_time, waiting_time, turnaround_time, response_ratio])
                    waiting_queue4[2].remove(process)
                else:
                    # Process zal nog niet klaar zijn na deze cycle
                    if (random.random() <= waiting_queue4[1]):
                        # Process zal yielden en dus indien mogelijk een promotie ontvangen
                        lenght = random.randint(1, waiting_queue4[0])  # Random lengte van de quantum cycle (nooit de volledige quantum cycle)
                        jiffy += lenght
                        process[3] -= lenght
                        waiting_queue4[2].remove(process)
                        waiting_queue3[2].append(process)
                    else:
                        # Process zal niet yielden en dus een demotie ontvangen
                        process[3] -= waiting_queue4[0]
                        jiffy += waiting_queue4[0]
                        waiting_queue4[2].remove(process)
                        waiting_queue5[2].append(process)

        elif waiting_queue5[2] != []:
            for process in waiting_queue5[2]:
                if process[3] <= waiting_queue5[0]:
                    # Process zal klaar zijn na deze cycle (geen rekening gehouden dat voor deze quantum cycle ook geyield kan worden, 
                    # maar dat is niet belangrijk omdat ze toch klaar zullen zijn en dus niks meer hebben aan een eventuele promotie/demotie)
                    jiffy += process[3]
                    pid = process[0]
                    service_time = process[2]
                    waiting_time = jiffy - process[1] - service_time
                    turnaround_time = service_time + waiting_time
                    response_ratio = turnaround_time / service_time
                    if debug: print(f"PID: {pid}\t Einde: {jiffy}\t Arrival time: {process[1]}\t Service time: {service_time}\t Waiting time: {waiting_time}\t Turnaround time: {turnaround_time}\t Response ratio: {round(response_ratio, 2)}")
                    scheduled.append([pid, process[1], service_time, waiting_time, turnaround_time, response_ratio])
                    waiting_queue5[2].remove(process)
                else:
                    # Process zal nog niet klaar zijn na deze cycle
                    if (random.random() <= waiting_queue5[1]):
                        # Process zal yielden en dus indien mogelijk een promotie ontvangen
                        lenght = random.randint(1, waiting_queue5[0])  # Random lengte van de quantum cycle (nooit de volledige quantum cycle)
                        jiffy += lenght
                        process[3] -= lenght
                        waiting_queue5[2].remove(process)
                        waiting_queue4[2].append(process)
                    else:
                        # Process zal niet yielden en dus een demotie ontvangen, 
                        # omdat het hier alreeds in de laagste priority queue staat is dit niet mogelijk maar houdt het zijn plek in de laagste priority queue
                        process[3] -= waiting_queue5[0]
                        jiffy += waiting_queue5[0]
        else:
            # Lege cycle
            jiffy += 1

    print(f"=========================== FB {quanta} ({len(scheduled)} processes) ===========================")
    calculate_mean(scheduled)

    return scheduled
