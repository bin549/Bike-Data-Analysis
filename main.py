import pandas as pd
import matplotlib.pyplot as plt
import spacy

excel_data = pd.read_excel('./excel/bike_data.xlsx', encoding='utf-8', sheet_name='Sheet1')

def excel_info():
    print(len(excel_data))


def nlp_info():
    nlp = spacy.load('zh_core_web_sm')
    print(nlp.Defaults.stop_words)
    print(len(nlp.Defaults.stop_words))


def get_ents(doc):
    entities = []
    if doc.ents:
        for ent in doc.ents:
            entities.append(ent.text)
    return entities


def bike_way():

    sex = pd.DataFrame(excel_data["性别"])

    male = excel_data[excel_data['性别'] == 1]
    female = excel_data[excel_data['性别'] == 2]

    index_ls = ['步行', '自行车', '电瓶车', '私家车', '平衡车', '其他']
    scale_ls = range(len(index_ls))


    goway = pd.DataFrame([
        [pd.DataFrame(male["步行"].value_counts()).loc[1][0], pd.DataFrame(female["步行"].value_counts()).loc[1][0]],
        [pd.DataFrame(male["自行车"].value_counts()).loc[1][0], pd.DataFrame(female["自行车"].value_counts()).loc[1][0]],
        [pd.DataFrame(male["电瓶车"].value_counts()).loc[1][0], pd.DataFrame(female["电瓶车"].value_counts()).loc[1][0]],
        [pd.DataFrame(male["私家车"].value_counts()).loc[1][0], pd.DataFrame(female["私家车"].value_counts()).loc[1][0]],
        [pd.DataFrame(male["平衡车"].value_counts()).loc[1][0], pd.DataFrame(female["平衡车"].value_counts()).loc[1][0]],
        [pd.DataFrame(male["其他"].value_counts()).loc[1][0], pd.DataFrame(female["其他"].value_counts()).loc[1][0]]
    ], columns=[1, 2])
    df = pd.DataFrame(goway, columns=[sex.loc[1][0], sex.loc[2][0]])
    df.plot.bar(color=['#66b3ff', '#ff9999'])
    plt.xticks(scale_ls, index_ls)
    plt.legend(['男', '女'])
    plt.title("男女生各种出行方式")
    plt.ylabel("数量（/个）")
    plt.show()


def age_way():
    sex = pd.DataFrame(excel_data["性别"])

    male = excel_data[excel_data['性别'] == 1]
    female = excel_data[excel_data['性别'] == 2]

    male_bikeower = male[male['是否购买自行车'] == 1]
    female_bikeower = female[female['是否购买自行车'] == 1]

    ageway = pd.DataFrame([
            [pd.DataFrame(male_bikeower["年级"].value_counts()).loc[1][0], pd.DataFrame(female_bikeower["年级"].value_counts()).loc[1][0]],
            [pd.DataFrame(male_bikeower["年级"].value_counts()).loc[2][0], pd.DataFrame(female_bikeower["年级"].value_counts()).loc[2][0]],
            [pd.DataFrame(male_bikeower["年级"].value_counts()).loc[3][0], pd.DataFrame(female_bikeower["年级"].value_counts()).loc[3][0]],
            [pd.DataFrame(male_bikeower["年级"].value_counts()).loc[4][0], pd.DataFrame(female_bikeower["年级"].value_counts()).loc[4][0]]
        ], columns=[1, 2])

    index_ls = ['大一', '大二', '大三', '大四']
    scale_ls = range(len(index_ls))

    df = pd.DataFrame(ageway, columns=[sex.loc[1][0], sex.loc[2][0]])
    df.plot.bar(color=['#66b3ff', '#ff9999'])
    plt.xticks(scale_ls, index_ls)
    plt.legend(['男', '女'])
    plt.ylabel("共购买自行车人数（/人）")
    plt.title("各年级男女生购买自行车数量")
    plt.show()


def live_way():
    colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99']
    explode = (0, 0.1, 0, 0)
    df = pd.DataFrame(excel_data["宿舍位置"])
    blanks = []
    for i, rv in df.itertuples():
        if type(rv) == str:
            if rv == "(空)":
                blanks.append(i)
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
    df.plot.pie(subplots=True, explode=explode, colors=colors, shadow=True, autopct='%0.1f%%', fontsize=10, startangle=20,
                figsize=(6, 6))
    plt.title("出行学生所住宿舍百分比")
    plt.show()

