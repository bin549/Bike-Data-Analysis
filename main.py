import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jieba
import spacy

def get_ents(doc):
    entities = []
    if doc.ents:
        for ent in doc.ents:
            entities.append(ent.text)
    return entities


def main():
    nlp = spacy.load('zh_core_web_sm')
    # print(len(excel_data))
    excel_data = pd.read_excel('./excel/bike_data.xlsx', encoding='utf-8', sheet_name='Sheet1')
    # print(nlp.Defaults.stop_words)
    # print(len(nlp.Defaults.stop_words))

"""
    # df = pd.DataFrame(excel_data["不坐电瓶车的原因"].value_counts())
    # df = pd.DataFrame(excel_data["购买自行车的原因"].value_counts())
    # df = pd.DataFrame(excel_data["坐电瓶车的原因"].value_counts())

    df = pd.DataFrame(excel_data["不坐电瓶车的原因"])
    blanks = []
    for i, rv in df.itertuples():
        if type(rv) == str:
            if rv == "(空)":
                blanks.append(i)  # add matching index numbers to the list
    df.drop(blanks, inplace=True)

    words = {}
    for i, rv in df.itertuples():
        doc = nlp(rv)
        entities = get_ents(doc)
        if len(entities) != 0:
            for entity in entities:
                if entity in words:
                    words[entity] += 1
                else:
                    words[entity] = 1
    print(words)

    df = pd.DataFrame(pd.Series(words))
    df.plot(kind="bar")
    plt.show()
"""

"""
    df = pd.DataFrame(excel_data["购买自行车的价格"])
    blanks = []
    for i, rv in df.itertuples():
        if type(rv) == str:
            if rv == "(空)":
                blanks.append(i)  # add matching index numbers to the list
    df.drop(blanks, inplace=True)

    words = {}

    for i, rv in df.itertuples():
        if not str(rv).isdigit():
            continue
        else:
            if rv in words.keys():
                words[rv] += 1
            else:
                words[rv] = 1
    print(words)
    df = pd.DataFrame(pd.Series(words))
    df.plot.pie(subplots=True, figsize=(8, 4))
    plt.show()
"""

"""
    df = pd.DataFrame([pd.DataFrame(excel_data["相较于疫情之前，您的出行方式是否有变化"].value_counts()).loc[1],
                       pd.DataFrame(excel_data["相较于疫情之前，您的出行方式是否有变化"].value_counts()).loc[2]],
                      index=['y', 'n'])
    df.plot.pie(subplots=True, figsize=(8, 4))
    plt.show()
"""

"""
    df = pd.DataFrame([pd.DataFrame(excel_data["缩减开支"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["锻炼身体"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["上课地点调动"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["宿舍调动"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["其他"].value_counts()).loc[1][0]],
                       index = ['缩减开支', '锻炼身体', '上课地点调动', '宿舍调动', '其他'])
    df.plot.pie(subplots=True, figsize=(8, 4))
    plt.show()
"""
"""
    df = pd.DataFrame([pd.DataFrame(excel_data["电瓶车价格是否合理"].value_counts()).loc[1],
                       pd.DataFrame(excel_data["电瓶车价格是否合理"].value_counts()).loc[2]],
                      index=['y', 'n'])
    df.plot.pie(subplots=True, colors=['r', 'g', 'b', 'c'], autopct='%.2f', fontsize=20, figsize=(6, 6))
    plt.show()
"""
"""
    df = pd.DataFrame([pd.DataFrame(excel_data["是否购买自行车"].value_counts()).loc[1],
                       pd.DataFrame(excel_data["是否购买自行车"].value_counts()).loc[2]],
                       index=['y', 'n'])
    df.plot.pie(subplots=True, colors=['r', 'g', 'b', 'c'], autopct='%.2f', fontsize=20, figsize=(6, 6))
    plt.show()
"""

