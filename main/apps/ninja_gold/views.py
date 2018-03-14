# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import strftime
import random

# Create your views here.
def index(req):
    if 'gold' not in req.session:
        req.session['gold'] = 0
    if 'activity_log' not in req.session:
        req.session['activity_log'] = []
    context = {
        'gold': req.session['gold'],
        'activity_log': req.session['activity_log'],
    }
    return render(req, 'ninja_gold/index.html', context)

def farm(req):
    number = random.randrange(10, 21)
    req.session['time'] = strftime("%Y-%m-%d %H:%M %p")
    req.session['gold'] += number
    req.session['amount'] = number
    req.session['color'] = 'gold'
    req.session['word'] = 'earned'
    req.session['building'] = 'farm'

    dic = {
        'time': req.session['time'],
        'amount': req.session['amount'],
        'color': req.session['color'],
        'word': req.session['word'],
        'building': req.session['building'],
    }
    req.session['activity_log'].append(dic)

    return redirect('/')

def cave(req):
    number = random.randrange(5, 11)
    req.session['time'] = strftime("%Y-%m-%d %H:%M %p")
    req.session['gold'] += number
    req.session['amount'] = number
    req.session['color'] = 'gold'
    req.session['word'] = 'earned'
    req.session['building'] = 'cave'

    dic = {
        'time': req.session['time'],
        'amount': req.session['amount'],
        'color': req.session['color'],
        'word': req.session['word'],
        'building': req.session['building'],
    }
    req.session['activity_log'].append(dic)

    return redirect('/')

def house(req):
    number = random.randrange(2, 6)
    req.session['time'] = strftime("%Y-%m-%d %H:%M %p")
    req.session['gold'] += number
    req.session['amount'] = number
    req.session['color'] = 'gold'
    req.session['word'] = 'earned'
    req.session['building'] = 'house'

    dic = {
        'time': req.session['time'],
        'amount': req.session['amount'],
        'color': req.session['color'],
        'word': req.session['word'],
        'building': req.session['building'],
    }
    req.session['activity_log'].append(dic)

    return redirect('/')

def casino(req):
    number = random.randrange(-50, 51)
    req.session['time'] = strftime("%Y-%m-%d %H:%M %p")
    req.session['gold'] += number
    req.session['amount'] = number
    if number < 0:
        req.session['color'] = 'red'
        req.session['word'] = 'lost'
        req.session['building'] = 'casino'
    else:
        req.session['color'] = 'gold'
        req.session['word'] = 'earned'
        req.session['building'] = 'casino'
    
    dic = {
        'time': req.session['time'],
        'amount': req.session['amount'],
        'color': req.session['color'],
        'word': req.session['word'],
        'building': req.session['building'],
    }
    req.session['activity_log'].append(dic)

    return redirect('/')

def reset(req):
    req.session.pop('gold')
    req.session.pop('activity_log')
    return redirect('/')