import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


# current_app 是另一个特殊对象，该对象指向处理请求的 Flask 应用。这里 使用了应用工厂，那么在其余的代码中就不会出现应用对象。当应用创建后，在处理 一个请求时， get_db 会被调用。这样就需要使用 current_app 。
# g 是一个特殊对象，独立于每一个请求。在处理请求过程中，它可以用于储存 可能多个函数都会用到的数据。把连接储存于其中，可以多次使用，而不用在同一个 请求中每次调用 get_db 时都创建一个新的连接。
def get_db():
    if 'db' not in g:
        # sqlite3.connect() 建立一个数据库连接，该连接指向配置中的 DATABASE 指定的文件。这个文件现在还没有建立，后面会在初始化数据库的时候建立该文件。
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.Row 告诉连接返回类似于字典的行，这样可以通过列名称来操作 数据。
        g.db.row_factory = sqlite3.Row
    return g.db


# close_db 通过检查 g.db 来确定连接是否已经建立。如果连接已建立，那么 就关闭连接。以后会在应用工厂中告诉应用 close_db 函数，这样每次请求后就会 调用它。
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    # get_db 返回一个数据库连接，用于执行文件中的命令
    db = get_db()
    # open_resource() 打开一个文件，该文件名是相对于 flaskr 包的。这样就不需要考虑以后应用具体部署在哪个位置
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# click.command() 定义一个名为 init-db 命令行，它调用 init_db 函数，并为用户显示一个成功的消息。 更多关于如何写命令行的内容请参阅 ref:cli 。
@click.command('init-db')
@with_appcontext
def init_db_command():
    """clear the existing data and create new tables"""
    init_db()
    click.echo('initialized the database.')


def init_app(app):
    # app.teardown_appcontext() 告诉 Flask 在返回响应后进行清理的时候调用此函数。
    app.teardown_appcontext(close_db)
    # app.cli.add_command() 添加一个新的 可以与 flask 一起工作的命令。
    app.cli.add_command(init_db_command)
