from app import create_app 

app=create_app()

@app.route('/',methods=["GET"])
def home():
    return {"message":"Welcome to Blog-Paywall API"},200

if __name__=="__main__":
    app.run(port=5555,debug=True)