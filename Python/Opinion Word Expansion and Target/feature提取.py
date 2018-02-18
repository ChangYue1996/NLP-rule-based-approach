#输入{O}为情感词典中的情感词集。
#**输出所有可能的features{F}，即target集合
#输出扩展情感词集{O-Expand}
corpus = open("positive_reln1.txt","r")
str=corpus.read()#得到全部评论
corpus.close()

dic1= open("negative-words.txt","r")
seedneg=dic1.read()
dic1.close()
dic2= open("positive-words.txt","r")
seedpos=dic2.read()
dic2.close()
tar= open("positive-words.txt","r")
Feature=tar.read()
dic2.close()
#O-EXP
O-EXP=seedneg+seedpos
Oi=[]
negtivesen= [];
positivesen= [];
#Fi
Fi=[];
negtivefea= [];
positivefea= [];
noblank=str.split(" ")#用空格分割全部评论


for index, item in enumerate(noblank):#遍历列表找出nsubj和amod的索引值
        if Fi is not in F:
            #R11
            if item=='NN'    
            #NN是关系里后一个词时
                if noblank[index+1]=='mod'or noblank[index+1]=='pnmod'or noblank[index+1]=='subj'or noblank[index+1]=='s'or noblank[index+1]=='obj'or noblank[index+1]=='obj2'or noblank[index+1]=='desc':
           
                   if noblank[index-5] in O-EXP:#o在O中,输出t
                   negtivefea.append( noblank[index-2]); 
         
                   if noblank[index-5] in O-EXP:
                       positivefea.append( noblank[index-2]);
            #NN是关系里前一个词时                       
                if noblank[index+4]=='mod'or noblank[index+4]=='pnmod'or noblank[index+4]=='subj'or noblank[index+4]=='s'or noblank[index+4]=='obj'or noblank[index+4]=='obj2'or noblank[index+4]=='desc':
           
                   if noblank[index+2] in O-EXP:#o在O中，输出t
                   negtivefea.append( noblank[index-2]); 
         
                   if noblank[index+2] in O-EXP:#o在O中
                       positivefea.append( noblank[index-2]);

             if item=='NN':#R12
                 if (noblank[index-6]=='mod'or noblank[index-6]=='pnmod'or noblank[index-6]=='subj'or noblank[index-6]=='s'or noblank[index-6]=='obj'or noblank[index-6]=='obj2'or noblank[index-6]=='desc' ) and (noblank[index+1]=='mod'or noblank[index+1]=='pnmod'or noblank[index+1]=='subj'\
                    or noblank[index+1]=='s'or noblank[index+1]=='obj'or noblank[index+1]=='obj2'or noblank[index+1]=='desc' )#NN是两个关系中的第四个词的词性；词为[In-12],[In-9],[In-5],[In-2];关系为[In-6][In+1];
                     if noblank[index-5]==noblank[index-9]:#H是-5，-9
                         if noblank[index-12]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index-12]in seedpos:
                             positivefea.append(noblank[index-2])
                     if noblank[index-5]==noblank[index-12]:#H是-5，-12
                         if noblank[index-9]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index-9]in seedpos:
                             positivefea.append(noblank[index-2])
                 if (noblank[index-3]=='mod'or noblank[index-3]=='pnmod'or noblank[index-3]=='subj'or noblank[index-3]=='s'or noblank[index-3]=='obj'or noblank[index-3]=='obj2'or noblank[index-3]=='desc' ) and (noblank[index+4]=='mod'or noblank[index+4]=='pnmod'or noblank[index+4]=='subj'\
                    or noblank[index+4]=='s'or noblank[index+4]=='obj'or noblank[index+4]=='obj2'or noblank[index+4]=='desc' )#NN是两个关系中的第三个词的词性；词为[In-9],[In-6],[In-2],[In+1];关系为[In-3][In+4];
                     if noblank[index+1]==noblank[index-6]:#H是+1，-6
                         if noblank[index-9]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index-9]in seedpos:
                             positivefea.append(noblank[index-2])
                     if noblank[index+1]==noblank[index-9]:#H是+1，-9
                         if noblank[index-6]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index-6]in seedpos:
                             positivefea.append(noblank[index-2])
                 if (noblank[index+1]=='mod'or noblank[index+1]=='pnmod'or noblank[index+1]=='subj'or noblank[index+1]=='s'or noblank[index+1]=='obj'or noblank[index+1]=='obj2'or noblank[index+1]=='desc' ) and (noblank[index+8]=='mod'or noblank[index+8]=='pnmod'or noblank[index+8]=='subj'\
                    or noblank[index+8]=='s'or noblank[index+8]=='obj'or noblank[index+8]=='obj2'or noblank[index+8]=='desc' )#NN是两个关系中的第二个词的词性；词为[In-5],[In-2],[In+2],[In+5];关系为[In+1][In+8];
                     if noblank[index-5]==noblank[index+2]:#H是-5，+2
                         if noblank[index+5]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index+5]in seedpos:
                             positivefea.append(noblank[index-2])
                     if noblank[index-5]==noblank[index+5]:#H是-5，+5
                         if noblank[index+2]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index+2]in seedpos:
                             positivefea.append(noblank[index-2])
                 if (noblank[index+4]=='mod'or noblank[index+4]=='pnmod'or noblank[index+4]=='subj'or noblank[index+4]=='s'or noblank[index+4]=='obj'or noblank[index+4]=='obj2'or noblank[index+4]=='desc' ) and (noblank[index+11]=='mod'or noblank[index+11]=='pnmod'or noblank[index+11]=='subj'\
                    or noblank[index+11]=='s'or noblank[index+11]=='obj'or noblank[index+11]=='obj2'or noblank[index+11]=='desc' )#NN是两个关系中的第一个词的词性；词为[In-2],[In+1],[In+8],[In+5];关系为[In+1][In+8];
                     if noblank[index+1]==noblank[index+5]:#H是+1，+5
                         if noblank[index+8]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index+8]in seedpos:
                             positivefea.append(noblank[index-2])
                     if noblank[index+1]==noblank[index+8]:#H是+1，+8
                         if noblank[index+5]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index+5]in seedpos:
                             positivefea.append(noblank[index-2])



            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            #R21
            if item=='JJ'    
            #JJ是关系里后一个词时
                if noblank[index+1]=='mod'or noblank[index+1]=='pnmod'or noblank[index+1]=='subj'or noblank[index+1]=='s'or noblank[index+1]=='obj'or noblank[index+1]=='obj2'or noblank[index+1]=='desc':
           
                   if noblank[index-5] in seedneg:#t在T中，输出o
                   negtivesen.append( noblank[index-2]); 
         
                   if noblank[index-5] in seedpos:
                       positivesen.append( noblank[index-2]);
            #JJ是关系里前一个词时                       
                if noblank[index+4]=='mod'or noblank[index+4]=='pnmod'or noblank[index+4]=='subj'or noblank[index+4]=='s'or noblank[index+4]=='obj'or noblank[index+4]=='obj2'or noblank[index+4]=='desc':
           
                   if noblank[index+2] in seedneg:#t在T中,输入o
                   negtivesen.append( noblank[index-2]); 
         
                   if noblank[index+2] in seedpos:#t在T中
                       positivesen.append( noblank[index-2]);

            #R22
             if item=='JJ':
                 if (noblank[index-6]=='mod'or noblank[index-6]=='pnmod'or noblank[index-6]=='subj'or noblank[index-6]=='s'or noblank[index-6]=='obj'or noblank[index-6]=='obj2'or noblank[index-6]=='desc' ) and (noblank[index+1]=='mod'or noblank[index+1]=='pnmod'or noblank[index+1]=='subj'\
                    or noblank[index+1]=='s'or noblank[index+1]=='obj'or noblank[index+1]=='obj2'or noblank[index+1]=='desc' )#JJ是两个关系中的第四个词的词性；词为[In-12],[In-9],[In-5],[In-2];关系为[In-6][In+1];
                     if noblank[index-5]==noblank[index-9]:#H是-5，-9
                         if noblank[index-12]in seedneg:#t在T中，把O加入O
                             negtivefea.append(noblank[index-2])
                         if noblank[index-12]in seedpos:
                             positivefea.append(noblank[index-2])
                     if noblank[index-5]==noblank[index-12]:#H是-5，-12
                         if noblank[index-9]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index-9]in seedpos:
                             positivefea.append(noblank[index-2])
                 if (noblank[index-3]=='mod'or noblank[index-3]=='pnmod'or noblank[index-3]=='subj'or noblank[index-3]=='s'or noblank[index-3]=='obj'or noblank[index-3]=='obj2'or noblank[index-3]=='desc' ) and (noblank[index+4]=='mod'or noblank[index+4]=='pnmod'or noblank[index+4]=='subj'\
                    or noblank[index+4]=='s'or noblank[index+4]=='obj'or noblank[index+4]=='obj2'or noblank[index+4]=='desc' )#JJ是两个关系中的第三个词的词性；词为[In-9],[In-6],[In-2],[In+1];关系为[In-3][In+4];
                     if noblank[index+1]==noblank[index-6]:#H是+1，-6
                         if noblank[index-9]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index-9]in seedpos:
                             positivefea.append(noblank[index-2])
                     if noblank[index+1]==noblank[index-9]:#H是+1，-9
                         if noblank[index-6]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index-6]in seedpos:
                             positivefea.append(noblank[index-2])
                 if (noblank[index+1]=='mod'or noblank[index+1]=='pnmod'or noblank[index+1]=='subj'or noblank[index+1]=='s'or noblank[index+1]=='obj'or noblank[index+1]=='obj2'or noblank[index+1]=='desc' ) and (noblank[index+8]=='mod'or noblank[index+8]=='pnmod'or noblank[index+8]=='subj'\
                    or noblank[index+8]=='s'or noblank[index+8]=='obj'or noblank[index+8]=='obj2'or noblank[index+8]=='desc' )#JJ是两个关系中的第二个词的词性；词为[In-5],[In-2],[In+2],[In+5];关系为[In+1][In+8];
                     if noblank[index-5]==noblank[index+2]:#H是-5，+2
                         if noblank[index+5]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index+5]in seedpos:
                             positivefea.append(noblank[index-2])
                     if noblank[index-5]==noblank[index+5]:#H是-5，+5
                         if noblank[index+2]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index+2]in seedpos:
                             positivefea.append(noblank[index-2])
                 if (noblank[index+4]=='mod'or noblank[index+4]=='pnmod'or noblank[index+4]=='subj'or noblank[index+4]=='s'or noblank[index+4]=='obj'or noblank[index+4]=='obj2'or noblank[index+4]=='desc' ) and (noblank[index+11]=='mod'or noblank[index+11]=='pnmod'or noblank[index+11]=='subj'\
                    or noblank[index+11]=='s'or noblank[index+11]=='obj'or noblank[index+11]=='obj2'or noblank[index+11]=='desc' )#JJ是两个关系中的第一个词的词性；词为[In-2],[In+1],[In+8],[In+5];关系为[In+1][In+8];
                     if noblank[index+1]==noblank[index+5]:#H是+1，+5
                         if noblank[index+8]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index+8]in seedpos:
                             positivefea.append(noblank[index-2])
                     if noblank[index+1]==noblank[index+8]:#H是+1，+8
                         if noblank[index+5]in seedneg:
                             negtivefea.append(noblank[index-2])
                         if noblank[index+5]in seedpos:
                             positivefea.append(noblank[index-2])



                    
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