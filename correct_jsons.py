# -*- coding: utf-8 -*-
# @Author: Tom Lotze
# @Date:   2020-04-11 14:53
# @Last Modified by:   Tom Lotze
# @Last Modified time: 2020-04-11 14:58

import os
import json



json_files = [file for file in os.listdir("./data") if file.endswith(".json")]

for file in json_files:
    with open("./data/" + file) as f:
        dic = json.load(f)
        assert len(list(dic.keys())) == 1
        key = list(dic.keys())[0]
        ranking = dic[key]

    with open(f"./data/" + file, "w") as writer:
        json.dump(ranking, writer, indent=1)

