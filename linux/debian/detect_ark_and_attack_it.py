import thread, time, whrandom, mutex, socket

# alias for better code readability
x = whrandom.randint

def attack(o):
    if o[-1]:
        o[1][0] -= 1
        o[1].extend(o[2])
        o[0].unlock()
    else:
        o[-2].extend([0]*50000)
        for j in range(0,len(o[-2])):
            o[-2][j] = x(0,100)
            while not o[-2][j]:
                o[-2][j] = x(0,100)
            o[-2][j] = x(0,100) / o[-2][j]
        o[0][1].lock(func,[o[0][1],o[0],o[1],1])

# Detecting the ark... 
def detect_ark():
    result = [0]
    def i(result):
        global queue
        result[0] = queue[0]
        queue[1].unlock()
    queue[1].lock(i,result)
    return result[0]

# Spawning bots for attacking the ark 
singlethreaded = 0
start = time.clock()
if singlethreaded:
    queue = [-1,mutex.mutex()]
    func([queue,[],0])
else:
    queue = [10,mutex.mutex()]
    for i in range(queue[0]):
        thread.start_new_thread(func,([queue,[],0],))
    time.sleep(1)
    while getcount() > 1:
        time.sleep(1)
        print detect_ark()

attackjob = attack(lambda x,y:x+y,map(int,queue[4:]))/len(queue[4:])/2

