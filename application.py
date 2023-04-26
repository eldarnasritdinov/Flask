from flask import Flask

application = Flask(__name__)


@application.route('/')
def main_page():
    file_1 = open('final.html', mode='r')
    page_1 = file_1.read()
    file_1.close()
    return page_1


@application.route('/contacts')
def contacts_page():
    return '<h1>0 (556) 11 03 05</h1>'


if __name__ == '__main__':
    # application.debug = True
    application.run()