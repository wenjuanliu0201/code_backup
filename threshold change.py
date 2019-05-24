# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:33:30 2019

@author: wenjuanliu
"""

import numpy as np
import os
import codecs
#input
con = 'B'
participant = '001'
thre = 0.2

N_data= []
header=['stim','leftup_1','leftup_2','leftup_3','leftlow_1','leftlow_2','leftlow_3','rightup_1','rightup_2','rightup_3','rightlow_1','rightlow_2','rightlow_3'
]
'''
#file name list
path= 'E:/CloudStation/2019/本実験/二つ目/0conditionlist/Condition_exp4/'+ con + 'con/'

files = os.listdir(path)
for i in range(12):
    tmp =files[i][:-5]
    files[i]= tmp
'''

#make a letter list form csv
f = open('N-back.csv')
for line in f:
    tmp = line.split('\n')
    
    N_data.append(tmp[0])
 

#make a luminance array from csv
Lum_data = np.loadtxt('condition_format.csv', delimiter= ',')
Lum_data = np.array(Lum_data)
Lum_data[Lum_data != 1.0] = thre

#output twolve files
out = []
num = len(N_data)
for i in range(num):
    tmp =[]
    tmp.append(N_data[i])
    for m in range(12):
        tmp.append(Lum_data[i][m])
    out.append(tmp)

conditionfile =[]
block =[['01','02','03','04','05','06','07','08','09','10','11','12'],['03','04','01','02','07','08','05','06','11','12','09','10']]
A_contact =['con','con','nocon','nocon']*3
B_contact = ['nocon','nocon','con','con']*3
smartphone = ['p0','p0','p0','p0','p1','p1','p1','p1','p2','p2','p2','p2']
repeat = ['1','2']*6

if con == 'A':
    blocktmp =block[0] 

    for i in range(12):
    
        conditionfile =[]
        conditionfile.append(header)
        for m in range(144):
            conditionfile.append(out[i*144+m])
    
        with codecs.open(con+'_'+blocktmp[i]+'_'+A_contact[i]+'_'+smartphone[i]+'_'+repeat[i]+'_'+participant+'.csv','w','utf-8') as fp:
            for condition in conditionfile:
                fp.write('{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(*condition))
            fp.close()
else:
    blocktmp =block[1] 
    for i in range(12):
    
        conditionfile =[]
        conditionfile.append(header)
        for m in range(144):
            conditionfile.append(out[i*144+m])
    
        with codecs.open(con+'_'+blocktmp[i]+'_'+A_contact[i]+'_'+smartphone[i]+'_'+repeat[i]+'_'+participant+'.csv','w','utf-8') as fp:
            for condition in conditionfile:
                fp.write('{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(*condition))