"""
    df = pd.DataFrame([pd.DataFrame(excel_data["距离近"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["锻炼身体"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["时间充裕"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["与人同行"].value_counts()).loc[1][0]],
                                 index=['距离近', '锻炼身体', '时间充裕', '与人同行'])
    df.plot.pie(subplots=True, figsize=(8, 4))
    plt.show()
"""

"""
    df = pd.DataFrame(excel_data["月消费"].value_counts())
    df.plot.pie(subplots=True, figsize=(8, 4))
    plt.show()
"""
"""
    df = pd.DataFrame(excel_data["性别"].value_counts())
    df.plot.pie(subplots=True, figsize=(8, 4))
    plt.show()
"""

"""
    df = pd.DataFrame(excel_data["年级"].value_counts())
    df.plot.pie(subplots=True, figsize=(8, 4))
    plt.show()
"""

"""
    # df = pd.DataFrame([pd.DataFrame(excel_data["步行"].value_counts()).loc[1][0],
    #                 pd.DataFrame(excel_data["自行车"].value_counts()).loc[1][0],
    #                 pd.DataFrame(excel_data["电瓶车"].value_counts()).loc[1][0],
    #                 pd.DataFrame(excel_data["私家车"].value_counts()).loc[1][0],
    #                 pd.DataFrame(excel_data["平衡车"].value_counts()).loc[0][0],
    #                 pd.DataFrame(excel_data["其他"].value_counts()).loc[1][0]],
    #                              index = ['步行', '自行车', '电瓶车', '私家车', '平衡车', '其他'])
    # df.plot.pie(subplots=True, figsize=(8, 4))
    # plt.show()
"""

"""
    df = pd.DataFrame(excel_data["宿舍位置"])
    blanks = []
    for i, rv in df.itertuples():
        if type(rv) == str:
            if rv == "(空)":
                blanks.append(i)  # add matching index numbers to the list
    df.drop(blanks, inplace=True)

    TAG = {"燕": "燕华苑", "海": "海华苑", "粤": "粤华苑", "京": "京华苑"}

    words = {}

    for i, rv in df.itertuples():
        if rv[0] not in TAG.keys():
            continue
        else:
            if TAG[rv[0]] in words.keys():
                words[TAG[rv[0]]] += 1
            else:
                words[TAG[rv[0]]] = 1
    print(words)
    df = pd.DataFrame(pd.Series(words))
    df.plot.pie(subplots=True, figsize=(8, 4))
    plt.show()
"""

"""
    df = pd.DataFrame(excel_data["日常选择哪种品牌的共享单车"])
    blanks = []
    for i, rv in df.itertuples():
        if type(rv) == str:
            if rv == "(空)":
                blanks.append(i)  # add matching index numbers to the list
    df.drop(blanks, inplace=True)

    words = {}
    for i, rv in df.itertuples():
        doc = nlp(rv)
        entities = get_ents(doc)
        if len(entities) != 0:
            for entity in entities:
                if entity in words:
                    words[entity] += 1
                else:
                    words[entity] = 1
    print(words)

    df = pd.DataFrame(pd.Series(words))
    df.plot(kind="bar")
    plt.show()
"""

"""
    df = pd.DataFrame([pd.DataFrame(excel_data["价格贵"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["道路拥堵"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["排队时间长"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["手续办理麻烦"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["通勤时间长"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["保安有冲突"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["防盗"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["其他"].value_counts()).loc[1][0]],
                                 index=['价格贵', '道路拥堵', '排队时间长', '手续办理麻烦', '通勤时间长', '保安有冲突', '防盗', '其他'])
    df.plot.pie(subplots=True, figsize=(8, 4))
    plt.show()
"""

"""
    df = pd.DataFrame(excel_data["意见与建议"])
    blanks = []
    for i, rv in df.itertuples():
        if type(rv) == str:
            if rv == "(空)":
                blanks.append(i)
    df.drop(blanks, inplace=True)
    print(df)
"""


if __name__ == '__main__':
    main()
