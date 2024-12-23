from flask import Flask,request,jsonify
from linkedin_api import Linkedin


app = Flask(__name__)
@app.route("/")
def home():
    return "Home"

@app.route("/get-user/<username>")
def get_user(username):
    
    api=Linkedin("tgj0464@gmail.com","Nikhil#393")
    try:
        data = api.get_profile(username)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify(data),200


if __name__ == "__main__":
    app.run(debug=True)