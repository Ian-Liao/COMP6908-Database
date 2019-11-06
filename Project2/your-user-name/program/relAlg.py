import json
import pandas as pd


def select(rel, att, op, val):
    with open(rel) as f:
        content = f.readlines()[0]
        data = json.loads(content)
        df = pd.DataFrame(data[1:], columns=data[0])
        print(df)
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
        print(res)


def project(rel, attList):
    with open(rel) as f:
        content = f.readlines()[0]
        data = json.loads(content)
        df = pd.DataFrame(data[1:], columns=data[0])
        df = df.filter(attList)
        df.drop_duplicates(keep=False, inplace=True)
        res = [df.columns.values.tolist()] + df.values.tolist()
        print(res)


def join(rel1, att1, rel2, att2):
    pass
