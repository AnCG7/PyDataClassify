# PyDataClassify

使用 Levenshtein 进行字符串相似度比较 读取excel中商品数据然后根据名字分类，将分类好的数据 再写回excel。  
该文件只是起了粗略的分类，因为我的业务只需要大致的分类。可以调整相似度来规范类别。

#依赖库
pandas  
Levenshtein

#使用py文件
data_classify.py 

#参数按顺序说明
任意参数填写--或者不填表示使用默认值(--作为占位符使用)
文件路径:excel文件路径(默认:simple_data.xlsx)  
相似度:指比较字符串所使用的相似度(0～1)(默认:0.6)
行号:表格的每一列的名子所在行的行号(0是第一行)(默认:1)
比较用的列的名字:归类时所用的列名(默认:货物全名)
条件比较使用的列名:当达到条件时删除列名对应行的数据(默认:价格)
删除条件:删除大于此参数对应的该行数据(默认:100)

#举例
your_path/data_classify.py 
your_path/data_classify.py -- -- -- -- -- --
(注意以上2个得到的结果是一样的这里是距离说明占位符怎么用)
##常用
your_path/data_classify.py xlsx文件路径 相似度
your_path/data_classify.py -- 相似度
