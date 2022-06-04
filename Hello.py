from flask import Flask

app = Flask(__name__)

@app.route('/')         # создаёт  домашнюю страницу
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>Next text</p>' \
           '<img src="https://media.giphy.com/media/VxbvpfaTTo3le/giphy.gif" width=250>'


def make_bold(function):
    """Обёртка для жирного текста"""
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_em(function):
    """Обёртка для курсива текста"""
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    """Обёртка для подчёркивания текста"""
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/bye")    # создаёт страницу bye
@make_bold
@make_em
@make_underlined
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")    # создаёт страницу c именем которое вводиться в браузере
def great(name, number):
    return f"Hello {name}, you are {number}"

if __name__ == '__main__':
    app.run(debug=True)      # debug=True запускает дебаг чтобы не перезагружать сервер
