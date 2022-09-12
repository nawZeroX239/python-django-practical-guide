from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
  'january'   : 'january challenge', 
  'february'  : 'february challenge',
  'march'     : 'march challenge',
  'april'     : 'april challenge',
  'may'       : 'maychallenge',
  'june'      : 'june challenge',
  'july'      : 'july challenge',
  'august'    : 'august challenge',
  'september' : 'september challenge',
  'october'   : 'october challenge',
  'november'  : 'november challenge',
  'december'  : 'december challenge'
}

forward_month = list(monthly_challenges.keys())

def redirect_path(redirect_month):
    return reverse('month-challenge', args=[redirect_month])

def monthly_challenge_by_number(request, month):
  try:
    return HttpResponseRedirect(redirect_path(forward_month[month - 1]))
  except:
    return HttpResponseNotFound('<h1> Path not supported! </h1>')

def monthly_challenge(request, month):
  try:
    challenge = monthly_challenges[month]
    response_data = f"<h1>{challenge}</h1>"
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound('<h1> Path not supported! </h1>')

def formatted_month(month): 
  return f"<li><a href={redirect_path(month)}>{month.capitalize()}<a/></li>"

def all_monthly_challenges(request):
  response_data = '<ul>'
  response_data += ''.join(list(map(lambda month: formatted_month(month), forward_month)))
  response_data += '</ul>'
  # print('response_data: ' + response_data)
  return HttpResponse(response_data)