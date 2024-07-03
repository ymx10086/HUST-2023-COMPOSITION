# coding=gbk

import pandas
import os
import shutil
import numpy as np

# ��ȡ�ֿ��ļ�HZK16_1.txt, ����ǰ����
df = pandas.read_csv('HZK16_1.txt', sep='\t', skiprows=2, header=None)
print(df)

df1 = df.iloc[0:4096, :]
df2 = df.iloc[4096:8192, :]
df3 = df.iloc[8192:, :]

# ���浽HZK16_1_1.txt, HZK16_1_2.txt, HZK16_1_3.txt, ÿ���ļ���ʼ���������ֿ��ļ���ͷ����Ϣv2.0 raw\n
df1.to_csv('HZK16_1_1.txt', sep='\t', index=False, header=False)
df2.to_csv('HZK16_1_2.txt', sep='\t', index=False, header=False)
df3.to_csv('HZK16_1_3.txt', sep='\t', index=False, header=False)
