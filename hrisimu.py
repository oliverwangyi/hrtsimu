import random

#generate all interaction pairs

pairs=[]

for i in range (1,2001):
    p = random.sample(range(1,20),2)
    pairs.append(p)

#print(pairs)
#print(len(pairs))


Rob = []
Hum = []
Rob_Hum = []

#suppose 4 robs, 16 human

for item in pairs:
    if item[0] <=4 and item[1] <=4:
        Rob.append(item)

#print(Rob)
#print(len(Rob))

for item in pairs:
    if item[0] > 4:
        if item[1] > 4:
            Hum.append(item)
        else:
            Rob_Hum.append(item)
    else:
        if item[1] > 4:
            Rob_Hum.append(item)


#That concludes generating the pairs

#switch order, lower first
Rob_s = []

for item in Rob:
    if item[0] < item[1]:
        Rob_s.append(item)
    else:
        Rob_s.append(item[: :-1])

Hum_s = []

for item in Hum:
    if item[0] < item[1]:
        Hum_s.append(item)
    else:
        Hum_s.append(item[: :-1])

Rob_Hum_s = []

for item in Rob_Hum:
    if item[0] < item[1]:
        Rob_Hum_s.append(item)
    else:
        Rob_Hum_s.append(item[: :-1])

#66-125, simulating rob-rob

rob_his = []


#initiating rob-rob history, first 5 random

temp = [[0 for col in range(2)] for row in range(5)]

for i in range(5):
    temp[i][0]=random.randint(1,4)
    temp[i][1]=random.randint(1,4)

for item in temp:
    rob_his.append(item)

rob_his_single = []

for item in rob_his:
    rob_his_single.append(item[0])
    rob_his_single.append(item[1])


maxlabel = max(rob_his_single,key=rob_his_single.count)

perturbation_n=round(len(Rob_s)*0.05)

#print(perturbation_n)

for i in range(len(Rob_s)-5):
    rob_his.append([maxlabel,maxlabel])

perturbation_substitute = random.sample(range(5,len(Rob_s)-1),perturbation_n)

#print(perturbation_substitute)

temp_p = [[0 for col in range(2)] for row in range(perturbation_n)]

for i in range(perturbation_n):
    temp_p[i][0]=random.randint(1,4)
    temp_p[i][1]=random.randint(1,4)

per_count = 0
for item in perturbation_substitute:
        rob_his[item]=temp_p[per_count]
        per_count = per_count + 1

#print(rob_his[perturbation_substitute[0]])


#write all rob-rob history to file








#This concludes rob-rob simu

#127-, simulating hun-hum

#This requires label pairs and history
#Ten labels:1-1, 1-2, 1-3, 1-4, 2-2, 2-3, 2-4, 3-3, 3-4, 4-4
#letter: a, b, c, d, e, f, g, h, i, j

label_list = []
for item in Hum_s:
    if 4 < item[0] < 9 and 4 < item[1] < 9:
        label_list.append('a')
    if 4 < item[0] < 9 and 8 < item[1] < 13:
        label_list.append('b')
    if 4 < item[0] < 9 and 12 < item[1] < 17:
        label_list.append('c')
    if 4 < item[0] < 9 and 16 < item[1] <= 20:
        label_list.append('d')
    if 8 < item[0] < 13 and 8 < item[1] < 13:
        label_list.append('e')
    if 8 < item[0] < 13 and 12 < item[1] < 17:
        label_list.append('f')
    if 8 < item[0] < 13 and 16 < item[1] <= 20:
        label_list.append('g')
    if 12 < item[0] < 17 and 12 < item[1] < 17:
        label_list.append('h')
    if 12 < item[0] < 17 and 16 < item[1] <= 20:
        label_list.append('i')
    if 16 < item[0] <= 20 and 16 < item[1] <= 20:
        label_list.append('j')

#print(len(label_list))

#print(label_list.count('a'))
#print(label_list.count('b'))
#print(label_list.count('c'))
#print(label_list.count('d'))
#print(label_list.count('e'))
#print(label_list.count('f'))
#print(label_list.count('g'))
#print(label_list.count('h'))
#print(label_list.count('i'))
#print(label_list.count('j'))

#get all different pairs
#keep the original index?

a_pair = []
for i in range(len(label_list)):
    if label_list[i] == 'a':
        a_pair.append(Hum_s[i])
b_pair = []
for i in range(len(label_list)):
    if label_list[i] == 'b':
        b_pair.append(Hum_s[i])
c_pair = []
for i in range(len(label_list)):
    if label_list[i] == 'c':
        c_pair.append(Hum_s[i])
d_pair = []
for i in range(len(label_list)):
    if label_list[i] == 'd':
        d_pair.append(Hum_s[i])
e_pair = []
for i in range(len(label_list)):
    if label_list[i] == 'e':
        e_pair.append(Hum_s[i])
f_pair = []
for i in range(len(label_list)):
    if label_list[i] == 'f':
        f_pair.append(Hum_s[i])
