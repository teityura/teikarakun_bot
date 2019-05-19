#!/bin/env python3.6
# encoding: utf-8

import argparse
import requests
from datetime import datetime


# 引数解析
def getargs():
    parser = argparse.ArgumentParser(
        prog='match.py',
        usage=r'''
        ex:
            match.py regular
            match.py gachi
            match.py league
        ''',
        add_help=True,
    )
    parser.add_argument('mode', help='mode')
    args = parser.parse_args()

    # 辞書で返す
    return vars(args)


def main(mode=None):
    if mode is None:
        args = getargs()
        res_json = requests.get(f'''https://spla2.yuu26.com/{args["mode"]}/now''').json()["result"]
    else:
        res_json = requests.get(f'''https://spla2.yuu26.com/{mode}/now''').json()["result"]

    target_dic = {
        "ルール": res_json[0]["rule"],
        "開始": datetime.strptime(res_json[0]["start"], '%Y-%m-%dT%H:%M:%S').strftime('%m/%d %H:%M'),
        "終了": datetime.strptime(res_json[0]["end"], '%Y-%m-%dT%H:%M:%S').strftime('%m/%d %H:%M'),
        "ステージ1": res_json[0]["maps"][0],
        "ステージ2": res_json[0]["maps"][1],
    }
    if mode in ["gachi", "league"]:
        target_dic["ルール"] += f"({mode})"
    try:
        target_dic["ステージ3"] = res_json[0]["maps"][2],  # フェス用
    except IndexError:
        target_dic["ステージ3"] = None

    rtn_text = "\n".join([f"{k} : {v}" for k, v in target_dic.items() if v is not None])
    print(rtn_text)
    return rtn_text


if __name__ == "__main__":
    main()

