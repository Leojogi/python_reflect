def new_method(self):
    print('我是新来的方法')

def main():
    """
    动态导入模块，并创建类实例执行其中方法
    :return:
    """
    # 动态导入func_001模块
    func001_module = __import__('src.func_001', fromlist=True)
    print(func001_module)

    # 判断是否存在对应类
    if hasattr(func001_module, 'Func001'):
        # 创建Func001类的实例
        func001 = getattr(func001_module, 'Func001')

        # 判断是否存在方法
        if hasattr(func001, 'process'):
            # 获取process方法
            func001_process = getattr(func001, 'process')
            # 执行process方法
            func001_process(func001)
        else:
            print('没有找到对应的方法...')

        # 向实例func001添加new_method方法
        setattr(func001, 'new_method', new_method)

        # 判断是否存在方法
        if hasattr(func001, 'new_method'):
            # 获取new_method方法
            func001_new_method = getattr(func001, 'new_method')
            # 执行new_method方法
            func001_new_method(func001)

        # 删除func001新增的方法
        delattr(func001, 'new_method')
        print('是否存在新增的方法new_method', hasattr(func001, 'new_method'))
    else:
        print('没有找到类Func001')

if __name__ == '__main__':
    main()