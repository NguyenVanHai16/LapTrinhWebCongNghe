from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user
from app.models import Product, Category
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Lấy sản phẩm mới (không có giảm giá)
    new_products = Product.query.filter(
        Product.is_new == True,
        (Product.discounted_price == None) | (Product.price <= Product.discounted_price)
    ).order_by(Product.created_at.desc()).limit(4).all()

    # Lấy sản phẩm nổi bật (không có giảm giá)
    featured_products = Product.query.filter(
        Product.featured == True,
        (Product.discounted_price == None) | (Product.price <= Product.discounted_price)
    ).order_by(Product.rating.desc()).limit(4).all()

    # Lấy sản phẩm giảm giá (dựa trên price > discounted_price, xử lý NULL)
    sale_products = Product.query.filter(
        Product.discounted_price != None,
        Product.price > Product.discounted_price
    ).limit(4).all()

    return render_template('main/index.html',
                           title='TechMart - Cửa hàng công nghệ',
                           featured_products=featured_products,
                           new_products=new_products,
                           sale_products=sale_products)

@main.route('/about')
def about():
    return render_template('main/about.html', title='Về chúng tôi')

@main.route('/contact')
def contact():
    return render_template('main/contact.html', title='Liên hệ')

@main.route('/terms')
def terms():
    return render_template('main/terms.html', title='Điều khoản sử dụng')

@main.route('/privacy')
def privacy():
    return render_template('main/privacy.html', title='Chính sách bảo mật')

@main.route('/guide')
def guide():
    return render_template('main/guide.html', title='Hướng dẫn mua hàng')

@main.route('/payment')
def payment():
    return render_template('main/payment.html', title='Phương thức thanh toán')

@main.route('/shipping')
def shipping():
    return render_template('main/shipping.html', title='Chính sách vận chuyển')

@main.route('/warranty')
def warranty():
    return render_template('main/warranty.html', title='Chính sách bảo hành')