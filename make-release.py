# coding=utf-8

import shutil
import time
import sys
import codecs
import os.path
import re

project_home = r'C:\Users\xiaoy\Documents\中证监测\技术服务\中央监控系统2期1阶段2批'
target_path = os.path.join(project_home, 'target')

print project_home


def find_source_files(patterns):
    result = []
    for root, sub_dirs, files in os.walk(codecs.encode(codecs.decode(project_home, 'utf-8'), 'gbk')):
        for a_dir in sub_dirs:
            for p in patterns:
                if p.search(os.path.join(codecs.decode(root, 'gbk'), codecs.decode(a_dir, 'gbk'))):
                    result.append(os.path.join(codecs.decode(root, 'gbk'), codecs.decode(a_dir, 'gbk')))
        for a_file in files:
            for p in patterns:
                if p.search(os.path.join(codecs.decode(root, 'gbk'), codecs.decode(a_file, 'gbk'))):
                    result.append(os.path.join(codecs.decode(root, 'gbk'), codecs.decode(a_file, 'gbk')))

    return result


def collect_test_files():
    source_patterns = []
    for s in [
        r'.*\.docx'.decode('utf8'),
        '测试用例及报告'.decode('utf8')
    ]:
        source_patterns.append(re.compile(s))

    return find_source_files(source_patterns)

