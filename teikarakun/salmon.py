#!/bin/env python3.6
# encoding: utf-8

import requests
from datetime import datetime


def main():
    res_json = requests.get("https://spla2.yuu26.com/coop/schedule").json()["result"]

    target_dic = {
        "空き状況": None,
        "ステージ": None,
        "オープン": None,
        "クローズ": None,
        "ブキ1": None,
        "ブキ2": None,
        "ブキ3": None,
        "ブキ4": None,
    }

    start = datetime.strptime(res_json[0]["start"], '%Y-%m-%dT%H:%M:%S')
    end = datetime.strptime(res_json[0]["end"], '%Y-%m-%dT%H:%M:%S')
    now = datetime.now()
    if start <= now <= end:
        target_dic["空き状況"] = "オープン"
    else:
        target_dic["空き状況"] = "クローズ"
    target_dic["ステージ"] = res_json[0]["stage"]["name"]
    target_dic["オープン"] = start.strftime('%m/%d %H:%M')
    target_dic["クローズ"] = end.strftime('%m/%d %H:%M')
    target_dic["ブキ1"] = res_json[0]["weapons"][0]["name"]
    target_dic["ブキ2"] = res_json[0]["weapons"][1]["name"]
    target_dic["ブキ3"] = res_json[0]["weapons"][2]["name"]
    target_dic["ブキ4"] = res_json[0]["weapons"][3]["name"]

    rtn_text = "\n".join([f"{k} : {v}" for k, v in target_dic.items()])
    print(rtn_text)
    return rtn_text


if __name__ == "__main__":
    main()

