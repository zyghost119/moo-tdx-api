# -*- coding: utf-8 -*-
"""
@Author Andon
@Time 2021/3/11

"""
import json

import flask
from mootdx import consts
from mootdx.consts import MARKET_SH
from mootdx.quotes import Quotes

server = flask.Flask(__name__)


# 指数K线行情
@server.route("/getPriceTdx", methods=["get"])
def getPriceTdx():
    frequency = flask.request.values.get("frequency")
    symbol = flask.request.values.get("symbol")
    start = flask.request.values.get("start")
    offset = flask.request.values.get("offset")
    client = Quotes.factory(market='std')
    price = client.index(frequency=frequency, market=MARKET_SH, symbol=symbol, start=start, offset=offset)
    columns = price.columns
    print(type(columns))
    print(columns)
    to_json = price.to_json(orient="records", force_ascii=False)
    return to_json


# 查询股票列表
@server.route("/getCodeTdx", methods=["get"])
def getCodeTdx():
    client = Quotes.factory(market='std')
    symbol = client.stocks(market=consts.MARKET_SH)
    columns = symbol.columns
    print(type(columns))
    print(columns)
    to_json = symbol.to_json(orient="records", force_ascii=False)
    return to_json


@server.route("/hello", methods=["get"])
def hello():
    res = {"msg": "这是一个接口", "msg_code": 0}
    print(type(res))
    json_str = json.dumps(res, ensure_ascii=False)
    print(type(json_str))
    print(json_str)
    return json_str


@server.route("/postTest", methods=["post"])
def postTest():
    key = flask.request.values.get("key")
    value = flask.request.values.get("value")
    print(type(key))
    print(key)
    print(value)
    return value


server.run(host="0.0.0.0", port=9999, debug=True)  # 改了代码之后,不用重启服务,会自动重启
