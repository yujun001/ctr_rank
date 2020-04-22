# -*- coding: utf-8 -*-

#### 导入包
import pandas as pd
import numpy as np
import os
import copy
import datetime
from datetime import date
import md_tool


##### 根目录
os.chdir(r'C:\hao\aiwen_model1')


# 读取数据 
data = pd.read_csv('aiwen_data/query-hive-48543.csv',dtype=np.str) 

data = data.drop(['h.userid'],axis=1)

data.columns  = list(data.columns.str.replace("f\.",""))
data.columns  = list(data.columns.str.replace("h\.",""))
# data_ss1 = data.dtypes

data = data.drop_duplicates(['userid'])

data_merge = data[['userid']]

# target
data['totallimit'] = data['totallimit'].apply(md_tool.to_float)
data_merge['target'] =np.nan
data_merge['target'][data['totallimit'].notnull()] =1
data_merge['target'][data['totallimit'].isnull()] =0


# degree
data_merge['degree'] = np.nan
data_merge['degree'][data['degree']=='E01'] =1
data_merge['degree'][data['degree']=='E02'] =2
data_merge['degree'][data['degree']=='E03'] =3
data_merge['degree'][data['degree']=='E04'] =4
data_merge['degree'][data['degree']=='E05'] =5


# indiv_mtrital
indiv_mtrital_dict = {'D01':'unmarried','D02':'married','D03':'Widowedspouse','D04':'Divorce','D05':'Unknown'}
data['indiv_mtrital'] =  data['indiv_mtrital'].map(indiv_mtrital_dict)
data_merge_2 = pd.get_dummies(data['indiv_mtrital'],prefix="indiv_mtrital")

data_merge = pd.concat([data_merge,data_merge_2],axis=1)


## 时间转换处理
data['apply_time']  = pd.to_datetime(data['apply_time'])
data['register_time']  = pd.to_datetime(data['register_time'])
data['valid_end_date'] = pd.to_datetime(data['valid_end_date'],format='%Y%m%d',errors='ignore')


data['apply_time_hour'] = data['apply_time'].map(lambda x:x.hour)
data['valid_end_date_apply_time_days'] = (data['valid_end_date']- data['apply_time']).dt.days

data['apply_time_register_time'] = data['apply_time']- data['register_time']
data['apply_time_register_time_days'] = data['apply_time_register_time'].dt.days
data['apply_time_register_time_seconds'] = data['apply_time_register_time'].map(lambda x:x.total_seconds())

date_col = ['apply_time_hour','valid_end_date_apply_time_days','apply_time_register_time_days','apply_time_register_time_seconds']
for x in date_col:
    data_merge[x] = data[x]


### 公司 行业字段处理
data_word =['金融|资产|投资|融资|金服|贷款|普惠|小微|消费|金控|借贷|信用|财富|租赁|担保|网贷|中介|极光|佰仟|区块链|企业管理|金融信息|融',\
       'KTV|会所|美容|女子|美颜|美妆|美发|养生|足浴|洗脚|酒店|理发|酒吧|洗浴中心|沙龙|宾馆|理疗|富士康'\
           ,'保险|人寿|平安|太平|寿险|险'\
           ,'银行|信用社|城商行|商业银行|合作社'\
           ,'医院|学校|教育|幼儿园|卫生院|医疗|医|小学|中学|学院|大学|诊所|门诊|学前|救护'\
           ,'交警|执法大队|公安|派出所|政府|监狱|治安|法院|武警|保安|城管|城市管理|军区|军队|特警|巡警|警|市委|国税|省委|党委|消防|管理局|武装|'
           ,'统计局|中国铁路|保护局|管理所|保障局|街道办|研究所|食药局|防治所|税务局|管理局|供电局|民政局|农业局'\
           ,'房地产|房|置业|房地产开发|地产|房产|乐有家'
           ,'转井|装修|挖掘|钻井|装饰|采石|建筑|建材|工程|煤|重工|化工|混凝土|机械|钢结构|中铁|钢|矿|铝业|石材|运输|铝|门窗']

data_word_col =['occupation_p1','occupation_p2','occupation_p3','occupation_p4','occupation_p5','occupation_p6','occupation_p7','occupation_p8','occupation_p9']
arr1 =np.array(data_word_col)
arr2 =np.array(data_word)

for x in range(len(arr1)):
    #print(x)
    aa=arr1[x]
    #print(aa)
    #aa=arr1[x]
    bb=arr2[x]
    data[aa] = data['company_name'].str.contains(bb,case=False)
    data[aa] = data[aa].astype(np.float64)
    data_merge[aa] = data[aa]


#### 运营商字段处理


####  判断户籍地址和现居住地址是否一致
#idcard_address	户籍地址（身份证首6位） live_address	现居住地址（6位数编码） company_address	公司所在地址（6位数编码） phone_address	手机号归属地（6位数编码）
data_merge['idcard_address_equal_live_address'] = 0.0
data_merge['idcard_address_equal_live_address'][data['idcard_address']== data['live_address']] = 1.0

