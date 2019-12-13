import os
from flask import Flask
from . import db
from . import auth
from . import blog

def create_app(test_config=None):
    # 创建和配置app实例
    app = Flask(__name__, instance_relative_config=True)
    # 是当前 Python 模块的名称
    #  instance_relative_config=True 告诉应用配置文件是相对于 instance folder 的相对路径。实例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当 提交到版本控制系统。
    app.config.from_mapping(
        SECRET_KEY="dev",
        # SECRET_KEY 是被 Flask 和扩展用于保证数据安全的。在开发过程中， 为了方便可以设置为 'dev' ，但是在发布的时候应当使用一个随机值来 重载它。
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite')
        # DATABASE SQLite 数据库文件存放在路径
    )
    if test_config is None:
        # 如果实例配置存在且没有测试，那就加载
        app.config.from_pyfile('config.py', silent=True)
        # app.config.from_pyfile() 使用 config.py 中的值来重载缺省配置，如果 config.py 存在的话。 例如，当正式部署的时候，用于设置一个正式的 SECRET_KEY 。
    else:
        # 如果通过就加载测试配置
        app.config.from_mapping(test_config)
        # 确保实例文件夹存在
        # test_config 也会被传递给工厂，并且会替代实例配置。这样可以实现 测试和开发的配置分离，相互独立。
    try:
        os.makedirs(app.instance_path)
        # Flask 不会自动 创建实例文件夹，但是必须确保创建这个文件夹，因为 SQLite 数据库文件会被 保存在里面。
    except OSError:
        pass

        # 简单页面

    @app.route('/home')
    def home():
        return 'home'

    # 在工厂中导入并调用这个函数
    db.init_app(app)
    
    # 使用 app.register_blueprint() 导入并注册 蓝图。新的代码放在工厂函数的尾部返回应用之前。
    app.register_blueprint(auth.bp)

    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
