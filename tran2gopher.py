#coding: utf-8
#author: JoyChou
import sys
exp = ''
with open(sys.argv[1]) as f:
    for line in f.readlines():
        if line[0] in '><+':
            continue
        # 判断倒数第2、3字符串是否为\r
        elif line[-3:-1] == r'\r':
            # 如果该行只有\r，将\r替换成%0a%0d%0a
            if len(line) == 3:
                exp = exp + '%0a%0d%0a'
            else:
                line = line.replace(r'\r', '%0d%0a')
                # 去掉最后的换行符
                line = line.replace('\n', '')
                exp = exp + line
        # 判断是否是空行，空行替换为%0a
        elif line == '\x0a':
            exp = exp + '%0a'
        else:
            line = line.replace('\n', '')
            exp = exp + line
print exp
