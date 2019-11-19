import os
import sys
import pandas as pd
import Levenshtein as lestn
import time


#使用Levenshtein比较2个字符串
def get_equal_ratio(str1, str2):
   return lestn.ratio(str1,str2)

#检查当前数据是否已经被记录了(已经被分过类了)
def is_exist(arr,str):
    if str in arr:
        return True
    return False

#主要代码
def main():
    #默认数据文件
    filePath='simple_data.xlsx'
    #默认相似度
    similarRatio=0.6
    #默认的列名所在的行
    headerRow=1
    #默认对比的列
    compareColName='货物全名'
    #默认排除条件的列
    dropWhereColName='价格'
    #默认排除的条件 大于 该值的全部删除
    dropWhereColValue=100
    #支持命令行启动参数
    useDefaultFlag='--'
    if len(sys.argv)>1 and sys.argv[1]!=useDefaultFlag:
        filePath=sys.argv[1]
    if len(sys.argv)>2 and sys.argv[2]!=useDefaultFlag:
        similarRatio=float(sys.argv[2])
    if len(sys.argv)>3 and sys.argv[3]!=useDefaultFlag:
        headerRow=int(sys.argv[3])
        if headerRow <0: # 小于0，被认为是没有header
            headerRow=None
    if len(sys.argv)>4 and sys.argv[4]!=useDefaultFlag:
        compareColName=sys.argv[4]
    if len(sys.argv)>5 and sys.argv[5]!=useDefaultFlag:
        dropWhereColName=sys.argv[5]
    if len(sys.argv)>6 and sys.argv[6]!=useDefaultFlag:
        dropWhereColValue=int(sys.argv[6]) 
    

    print('\n参数描述\n文件路径:'+filePath+' \n相似度:'+str(similarRatio)+' \n列名所在行数行号(0是第一行):'+str(headerRow)+'\n归类所用的列名:'+compareColName+' \n 条件删除所需的列名:'+dropWhereColName+' \n删除大于:'+str(dropWhereColValue)+'\n')
    #读取excel指定行是列名
    excel_data = pd.read_excel(filePath,header=headerRow)
    #过滤掉价格大于100的行
    excel_data.drop(excel_data[excel_data[dropWhereColName] > dropWhereColValue].index,inplace=True)
    #重置索引，不重置的话索引会断掉
    excel_data.reset_index(drop=True, inplace=True)
    #获取指定列
    data=excel_data[compareColName]
    #2维数组，记录分类，其中每一个数组都是一个新的类别
    categorysArr=[]
    #记录已经被分过类的索引，避免重复检查
    recorder=[]
    #取每个字符串相互比较
    for f in range(0,len(data)):
        first=data[f]
        #判断该商品编号是否被记录分类，已经分过类的不再重复比较
        if is_exist(recorder,f)==False :
            categorysArr.append([])
        else:
            continue
        for s in range(0,len(data)):
            second=data[s]
            #如果相似度大于similarRatio，即认为是一个类别
            if get_equal_ratio(first,second) > similarRatio :
                #判断该商品编号是否被记录分类，已经分过类的不再记录
                if is_exist(recorder,s)==False :
                    #记录编号
                    recorder.append(s)
                    #添加分类
                    categorysArr[-1].append(s)

    #将处理过的数据，放入新的容器，这里可以做数据的二次处理，在这里categorysArr里面的数据已经是归好类的
    finalFormatArr=[]
    for category in categorysArr:
        if len(category) >0:
            for i in category:
                finalFormatArr.append(excel_data.iloc[i].array)
        #加入一个空行，为了显示的时候把不同类别更好分开
        finalFormatArr.append([])

    #取文件名字，不包括扩展名
    (shotname,extension)=os.path.splitext(os.path.basename(filePath))
    #创建新的 DataFrame
    result=pd.DataFrame(finalFormatArr,columns=excel_data.columns)
    resultFilePath=shotname+'_filter_ratio_'+str(similarRatio)+'_'+time.strftime("%Y%m%d%H%M%S%Y", time.localtime())+'.xlsx'
    #写入excel
    result.to_excel(resultFilePath,index=False)



if __name__ == '__main__':
    main()
