class Process:
    # Process arrival time , CPU burst time and priority
    atime = 0
    cbt = 0
    priority = 0

    # Taking input for the variables
    def input(self):
        sc = "Python-inputs"
        print("Enter Process Priority: ")
        self.priority = input()
        print("Enter Process Arrival Time: ")
        self.atime = input()
        print("Enter Process CPU Burst Time: ")
        self.cbt = input()

    @staticmethod
    def main(args):
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
        print("Enter the number of process:- ")
        sc = "Python-inputs"
        n = input()
        p = [None] * (n)
        i = 0
        while (i < n):
            p[i] = Process()
            p[i].input()
            i += 1
        # Making Arraylist for all the process parameters
        arrival = []
        i = 0
        while (i < n):
            arrival.append(p[i].atime)
            i += 1
        burst = []
        i = 0
        while (i < n):
            burst.append(p[i].cbt)
            i += 1
        prio = []
        i = 0
        while (i < n):
            prio.append(p[i].priority)
            i += 1
        # Temporary Arraylist
        temp2 = []
        # Declaring thread

        # Storing the sum of all the CPU burst time and the total time needed for execution in sum
        sum = 0
        i = 0
        while (i < len(burst)):
            sum += burst[i]
            sum += arrival[i]
            i += 1
        sum = sum + Collections.min(burst)
        try:
            leq2 = 0
            leq3 = 0
            leq4 = 0
            istwenty = False
            time = 0
            while (time <= sum):
                # Storing in Round Robin Queue for all the Process which arrives first
                i = 0
                while (i < len(arrival)):
                    if (arrival[i] <= time and arrival[i] >= 0):
                        temp2.append(arrival[i])
                    i += 1
                counter = len(temp2)
                i = 0
                while (i < counter):
                    min = Collections.min(temp2)
                    del temp2[temp2.indexOf(min)]
                    rrqueue1.append(burst[arrival.indexOf(min)])
                    arrival[arrival.indexOf(min)] = -1
                    i += 1
                if (rrqueue1.isEmpty() == False):
                    len = rrqueue1.size()
                    i = 0
                    while (i < len):
                        q1.add(rrqueue1.pop(0))
                        i += 1
                # For Queue 1
                # Following Round Robin
                if (q1.isEmpty() == False):
                    print("Processing In Queue 1")
                    print("Executing Process P" + str(prio[burst.indexOf(q1[0])]))
                    if (q1[0] < qt1):
                        print("Wait for " + str(q1[0]) + " Seconds...")
                    else:
                        print("Wait for 2 Seconds...")
                    i = 1
                    i = 1
                    while (i <= qt1):
                        # Process Executing

                        # Incrementing the time
                        time += 1
                        # Checking if the time is a multiple of 20
                        if (time % 20 == 0 and time != 0):
                            istwenty = True
                        # reducing the burst time by 1
                        temp3 = 0
                        temp3 = q1.removeFirst() - 1
                        burst[burst.indexOf(temp3 + 1)] = temp3
                        q1.addFirst(temp3)
                        # checking if the time becomes 0
                        if (temp3 == 0):
                            if (q1.isEmpty() == False):
                                q1.pop(0)
                            break
                        i += 1
                    if (i == qt1 + 1):
                        temp = q1.pop(0)
                        q2.append(temp)
                elif (q2.isEmpty() == False):
                    print("Processing In Queue 2")
                    print("Executing Process P" + str(prio[burst.indexOf(q2[0])]))
                    if (q2[0] < qt2):
                        print("Wait for " + str(q2[0]) + " Seconds...")
                    else:
                        print("Wait for 4 Seconds...")
                    i = 1
                    i = 1
                    while (i <= qt2):


                        # Incrementing the time
                        time += 1
                        # Checking if the time is a multiple of 20
                        if (time % 20 == 0 and time != 0):
                            istwenty = True
                        # reducing the burst time by 1
                        temp3 = 0
                        temp3 = q2.removeFirst() - 1
                        burst[burst.indexOf(temp3 + 1)] = temp3
                        q2.addFirst(temp3)
                        # checking if the time becomes 0
                        if (temp3 == 0):
                            if (q2.isEmpty() == False):
                                q2.pop(0)
                            break
                        i += 1
                    if (i == qt2 + 1):
                        temp = q2.pop(0)
                        q3.append(temp)
                    leq2 = time
                elif (q3.isEmpty() == False):
                    print("Processing In Queue 3")
                    print("Executing Process P" + str(prio[burst.indexOf(q3[0])]))
                    if (q3[0] < qt3):
                        print("Wait for " + str(q3[0]) + " Seconds...")
                    else:
                        print("Wait for 6 Seconds...")
                    i = 1
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
                        temp3 = q3.removeFirst() - 1
                        burst[burst.indexOf(temp3 + 1)] = temp3
                        q3.addFirst(temp3)
                        # checking if the time becomes 0
                        if (temp3 == 0):
                            if (q3.isEmpty() == False):
                                q3.pop(0)
                            break
                        i += 1
                    if (i == qt3 + 1):
                        temp = q3.pop(0)
                        q4.append(temp)
                elif (q4.isEmpty() == False):
                    print("Processing In Queue 4")
                    print("Executing Process P" + str(prio[burst.indexOf(q4[0])]))
                    if (q4[0] < qt4):
                        print("Wait for " + str(q4[0]) + " Seconds...")
                    else:
                        print("Wait for 8 Seconds...")
                    i = 1
                    i = 1
                    while (i <= qt4):

                        # Incrementing the time
                        time += 1
                        # Checking if the time is a multiple of 20
                        if (time % 20 == 0 and time != 0):
                            istwenty = True
                        # reducing the burst time by 1
                        temp3 = 0
                        temp3 = q4.removeFirst() - 1
                        burst[burst.indexOf(temp3 + 1)] = temp3
                        q4.addFirst(temp3)
                        # checking if the time becomes 0
                        if (temp3 == 0):
                            if (q4.isEmpty() == False):
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
                    while (q2.size() > 0):
                        q1.append(q2.pop(0))
                    # Transferring all the processes of Queue 3 to Queue 1
                    while (q3.size() > 0):
                        q1.append(q3.pop(0))
                    # Transferring all the processes of Queue 3 to Queue 1
                    while (q4.size() > 0):
                        q1.append(q4.pop(0))
                    istwenty = False
        # Catching Exception used for any exception for sleep function
        except Exception as e:
            print("There was an Exception")


if __name__ == "__main__":
    Process.main([])