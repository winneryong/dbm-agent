import logging
from logging import handlers
import argparse


def log_config(root_logger_name='dbma',filename="/usr/local/dbma/logs/dbma.log",max_bytes=1024*1024*64,backup_count=7):
    """
    完成两件事 1): 日志相关内容的设置 
    """
    logger = logging.getLogger(root_logger_name)
    logger.setLevel(logging.DEBUG)
    #当文件大小达到64M时就创建一个新的文件，用于记录日志，留7个备份
    file_handler = handlers.RotatingFileHandler(filename,maxBytes=max_bytes,backupCount=backup_count)
    formater = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s]    %(message)s")
    file_handler.setFormatter(formater)
    logger.addHandler(file_handler)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='dbm-agent')
    parser.add_argument('--user',default='dbma')
    args = parser.parse_args()



