from flask import Flask, render_template, request, redirect
import os

from sympy import im
import PIL import Image

# Flask는 Flask 객체를 먼저 생성한다
app = Flask(__name__)


#──────────────────────────────────────
# 호출되는 주소를 적어준다.
@app.route('/')
# root 페이지 호출시 처리하는 함수 처리
def index():
    return render_template('index.html')
#──────────────────────────────────────
@app.route('/main')
def main():
    return render_template('method.html')

# <> 안에 있는건 변수를 의미한다 즉 <username>은 username 변수를 만든것이다.
@app.route('/user/<username>')
# 변수를 만들었으므로 함수의 인자 값에 반드시 넣어준다. 
# ex) def show_user() X → def show_user(username) O
def show_user(username):
    # return username +'!!!' 은 /user/hong 을 url에 쓰면 페이지 내용으로  hong!!!가 나온다.
    return username +'!!!'

@app.route('/user/<username>/<int:age>')
def show_user_age(username, age):
    return username+ ':' + str(age)
# return에 int나 그냥 age를 쓰면 Type error 발생
# TypeError: can only concatenate str (not "int") to str


# request object
# Form(post, 딕셔너리), args(get,?뒤에 있는 값 파싱), files, method(post, get, ....)
# methods를 적지 않는다면 default는 'GET'방식이다.

@app.route('/method', methods=['GET','POST'])
def method_test():
    if request.method == 'POST':
        return render_template('show_result.html',data=request.form)
    else :
        return render_template('show_result.html', data=request.args)


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method=='GET':
        return render_template('fileup.html')
    else:
        f = request.files['file']
        #전체경로에서 디렉토리 네임만 들고온다
        path = os.path.dirname(__file__)+'/upload/'+f.filename #저장할 경로 만들기
        print(path)
        f.save(path)
        return redirect('/')   #/를 받는 함수로 가라


@app.route('/mnist',methods=['GET','POST'])
def mnist():
    if request.method == 'GET':
        return render_template('mnistform.html')
    else:
        pass

# app을 run한다.
# 자기가 스스로 동작한다면 __main__이 들어간다.
# debug=True로 주면 서버를 재시작 안하더라도 새로고침으로 변경사항을 바로 확인 할 수 있다.
if __name__ == '__main__':
    app.run(debug=True,port=80)

# static js, css file
# templates html file
# flask에서는 위의 두개의 디렉토리를 자동으로 인식하므로 따로 path를 설정할 필요가 없다.
# ?asdfasd -> QueryString(? 뒤에 붙는다.)