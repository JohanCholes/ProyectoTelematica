from flask import Flask, jsonify

app = Flask(__name__)

names = ['Chucho', 'Benju', 'Mafe']
passwords = ['1234', 'abcd', 'qwerty']


@app.route('/users')
def get_users():
    users = [{'nombre': nombre, 'contraseña': contraseña} for nombre, contraseña in zip(names, passwords)]
    return jsonify(users)

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=80)
