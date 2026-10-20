from flask import request,make_response,session,Blueprint
from app.models import Article

article_bp=Blueprint("article",__name__)
@article_bp.route('/clear',methods=["GET"])
def clear_session():
    #session["page_views"]=0
    session.clear()

    response={"message":"200:Successfully cleared session data"}

    return make_response(response,200)
@article_bp.route('/all',methods=["GET"])
def show_articles():
    articles=[article.to_dict(rules=("-user",)) for article in Article.query.all()]

    response=make_response(
        articles,
        200
    )
    return response
@article_bp.route('/<int:id>',methods=["GET"])
def show_article(id):
    article=Article.query.filter(Article.id == id).first()

    if article is None:
        return {"message":"OOOPPs!!! The record does not exist in our database"},404
    session["page_views"]=session.get("page_views") or 0
    session["page_views"] +=1

    if session["page_views"] <=3:
        return article.to_dict(rules=("-user",)),200
    return {"message":"Maximum pageview limit reached"},401

    