"""
反射
"""
class User:
    def add(self):
        print('新增一名用户')

    def delete(self):
        print('删除一名用户')

    def update(self):
        print('更新一名用户')

    def select(self):
        print('查询一名用户')

    def before_process(self, method):
        if method == 'add':
            self.add()
        elif method == 'delete':
            self.delete()
        elif method == 'update':
            self.update()
        elif method == 'select':
            self.select()
        else:
            print('无效调用')

    def after_process(self, method):
        """
        类似路由转发
        :param method:
        :return:
        """
        if hasattr(self, method):
            # 获取方法
            func = getattr(self, method)
            # 执行
            func()
        else:
            print('无效调用')

if __name__ == '__main__':
    user = User()
    user.before_process('add')
    user.after_process('add')
