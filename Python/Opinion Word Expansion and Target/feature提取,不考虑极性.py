#输入{O}为情感词典中的情感词集。
#**输出所有可能的features{F}，即target集合
#输出扩展情感词集{O-Expand}
import pdb


corpus = open("positive_reln.txt","r")
noblank = []
for line in corpus:  # 把文件存到数组中
    line = line.rstrip()
    pairs = line.split('\t')  # 一句话里所有的pair
    sent = []
    for pair in pairs:
        information = pair.split()
        sent.append(information)
    noblank.append(sent)
    
str=corpus.read()#得到全部评论
corpus.close()

seedneg = []  # neg list
dic1= open("negative-words.txt","r")
for line in dic1:
    if ';' in line or len(line) < 2:
        continue
    word = line.rstrip()
    seedneg.append(word)
dic1.close()
seedpos = []
dic2= open("positive-words.txt","r")

for line in dic2:
    if ';' in line or len(line) < 2:
        continue
    word = line.rstrip()
    seedpos.append(word)
    
dic2.close()
tar= open("positive-words.txt","r")
Feature=tar.read()
tar.close()
#OEXP=seed
OEXP=seedneg+seedpos

Oi=[]#因为空集是一切的子集，不能用空集
Oo=[]#O'
negtivesen= [];
positivesen= [];
#Fi
Fi=[];
Ff=[];#F'
F=[];
negtivefea= [];
positivefea= [];
n=0
def R11(pair, F, Fi):
    if len(pair) == 0:
        return
    word1 = pair[0]
    pos1 = pair[2]
    word2 = pair[3]
    pos2 = pair[5]
    rel = pair[6]
    
    if 'NN' in pos1:
        if 'JJ' in pos2:
            if 'amod' in rel or 'nsubj' in rel:
                if word2 in OEXP and word1 not in F:
                    Fi.append(word1)
    if 'NN' in pos2:
        if 'JJ' in pos1:
            if 'amod' in rel or 'nsubj' in rel:
                if word1 in OEXP and word2 not in F:
                    Fi.append(word2)
    return Fi

def R12(pair1,pair2,F,Fi,OEXP):
    if len(pair1) == 0 or len(pair2):
        return
    word1 = pair1[0]
    pos1 = pair1[2]
    word2 = pair1[3]
    pos2 = pair1[5]
    rel1 = pair1[6]
    word3 = pair2[0]
    pos3 = pair2[2]
    word4 = pair2[3]
    pos4 = pair2[5]
    rel2 = pair2[6]
    if ('amod' in rel1 or 'nsubj' in rel1) and ('amod' in rel2 or 'nsubj' in rel2):
        if 'NN' in pos4:
            if word3 == word1:
                if word2 in OEXP and word4 not in F:
                    Fi.append(word4)
            if word3 == word2:
                if word3 in OEXP and word4 not in F:
                    Fi.append(word4)
        if 'NN' in pos3:
            if word4 == word1:
                if word2 in OEXP and word3 not in F:
                    Fi.append(word3)
            if word4 == word2:
                if word1 in OEXP and word3 not in F:
                    Fi.append(word3)
        if 'NN' in pos2:
            if word1 == word3:
                if word4 in OEXP and word2 not in F:
                    Fi.append(word2)
            if word1 == word4:
                if word3 in OEXP and word2 not in F:
                    Fi.append(word2)
        if 'NN' in pos1:
            if word2 == word3:
                if word4 in OEXP and word1 not in F:
                    Fi.append(word1)
            if word2 == word4:
                if word3 in OEXP and word1 not in F:
                    Fi.append(word1)        
    return Fi   
def R41(pair, OEXP, Oi):
    if len(pair) == 0:
        return
    word1 = pair[0]
    pos1 = pair[2]
    word2 = pair[3]
    pos2 = pair[5]
    rel = pair[6]
    
    if 'conj' in rel:
        if 'JJ' in pos1 and 'JJ' in pos2:
            if word1 in OEXP and word2 not in OEXP:
                Oi.append(word2)
            if word2 in OEXP and word1 not in OEXP:
                Oi.append(word1)
    return Oi
def R42(pair1,pair2,Oi,OEXP):
    if len(pair1) == 0 or len(pair2):
        return
    word1 = pair1[0]
    pos1 = pair1[2]
    word2 = pair1[3]
    pos2 = pair1[5]
    rel1 = pair1[6]
    word3 = pair2[0]
    pos3 = pair2[2]
    word4 = pair2[3]
    pos4 = pair2[5]
    rel2 = pair2[6]   
    if ('amod' in rel1 or 'nsubj' in rel1) and ('amod' in rel2 or 'nsubj' in rel2):
        if 'JJ' in pos4:
            if word3 == word1:
                if word2 in OEXP and word4 not in OEXP:
                    Oi.append(word4)
            if word3 == word2:
                if word3 in OEXP and word4 not in OEXP:
                    Oi.append(word4)
        if 'JJ' in pos3:
            if word4 == word1:
                if word2 in OEXP and word3 not in OEXP:
                    Oi.append(word3)
            if word4 == word2:
                if word1 in OEXP and word3 not in OEXP:
                    Oi.append(word3)
        if 'JJ' in pos2:
            if word1 == word3:
                if word4 in OEXP and word2 not in OEXP:
                    Oi.append(word2)
            if word1 == word4:
                if word3 in OEXP and word2 not in OEXP:
                    Oi.append(word2)
        if 'JJ' in pos1:
            if word2 == word3:
                if word4 in OEXP and word1 not in OEXP:
                    Oi.append(word1)
            if word2 == word4:
                if word3 in OEXP and word1 not in OEXP:
                    Oi.append(word1)    
    return Oi
