from django.shortcuts import render, redirect
from django.urls import reverse
from frontend.helper import user_detail
import tweepy, json, requests
from twitter_influencer import settings
from django.http import Http404
from urllib.parse import unquote, urlencode


# Create your views here.
def index(request):
    name = ''
    image = ''
    username = ''
    user_dtl = ''
    description = ''
    template = 'index.html'
    followers = 0
    following = 0
    data_tweet = ''

    if 'oauth_token' and 'oauth_verifier' in request.GET:
        verifier = request.GET['oauth_verifier']
        status, user_dtl, data_tweet = user_detail(request,verifier=verifier)
        username = status['name']
        name = user_dtl['data'][0]['name']
        image = user_dtl['data'][0]['profile_image_url']
        description = user_dtl['data'][0]['description']
        followers = user_dtl['data'][0]['public_metrics']['followers_count']
        following = user_dtl['data'][0]['public_metrics']['following_count']
        data_tweet = data_tweet['data']

    data = {
        'twitter' : reverse('twitter'),
        'userdtl' : user_dtl,
        'name' : name,
        'username' : username,
        'image' : image,
        'description' : description,
        'followers' : followers,
        'following' : following,
        'tweet' : data_tweet

    }

    return render(request, template, data)


def login_twitter(request):
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)

    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError as e:
        raise Http404(e)

    request.session['request_token'] = auth.request_token

    return redirect(redirect_url)


def login_facebook(request):
    redirect_uri = request.build_absolute_uri(reverse('home_fb'))

    params = {'display': 'page',
              'client_id': '187960271237149',
              'redirect_uri': redirect_uri,
              }

    fb_query_string = unquote(urlencode(params))
    fb_url = 'https://www.facebook.com/dialog/oauth?' + fb_query_string

    return redirect(fb_url)


def non_public(request):
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)

    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError as e:
        raise Http404(e)

    request.session['request_token'] = auth.request_token

    return redirect(redirect_url)


def get_access_token(request, **kwargs):
    redirect_uri = request.build_absolute_uri(reverse("home_fb"))

    params = {'client_id': '187960271237149',
              'client_secret': '29614e2e959ac53655d5283a2a860cf4',
              'redirect_uri': redirect_uri,
              'code': kwargs['code']}

    fb_token_url = 'https://graph.facebook.com/oauth/access_token?'
    fb_query_string = unquote(urlencode(params))

    return requests.get(fb_token_url + fb_query_string)


def index_fb(request):
    template = 'index.html'
    data=''

    if 'code' in request.GET:
        fb_access_token_resp = get_access_token(request, code=request.GET['code'])

    return render(request, template, data)
