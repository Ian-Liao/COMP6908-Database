import json
import pandas as pd


def select(rel, att, op, val):
    res = ""
    with open(rel) as f:
        content = f.readlines()[0]
        data = json.loads(content)
        df = pd.DataFrame(data[1:], columns=data[0])
        if op == '<':
            df = df.loc[df[att] < val]
        elif op == '<=':
            df = df.loc[df[att] <= val]
        elif op == '=':
            df = df.loc[df[att] == val]
        elif op == '>':
            df = df.loc[df[att] > val]
        elif op == '>=':
            df = df.loc[df[att] >= val]
        else:
            raise Exception('Invalid op value!!!')
        res = [df.columns.values.tolist()] + df.values.tolist()

    tmp_result = "../data/Temporary/tmp.txt"
    with open(tmp_result, "w") as f:
        f.write(json.dumps(res))

    return tmp_result


def project(rel, attList):
    with open(rel) as f:
        content = f.readlines()[0]
        data = json.loads(content)
        df = pd.DataFrame(data[1:], columns=data[0])
        df = df.filter(attList)
        df.drop_duplicates(keep=False, inplace=True)
        res = [df.columns.values.tolist()] + df.values.tolist()

    tmp_result = "../data/Temporary/tmp.txt"
    with open(tmp_result, "w") as f:
        f.write(json.dumps(res))

    return tmp_result


def join(rel1, att1, rel2, att2):
    with open(rel1) as f1, open(rel2) as f2:
        content1 = f1.readlines()[0]
        content2 = f2.readlines()[0]
        data1 = json.loads(content1)
        data2 = json.loads(content2)
        df1 = pd.DataFrame(data1[1:], columns=data1[0])
        df2 = pd.DataFrame(data2[1:], columns=data2[0])
        df = pd.merge(df1, df2, left_on=att1, right_on=att2, how='inner')
        res = [df.columns.values.tolist()] + df.values.tolist()

    tmp_result = "../data/Temporary/tmp.txt"
    with open(tmp_result, "w") as f:
        f.write(json.dumps(res))

    return tmp_result
