# jobs = []
# index = 0
# while True:

#     job = input()

#     if job == "-99":
#         break

#     print(job)

#     jobs.append([])

#     print(jobs)

#     job = job.split(" ")

#     print(job)

#     for j in job:
#         jobs[index].append(j)

#     print(jobs)
    
#     index += 1



# print(jobs)

# C13 W6 C18
# C6 W13 C9 W24 C3
# C24 W30 C4 W6 C20
# C20 W21 C17
# C28 W12 C15 W24 C4

jobs = [['C13', 'W6', 'C18'], ['C6', 'W13', 'C9', 'W24', 'C3'], ['C24', 'W30', 'C4', 'W6', 'C20'], ['C20', 'W21', 'C17'], ['C28', 'W12', 'C15', 'W24', 'C4']]

timeTaken = [0] * 5
completed = [False] * 5
allDone = ""
activeTime = 0
timeWaiting = 0

done = False

timeElapsed = 0

while not done:

    for i in range(len(jobs)):

        currentTimeElapsed = timeElapsed

        if completed[i] != True:
            for j in range(len(jobs[i])):
                task = jobs[i][j]
                if task[0] == "C":
                    timeForTask = ""
                    for k in range(1, len(task)):
                        timeForTask += task[k]
                    timeElapsed += int(timeForTask)
                    activeTime += int(timeForTask) 
                    task = list(task)
                    task[0] = "D"
                    task[1] = str(timeElapsed)
                    task = "".join(task)
                    jobs[i][j] = task[0:len(str(timeElapsed)) + 1]
                    if j == len(jobs[i]) - 1:
                        timeTaken[i] = timeElapsed
                        completed[i] = True
                        allDone += "#"
                    break

                elif task[0] == "W":
                    timeForWait = ""
                    for k in range(1, len(task)):
                        timeForWait += task[k]

                    computeTimeBeforeWait = ""
                    
                    for k in range(1, len(jobs[i][j-1])):
                        computeTimeBeforeWait += jobs[i][j-1][k]

                    if timeElapsed >= int(computeTimeBeforeWait) + int(timeForWait):
                        task = list(task)
                        task[0] = "D"
                        task = "".join(task)
                        jobs[i][j] = task
                        timeWaiting += int(timeForWait)

                    else:
                        if len(allDone) == len(jobs) - 1:
                            timeElapsed += int(timeForWait)
                            timeWaiting += int(timeForWait)
                            continue
                        break
        

        if currentTimeElapsed != timeElapsed:
            break

    if len(allDone) == len(jobs):
            done = True
print(f"Time Active = {activeTime}\nTime Waiting = {timeWaiting}")
for i in range(len(timeTaken)):
    print(f"Job {i} = {timeTaken[i]}s")
print(f"Throughput = {len(jobs)/ 205}")    
print(f"Processor utilization = {activeTime / 205}")   





