#因\t影响查找关系在列表中的索引，提前在txt中把\t替换为空格
corpus = open("/positive_reln1.txt","r")
str=corpus.read()#得到全部评论
corpus.close()

dic1= open("negative-words.txt","r")
seedneg=dic1.read()
dic1.close()
dic2= open("positive-words.txt","r")
seedpos=dic2.read()
dic2.close()

negtivesen= [];
negtivefea= [];
positivesen= [];
positivefea= [];
noblank=str.split(" ")#用空格分割全部评论

n=0;#记while循环次数
#加循环，扩大seed集，直到seed长度不再变化
while 1:

#找出 nsubj的索引值print(noblank.index('nsubj'))
    for index, item in enumerate(noblank):#遍历列表找出nsubj和amod的索引值
        if item=='nsubj'or item=='amod':
       # print(index, item) negtivesen.append( sssindex );
            if noblank[index-1]=='NN' and noblank[index-4]=='JJ':#noblank[index-3](全是名词),noblank[index-6](全是形容词)
           # R21+negative：用f提取s.if noblank[index-3] exist in seedneg:把noblank[index-3]加入sensitive集 (把noblank[index-6]加入negtivesen集)
               if noblank[index-3] in seedneg:
                   negtivesen.append( noblank[index-6]);    
           # R21+positive：用f提取s.if noblank[index-3] exist in seedpos:把noblank[index-3]加入sensitive集 (把noblank[index-6]加入positivesen集)
               if noblank[index-3] in seedpos:
                   positivesen.append( noblank[index-6]); 
           # R31+negative：用s提取f.if noblank[index-6] exist in seedneg:把noblank[index-3]加入feature集 (把noblank[index-3]加入negtivefea集)
               if noblank[index-6] in seedneg:
                   negtivefea.append( noblank[index-3]); 
           # R31+positive：用s提取f.if noblank[index-6] exist in seedpos:把noblank[index-3]加入feature集 (把noblank[index-3]加入positivefea集)
               if noblank[index-6] in seedpos:
                   positivefea.append( noblank[index-3]);
        #elif noblank[index-1]=='NN' and noblank[index-4]=='NN':
            elif noblank[index-1]=='JJ' and noblank[index-4]=='NN':#noblank[index-3](全是形容词),noblank[index-6](全是名词)
           # R21+negative：用f提取s.if noblank[index-6] exist in seedneg:把noblank[index-3]加入sensitive集 (把noblank[index-3]加入negtivesen集)
               if noblank[index-6] in seedneg:
                   negtivesen.append( noblank[index-3]);  
           # R21+positive：用f提取s.if noblank[index-6] exist in seedpos:把noblank[index-3]加入sensitive集 (把noblank[index-3]加入positivesen集)
               if noblank[index-6] in seedpos:
                   positivesen.append( noblank[index-3]);  
           # R31+negative：用s提取f.if noblank[index-3] exist in seedneg:把noblank[index-6]加入feature集 (把noblank[index-6]加入negtivefea集)
               if noblank[index-3] in seedneg:
                   negtivefea.append( noblank[index-6]);  
           # R31+positive：用s提取f.if noblank[index-3] exist in seedpos:把noblank[index-6]加入feature集 (把noblank[index-6]加入positivefea集)
               if noblank[index-3] in seedpos:
                   positivefea.append( noblank[index-6]); 
        #elif noblank[index-1]=='JJ' and noblank[index-4]=='JJ':
        
#把sensitive和feature的list变为str
    addns=''.join(negtivesen)
    addps=''.join(positivesen)
    addnf=''.join(negtivefea)
    addpf=''.join(positivefea)
#扩大seedneg和seedpos
    seedneg=seedneg+addns+addnf
    seedpos=seedpos+addps+addpf
#判断seed集是否还在扩大
    numneg=[]
    numpos=[]
    numneg.append(len(seedneg))
    numpos.append(len(seedpos))
    if numneg[n]==numneg[n-1] and numpos[n]==numpos[n-1]:
        break

print(negtivesen)        

    #改变为只把NN提取，赋予极性 放入一个list（提取的情感词只加入seed继续用于提取）。因为我们要做的是把这个领域内的名词提取出来



