#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- 作者： codervibe -*-
# -*- 时间: 18 ：46 -*-
# -*- 获取某个城市的天气 -*-
# -*-  1.9  -*-

import requests
import argparse
import json
import random

def get_parameter():
    parser = argparse.ArgumentParser(description='查看IP的归属地')
    parser.add_argument('-a', dest='ipaddr', type=str, default='', help='输入查询IP')
    # 设定一个参数 c 或者 city 将这个参数传入并查询
    parser.add_argument('-v', help='Optional parameters', action='version', version="IPAddressQuery version 1.2.0")
    args = parser.parse_args()
    if not args.ipaddr:
        parser.print_help()
        exit()
    ipaddr = args.ipaddr

    return ipaddr


def get_json(ipaddr):
    url = 'http://ip-api.com/json/{}?lang=zh-CN'.format(ipaddr)
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    ]
    headers = {
        'User-Agent': random.choice(user_agents),
        'Connection': 'keep-alive'
    }

    try:
        r = requests.get(url, timeout=15, headers=headers)
        r.raise_for_status()  # 如果请求失败，会抛出异常
        r.close()
        result = r.content.decode()
        return result
    except requests.RequestException as e:
        print("网络请求异常:", e)
        return None


def main():
    ipaddr = get_parameter()
    ip_str = get_json(ipaddr)
    if ip_str is None:
        print("获取 IP 归属地信息失败，请检查网络连接或稍后重试。")
        return

    ip_json = json.loads(ip_str)
    # print(ip_json)
    # 国家
    ip_country = ip_json['country']
    # 城市
    ip_city = ip_json['city']
    # IP地址
    ip_query = ip_json['query']
    # 地区名称
    ip_regionName = ip_json['regionName']
    # 时区
    ip_timezone = ip_json['timezone']
    #  lat是纬度的意思。lon经度，经线的意思。
    # 经度
    ip_lon = ip_json['lon']
    # 纬度
    ip_lat = ip_json['lat']
    # 互联网服务提供商
    ip_isp = ip_json['isp']
    print('查询的IP：{}\n归属地为:{},{},{}\n时区:{}\t'.format(ip_query, ip_country,
                                                    ip_regionName, ip_city, ip_timezone))

    print('经度:{}\t纬度:{}\t'.format(ip_lon, ip_lat))

    print('互联网服务提供商:\t{}'.format(ip_isp))


if __name__ == '__main__':
    main()
