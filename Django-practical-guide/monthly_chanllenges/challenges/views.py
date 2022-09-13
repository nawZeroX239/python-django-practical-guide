from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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
  'december'  : None
}

forward_month = list(monthly_challenges.keys())
response_not_found = render_to_string('404.html')

def redirect_path(redirect_month):
    return reverse('month-challenge', args=[redirect_month])

def monthly_challenge_by_number(request, month):
  try:
    return HttpResponseRedirect(redirect_path(forward_month[month - 1]))
  except:
    raise Http404()

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    # response_data = render_to_string('challenges/challenge.html')
    return render(request, 'challenges/challenge.html', {
      'text' : challenge_text,
      'month_name' : month
    })
  except:
    raise Http404()

def all_monthly_challenges(request):
  # response_data = '<ul>'
  # response_data += ''.join(list(map(lambda month: formatted_month(month), forward_month)))
  # response_data += '</ul>'
  # print('response_data: ' + response_data)
  return render(request, 'challenges/index.html', {
    'months': forward_month
  })