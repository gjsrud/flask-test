from flask import Flask,render_template
#간단하게 웹을 띄울 수 있다. 

#플라스크 객체를 생성
app = Flask(__name__)

@app.route('/')
#호출을 처리하는 함수
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return 'main!'

# __name__: 다른곳에서 실행시키면 파일이름이 뜨고
# 직접 실행하면 __main__이 뜬다
if __name__ == '__main__':
    #debug=True는 서버를 안내리고 새로고침해도 수정이 되어있다.
    app.run(debug=True,port=80)