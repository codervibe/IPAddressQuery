#  IPAddressQuery
~~~shell
PS D:\python\Python_project\IPAddressQuery\main> python .\IPAddressQuery.py  -h

查看IP的归属地

options:
  -h, --help     show this help message and exit
  -a IPADDR      输入查询IP
  -f FILE        从文件中读取IP列表进行查询
  -v, --version  显示脚本的版本信息


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
IPAddressQuery -a 114.114.114.114
查询的IP: 114.114.114.114
归属地为: 中国, 山东省, 潍坊市
时区: Asia/Shanghai
经度: 119.162	纬度: 36.7069
互联网服务提供商: China Unicom Shandong Province network
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
  -h, --help     show this help message and exit
  -a IPADDR      输入查询IP
  -f FILE        从文件中读取IP列表进行查询
  -v, --version  显示脚本的版本信息
~~~
### exe 使用方法
~~~powershell
IPAddressQuery.exe -a  114.114.114.114
查询的IP：114.114.114.114
归属地为: 中国, 山东省, 潍坊市
时区: Asia/Shanghai
经度: 119.162	纬度: 36.7069
互联网服务提供商: China Unicom Shandong Province network
~~~