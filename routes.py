from flask import render_template, redirect, url_for, request, flash
from . import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        # lógica para manejar la reserva
        return redirect(url_for('payment'))
    return render_template('reservation.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        # lógica para manejar el pago
        flash('Pago realizado con éxito')
        return redirect(url_for('home'))
    return render_template('payment.html')
