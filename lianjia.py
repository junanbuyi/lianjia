import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mlt
import numpy as np
def_data = pd.read_excel("C:\\Users\\13279\\Desktop\\lianjia1.xls")
def_data.describe()
def_data.isnull().sum()
def_data.fillna()
plt.rcParams['font.sans-serif'] = ['SimHei']
class source1:
    Site = []
    sumprice = 0
    price = 0
    def __str__(self):
        return "总价(以万为单位)：" + str(self.sumprice) + "\t单价：" + str(self.price) + "\t小区："+str(self.Site)

def fun_1():
    length = len(def_data["cjzongjia"])
    m_sheet = [source1() for i in range(length)]
    for j in range(length):
       h =def_data["cjxiaoqu"][j].split()
       m_sheet[j].Site = (h[0])
       m_sheet[j].sumprice = def_data["cjzongjia"][j]
       m_sheet[j].price = int(def_data["cjdanjia"][j][:len(def_data["cjdanjia"][j]) - 3])
    #for p in m_sheet:
        #print(p)
    print(m_sheet[0].sumprice)
    all_sumprice = []
    all_Site = []
    for p in m_sheet:
        all_sumprice.append(p.sumprice)
        all_Site.append(p.Site)
    p_sheet = np.array(all_sumprice)
    n_sheet = np.array(all_Site)
    plt.title("各小区买房分布总价值")
    plt.xlabel("小区")
    plt.ylabel("买房总价")
    #plt.scatter(n_sheet,p_sheet)
    plt.bar(n_sheet,p_sheet)
    plt.grid()
    plt.show()
