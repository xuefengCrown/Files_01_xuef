#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import datetime
#import scipy as sp
#from scipy import stats

def get_sum(roll_lst):
    """计算字符串列表中数字和"""
    # filter函数的返回值是什么？值得注意
    filtered_roll_lst = list(filter(is_convert_float, roll_lst))
    # 数据类型转换
    float_roll_array = np.array(filtered_roll_lst, np.float)
    
    return np.sum(float_roll_array)

def is_convert_float(s):
    """一个字符串是否能转化为float"""
    try:
        float(s)
    except:
        return False
    return True

def main():
    filename = './presidential_polls.csv'

    # 读取文件首行，解析出列名
    with open(filename, 'r') as f:
        col_name_str = f.readline()[:-1]

    col_name_lst = col_name_str.split(',')
    # 使用的列名
    interest_col_name_lst = ['enddate', 'rawpoll_clinton', 'rawpoll_trump', 'adjpoll_clinton', 'adjpoll_trump']
    interest_col_index_lst = [col_name_lst.index(col_name) for col_name in interest_col_name_lst]

    # step2 读取数据
    data_array = np.loadtxt(filename, 
                            delimiter=',',
                            skiprows=1, # 跳过第一行
                            dtype=str,  # 数据类型
                            usecols=interest_col_index_lst) # 通过列索引指定要读取的列
    
    # step3 数据处理
    ## 处理日期格式数据
    enddate_idx = interest_col_name_lst.index('enddate')
    # 在两个维度上筛选，[:, enddate_idx], ':'选择所有行，enddate_idx获取这一列
    enddate_lst = data_array[:, enddate_idx].tolist()

    # 日期格式统一为，mm/dd/yy
    enddate_lst = [enddate.replace('-', '/') for enddate in enddate_lst]
    # 将日期字符创转换为日期
    date_lst = [datetime.datetime.strptime(enddate, '%m/%d/%Y') for enddate in enddate_lst]

    # 构造年份-月份列表
    month_lst = ['%d-%02d' %(date_obj.year, date_obj.month) for date_obj in date_lst]
    month_array = np.array(month_lst)
    months = np.unique(month_array)

    # step4 数据分析
    ## 统计民意投票数
    ### clinton
    rawpoll_clinton_idx = interest_col_name_lst.index('rawpoll_clinton')
    rawpoll_clinton_data = data_array[:, rawpoll_clinton_idx]
    adjpoll_clinton_idx = interest_col_name_lst.index('adjpoll_clinton')
    adjpoll_clinton_data = data_array[:, adjpoll_clinton_idx]

    ### trump
    rawpoll_trump_idx = interest_col_name_lst.index('rawpoll_trump')
    rawpoll_trump_data = data_array[:, rawpoll_trump_idx]
    adjpoll_trump_idx = interest_col_name_lst.index('adjpoll_trump')
    adjpoll_trump_data = data_array[:, adjpoll_trump_idx]

    result = []

    for month in months:
        # clinton
        ### 条件索引，筛选出月数据。利用month_array 映射出 rawpoll_clinton_data中符合条件的数据
        rawpoll_clinton_month_data = rawpoll_clinton_data[month_array == month]
        ## 统计当月的总票数
        rawpoll_clinton_month_sum = get_sum(rawpoll_clinton_month_data)

        adjpoll_clinton_month_data = adjpoll_clinton_data[month_array == month]
        adjpoll_clinton_month_sum = get_sum(adjpoll_clinton_month_data)

        # trump
        rawpoll_trump_month_data = rawpoll_trump_data[month_array == month]
        ## 统计当月的总票数
        rawpoll_trump_month_sum = get_sum(rawpoll_trump_month_data)

        adjpoll_trump_month_data = adjpoll_trump_data[month_array == month]
        adjpoll_trump_month_sum = get_sum(adjpoll_trump_month_data)

        result.append((month, rawpoll_clinton_month_sum,adjpoll_clinton_month_sum,rawpoll_trump_month_sum,adjpoll_trump_month_sum))
    #print(result)

    month, raw_clinton_sum, adj_clinton_sum, raw_trump_sum, adj_trump_sum = zip(*result)

    # step5 可视化
    fig, subplot_arr = plt.subplots(2,2, figsize=(15,10))
    ## 原始数据趋势展示
    subplot_arr[0,0].plot(raw_clinton_sum, color='r')
    subplot_arr[0,0].plot(raw_trump_sum, color='g')

    width = 0.25
    x = np.arange(len(months))
    subplot_arr[0,1].bar(x, raw_clinton_sum, width, color='r')
    subplot_arr[0,1].bar(x+width, raw_trump_sum, width, color='g')
    subplot_arr[0,1].set_xticks(x + width)
    subplot_arr[0,1].set_xticklabels(months, rotation='vertical')

    ## 调整后数据趋势展示
    subplot_arr[1,0].plot(adj_clinton_sum, color='r')
    subplot_arr[1,0].plot(adj_trump_sum, color='g')

    plt.subplots_adjust(wspace=0.2)
    plt.show()


    
if __name__ == '__main__':
    main()



