def R31(pair, F, Ff):
    if len(pair) == 0:
        return
    word1 = pair[0]
    pos1 = pair[2]
    word2 = pair[3]
    pos2 = pair[5]
    rel = pair[6]

    
    if'conj' in rel:
        if 'NN' in pos1 and 'NN' in pos2 :
            if word2 in Fi and word1 not in F:
                Ff.append(word1)
        if 'NN' in pos2 and 'NN' in pos1:
            if word1 in Fi and word2 not in F:
                Ff.append(word2)        
         
    return Ff

def R32(pair1,pair2,Ff,OEXP):
    if len(pair1) == 0 or len(pair2):
        return
    word1 = pair1[0]
    pos1 = pair1[2]
    word2 = pair1[3]
    pos2 = pair1[5]
    rel1 = pair1[6]
    word3 = pair2[0]
    pos3 = pair2[2]
    word4 = pair2[3]
    pos4 = pair2[5]
    rel2 = pair2[6]   
    if rel1 == rel2:
        if 'NN' in pos4:
            if word3 == word2:
                if word1 in Fi and word4 not in F:
                    Ff.append(word4)
            if word3 == word1:
                if word2 in Fi and word4 not in F:
                    Ff.append(word4)
        if 'NN' in pos3:
            if word4 == word2:
                if word1 in Fi and word3 not in F:
                    Ff.append(word3)
            if word4 == word1:
                if word2 in Fi and word3 not in F:
                    Ff.append(word3)
        if 'NN' in pos2:
            if word1 == word3:
                if word4 in Fi and word2 not in F:
                    Ff.append(word2)
            if word1 == word4:
                if word3 in Fi and word2 not in F:
                    Ff.append(word2)
        if 'NN' in pos1:
            if word2 == word3:
                if word4 in Fi and word1 not in F:
                    Ff.append(word1)
            if word2 == word4:
                if word3 in Fi and word1 not in F:
                    Ff.append(word1)                                     
    return Ff
def R21(pair, Oi, Fi,OEXP):
    if len(pair) == 0:
        return
    word1 = pair[0]
    pos1 = pair[2]
    word2 = pair[3]
    pos2 = pair[5]
    rel = pair[6]

    
    if 'amod' in rel or 'nsubj' in rel:
        if 'JJ' in pos1:
            if word2 in Fi and word1 not in OEXP:
                Oi.append(word1)
        if 'JJ' in pos2:
            if word1 in Fi and word2 not in OEXP:
                Oi.append(word2)        
         
    return Oi
def R22(pair1,pair2,Oo,OEXP):
    if len(pair1) == 0 or len(pair2):
        return
    word1 = pair1[0]
    pos1 = pair1[2]
    word2 = pair1[3]
    pos2 = pair1[5]
    rel1 = pair1[6]
    word3 = pair2[0]
    pos3 = pair2[2]
    word4 = pair2[3]
    pos4 = pair2[5]
    rel2 = pair2[6]   
    if ('amod' in rel1 or 'nsubj' in rel1) and ('amod' in rel2 or 'nsubj' in rel2):
        if 'JJ' in pos4:
            if word3 == word1:
                if word2 in Fi and word4 not in OEXP:
                    Oo.append(word4)
            if word3 == word2:
                if word3 in Fi and word4 not in OEXP:
                    Oo.append(word4)
        if 'JJ' in pos3:
            if word4 == word1:
                if word2 in Fi and word3 not in OEXP:
                    Oo.append(word3)
            if word4 == word2:
                if word1 in Fi and word3 not in OEXP:
                    Oo.append(word3)
        if 'JJ' in pos2:
            if word1 == word3:
                if word4 in Fi and word2 not in OEXP:
                    Oo.append(word2)
            if word1 == word4:
                if word3 in Fi and word2 not in OEXP:
                    Oo.append(word2)
        if 'JJ' in pos1:
            if word2 == word3:
                if word4 in Fi and word1 not in OEXP:
                    Oo.append(word1)
            if word2 == word4:
                if word3 in Fi and word1 not in OEXP:
                    Oo.append(word1)    
    return Oo
   
while 1:
    for index, item in enumerate(noblank):#遍历列表找出nsubj和amod的索引值
        # R11
        print(1)
        for pair in item:
            R11(pair, F, Fi)
        R12(item[index],item[index-1],F,Fi,OEXP)
        
        for pair in item:
            R41(pair, OEXP, Oi)
        R42(item[index],item[index+1],Oi,OEXP)        

    F=F+Fi;
    OEXP=OEXP+Oi
    
    pdb.set_trace()

    for index, item in enumerate(noblank):#遍历列表找出nsubj和amod的索引值
        # R11
        print(1)
        for pair in item:
            R31(pair, F, Ff)
        R32(item[index],item[index+1],Ff,OEXP)
        
        for pair in item:
            R21(pair,Oi, Fi,OEXP)
        R22(item[index],item[index+1],Oo,OEXP)   


    Fi=Fi+Ff;
    Oi=Oi+Oo;
    F=F+Ff;
    OEXP=OEXP+Oo;
    print(F)
    if Fi==['2222'] and Oi==['1111']:
        break;

    Fi=['2222'];
    Oi=['1111'];
    print(F)

                    
       