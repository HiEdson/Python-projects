from flask import render_template,request,Blueprint
from puppycompanyblog.models import BlogPost
from puppycompanyblog.blog_posts.forms import SearchForm

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.filter_by(title='brand')
    return render_template('index.html',blog_posts=blog_posts)
    #order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)


@core.route('/info')
def info():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('info.html')




"""@core.route('/search')  sess.query(User).filter(User.age == 25)
def w_search():
    keyword = request.args.get('keyword')
    results = BlogPost.query.msearch(keyword,fields=['title'],limit=20).all()   #.filter(...)
    # elasticsearch
    keyword = "title:book AND content:read"
    # more syntax please visit https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html
    results = BlogPost.query.msearch(keyword,limit=20).all()
    return render_template('index.html',blog_posts=results)"""