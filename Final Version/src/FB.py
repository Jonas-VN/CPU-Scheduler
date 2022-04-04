from src.functions import calculate_average
import random


# RR algoritme per process dat wordt toegepast per waiting queue
def RR(process, queue, scheduled, jiffy, debug):
    promotion = None

    if process[3] <= queue[0]:
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
        queue[2].remove(process)
    else:
        # Process zal nog niet klaar zijn na deze cycle
        if (random.random() <= queue[1]):
            # Process zal yielden en dus indien mogelijk een promotie ontvangen
            length = random.randint(1, queue[0] - 1)  # Random lengte van de quantum cycle (nooit de volledige quantum cycle)
            jiffy += length
            process[3] -= length
            promotion = True
        else:
            # Process zal niet yielden en dus een demotie ontvangen
            process[3] -= queue[0]
            jiffy += queue[0]
            promotion = False

    return queue, scheduled, jiffy, promotion


def FB(data, quanta, debug = False):
    #random.seed(1)

    waiting_queue1 = [quanta[0], 1/6, []]  # [quantum, chance of yielding, queue]
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
    while data != [] or waiting_queue1[2] != [] or waiting_queue2[2] != [] or waiting_queue3[2] != [] or waiting_queue4[2] != [] or waiting_queue5[2] != []:
        # Checken ofdat er een nieuw process moet worden toegevoegd
        for process in data:
            if process[1] <= jiffy:
                # Elk process begint standaard in de hoogste priority queue
                waiting_queue1[2].append(process)
                data.remove(process)
            else:
                # data is al gesorteerd op arrival time, dus als er 1 niet voldoet zullen de volgende ook niet voldoen
                break

        if waiting_queue1[2] != []:
            for process in waiting_queue1[2]:
                waiting_queue1, scheduled, jiffy, promotion = RR(process, waiting_queue1, scheduled, jiffy, debug)
                if promotion != None: 
                    if promotion:
                        pass
                    else:
                        waiting_queue1[2].remove(process)
                        waiting_queue2[2].append(process)
        
        # Elif's omdat de hogere queue eerst volledig leeg moet zijn voordat we aan een lagere prioriteit queue beginnen
        elif waiting_queue2[2] != []:
            for process in waiting_queue2[2]:
                waiting_queue2, scheduled, jiffy, promotion = RR(process, waiting_queue2, scheduled, jiffy, debug)
                if promotion != None:
                    if promotion:
                        waiting_queue2[2].remove(process)
                        waiting_queue1[2].append(process)
                    else:
                        waiting_queue2[2].remove(process)
                        waiting_queue3[2].append(process)

        elif waiting_queue3[2] != []:
            for process in waiting_queue3[2]:
                waiting_queue3, scheduled, jiffy, promotion = RR(process, waiting_queue3, scheduled, jiffy, debug)
                if promotion != None:
                    if promotion:
                        waiting_queue3[2].remove(process)
                        waiting_queue2[2].append(process)
                    else:
                        waiting_queue3[2].remove(process)
                        waiting_queue4[2].append(process)

        elif waiting_queue4[2] != []:
            for process in waiting_queue4[2]:
                waiting_queue4, scheduled, jiffy, promotion = RR(process, waiting_queue4, scheduled, jiffy, debug)
                if promotion != None:
                    if promotion:
                        waiting_queue4[2].remove(process)
                        waiting_queue3[2].append(process)
                    else:
                        waiting_queue4[2].remove(process)
                        waiting_queue5[2].append(process)

        elif waiting_queue5[2] != []:
            for process in waiting_queue5[2]:
                waiting_queue5, scheduled, jiffy, promotion = RR(process, waiting_queue5, scheduled, jiffy, debug)
                if promotion != None:
                    if promotion:
                        waiting_queue5[2].remove(process)
                        waiting_queue4[2].append(process)
                    else:
                        pass
        else:
            # Lege cycle
            jiffy += 1

    print(f"=========================== FB quanta={quanta} ({len(scheduled)} processes) ===========================")
    calculate_average(scheduled)

    return scheduled