data_merge['live_address_equal_company_address'] = 0.0
data_merge['live_address_equal_company_address'][data['live_address']== data['company_address']] = 1.0

data_merge['live_address_equal_phone_address'] = 0.0
data_merge['live_address_equal_phone_address'][data['live_address']== data['phone_address']] = 1.0

data_merge['phone_address_equal_company_address'] = 0.0
data_merge['phone_address_equal_company_address'][data['phone_address']== data['company_address']] = 1.0


## tongdun_decision
data_merge['tongdun_decision'] = np.nan
data_merge['tongdun_decision'][data['tongdun_decision']=='Accept'] = 1.0
data_merge['tongdun_decision'][data['tongdun_decision']=='Reject'] = -1.0
data_merge['tongdun_decision'][data['tongdun_decision']=='Review'] = 0


# contact_type_180d	直接联系人命中黑名单的类型
data['contact_type_180d_overdue'] = data['contact_type_180d'].str.contains('逾期',case=False).astype(np.float64)
data['contact_type_180d_cheat'] = data['contact_type_180d'].str.contains('欺诈',case=False).astype(np.float64)
data['contact_type_180d_losetouch'] = data['contact_type_180d'].str.contains('失信',case=False).astype(np.float64)
data_merge['contact_type_180d_cheat'] = data['contact_type_180d_overdue']
data_merge['contact_type_180d_cheat'] = data['contact_type_180d_cheat']
data_merge['contact_type_180d_losetouch'] = data['contact_type_180d_losetouch']



## boole类型转换
boole_dict ={'True':1.0,'False':0.0}
data_merge['mobile_name_in_blacklist'] = data['mobile_name_in_blacklist'].map(boole_dict)
data_merge['idcard_name_in_blacklist'] = data['idcard_name_in_blacklist'].map(boole_dict)
data_merge['mobile_name_in_gray'] = data['idcard_name_in_blacklist'].map(boole_dict)



## 不需要衍生处理，直接转换为float类型
float_col = ['age','sex','income','apply_amount','device_type',
             'month3_idcard_emial_num','month3_idacard_mobile_num','month3_idcard_addr_num',
             'day7_applay_borrow_num','month1_applay_borrow_num','month3_applay_borrow_num','overdue_num',
             'tongdun_score','match_score','contactnum','auth_contactnum','auth_contactnum_ratio_30d','auth_contactnum_ratio_180d',
             'black_contactnum_180d','black_contactnum_ratio_180d','auth_indirectnum_180d','auth_indirectnum_ratio_180d','black_indirectnum_180d',
             'black_indirectnum_ratio_180d','black_indirect_peernum_180d','black_indirect_peernum_ratio_180d','auth_indirect_peernum_180d',
             'auth_indirect_peernum_ratio_180d','org_count','other_count','queried_detail_org_count','loan_org_cnt_all','loan_org_cnt',
             'loan_org_cnt_90d','loan_cnt_90d','blacklist_record_overdue_count']


for x in float_col:
    data[x] = data[x].apply(md_tool.to_float)
    data_merge[x] = data[x]


### 额外的衍生
## 'income','apply_amount'
# 月收入和申请额度比例
income_dict = {0:1500,3:4000,4:7500,5:15000,6:23000}
data['income2'] =  data['income'].map(income_dict)
data['apply_amount_div_income'] = data['apply_amount']/data['income2']


derivation_col = ['apply_amount_div_income']
for x in derivation_col:
    data_merge[x] = data[x]


# data_ss4 =  data_merge.dtypes

model_col = list(data_merge.columns)
model_col.remove('userid')
model_col.remove('target')

for x in model_col:
    data_merge[x] = data_merge[x].apply(md_tool.to_float)


feature_types = data_merge.dtypes
feature_types.to_csv('train_data/feature_types.csv')

"""
# 数据观察
cl = ['mobile_name_in_blacklist','mobile_name_in_blacklist2','idcard_name_in_blacklist','idcard_name_in_blacklist2','idcard_name_in_blacklist','mobile_name_in_gray2']
data_ss1 = data[cl]

"""



# 选取日期
#data_merge = data_merge.drop_duplicates(['userid'])
#data['apply_date'] = [str(x)[:10] for x in data['apply_time']]

data_oot = data[data['apply_time']>='2018-11-18']
data_traintest = data[data['apply_time']<'2018-11-18']

data_merge_traintest = pd.merge(data_traintest[['userid']],data_merge,on='userid',how='inner')
data_merge_oot = pd.merge(data_oot[['userid']],data_merge,on='userid',how='inner') 




#data_merge_traintest.to_pickle('train_data/data_merge_traintest.pkl')
#data_merge_oot.to_pickle('train_data/data_merge_oot.pkl')


data_merge_traintest.to_csv('train_data/data_merge_traintest.csv',index=False,encoding='utf-8')



