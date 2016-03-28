#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse
import os

def cron_save():
	os.system("cd ~")
	os.system("crontab -l > cronsave.txt")  #将crontab信息存入cronsave.txt中

def cron_delt():
	os.system("rm -f cronsave.txt")

def cron_start(arg):
	try:
		start_flag=0
		cron_save()
		rfile=open("cronsave.txt")
		while 1:
			line=rfile.readline()
			if line:
				index=line.find(str(arg.start[0]))#本行包含任务名
				if index!=-1:
					command='''crontab -l |sed "/^#.*%s/s/^#//"|crontab''' % str(arg.start[0])#sed+正则表达式将指定的任务修改--以#开头的该任务去掉#号
					os.system(command)
					start_flag=start_flag+1 #该任务名可能有多个任务
			else:
				break
		if start_flag==0:
			print("         crontab not has this job,please make sure jobname right")
		else:
			print("         start %s successful" % str(arg.start[0]))
		rfile.close()
		cron_delt()
	except:
		print("		something error")
		rfile.close()
		cron_delt()
		os.exit()

def cron_stop(arg):
	try:
		stop_flag=0
		cron_save()
		rfile=open("cronsave.txt","r")
		while 1:
			line=rfile.readline()
			if line:
	                	index=line.find(str(arg.stop[0]))
				if index!=-1:
	                	        command='''crontab -l |sed "/^[^#].*%s/s/^/#/"|crontab''' % str(arg.stop[0])#sed+正则表达式将指定的任务修改--非#开头的该任务加上#号
	                	        os.system(command)
					stop_flag=stop_flag+1
			else:
				break
		if stop_flag==0:
			print("         crontab not has this job,please make sure jobname right")
		else:
			print("         stop %s successful" % str(arg.stop[0]))
		rfile.close()
	        cron_delt()
	except:
		print("		something error")
                rfile.close()
                cron_delt()
		os.exit()
		

def cron_list(arg):
        command="crontab -l|grep %s" % str(arg.list[0])
        os.system(command)
	
#__main__
par=argparse.ArgumentParser()#能够识别--start,--stop,--list参数
par.add_argument('--start',nargs=1,help="start your job,demo: ./demo3.py --start job1")#nargs=1：后面必须跟一个参数
par.add_argument('--stop',nargs=1,help="stop your job,demo: ./demo3.py --stop job1")
par.add_argument('--list',nargs=1,help="list your job,demo: ./demo3.py --list job1")
arg=par.parse_args()#返回参数对象
if arg.start!=None and arg.stop==None and arg.list==None:#--start
	INDEX=str(arg.start[0]).find("/") #字符串出现/，sed需要对其转义，/前加上\，但这样代码会很繁琐，所以直接禁止比较好
	if INDEX==-1:
		cron_start(arg)
	else:
		print(" argument must not have /")
elif arg.stop!=None and arg.start==None and arg.list==None:#--stop
	INDEX=str(arg.stop[0]).find("/")
        if INDEX==-1:
		cron_stop(arg)
	else:
                print(" argument must not have /")
elif arg.list!=None and arg.start==None and arg.stop==None:#--list
	INDEX=str(arg.list[0]).find("/")
        if INDEX==-1:
		cron_list(arg)
	else:
                print(" argument must not have /")
else:							#--help
	print("		pleas input ./demo3.py -h to get help")