g_pair = []
for i in range(len(label_list)):
    if label_list[i] == 'g':
        g_pair.append(Hum_s[i])
h_pair = []
for i in range(len(label_list)):
    if label_list[i] == 'h':
        h_pair.append(Hum_s[i])
i_pair = []
for i in range(len(label_list)):
    if label_list[i] == 'i':
        i_pair.append(Hum_s[i])
j_pair = []
for i in range(len(label_list)):
    if label_list[i] == 'j':
        j_pair.append(Hum_s[i])


#consistency check

if (len(a_pair)+len(b_pair)+len(c_pair)+len(d_pair)+len(e_pair)+len(f_pair)+len(g_pair)+len(h_pair)+len(i_pair)+len(j_pair))!=len(Hum_s):
    print("ERROR")
else:
    pass

#get the pertubation positions
#perturbation_n=round(len(Hum_s)*0.05)

#set idiosyncratic payoff, change here if you like
idi_one = [0.8, 0.4, 0, 0]
idi_two = [0.4, 0.8, 0, 0]
idi_three = [0, 0, 0.8, 0.4]
idi_four = [0, 0, 0.4, 0.8]

#let memory size == 3, initiate it
memory=[[0,0],[0,0],[0,0]]

#interactions of a-pairs-same
#deal with a-pairs

a_his = []

perturbation_pos_a = random.sample(range(6, len(a_pair)), round(len(a_pair)*0.05))
perturbation_pos_a = sorted(perturbation_pos_a)
print(perturbation_pos_a)


#first 5 are randomly generated:



#calculating potential payoff from memory.
def calculate_strategy_a(memoryA, memoryB):
    t1 = [0,0,0]
    t2 = [0,0,0]
    for i in range(len(memoryA)):
        t1[i] = memoryB[i][0]
        t2[i] = memoryA[i][1]
    dis1 = [t2.count(1)/3, t2.count(2)/3]
    dis2 = [t1.count(1)/3, t1.count(2)/3]
    payoff1_A = 1.8 * dis1[0] + 0.8 * dis1[1]
    payoff2_A = 0.4 * dis1[0] + 1.4 * dis1[1]
    if payoff1_A >= payoff2_A: #>= implements the tie-breaker
        n = 1
    else:
        n = 2
    payoff1_B = 1.8 * dis2[0] + 0.8 * dis2[1]
    payoff2_B = 0.4 * dis2[0] + 1.4 * dis2[1]
    if payoff1_B >= payoff2_B:
        m = 1
    else:
        m = 2
    return [n,m]

#testing a little bit
#memoryA = [[1, 1], [1, 2], [2, 1]]
#memoryB = [[2, 2], [2, 2], [2, 2]]
#print(calculate_strategy(memoryA, memoryB))

def random_pick_a():
    n = random.randint(1,2)
    m = random.randint(1,2)
    return [n,m]

a_his = []

temp = [[0 for col in range(2)] for row in range(5)]

for i in range(5):
    temp[i][0]=random.randint(1,2)
    temp[i][1]=random.randint(1,2)

for item in temp:
    a_his.append(item)



memoryA = []
memoryB = []

#form history iteratively
for i in range(5, len(a_pair)):
    memoryA = random.sample(a_his,3)
    memoryB = random.sample(a_his,3)
    if i not in perturbation_pos_a:
        k = calculate_strategy_a(memoryA, memoryB)
        a_his.append(k)
    else:
        k = random_pick_a()
        a_his.append(k)


if len(a_his)!= len(a_pair):
    print('ERROR')
else:
    print(a_his)


#interactions of b-pairs
#deal with b-pairs

#interactions of c-pairs

#interactions of d-pairs
#no overleap, skip


#interactions of e-pairs-same

e_his = []

perturbation_pos_e = random.sample(range(6, len(e_pair)), round(len(e_pair) * 0.05))
perturbation_pos_e = sorted(perturbation_pos_e)
print(perturbation_pos_e)

def calculate_strategy_e(memoryA, memoryB):
    t1 = [0,0,0]
    t2 = [0,0,0]
    for i in range(len(memoryA)):
        t1[i] = memoryB[i][0]
        t2[i] = memoryA[i][1]
    dis1 = [t2.count(1)/3, t2.count(2)/3, t2.count(3)/3]
    #print(dis1)
    dis2 = [t1.count(1)/3, t1.count(2)/3, t1.count(3)/3]
    #print(dis2)
    payoff1_A = 1.4 * dis1[0] + 0.4 * dis1[1] + 0.4 * dis1[2]
    payoff2_A = 0.8 * dis1[0] + 1.8 * dis1[1] + 0.8 * dis1[2]
    payoff3_A = 0 * dis1[0] + 0 * dis1[1] + 1 * dis1[2]
    if payoff1_A > payoff2_A and payoff1_A > payoff3_A:
        n = 1
    if payoff2_A >= payoff1_A and payoff2_A >= payoff3_A: #>= implements the tie-breaker
        n = 2
    if payoff3_A > payoff1_A and payoff3_A > payoff2_A:
        n = 3

    payoff1_B = 1.4 * dis2[0] + 0.4 * dis2[1] + 0.4 * dis2[2]
    payoff2_B = 0.8 * dis2[0] + 1.8 * dis2[1] + 0.8 * dis2[2]
    payoff3_B = 0 * dis2[0] + 0 * dis2[1] + 1 * dis2[2]
    if payoff1_B > payoff2_B and payoff1_B > payoff3_B:
        m = 1
    if payoff2_B >= payoff1_B and payoff2_B >= payoff3_B:
        m = 2
    if payoff3_B > payoff1_B and payoff3_B > payoff2_B:
        m = 3


    return [n,m]

