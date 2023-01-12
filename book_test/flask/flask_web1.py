import pymysql  # 导入数据库模块
from flask import Flask  # 导入Flask框架，可以快捷地实现了一个WSGI应用
from flask import render_template  # 默认情况下，flask在程序文件夹中的templates子文件夹中寻找模块
from flask import request  # 导入前台请求的request模块
import traceback  # 传递根目录

app = Flask(__name__)


# 默认路径访问登录页面
@app.route('/')
def login():
    return render_template('login.html')


# 默认路径访问注册页面
@app.route('/regist')
def regist():
    return render_template('regist.html')


# 获取登录参数及处理
@app.route('/login')
def getLoginRequest():
    # 查询用户名及密码是否匹配及存在
    # 连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect("localhost", "root", "123456", "TESTDB")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select * from user where user=" + request.args.get('user') + " and password=" + request.args.get(
        'password') + ""
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print(len(results))
        if len(results) == 1:
            return '登录成功'
        else:
            return '用户名或密码不正确'
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()


# 使用__name__ == '__main__'是 Python 的惯用法，
# 确保直接执行此脚本时才启动服务器，若其他程序调用该脚本可能父级程序会启动不同的服务器
if __name__ == '__main__':
    app.run(debug=True)