def bike_price():
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
    words.pop(0)
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    fig1, ax1 = plt.subplots()
    patches, texts, autotexts = ax1.pie(words.values(), colors=colors, labels=words.keys(), autopct='%1.1f%%', startangle=90)
    for text in texts:
        text.set_color('grey')
    for autotext in autotexts:
        autotext.set_color('grey')
    plt.title("学生购买车辆价位百分比")
    ax1.axis('equal')
    plt.tight_layout()
    plt.show()


def electric_suitable():
    df = pd.DataFrame([pd.DataFrame(excel_data["电瓶车价格是否合理"].value_counts()).loc[1],
                       pd.DataFrame(excel_data["电瓶车价格是否合理"].value_counts()).loc[2]],
                      index=['合理', '不合理'])

    colors = ['#66b3ff','#ff9999',  '#99ff99', '#ffcc99']
    df.plot.pie(subplots=True, colors=colors, shadow=True, autopct='%1.1f%%', fontsize=10, startangle=90, figsize=(6, 6))
    plt.title("学生对电瓶车价格是否合理评价百分比")
    plt.ylabel(None)
    plt.show()



def nonbike_reason():
    df = pd.DataFrame([pd.DataFrame(excel_data["距离近"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["可锻炼身体"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["时间充裕"].value_counts()).loc[1][0],
                    pd.DataFrame(excel_data["与人同行"].value_counts()).loc[1][0]],
                                 index=['距离近', '可锻炼身体', '时间充裕', '与人同行'])
    colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99']
    df.plot.pie(subplots=True, colors=colors, shadow=True, autopct='%1.1f%%', fontsize=10, startangle=90,
                figsize=(6, 6))
    plt.title("行走学生出行各原因百分比")
    plt.show()


def change_or_not():
    df = pd.DataFrame([pd.DataFrame(excel_data["相较于疫情之前，您的出行方式是否有变化"].value_counts()).loc[1],
                       pd.DataFrame(excel_data["相较于疫情之前，您的出行方式是否有变化"].value_counts()).loc[2]],
                      index=['y', 'n'])
    colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99']
    df.plot.pie(subplots=True, colors=colors, shadow=True, autopct='%1.1f%%', fontsize=10, startangle=90,
                figsize=(6, 6))
    plt.title("疫情是否影响学生出行百分比")
    plt.show()


def sharebike_choose():
    nlp = spacy.load('zh_core_web_sm')
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
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    fig1, ax1 = plt.subplots()
    ax1.pie(words.values(), colors=colors, labels=words.keys(), autopct='%1.1f%%', startangle=90)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.title("学生所选用共享单车品牌百分比")
    plt.tight_layout()
    plt.show()


def some_reason():
    nlp = spacy.load('zh_core_web_sm')
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


def change_reason():
    labels = ['缩减开支', '锻炼身体', '上课地点调动', '宿舍调动', '其他_']
    df = pd.DataFrame([pd.DataFrame(excel_data["缩减开支"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["锻炼身体"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["上课地点调动"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["宿舍调动"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["其他_"].value_counts()).loc[1][0]],
                      index=labels)
    # colors
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffcd29']
    # explsion
    explode = (0.05, 0.05, 0.05, 0.05, 0.05)
    fig1, ax1 = plt.subplots()

    plt.pie(df.values, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode=explode)
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')

    plt.title("疫情影响学生出行原因因素百分比")
    plt.tight_layout()
    plt.show()


def out_trouble():
    labels = ['价格贵', '道路拥堵', '排队时间长', '手续办理麻烦', '通勤时间长', '保安有冲突', '防盗', '其他__']

    df = pd.DataFrame([pd.DataFrame(excel_data["价格贵"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["道路拥堵"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["排队时间长"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["手续办理麻烦"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["通勤时间长"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["保安有冲突"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["防盗"].value_counts()).loc[1][0],
                       pd.DataFrame(excel_data["其他"].value_counts()).loc[1][0]],
                      index=labels)

    colors = ['#ff9999', '#66b3bf', '#22ff99', '#ffcc99', '#66b3ff', '#44bf99', '#dd9999', '#fffc99']

    fig1, ax1 = plt.subplots()
    patches, texts, autotexts = ax1.pie(df.values, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
    for text in texts:
        text.set_color('grey')
    for autotext in autotexts:
        autotext.set_color('grey')
    ax1.axis('equal')

    plt.title("学生不做电瓶车原因百分比")
    plt.tight_layout()
    plt.show()


def fill_empty():
    df = excel_data
    excel_filepath = './excel/bike_data2.xlsx'
    write = pd.ExcelWriter(excel_filepath)
    df["步行"] = excel_data["步行"].fillna(0)
    df["自行车"] = excel_data["自行车"].fillna(0)
    df["电瓶车"] = excel_data["电瓶车"].fillna(0)
    df["私家车"] = excel_data["私家车"].fillna(0)
    df["平衡车"] = excel_data["平衡车"].fillna(0)
    df["其他"] = excel_data["其他"].fillna(0)

    df["距离近"] = excel_data["距离近"].fillna(0)
    df["可锻炼身体"] = excel_data["可锻炼身体"].fillna(0)
    df["时间充裕"] = excel_data["时间充裕"].fillna(0)
    df["与人同行"] = excel_data["与人同行"].fillna(0)

    df["不坐电瓶车的原因"] = excel_data["不坐电瓶车的原因"].fillna("(空)")
    df["电瓶车价格是否合理"] = excel_data["电瓶车价格是否合理"].fillna("(空)")

    df["购买自行车的原因"] = excel_data["购买自行车的原因"].fillna("(空)")
    df["购买自行车的价格"] = excel_data["购买自行车的价格"].fillna("(空)")
    df["日常选择哪种品牌的共享单车"] = excel_data["日常选择哪种品牌的共享单车"].fillna("(空)")
    df["坐电瓶车的原因"] = excel_data["坐电瓶车的原因"].fillna("(空)")
    df["相较于疫情之前，您的出行方式是否有变化"] = excel_data["相较于疫情之前，您的出行方式是否有变化"].fillna("(空)")

    df["缩减开支"] = excel_data["缩减开支"].fillna(0)
    df["锻炼身体"] = excel_data["锻炼身体"].fillna(0)
    df["上课地点调动"] = excel_data["上课地点调动"].fillna(0)
    df["宿舍调动"] = excel_data["宿舍调动"].fillna(0)
    df["其他_"] = excel_data["其他_"].fillna(0)

    df["价格贵"] = excel_data["价格贵"].fillna(0)
    df["道路拥堵"] = excel_data["道路拥堵"].fillna(0)
    df["排队时间长"] = excel_data["排队时间长"].fillna(0)
    df["手续办理麻烦"] = excel_data["手续办理麻烦"].fillna(0)
    df["通勤时间长"] = excel_data["通勤时间长"].fillna(0)
    df["保安有冲突"] = excel_data["保安有冲突"].fillna(0)
    df["防盗"] = excel_data["防盗"].fillna(0)
    df["其他__"] = excel_data["其他__"].fillna(0)

    df["意见与建议"] = excel_data["意见与建议"].fillna("(空)")


    # excel_header = ['自行车']
    df.to_excel(write, sheet_name='Sheet1',index=False)
    # df.to_excel(write, sheet_name='Sheet1', header = excel_header)
    write.save()


def get_advice():
    df = pd.DataFrame(excel_data["意见与建议"])
    blanks = []
    for i, rv in df.itertuples():
        if type(rv) == str:
            if rv == "(空)":
                blanks.append(i)
    df.drop(blanks, inplace=True)
    print(df)


def comsume():
    explode = (0.1, 0, 0, 0)
    df = pd.DataFrame(excel_data["月消费"].value_counts())
    colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99']
    df.plot.pie(subplots=True, label=None, colors=colors, shadow=True, autopct='%1.1f%%', fontsize=10, startangle=90,
                figsize=(6, 6), explode=explode)

    price_lim = ["<1000", "1000~2000", "2000~3000", ">4000"]
    plt.title("学生月消费水平百分比")
    plt.ylabel(None)
    plt.legend(price_lim)
    plt.show()


def main():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    excel_info()
    # nlp_info()
    bike_way()
    age_way()
    live_way()
    bike_price()
    electric_suitable()
    nonbike_reason()
    change_or_not()
    sharebike_choose()
    #some_reason()
    change_reason()
    out_trouble()
    get_advice()
    comsume()
    # fill_empty()
   

if __name__ == '__main__':
    main()
