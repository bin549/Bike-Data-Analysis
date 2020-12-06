import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jieba


def main():
    # read file
    excel_data = pd.read_excel('./excel/bike_data.xlsx', encoding='utf-8', sheet_name='Sheet1')

    # print(len(excel_data))

    # df = pd.DataFrame(excel_data["性别"].value_counts())
    # df = pd.DataFrame(excel_data["年级"].value_counts())
    # df = pd.DataFrame(excel_data["宿舍"].value_counts())
    # df = pd.DataFrame(excel_data["月消费"].value_counts())
    # df = pd.DataFrame(excel_data["月消费"].value_counts())

    # 出行方式
    # df = pd.DataFrame(excel_data["步行"].value_counts())
    # df = pd.DataFrame(excel_data["自行车"].value_counts())
    # df = pd.DataFrame(excel_data["电瓶车"].value_counts())
    # df = pd.DataFrame(excel_data["私家车"].value_counts())
    # df = pd.DataFrame(excel_data["平衡车"].value_counts())
    # df = pd.DataFrame(excel_data["其他"].value_counts())

    # 选择步行的原因
    # df = pd.DataFrame(excel_data["距离近"].value_counts())
    # df = pd.DataFrame(excel_data["锻炼身体"].value_counts())
    # df = pd.DataFrame(excel_data["时间充裕"].value_counts())
    # df = pd.DataFrame(excel_data["与人同行"].value_counts())

    # df = pd.DataFrame(excel_data["不坐电瓶车的原因"].value_counts())
    # df = pd.DataFrame(excel_data["电瓶车价格是否合理"].value_counts())
    # df = pd.DataFrame(excel_data["是否购买自行车"].value_counts())
    # df = pd.DataFrame(excel_data["购买自行车的原因"].value_counts())
    # df = pd.DataFrame(excel_data["购买自行车的价格"].value_counts())

    df = pd.DataFrame(excel_data["日常选择哪种品牌的共享单车"])
    # df.drop()
    blanks = []

    for i, rv in df.itertuples():
        if type(rv) == str:
            if rv == "(空)":
                print(i, rv)
                blanks.append(i)  # add matching index numbers to the list

    df.drop(blanks, inplace=True)

    print(df)

    # df = pd.DataFrame(excel_data["坐电瓶车的原因"].value_counts())
    # df = pd.DataFrame(excel_data["相较于疫情之前，您的出行方式是否有变化"].value_counts())

    # 如果有变化，原因是
    # df = pd.DataFrame(excel_data["缩减开支"].value_counts())
    # df = pd.DataFrame(excel_data["锻炼身体"].value_counts())
    # df = pd.DataFrame(excel_data["上课地点调动"].value_counts())
    # df = pd.DataFrame(excel_data["宿舍调动"].value_counts())
    # df = pd.DataFrame(excel_data["其他"].value_counts())

    # 在校出行遇到的问题
    # df = pd.DataFrame(excel_data["价格贵，开销大"].value_counts())
    # df = pd.DataFrame(excel_data["道路拥堵"].value_counts())
    # df = pd.DataFrame(excel_data["排队时间长"].value_counts())
    # df = pd.DataFrame(excel_data["手续办理麻烦"].value_counts())
    # df = pd.DataFrame(excel_data["通勤时间长"].value_counts())
    # df = pd.DataFrame(excel_data["保安有冲突"].value_counts())
    # df = pd.DataFrame(excel_data["防盗"].value_counts())
    # df = pd.DataFrame(excel_data["其他"].value_counts())

    # df = pd.DataFrame(excel_data["意见与建议"].value_counts())


    # print(excel_data["是否购买自行车"].value_counts().iloc[0])
    # print(excel_data["是否购买自行车"].value_counts().iloc[1])


    # df.plot.pie(subplots=True, colors=['r', 'g', 'b', 'c'], autopct='%.2f', fontsize=20, figsize=(6, 6))
    # plt.show()


    # df = excel_data["宿舍位置"].value_counts()
    # df = excel_data["年级"].value_counts()
    # df = excel_data["年级"].value_counts()
    # df = excel_data["年级"].value_counts()
    # df = excel_data["年级"].value_counts()
    # df = excel_data["年级"].value_counts()
    #plt.hist(df)
    #df.plot.bar(stacked=True)



if __name__ == '__main__':
    main()
