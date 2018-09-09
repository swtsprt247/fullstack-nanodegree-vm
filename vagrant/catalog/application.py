from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import MainPage, Base, Categories
app = Flask(__name__)


engine = create_engine('sqlite:///frenchy_fabric.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/frenchyfabric/<int:main_page_id>/')
def MainpageCategories(main_page_id):
    main_page = session.query(MainPage).filter_by(id=main_page_id).one()
    items = session.query(Categories).filter_by(main_page_id=main_page.id)
    return render_template('categories.html', main_page=main_page, items = items)


# Route for new categories
@app.route('/frenchyfabric/<int:main_page_id>/new/', methods=['GET', 'POST'])
def newCategoryItem(main_page_id):
    if request.method == 'POST':
        newItem = Categories(name=request.form['name'], main_page_id=main_page_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('MainpageCategories', main_page_id=main_page_id))
    else:
        return render_template('NewCategoryItem.html', main_page_id=main_page_id)


# Route to edit categories
@app.route('/frenchyfabric/<int:main_page_id>/<int:categories_id>/edit/')
def editCategoryItem(main_page_id, categories_id):
    return "page to edit Category items. Yipee Skippee!!"


# Route to delete categories
@app.route('/frenchyfabric/<int:main_page_id>/<int:categories_id>/delete/')
def deleteCategoryItem(main_page_id, categories_id):
    return "page to delete Category items. Get er done!!"



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)