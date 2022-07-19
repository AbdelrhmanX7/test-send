version = '0.2'
import requests

session = requests.session()

r = session.get('https://twitter.com/i/flow/login')

save_string = r.content.decode('UTF-8')

res = save_string[save_string.index('154'): save_string.index('Max-Age') - 2]

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',

    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'cookie': f'guest_id_marketing=v1%3A163915078347732283; guest_id_ads=v1%3A163915078347732283; '
              'kdt=ZtOVqkYORTkEgudSoEFLtKhweBNBxBrBwlxWVxQc; des_opt_in=Y; '
              '_ga_ZJQNEMXF73=GS1.1.1657488019.1.1.1657488119.0; night_mode=2; _gcl_au=1.1.1377431567.1657630978; '
              'mbox=PC#aded097e1fc940d985dccecdf1b5033c.37_0#1720876750|session#461294dc3844404497cdefbf225893ad'
              '#1657633810; _ga_34PHSZMC42=GS1.1.1657630993.1.1.1657631952.0; _ga=GA1.2.1857441902.1639150783; dnt=1; '
              '_gid=GA1.2.2051268057.1658114352; _sl=1; personalization_id="v1_nxAjgv1+6HSyoMRotXOnTw=="; '
              'guest_id=v1%3A165813734255118325; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; '
              'ct0=b3c660ca25f63148ade45a26e436ae06; '
              '_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo'
              '%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCGK1LRKCAToMY3NyZl9p'
              '%250AZCIlNWFhODI4ODEyOTY3ODA0YTQzOTg0MzgyNWU4Y2U2OGQ6B2lkIiU0Mzcz'
              '%250AMTUzMTE5NmQxZmQ1MDcxOWY4MjE5ZmRhYzdmMQ%253D%253D--6675577b27e8cb2a3dbd6cacbab3064772b1984f; '
              'gt=1549071363855585281; att=1-NjQSKb3VldrVwjDhfEOPTiOdd2WmPB3tRrPc3mwW; g_state={"i_l":1,'
              '"i_p":1658169612568}',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/i/flow/login',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-csrf-token': 'b3c660ca25f63148ade45a26e436ae06',
    'x-guest-token': res,
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ar'
}

payload_data = {
    "input_flow_data": {"flow_context": {"debug_overrides": {}, "start_location": {"location": "manual_link"}}},
    "subtask_versions": {"contacts_live_sync_permission_prompt": 0, "email_verification": 1,
                         "topics_selector": 1,
                         "wait_spinner": 1, "cta": 4}}

j = session.post("https://twitter.com/i/api/1.1/onboarding/task.json?flow_name=login", headers=headers,
                 json=payload_data)
save_string = j.content.decode('UTF-8')

id1 = save_string.index("{") - 1
id2 = save_string.index(",")

flow_toke = ''
for i in range(id1 + len("{") + 1, id2):
    flow_toke = flow_toke + save_string[i]

flow_toke = flow_toke[14:-1]
print(f'x-guest-token ===> {res}')

payload_data = {
    "input_flow_data": {"flow_context": {"debug_overrides": {}, "start_location": {"location": "manual_link"}}},
    "subtask_versions": {"contacts_live_sync_permission_prompt": 0, "email_verification": 1,
                         "topics_selector": 1,
                         "wait_spinner": 1, "cta": 4}}


t = session.post("https://twitter.com/i/api/1.1/onboarding/task.json?flow_name=login", headers=headers, json=payload_data)

init = session.post('https://twitter.com/i/api/1.1/branch/init.json', headers=headers, json={})

username = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers, json={"flow_token":flow_toke,"subtask_inputs":[{"subtask_id":"LoginJsInstrumentationSubtask","js_instrumentation":{"response":"{\"rf\":{\"dd2b19ff23a9840c02d8d2b6fbd4298babb05fe25bfddd1b832cfeb4639860dc\":-1,\"d9bc9e2b84711e7e27f9b9ae56b0d7a5543e884ddfd4e00d9f7d5130a8452e3b\":-1,\"ac5ba49359e48da3a6cd16bd4882ac5b0cfcbfdedc6fd7e30379614f2a808e56\":0,\"dad83ded720ad64cdfb6aeb86a0f4d302344a2fae55dd6afb95996072f0ccdae\":0},\"s\":\"mvesx7UxLAxWAeAHMzwZjK3mUD3vhebrY7JUAPz7wr6T_GXG7E0bj9VLn14h45AZ8niOn5jpNemMNJXdzxTikjvn3o9LOm9GevWFlsqnC1MT4YoLHJbwSBqqV8P6QnNon2y6FIz8ZI31-bJOm50lF8ooGGT_OYwYkxMxu7Yt5ZStunbJswPUnpXyQkUTpfq58Rf-JDPDv-E1W60gqBmcFmGNQeolfkLdcTn1RBaxo7HcI8oUPT5DRoMZR39Dwc13SZhXPaiKDb4KZbwRrgIv9VcN2BSvhSpHxYlmh2vx482-UYQUv78kurtQUHE8YfgoYw6aDboVcSHkDbAkYTZoLwAAAYIUDvko\"}","link":"next_link"}}]})

print('First Request')
print(username)
print(username.content)
print(flow_toke)
flow_toke = flow_toke[:-1] + '1'
print(flow_toke)

while 1:
    write_user = input('Twitter id: ')

    username_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                               json={"flow_token": flow_toke, "subtask_inputs": [
                                   {"subtask_id": "LoginEnterUserIdentifierSSO", "settings_list": {
                                       "setting_responses": [{"key": "user_identifier",
                                                              "response_data": {"text_data": {"result": write_user}}}],
                                       "link": "next_link"}}]})

    if username_ts.status_code == 200:
        break
    print('Write a correct twitter id')

print('user find')

flow_toke = flow_toke[:-1] + '5'

while 1:
    write_pass = input('Twitter password: ')

    pass_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                           json={"flow_token": flow_toke, "subtask_inputs": [{"subtask_id": "LoginEnterPassword",
                                                                              "enter_password": {"password": write_pass,
                                                                                                 "link": "next_link"}}]})

    if pass_ts.status_code == 200:
        break
    print('Write a correct password')


flow_toke = flow_toke[:-1] + '6'

print('Password is correct')


last_request = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers, json={"flow_token":flow_toke,"subtask_inputs":[{"subtask_id":"AccountDuplicationCheck","check_logged_in_account":{"link":"AccountDuplicationCheck_false"}}]})

print('last Request')

print(last_request)
print(last_request.content)


what_is = session.get('https://twitter.com/home?precache=1')

print(what_is.cookies.get_dict())
value = what_is.cookies.get_dict()
value = str(value)
value = value[9: value.index(",") - 1]
print(value)


headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',

    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/i/flow/login',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-csrf-token': value,
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ar'
}

write_tweet = input('write tweet: ')

send_tweet = session.post('https://twitter.com/i/api/graphql/MIGRPGIYo1iAWFy_FXUJUA/CreateTweet', headers=headers, json={"variables":{"tweet_text":write_tweet,"media":{"media_entities":[],"possibly_sensitive":'false'},"withDownvotePerspective":'false',"withReactionsMetadata":'false',"withReactionsPerspective":'false',"withSuperFollowsTweetFields":'true',"withSuperFollowsUserFields":'true',"semantic_annotation_ids":[],"dark_request":'false'},"features":{"dont_mention_me_view_api_enabled":'true',"interactive_text_enabled":'true',"responsive_web_uc_gql_enabled":'false',"vibe_tweet_context_enabled":'false',"responsive_web_edit_tweet_api_enabled":'false',"standardized_nudges_misinfo":'false',"responsive_web_enhance_cards_enabled":'false'},"queryId":"MIGRPGIYo1iAWFy_FXUJUA"})

print('send_tweet Request')

print(send_tweet)
print(send_tweet.content)
