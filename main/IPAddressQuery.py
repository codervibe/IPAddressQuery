#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- 作者： codervibe -*-
# -*- 时间: 18 ：46 -*-
# -*- 获取 IP 地址定位 -*-
# -*-  2.5.2  -*-

import requests
import argparse
import json
import random
import logging
import subprocess

# 将User-Agent集合定义为一个配置项
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0"
]

# 定义脚本版本号
version = "3.0.0"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_parameter():
    """
    解析命令行参数，包括IP地址、文件路径、是否使用随机User-Agent、显示版本信息和更新脚本
    :return: 返回解析后的参数对象
    """
    parser = argparse.ArgumentParser(description='查看IP的归属地')
    parser.add_argument('-a', dest='ipaddr', type=str, default='', help='输入查询IP')
    parser.add_argument('-f', dest='file', type=str, default='', help='从文件中读取IP列表进行查询')
    parser.add_argument('-r', '--random-agent', action='store_true', help='启用随机User-Agent')
    parser.add_argument('-v', '--version', action='store_true', help='显示脚本的版本信息')
    parser.add_argument('-u', '--update', action='store_true', help='更新脚本')
    args = parser.parse_args()

    # 检查参数并打印帮助信息
    if not args.ipaddr and not args.file and not args.version and not args.update:
        parser.print_help()
        parser.exit()

    return args


def get_json(ipaddr, use_random_agent=False):
    """
    发送HTTP请求获取IP地址的JSON信息
    :param ipaddr: 需要查询的IP地址
    :param use_random_agent: 是否使用随机User-Agent
    :return: 返回请求结果的JSON字符串或None
    """
    url = 'http://ip-api.com/json/{}?lang=zh-CN'.format(ipaddr)
    headers = {'Connection': 'keep-alive'}

    if use_random_agent:
        headers['User-Agent'] = random.choice(USER_AGENTS)

    try:
        r = requests.get(url, timeout=15, headers=headers)
        r.raise_for_status()
        r.close()
        return r.content.decode()
    except requests.RequestException as e:
        print("网络请求异常:", e)
        return None


def parse_json(ip_str):
    """
    解析JSON字符串并返回相关信息，增加异常处理
    :param ip_str: JSON格式的字符串
    :return: 返回解析后的JSON对象或None
    """
    try:
        ip_json = json.loads(ip_str)
        return ip_json
    except json.JSONDecodeError:
        print("JSON解析失败，请检查返回的数据格式。")
        return None


def update_script():
    """
    更新本地仓库到最新版本。

    使用 `git pull` 命令从远程仓库拉取最新的代码，并记录日志。
    如果更新过程中出现错误，记录错误日志。
    """
    try:
        result = subprocess.run(['git', 'pull'], check=True, capture_output=True, text=True)
        logging.info("更新成功: %s", result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("更新失败: %s", e.stderr)
    except FileNotFoundError:
        logging.error("Git 命令未找到，请确保已安装 Git 并将其添加到系统路径中。")


def main():
    """
    主函数，处理命令行参数，读取IP地址，发送请求并解析响应
    """
    args = get_parameter()

    if args.update:
        update_script()
        return

    if args.version:
        print(f"IPAddressQuery version  {version}")
        return

    if args.ipaddr:
        ip_list = [args.ipaddr]
    else:
        try:
            with open(args.file, 'r') as file:
                ip_list = file.read().splitlines()
        except FileNotFoundError:
            print("指定的文件不存在。")
            return

    for ipaddr in ip_list:
        ip_str = get_json(ipaddr, use_random_agent=args.random_agent)
        if ip_str is None:
            print(f"获取 IP {ipaddr} 归属地信息失败，请检查网络连接或稍后重试。")
            continue

        ip_json = parse_json(ip_str)
        if ip_json is None:
            continue
        # 如果 ip_json 不为空 且 有 country
        if ip_json and 'country' in ip_json:
            print(f"IP {ipaddr} 归属地信息:")
            # 输出IP信息
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
            print(f"谷歌地图:  https://www.google.com/maps/place/{ip_lat}+{ip_lon}")
        else:
            ip_query = ip_json['query']
            ip_message = ip_json['message']
            print(f"查询的IP：{ip_query}\n归属地为: {ip_message}")

        if args.version:
            print(json.dumps(ip_json, indent=4))


if __name__ == '__main__':
    main()
