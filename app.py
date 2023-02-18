from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.ywsmxxc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    year_receive = request.form['year_give']
    month_receive = request.form['month_give']
    day_receive = request.form['day_give']
    hours_receive = request.form['hours_give']
    # year = datetime.today().year
    # month = datetime.today().month
    # day = datetime.today().day
    # time = datetime.today().hour

    doc = {
        'name' :name_receive,
        'comment': comment_receive,
        'year' : year_receive,
        'month' : month_receive,
        'day' : day_receive,
        'hours' : hours_receive
    }
    db.fan.insert_one(doc)
    
    return jsonify({'msg': '작완~ 작성완료~'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.fan.find({},{'_id':False}))
    return jsonify({'result' : all_comments})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)


# KST = timezone(timedelta(hours=9))

# year = datetime.now(KST).year
# month = datetime.now(KST).month
# day = datetime.now(KST).day
# time = datetime.now(KST).time


#    pip install flask pymongo dnspythone