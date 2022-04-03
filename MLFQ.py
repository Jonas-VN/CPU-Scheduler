from src.functions import parse_data, visualize_data


if __name__ == '__main__':
        data = parse_data("processen10000.xml")
        # index = 0
        total_p_no = len(data)  # aantal processen
        total_time = 0  # totale tijd te doen
        total_time_counted = 0  # totale tijd van proces dat al gescheduled is
        # proc is process list
        proc = []
        wait_time = 0
        turnaround_time = 0
        response_ratio = 0
        pid = 0
        priority = 0
        for index in range(total_p_no):
            # Getting the input for process
            service_time = data[index][2]
            arrival = data[index][1]
            remaining_time = service_time
            pid = data[index][0]

            # processes are appended to the proc list in following format
            proc.append([arrival, service_time, remaining_time, 0, pid, wait_time, turnaround_time, response_ratio,priority])
            # total_time gets incremented with burst time of each process
            total_time += service_time

        atime = arrival
        cbt = service_time

        # Declaring the queues and the quantum times
        qt1 = 2
        qt2 = 4
        qt3 = 6
        qt4 = 8
        q1 = []
        q2 = []
        q3 = []
        q4 = []
        # Making queue for the first Round Robin
        rrqueue1 = []
        # Entering the processes

        n = total_p_no #number of processes
        p = []

        # Making Arraylist for all the process parameters
        arrival = []
        i = 0
        while (i < n):
            arrival.append(proc[i][0])
            i += 1
        burst = []
        i = 0
        while (i < n):
            burst.append(proc[i][1])
            i += 1
        prio = []
        i = 0
        while (i < n):
            prio.append(proc[i][8])
            i += 1
        # Temporary Arraylist
        temp2 = []
        # Declaring thread

        # Storing the sum of all the CPU burst time and the total time needed for execution in sum
        sum = 0
        i = 0
        while i < len(burst):
            sum += burst[i]
            sum += arrival[i]
            i += 1
        sum += min(burst)
        try:
            leq2 = 0
            leq3 = 0
            leq4 = 0
            istwenty = False
            time = 0

            while time <= sum:
                # Storing in Round Robin Queue for all the Process which arrives first
                i = 0
                while i < len(arrival):
                    if time >= arrival[i] >= 0:
                        temp2.append(arrival[i])
                    i +=1
                counter = len(temp2)
                i = 0
                while i < counter:
                    minimum = min(temp2)

                    rrqueue1.append(burst[min(arrival)])
                    arrival[arrival.min] = -1
                    i += 1
                if not rrqueue1:
                    len = len(rrqueue1)
                    i = 0
                    while i < len:
                        q1.append(rrqueue1.pop(0))
                        i += 1
                # For Queue 1
                # Following Round Robin
                if not q1:
                    print("Processing In Queue 1")
                    if q1[0] < qt1:
                        print("Wait for " + str(q1[0]) + " Seconds...")
                    else:
                        print("Wait for 2 Seconds...")
                    i = 1
                    while i <= qt1:
                        # Process Executing

                        # Incrementing the time
                        time += 1
                        # Checking if the time is a multiple of 20
                        if time % 20 == 0 and time != 0:
                            istwenty = True
                        # reducing the burst time by 1
                        temp3 = 0
                        temp3 = q1.pop(0) - 1
                        burst[burst.indexOf(temp3 + 1)] = temp3
                        q1.insert(temp3)
                        # checking if the time becomes 0
                        if temp3 == 0:
                            if not q1:
                                q1.pop(0)
                            break
                        i += 1
                    if i == qt1 + 1:
                        temp = q1.pop(0)
                        q2.append(temp)
                elif not q2:
                    print("Processing In Queue 2")
                    if q2[0] < qt2:
                        print("Wait for " + str(q2[0]) + " Seconds...")
                    else:
                        print("Wait for 4 Seconds...")

                    i = 1
                    while (i <= qt2):


                        # Incrementing the time
                        time += 1
                        # Checking if the time is a multiple of 20
                        if (time % 20 == 0 and time != 0):
                            istwenty = True
                        # reducing the burst time by 1
                        temp3 = 0
                        temp3 = q2.pop(0) - 1
                        burst[burst.indexOf(temp3 + 1)] = temp3
                        q2.insert(temp3)
                        # checking if the time becomes 0
                        if (temp3 == 0):
                            if not q2:
                                q2.pop(0)
                            break
                        i += 1
                    if (i == qt2 + 1):
                        temp = q2.pop(0)
                        q3.append(temp)
                    leq2 = time
                elif not q3:
                    print("Processing In Queue 3")

                    if (q3[0] < qt3):
                        print("Wait for " + str(q3[0]) + " Seconds...")
                    else:
                        print("Wait for 6 Seconds...")

                    i = 1
                    while (i <= qt3):
                        # Process Executing

                        # Incrementing the time
                        time += 1
                        # Checking if the time is a multiple of 20
                        if (time % 20 == 0 and time != 0):
                            istwenty = True
                        # reducing the burst time by 1
                        temp3 = 0
                        temp3 = q3.pop(0) - 1
                        burst[burst.indexOf(temp3 + 1)] = temp3
                        q3.insert(temp3)
                        # checking if the time becomes 0
                        if (temp3 == 0):
                            if not q3:
                                q3.pop(0)
                            break
                        i += 1
                    if (i == qt3 + 1):
                        temp = q3.pop(0)
                        q4.append(temp)
                elif not q4:
                    print("Processing In Queue 4")

                    if (q4[0] < qt4):
                        print("Wait for " + str(q4[0]) + " Seconds...")
                    else:
                        print("Wait for 8 Seconds...")

                    i = 1
                    while (i <= qt4):

                        # Incrementing the time
                        time += 1
                        # Checking if the time is a multiple of 20
                        if (time % 20 == 0 and time != 0):
                            istwenty = True
                        # reducing the burst time by 1
                        temp3 = 0
                        temp3 = q4.pop(0) - 1
                        burst[burst.indexOf(temp3 + 1)] = temp3
                        q4.insert(temp3)
                        # checking if the time becomes 0
                        if (temp3 == 0):
                            if not q4:
                                q4.pop(0)
                            break
                        i += 1
                else:
                    # if all the queues are vacant the time increeases by 1
                    time += 1
                # Solution for starvation
                if (time % 20 == 0 and time != 0):
                    istwenty = True
                if (istwenty):
                    # Transferring all the processes of Queue 2 to Queue 1
                    while (len(q2) > 0):
                        q1.append(q2.pop(0))
                    # Transferring all the processes of Queue 3 to Queue 1
                    while (len(q3) > 0):
                        q1.append(q3.pop(0))
                    # Transferring all the processes of Queue 3 to Queue 1
                    while (len(q4) > 0):
                        q1.append(q4.pop(0))
                    istwenty = False
        # Catching Exception used for any exception for sleep function
        except Exception as e:
            print("There was an Exception")


