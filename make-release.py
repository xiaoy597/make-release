# coding=utf-8

import shutil
import time
import sys
import os.path
import re
import zipfile

project_name = '中央监控系统2期1阶段2批'
dist_file_name = '%s-%s.zip' % (project_name, time.strftime('%Y%m%d', time.localtime()))
project_home = r'C:\Users\xiaoy\Documents\中证监测\技术服务\中央监控系统2期1阶段2批'
release_tag = 'release-%s' % time.strftime('%Y%m%d', time.localtime())
release_dir = os.path.join(project_home, 'target', release_tag)

test_source_files = [
#    r'.*\.docx'.decode('utf8'),
    '测试用例及报告'.decode('utf8')
]


def find_source_files(patterns):
    result = []
    for root, sub_dirs, files in os.walk(project_home.decode('utf8').encode('gbk')):
        for a_dir in sub_dirs:
            for p in patterns:
                if p.search(os.path.join(root.decode('gbk'), a_dir.decode('gbk'))):
                    result.append(os.path.join(root.decode('gbk'), a_dir.decode('gbk')))
        for a_file in files:
            for p in patterns:
                if p.search(os.path.join(root.decode('gbk'), a_file.decode('gbk'))):
                    result.append(os.path.join(root.decode('gbk'), a_file.decode('gbk')))

    return result


def collect_files(source_files):
    source_patterns = []
    for s in source_files:
        source_patterns.append(re.compile(s))

    if os.path.exists(release_dir.decode('utf8').encode('gbk')):
        shutil.rmtree(release_dir.decode('utf8').encode('gbk'))

    os.makedirs(release_dir.decode('utf8').encode('gbk'))

    for f in find_source_files(source_patterns):
        target_file = f.encode('utf8').replace(project_home, release_dir)
#        print target_file
        if os.path.isdir(f.encode('gbk')):
            os.makedirs(target_file.decode('utf8').encode('gbk'))
        else:
            shutil.copy(f.encode('gbk'), target_file.decode('utf8').encode('gbk'))


if __name__ == "__main__":

    print 'Building release for %s-%s ...' % (project_name, time.strftime('%Y%m%d', time.localtime()))

    collect_files(test_source_files)

    os.chdir(os.path.join(project_home, 'target').decode('utf8').encode('gbk'))

    zip_handle = zipfile.ZipFile(dist_file_name.decode('utf8').encode('gbk'), 'w', zipfile.ZIP_DEFLATED)

    for root, sub_dirs, files in os.walk(release_tag):
        for a_dir in sub_dirs:
            print 'Adding %s ...' % os.path.join(root, a_dir).decode('gbk')
            zip_handle.write(os.path.join(root, a_dir))
        for a_file in files:
            print 'Adding %s ...' % os.path.join(root, a_file).decode('gbk')
            zip_handle.write(os.path.join(root, a_file))

    zip_handle.close()
