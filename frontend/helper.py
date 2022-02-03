from twitter_influencer import settings
import tweepy, json
from django.shortcuts import redirect
from django.urls import reverse
from django.http import Http404
from .models import Account
from .forms import AccountForm
from requests_oauthlib import OAuth1Session
import twitter


def user_detail(request, **kwargs):
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)

    if 'request_token' in request.session:
        token = request.session['request_token']
    else:
        return redirect(reverse('home'))

    verifier = kwargs['verifier']
    del request.session['request_token']
    auth.request_token = token

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError as e:
        raise Http404(e)

    api = tweepy.API(auth)
    username = auth.get_username()
    user = api.get_user(username)

    account_instance = {
        'username': '@' + username,
        'id_socmed': user.id,
        'account_type': 1,
        'oauth_token': auth.access_token,
        'oauth_token_secret': auth.access_token_secret,
    }

    status = {}
    account_obj, create = Account.objects.get_or_create(id_socmed=user.id)
    account = AccountForm(account_instance, instance=account_obj)
    if account.is_valid():
        account.save()
        status['success'] = 'Success add account '
        status['id'] = int(account.instance.id)
        status['name'] = account.instance.username
    else:
        status['error'] = 'Not Valid when add account ' + account_instance['username']


    data_fol = get_followers(auth.access_token,auth.access_token_secret,username)
    data_tweet = get_tweet(auth.access_token,auth.access_token_secret,data_fol['data'][0]['id'])
    messages = api.list_direct_messages(count=5)

    for message in reversed(messages):
        # who is sending?
        sender_id = message.message_create["sender_id"]
        # what is she saying?
        text = message.message_create["message_data"]["text"]

    return status, data_fol, data_tweet


def get_followers(access_token,access_token_secret,username):

    fields = "public_metrics,profile_image_url,description"
    params = {"usernames": username, "user.fields": fields}

    oauth = OAuth1Session(
        settings.consumer_key,
        client_secret=settings.consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    response = oauth.get(
        "https://api.twitter.com/2/users/by", params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    json_response = response.json()

    print(json.dumps(json_response, indent=4, sort_keys=True))

    return json_response


def get_tweet(access_token,access_token_secret,id):
    fields = 'non_public_metrics'
    params = {"max_results":12, "tweet.fields": fields}

    oauth = OAuth1Session(
        settings.consumer_key,
        client_secret=settings.consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    response = oauth.get(
        "https://api.twitter.com/2/users/{}/tweets".format(id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    json_response = response.json()

    print(json.dumps(json_response, indent=4, sort_keys=True))

    return json_response


def get_user_dtl(request):
    id='886131229'
    account = Account.objects.get(id=2)
    fields = 'non_public_metrics'
    params = {"max_results": 12, "tweet.fields": fields}

    oauth = OAuth1Session(
        settings.consumer_key,
        client_secret=settings.consumer_secret,
        resource_owner_key=account.oauth_token,
        resource_owner_secret=account.oauth_token_secret,
    )

    response = oauth.get(
        "https://api.twitter.com/2/users/{}/tweets".format(id), params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    json_response = response.json()

    print(json.dumps(json_response, indent=4, sort_keys=True))

    return json_response