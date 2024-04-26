#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- 作者： codervibe -*-
# -*- 时间: 18 ：46 -*-
# -*- 获取 IP 地址定位 -*-
# -*-  2.1  -*-

import requests
import argparse
import json
import random


def get_parameter():
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='查看IP的归属地')
    # 添加命令行参数
    parser.add_argument('-a', dest='ipaddr', type=str, default='', help='输入查询IP')
    parser.add_argument('-f', dest='file', type=str, default='', help='从文件中读取IP列表进行查询')
    parser.add_argument('-v', '--version', action='store_true', help='显示脚本的版本信息')
    # 解析参数
    args = parser.parse_args()

    # 如果没有提供查询IP地址、文件或版本信息，则报错
    if not args.version and not args.ipaddr and not args.file:
        parser.error("请指定要查询的IP地址或文件。")

    return args


def get_json(ipaddr):
    # 构造请求URL
    url = 'http://ip-api.com/json/{}?lang=zh-CN'.format(ipaddr)
    # 随机选择一个User-Agent
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0"
    ]
    headers = {
        'User-Agent': random.choice(user_agents),
        'Connection': 'keep-alive'
    }

    try:
        # 发起GET请求
        r = requests.get(url, timeout=15, headers=headers)  # 设置超时时间为15秒
        # 如果请求失败，会抛出异常
        r.raise_for_status()
        r.close()
        result = r.content.decode()
        return result
    except requests.RequestException as e:
        # 网络请求异常处理
        print("网络请求异常:", e)
        return None


def main():
    # 获取命令行参数
    args = get_parameter()

    # 如果提供了版本信息选项，则显示版本信息并退出
    if args.version:
        print("IPAddressQuery version  2.1")
        return

    # 根据参数中提供的IP地址或文件路径进行查询
    if args.ipaddr:
        ip_list = [args.ipaddr]
    else:
        try:
            with open(args.file, 'r') as file:
                ip_list = file.read().splitlines()
        except FileNotFoundError:
            print("指定的文件不存在。")
            return

    # 遍历查询结果并输出
    for ipaddr in ip_list:
        ip_str = get_json(ipaddr)
        if ip_str is None:
            print(f"获取 IP {ipaddr} 归属地信息失败，请检查网络连接或稍后重试。")
            continue

        ip_json = json.loads(ip_str)
        ip_query = ip_json['query']
        ip_country = ip_json['country']
        ip_city = ip_json['city']
        ip_regionName = ip_json['regionName']
        ip_timezone = ip_json['timezone']
        ip_lon = ip_json['lon']
        ip_lat = ip_json['lat']
        ip_isp = ip_json['isp']

        print(f"查询的IP：{ip_query}\n归属地为: {ip_country}, {ip_regionName}, {ip_city}\n时区: {ip_timezone}")
        print(f"经度: {ip_lon}\t纬度: {ip_lat}")
        print(f"互联网服务提供商: {ip_isp}")
        if args.version:
            print(json.dumps(ip_json, indent=4))


if __name__ == '__main__':
    main()
