from flask import Blueprint,url_for,render_template

bp = Blueprint('views_home',__name__,static_folder="../frontend/dist/",static_url_path="/",template_folder="../frontend/dist/")

# home page
@bp.route("/",methods=["GET"])
def home_page():
    print(url_for('static',filename="favicon.ico"))
    return render_template("index.html")


