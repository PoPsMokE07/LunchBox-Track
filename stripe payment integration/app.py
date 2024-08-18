from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv  # Updated import
from sqlalchemy import Nullable
import stripe
import os

load_dotenv()  # Updated function call

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'  # Corrected key
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

stripe.api_key=os.getenv('STRIPE_SECRET_KEY')
stripe_public_key=os.getenv('STRIPE_PUBLIC_KEY')


class Payment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    session_id=db.Column(db.String(120),unique=True, nullable=False)
    amount=db.Column(db.Integer, nullable=False)
    currency=db.Column(db.String(10),nullable=False)
    status=db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('checkout.html', public_key=stripe_public_key)

@app.route('/create-checkout-session', methods=['POST']) 
def create_checkout_session():  
    try: 
        price=258
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'INR',
                    'product_data': {
                        'name':'Order'
                    },
                    'unit_amount':price*100, 
                },
                'quantity':1,
            },
            ],
            mode='payment',
            success_url=url_for('success',_external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('cancel',_external=True),
            
        )
        payment=Payment(session_id=session.id, amount=price, currency='usd', status='created')
        db.session.add(payment)
        db.session.commit()
        return jsonify(id=session.id)
    
    except Exception as e:
        return jsonify(error=str(e)),403
    

@app.route('/success')

def success():
    session_id=request.args.get('session_id')
    session=stripe.checkout.Session.retrieve(session_id)
    payment=Payment.query.filter_by(session_id=session_id).first()
    if session.payment_status=='paid':
        payment.status='paid'
        db.session.commit()
    return f"Payment was successfull, session id:{session_id}"
        
@app.route('/cancel')

def cancel():
    return "payment was canceled"







if __name__ == '__main__':
    app.run(debug=True, port=5001)