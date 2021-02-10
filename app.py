from flask import Flask
from flask import jsonify
from flask import request
from flask import url_for
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
cache = Cache(app)

db = SQLAlchemy(app)


class Products(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    asin = db.Column(db.String(100), primary_key=True)
    reviews = db.relationship('Reviews', backref='reviews', lazy='dynamic')

    def get_url(self):
        return url_for('get_product', asin=self.asin, _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'name': self.title
        }


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    review = db.Column(db.Text)
    asin = db.Column(db.String(100), db.ForeignKey('products.asin'))

    def export_data(self):
        return {
            'review': self.review,
            'title': self.title
        }


@cache.cached(timeout=50)
@app.route('/products/', methods=['GET'])
def get_products():
    return jsonify({'products': [
        {"title": product.title, "url": product.get_url()} for product in
        Products.query.all()]})


@cache.cached(timeout=50)
@app.route('/product/<asin>/review', methods=['GET'])
def get_product(asin):
    url = request.base_url
    page = request.args.get('page', default=1, type=int)
    product = Products.query.get_or_404(asin)
    reviews = product.reviews.all()

    limit = 2
    count = len(reviews)

    if count < page:
        page = count
    paginate = {'count': count}
    if page == 1:
        paginate['previous'] = ''
    else:
        paginate['previous'] = url + f"?page={page - 1}"

    if page * limit >= count:
        paginate['next'] = ''
    else:
        paginate['next'] = url + f'?page={page + 1}'

    stop = page * limit
    start = stop - limit
    results = reviews[start:stop]
    results = [r.export_data() for r in results]
    if count == 0:
        paginate = ''
    return jsonify({'product': product.export_data(), 'page': paginate,
                    'result': results})


@app.route('/product/<asin>/add_review/', methods=['PUT'])
def add_review(asin):
    title = request.json.get('title')
    review_data = request.json.get('review')
    try:
        review = Reviews(title=title, review=review_data, asin=asin)
        db.session.add(review)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        print(e)
    return jsonify(request.json)


if __name__ == '__main__':
    app.run(debug=True)
