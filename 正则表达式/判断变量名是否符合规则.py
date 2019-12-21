import re


def main():
    variable_name = ['name0', 'name_one', '_name1', '0_name', 'name!#']
    for name in variable_name:
        ret = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$',name)
        if ret:
            print('%s 命名符合变量命名规范' % ret.group())
        else:
            print('%s 命名不符合变量名规范' % name)


if __name__=='__main__':
    main()
