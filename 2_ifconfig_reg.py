#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import subprocess,os

def el7(rfile):#版本7的解析函数
 while 1:
    line=rfile.readline()#每次读取一行
    if line:
        result_1=line.find("flags")#找新网卡所在的那一行
        if result_1==-1:
            result_2=line.find("inet ")#如果不是找该网卡对应的IP
            if result_2!=-1:
                result_3=line.find("  ",result_2)
                value=line[result_2+5:result_3]#分片，取IP那段
                flag_value=1#找到IP将IP标记置1
        else:			#解析网卡名称
            index=line.find(":")
            flag_key=0		#因为找到了新网卡名称，将网卡标记和IP标记都置0
            flag_value=0	
            key=line[0:index]
            flag_key=1		#网卡标记置1

        if flag_value!=0 and flag_key!=0:#当网卡标记和IP标记都为1时，表示该网卡配置了IP，则加入字典，否则不加入字典
            Ip_hash[key]=value
            flag_key=0
            flag_value=0	
    else:
        break

def el6(rfile):	#同el7，el6和el7的命令输出略有不同
 while 1:
    line=rfile.readline()
    if line:
        result_1=line.find("Link")
        if result_1==-1:
            result_2=line.find("addr:")
            if result_2!=-1:
                result_3=line.find(" ",result_2)
                value=line[result_2+5:result_3]
                flag_value=1
        else:
            index=line.find(" ")
            flag_key=0
            flag_value=0
            key=line[0:index]
            flag_key=1

        if flag_value!=0 and flag_key!=0:
            Ip_hash[key]=value
            flag_key=0
            flag_value=0
    else:
        break

# __main__
info=subprocess.Popen("ifconfig",shell=True,stdout=subprocess.PIPE)#运行ifconfig命令，输出并保存成文件对象
ver=subprocess.Popen("uname -a",shell=True,stdout=subprocess.PIPE)#运行uname -a 查询版本
flag_key=0
flag_value=0
Ip_hash={}
wfile=open("ifconfig.txt","w")
wfile.write(str(info.stdout.read()))
wfile.close()
rfile=open("ifconfig.txt")
str_ver=str(ver.stdout.readline())

if str_ver.find("el7")!=-1:
    el7(rfile)
elif str_ver.find("el6")!=-1:
    el6(rfile)
else:
    print("only support centos6/7 and redhat 6/7")
rfile.close()
os.system("rm -f ifconfig.txt")
print("网卡信息：")
print(Ip_hash)
