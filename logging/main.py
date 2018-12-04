# -*- coding: utf-8 -*-

# In[1]
import logging

# In[2]
# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# 默认情况下，logging将日志打印到屏幕，日志级别为WARNING
def simple_example():
	logging.debug('debug message')
	logging.info('info message')
	logging.warning('warn message')
	logging.error('error message')
	logging.critical('critical message')

# In[3]
def logging_to_file():
	FILENAME = "example.log"
	logging.basicConfig(filename=FILENAME, level=logging.DEBUG)	
	logging.debug('debug message')
	logging.info('info message')
	logging.warning('warn message')
	logging.error('error message')
	logging.critical('critical message')
	
# In[4]
def format_logging():
	'''
    format参数中可能用到的格式化串
    %(name)s Logger的名字
    %(levelno)s 数字形式的日志级别
    %(levelname)s 文本形式的日志级别
    %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    %(filename)s 调用日志输出函数的模块的文件名
    %(module)s 调用日志输出函数的模块名
    %(funcName)s 调用日志输出函数的函数名
    %(lineno)d 调用日志输出函数的语句所在的代码行
    %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
    %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
    %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
    %(thread)d 线程ID。可能没有
    %(threadName)s 线程名。可能没有
    %(process)d 进程ID。可能没有
    %(message)s用户输出的消息
	from: https://www.jianshu.com/p/4993b49b6888
    '''
	logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s - %(message)s')
	logging.warning("warning")

def complex_example():
	from logging import handlers
	FILENAME = "example.log"
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.INFO)
	formatter = logging.Formatter(
			fmt="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s - %(message)s",
			datefmt="%y/%m/%d %H:%M:%S")
	
	# 配置输出到控制台
	console_logging = logging.StreamHandler()
	console_logging.setLevel(logging.WARNING)
	console_logging.setFormatter(formatter)
	logger.addHandler(console_logging)
	
	# 配置输出到文件
	file_logging = logging.FileHandler(FILENAME)
	file_logging.setLevel(logging.WARNING)
	file_logging.setFormatter(formatter)
	logger.addHandler(file_logging)
	
	file_time_rotating = handlers.TimedRotatingFileHandler("app.log",when="s",interval=10,backupCount=5)
	file_time_rotating.setLevel(logging.INFO)
	file_time_rotating.setFormatter(formatter)
	logger.addHandler(file_time_rotating)

	
	logger.debug("debug")
	logger.info("info")
	logger.warning("warning")
	logger.error("error")
	logger.critical("critical message")
	
	import time
#	import random
	
	for i in range(100):	
		time.sleep(1)
		logger.warning(str(i)+' warn')

if __name__ == '__main__':
#	simple_example()
#	logging_to_file()
#	format_logging()
	complex_example()