# testing a little bit
#memoryA = [[1, 1], [1, 1], [1, 3]]
#memoryB = [[1, 2], [1, 2], [1, 2]]

#print(calculate_strategy_b(memoryA, memoryB))

def random_pick_e():
    n = random.randint(1,3)
    m = random.randint(1,3)
    return [n,m]

e_his = []

temp = [[0 for col in range(2)] for row in range(5)]

for i in range(5):
    temp[i][0] = random.randint(1, 3)
    temp[i][1] = random.randint(1, 3)

for item in temp:
    e_his.append(item)

#print(b_his)

memoryA = []
memoryB = []

#form history iteratively
for i in range(5, len(e_pair)):
    memoryA = random.sample(e_his,3)
    memoryB = random.sample(e_his,3)
    if i not in perturbation_pos_e:
        k = calculate_strategy_e(memoryA, memoryB)
        e_his.append(k)
    else:
        k = random_pick_e()
        e_his.append(k)

if len(e_his)!= len(e_pair):
    print('ERROR')
else:
    print(e_his)
#interactions of f-pairs

#interactions of g-pairs

#interactions of h-pairs-same
h_his = []

perturbation_pos_h = random.sample(range(6, len(h_pair)), round(len(h_pair) * 0.05))
perturbation_pos_h = sorted(perturbation_pos_h)
print(perturbation_pos_h)


def calculate_strategy_h(memoryA, memoryB):
    t1 = [0, 0, 0]
    t2 = [0, 0, 0]
    for i in range(len(memoryA)):
        t1[i] = memoryB[i][0]
        t2[i] = memoryA[i][1]
    dis1 = [t2.count(2) / 3, t2.count(3) / 3, t2.count(4) / 3]
    # print(dis1)
    dis2 = [t1.count(2) / 3, t1.count(3) / 3, t1.count(4) / 3]
    # print(dis2)
    payoff2_A = 1 * dis1[0] + 0 * dis1[1] + 0 * dis1[2]
    payoff3_A = 0.8 * dis1[0] + 1.8 * dis1[1] + 0.8 * dis1[2]
    payoff4_A = 0.4 * dis1[0] + 0.4 * dis1[1] + 1.4 * dis1[2]
    if payoff2_A > payoff3_A and payoff2_A > payoff4_A:
        n = 2
    if payoff3_A >= payoff2_A and payoff3_A >= payoff4_A:  # >= implements the tie-breaker
        n = 3
    if payoff4_A > payoff2_A and payoff4_A > payoff3_A:
        n = 4

    payoff2_B = 1 * dis2[0] + 0 * dis2[1] + 0 * dis2[2]
    payoff3_B = 0.8 * dis2[0] + 1.8 * dis2[1] + 0.8 * dis2[2]
    payoff4_B = 0.4 * dis2[0] + 0.4 * dis2[1] + 1.4 * dis2[2]
    if payoff2_B > payoff3_B and payoff2_B > payoff4_B:
        m = 2
    if payoff3_B >= payoff2_B and payoff3_B >= payoff4_B:
        m = 3
    if payoff4_B > payoff2_B and payoff4_B > payoff3_B:
        m = 4

    return [n, m]


    # testing a little bit
memoryA = [[2, 2], [3, 2], [4, 2]]
memoryB = [[3, 2], [3, 3], [4, 3]]

print(calculate_strategy_h(memoryA, memoryB))

def random_pick_h():
    n = random.randint(2, 4)
    m = random.randint(2, 4)
    return [n, m]


h_his = []

temp = [[0 for col in range(2)] for row in range(5)]

for i in range(5):
    temp[i][0] = random.randint(2, 4)
    temp[i][1] = random.randint(2, 4)

for item in temp:
    h_his.append(item)

    # print(b_his)

memoryA = []
memoryB = []

    # form history iteratively
for i in range(5, len(h_pair)):
    memoryA = random.sample(h_his, 3)
    memoryB = random.sample(h_his, 3)
    if i not in perturbation_pos_h:
        k = calculate_strategy_h(memoryA, memoryB)
        h_his.append(k)
    else:
        k = random_pick_h()
        h_his.append(k)

if len(h_his) != len(h_pair):
    print('ERROR')
else:
    print(h_his)

#interactions of i-pairs

#interactions of j-pairs-same
