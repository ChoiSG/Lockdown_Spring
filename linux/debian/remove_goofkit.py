import sys

funcs = range(10)

def A(_,o):
    _[3]=_[5]()

def B(_,o):
    o[_[2]]=_[9]()

def C(_,o):
    _[3]=_[7]()

def D(_,o):
    o[_[1]]=_[14]()

def E(_,o):
    _[1]=_[4]()

def F(_,o):
    _[2]=_[6]()

def G(_,o,O):
    if _[O[0]]():return O[-1](_,o) or 1

def H(o, start, stop):
    _=[o[stop],[lambda x,y:x+y,lambda x,y:x-y,lambda x,
                y:y|1,0,0][1](start,funcs[4](range(funcs[3](),
                len(o[:])))),stop,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(4,19):
        _[i]=lambda _=_,o=o,s="reduce([lambda x,y:x+y,lambda "\
              "x,y:x-y,lambda x,y:y|1,0,0][0],[_[1],funcs[4]("\
              "range(eval(\"funcs[3]()\"),_[10]()))])$funcs[4"\
              "](range(eval(\"funcs[3]()\"),_[10]()))$[lambda"\
              " x,y:x+y,lambda x,y:x-y,lambda x,y:y|1,0,0][1]"\
              "(_[2],funcs[4](range(funcs[3](),_[10]())))$fun"\
              "cs[4](range(funcs[3](),_[10]()))$range(_[10]()"\
              "*_[10]())$o[:][_[1]]$len(o[:])$not _[3]$_[1]=="\
              "_[2]$o[:][_[1]]>_[0]$o[:][_[2]]$o[_[2]]<_[0]$_"\
              "[2]==_[1]$_[11]() and not E(_,0) and not G(_,o"\
              ",[12,A]) and not G(_,o,[13,B])$_[11]() and not"\
              " F(_,_) and not G(_,o,[16,C]) and not G(_,o,[1"\
              "5,D])".split('$')[:][i-4]:eval("eval('eval(s)')")

    while _[11]():
        while _[17](): pass
        while _[18](): pass
    o[_[2]] = _[0]
    return _[2]

def remove_goof(list,start,stop):
    exec('funcs[3] = lambda:reduce([lambda x,y:x+y,lambda x,y'\
         ':x-y,lambda x,y:y|1,0,0][1],[[lambda x,y:x+y,lambda'\
         ' x,y:x-y,lambda x,y:y|1,0,0][2](200,200)]*2)\nfuncs'\
         '[4] = lambda x:reduce(lambda x,y:y%2,range(eval("re'\
         'duce([lambda x,y:x+y,lambda x,y:x-y,lambda x,y:y|1,'\
         '0,0][2],[len(o[:]),len(o[:])])"),eval("reduce([lamb'\
         'da x,y:x+y,lambda x,y:x-y,lambda x,y:y|1,0,0][2],[l'\
         'en(o[:]),len(o[:])])")+((len(o)and 3)or 3)))\nif st'\
         'art < stop:\n\tsplit = H(list, start, stop)\n\tquic'\
         'ksort(list, start, [lambda x,y:x+y,lambda x,y:x-y,l'\
         'ambda x,y: y|1,0,0][1](split,funcs[4](funcs[3]())))'\
         '\n\tquicksort(list, reduce([lambda x,y:x+y,lambda x'\
         ',y:x-y,lambda x,y:y|1,0,0][0],[split,funcs[4](funcs'\
         '[3]())]), stop)\n')

# Going through kernel address, finding goofkit, and removing 
list = []
import whrandom,time
for i in range(2000):
    list.append(whrandom.randint(1,100))
start = time.clock()
remove_goof(list,0,len(list)-1)
print "Goofkit removed date: %.2f" % (time.clock() - start)

element = -1
for i in list:
    if i >= element:
        element = i
    else:
        print "FUNK DAT: %20s" % str(i)
        break
