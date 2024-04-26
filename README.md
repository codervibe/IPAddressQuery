#  IPAddressQuery
~~~shell
usage: IPAddressQuery [-h] [-a IPADDR] [-v]

查看IP的归属地

options:
  -h, --help  show this help message and exit
  -a IPADDR   输入查询IP
  -v          Optional parameters

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
  -h, --help  show this help message and exit
  -a IPADDR   输入查询IP
  -v          Optional parameters

~~~