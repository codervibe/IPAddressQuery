#  IPAddressQuery
~~~shell
PS D:\python\Python_project\IPAddressQuery\main> python .\IPAddressQuery.py  -h

usage: IPAddressQuery.py [-h] [-a IPADDR] [-f FILE] [-r] [-v] [-u]

查看IP的归属地

options:
  -h, --help          show this help message and exit
  -a IPADDR           输入查询IP
  -f FILE             从文件中读取IP列表进行查询
  -r, --random-agent  启用随机User-Agent
  -v, --version       显示脚本的版本信息
  -u, --update        更新脚本



~~~
### 下载和使用 
~~~
git clone https://github.com/codervibe/IPAddressQuery
cd IPAddressQuery/main
python3 IPAddressQuery.py
~~~
* 因为 kali linux 是可以 执行 py脚本的所以 可以这样使用
~~~bash
cd IPAddressQuery/main/
cp ./IPAddressQuery.py /usr/bin/IPAddressQuery
# 直接执行即可
cd ~ 
IPAddressQuery -a 114.114.114.11
~~~
* 运行效果
~~~shell
IPAddressQuery -a 69.154.123.56
查询的IP: 69.154.123.56
归属地为: 美国, 阿肯色州, 费耶特维尔
时区: America/Chicago
经度: -94.1523	纬度: 36.0613
互联网服务提供商: AT&T Services, Inc.
谷歌地图:  https://www.google.com/maps/place/36.0613+-94.1523

~~~
* 支持 proxychains4 代理 查询
~~~shell
proxychains4 IPAddressQuery -h              
[proxychains] config file found: /etc/proxychains4.conf
[proxychains] preloading /usr/lib/aarch64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.17
usage: IPAddressQuery [-h] [-a IPADDR] [-v]

查看IP的归属地

options:
  -h, --help      show this help message and exit
  -a IPADDR       输入查询IP
  -f FILE         从文件中读取IP列表进行查询
  --random-agent  启用随机User-Agent
  -v, --version   显示脚本的版本信息

~~~
### exe 使用方法
~~~powershell
IPAddressQuery -a 69.154.123.56
查询的IP：69.154.123.56
归属地为: 美国, 阿肯色州, 费耶特维尔
时区: America/Chicago
经度: -94.1523	纬度: 36.0613
互联网服务提供商: AT&T Services, Inc.
谷歌地图:  https://www.google.com/maps/place/36.0613+-94.1523
~~~