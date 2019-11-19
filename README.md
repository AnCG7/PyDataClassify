# PyDataClassify

使用 Levenshtein 进行字符串相似度比较，读取excel中商品数据然后根据名字分类，将分类好的数据 再写回excel。  
该文件只是起了粗略的分类，因为我的业务只需要大致的分类。可以调整相似度来规范类别。

# 依赖库  
pandas  
Levenshtein

# 执行文件  
data_classify.py 

# 参数按顺序说明  
任意参数填写--或者不填表示使用默认值(--作为占位符使用)  
文件路径:excel文件路径(默认:simple_data.xlsx)  
相似度:指比较字符串所使用的相似度(0～1)(默认:0.6)  
行号:表格的每一列的名子所在行的行号(0是第一行)(默认:1)  
比较用的列的名字:归类时所用的列名(默认:货物全名)  
条件比较使用的列名:当达到条件时删除列名对应行的数据(默认:价格)  
删除条件:删除大于此参数对应的该行数据(默认:100)  
  
默认参数的意思是:使用simple_data.xlsx文件作为数据样本,使用0.6作为默认的比较相似度,使用数据第1行作为列的名字,比较所用的列是"货物全名",删除"价格"列中,数值大于100的行
# 举例  
your_path/data_classify.py   
your_path/data_classify.py -- -- -- -- -- --  
(注意以上2个得到的结果是一样的这里是举例说明占位符怎么用，他们表示使用默认值)  
## 常用  
your_path/data_classify.py xlsx文件路径 相似度  
your_path/data_classify.py -- 相似度  

# 注意
因为数据处理总会和数据格式有关,如果你打算直接使用,请注意参考simple_data.xlsx文件的数据是否符合你的数据格式  
如果你想要数据结果表现的更好,请先对数据做清洗和格式化    
如果它不能达到你的需求,请作为一个Levenshtein 和 pandas 库的一个展示如何使用的小demo。
