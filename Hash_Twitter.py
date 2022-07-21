update_version = 2
import requests
import random
import sys
import time
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f'{bcolors.OKCYAN}Script version ===> [1.3]{bcolors.BOLD}')
print('[*] لو مش هياخد من وقتك حاجة ف ياريت تستغفر ربنا و لو ينفع ف ممكن تدعيلي و شكرا ليك')
Hashtag = '#انترنت_غير_محدود_بمصر'

print(Hashtag)

arr = ["It's very close but plz u have must some patient and don't give up\n" +
       Hashtag, "It's very close but plz u have must some patient and don't give up\n" + Hashtag, "I am sure very "
                                                                                                  "soon we will see i "
                                                                                                  "good news "
                                                                                                  "inshallah\n" +
       Hashtag, "No one in this world can stop us from asking and taking our rights in unlimited internet in Egypt\n"
       + Hashtag, "It's only what we need it's easy unlimited internet in Egypt very simple\n" + Hashtag, "That's war "
                                                                                                          "must end "
                                                                                                          "with a "
                                                                                                          "good and "
                                                                                                          "easy way "
                                                                                                          "or with "
                                                                                                          "the hard "
                                                                                                          "way\n" +
       Hashtag, "Don't stop asking for ur rights u can change the future keep fighting like a wirror this is ur war "
                "and u can win it and u will win it\n" + Hashtag, "Trust me they will pay what they have done on "
                                                                  "us\n" + Hashtag, "Stop stealing we want unlimited "
                                                                                    "internet in Egypt\n" + Hashtag,
       "Never give up\n" + Hashtag, "We can win this\n" + Hashtag, "Don't give up u will make them happy if we give "
                                                                   "up don't be stupid\n" + Hashtag, "Keep fighting "
                                                                                                     "for ur and our "
                                                                                                     "dream\n" +
       Hashtag, "We will make u regret for don't give us our rights\n" + Hashtag, "We will fight for end with all "
                                                                                  "power we have\n" + Hashtag,
       "We only need a good internet unlimited and chaep like any country\n" + Hashtag, "Stop stilling us we are not "
                                                                                        "stupides\n" + Hashtag,
       "Don't give up we are very close to the end of way\n" + Hashtag, "Keep going that's our last chance to have an "
                                                                        "unlimited internet in Egypt\n" + Hashtag,
       "We still in it\n" + Hashtag, "عمرنا ما هنزهق لغيت ما كل مطالبنا تتحقق\n" + Hashtag, "احنا مش هنسكت لغيت ما كل "
                                                                                            "المصريين يبق عندهم نت "
                                                                                            "كويس و غير محدود و "
                                                                                            "رخيص\n" + Hashtag,
       "عمرنا ما هسيب حقنا حتي لو قطعوت النت عن مصر كله\n" + Hashtag, "هتفضلو تسكتو و تضحك و تستغلو وتسرقو الشعب لغيت "
                                                                      "ما هينفجر فيكو مرة واحدة\n" + Hashtag,
       "ليه ميبقش عندنا انترنت شبه اي دولة احنا مش اقل من اي دولة في العالم و لو المسئوليين مش عارفيين يحلو الموضوع "
       "يمشو احسن\n" + Hashtag, "كل ال انتو بتعملو فينا ده عشان بنطلب بحقنا ؟؟؟\n" + Hashtag, "ال بيحصل دلوقتي اقل "
                                                                                              "حاجة نقدر نقول عليه "
                                                                                              "انهم لعبة قذر من شركة "
                                                                                              "اقذر عشان حنفية الفلوس "
                                                                                              "تفضل فتح\n" + Hashtag,
       "من حقنا دولة من اهم اهم دول الشرق الاوسط ازي مكنتش الاهم بانترنت غير محدود و سريع\n" + Hashtag,
       "مش كفاية سبوبة التلفون الارضي المحدش بيستخدمه وبيدفع تمنه اجباري ياعني الباقة وقفة علينا اغلي من سعرها بطلو "
       "بق شغل العصابات و الحرامية و كماية النصب ده\n" + Hashtag, "مش هنوقف مهم حصل عشان الكل جاب اخر\n" + Hashtag,
       "هل موقع مصر الكتميز و كماية الكابلات ال بتعدي عليه مش كفاية لانترنت غير محدود؟\n" + Hashtag,
       "ازاي بتقول مفيش بنية تحتية كويسة واحن كل شهر بنجدد و بتستحمل عادي ؟\n" + Hashtag, "مصلحتنا في انترنت سريع غير "
                                                                                          "محدود و موفر يخدم اهداف "
                                                                                          "الجمتمع المصري في كل "
                                                                                          "المجالات سواء تعليمية او "
                                                                                          "ترفيهية او تجارية او عملية "
                                                                                          "النت اصبح ضرورة اساسية مش "
                                                                                          "ثانوية\n" + Hashtag,
       "كفاية سرقة عايزين نشتغل ونتعلم ونعيش ونلعب زي اي دولة\n" + Hashtag, "انك تقدر دلوقتي تكتاسب خبرات من كورسات و "
                                                                            "تستثمار من خلال الانترنت لكن انك مش قادر "
                                                                            "تعمل كده لمجرد ان دولتك مش عايز يبق فيه "
                                                                            "انترنت غير محدود عشان يسرقوك فا اعرف ان "
                                                                            "النظام فيه حاجة غلط\n" + Hashtag,
       "الإنترنت منفع عامة للجميع يجب توزيع بعادل فعلا علي كل الشعب\n" + Hashtag, "النت مش مياه او كهرباء عشان يخلص "
                                                                                  "او بستخرج من تحت الارض يا سيادة "
                                                                                  "الوزير احنا مش حقنا في دولتنا يبق "
                                                                                  "عندنا شبه بقيت دول العالم\n" +
       Hashtag]

session = requests.session()

r = session.get('https://twitter.com/i/flow/login')

save_string = r.content.decode('UTF-8')

res = save_string[save_string.index('decodeURIComponent("gt=') + 23: save_string.index('Max-Age') - 2]

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
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

print(f'{bcolors.WARNING}[*] Collect Twitter Data{bcolors.BOLD}')


init = session.post('https://twitter.com/i/api/1.1/branch/init.json', headers=headers, json={})

username = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                        json={"flow_token": flow_toke, "subtask_inputs": [
                            {"subtask_id": "LoginJsInstrumentationSubtask", "js_instrumentation": {
                                "response": "{\"rf\":{\"dd2b19ff23a9840c02d8d2b6fbd4298babb05fe25bfddd1b832cfeb4639860dc\":-1,\"d9bc9e2b84711e7e27f9b9ae56b0d7a5543e884ddfd4e00d9f7d5130a8452e3b\":-1,\"ac5ba49359e48da3a6cd16bd4882ac5b0cfcbfdedc6fd7e30379614f2a808e56\":0,\"dad83ded720ad64cdfb6aeb86a0f4d302344a2fae55dd6afb95996072f0ccdae\":0},\"s\":\"mvesx7UxLAxWAeAHMzwZjK3mUD3vhebrY7JUAPz7wr6T_GXG7E0bj9VLn14h45AZ8niOn5jpNemMNJXdzxTikjvn3o9LOm9GevWFlsqnC1MT4YoLHJbwSBqqV8P6QnNon2y6FIz8ZI31-bJOm50lF8ooGGT_OYwYkxMxu7Yt5ZStunbJswPUnpXyQkUTpfq58Rf-JDPDv-E1W60gqBmcFmGNQeolfkLdcTn1RBaxo7HcI8oUPT5DRoMZR39Dwc13SZhXPaiKDb4KZbwRrgIv9VcN2BSvhSpHxYlmh2vx482-UYQUv78kurtQUHE8YfgoYw6aDboVcSHkDbAkYTZoLwAAAYIUDvko\"}",
                                "link": "next_link"}}]})

print(f'{bcolors.OKGREEN}[*] Data has been Collected{bcolors.BOLD}')

print(f'#####################################')

flow_toke = flow_toke[:-1] + '1'

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
    print(f'{bcolors.FAIL}Write a correct twitter id{bcolors.BOLD}')

print(f'{bcolors.OKGREEN}USER_FIND{bcolors.BOLD}')

flow_toke = flow_toke[:-1] + '5'

while 1:
    write_pass = input('Twitter password: ')

    pass_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                           json={"flow_token": flow_toke, "subtask_inputs": [{"subtask_id": "LoginEnterPassword",
                                                                              "enter_password": {"password": write_pass,
                                                                                                 "link": "next_link"}}]})

    if pass_ts.status_code == 200:
        break
    print(f'{bcolors.FAIL}Write a correct password{bcolors.BOLD}')

flow_toke = flow_toke[:-1] + '6'

print(f'{bcolors.OKGREEN}Password is correct{bcolors.BOLD}')

last_request = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                            json={"flow_token": flow_toke, "subtask_inputs": [{"subtask_id": "AccountDuplicationCheck",
                                                                               "check_logged_in_account": {
                                                                                   "link": "AccountDuplicationCheck_false"}}]})

print(f'{bcolors.OKCYAN}Almost_Done{bcolors.BOLD}')

command = 'clear'
if os.name in ('nt', 'dos'):
 command = 'cls'
os.system(command)

what_is = session.get('https://twitter.com/home?precache=1')

value = what_is.cookies.get_dict()
value = str(value)
value = value[9: value.index(",") - 1]

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

number_of_tweet = 1

choose_random_tweet = random.randint(0, len(arr) - 1)
Tweet_Text = arr[choose_random_tweet] + f"\nللمرة {random.randint(0, 99999999)} دة حقنا"
SEND_TWEET = session.post('https://twitter.com/i/api/graphql/MIGRPGIYo1iAWFy_FXUJUA/CreateTweet',
                          headers=headers,
                          json={"variables": {"tweet_text": Tweet_Text,
                                              "media": {"media_entities": [], "possibly_sensitive": 'false'},
                                              "withDownvotePerspective": 'false',
                                              "withReactionsMetadata": 'false',
                                              "withReactionsPerspective": 'false',
                                              "withSuperFollowsTweetFields": 'true',
                                              "withSuperFollowsUserFields": 'true',
                                              "semantic_annotation_ids": [],
                                              "dark_request": 'false'},
                                "features": {"dont_mention_me_view_api_enabled": 'true',
                                             "interactive_text_enabled": 'true',
                                             "responsive_web_uc_gql_enabled": 'false',
                                             "vibe_tweet_context_enabled": 'false',
                                             "responsive_web_edit_tweet_api_enabled": 'false',
                                             "standardized_nudges_misinfo": 'false',
                                             "responsive_web_enhance_cards_enabled": 'false'},
                                "queryId": "MIGRPGIYo1iAWFy_FXUJUA"})
Tweet_Send_Text = f'{bcolors.OKGREEN}Tweet has been send [{number_of_tweet}]{bcolors.BOLD}'
sys.stdout.write('\r' + Tweet_Send_Text + '\n')

Timer_Countdown = 45
while 1:
    Timer_Countdown = Timer_Countdown - 1
    b = f"{bcolors.OKCYAN}TWEET_WILL_SEND_AFTER ==> [{Timer_Countdown}]{bcolors.BOLD}"
    sys.stdout.write('\r' + b)
    if Timer_Countdown == 0:
        number_of_tweet += 1
        choose_random_tweet = random.randint(0, len(arr) - 1)
        Tweet_Text = arr[choose_random_tweet] + f"\nللمرة {random.randint(0, 99999999)} دة حقنا"
        SEND_TWEET = session.post('https://twitter.com/i/api/graphql/MIGRPGIYo1iAWFy_FXUJUA/CreateTweet',
                                  headers=headers,
                                  json={"variables": {"tweet_text": Tweet_Text,
                                                      "media": {"media_entities": [], "possibly_sensitive": 'false'},
                                                      "withDownvotePerspective": 'false',
                                                      "withReactionsMetadata": 'false',
                                                      "withReactionsPerspective": 'false',
                                                      "withSuperFollowsTweetFields": 'true',
                                                      "withSuperFollowsUserFields": 'true',
                                                      "semantic_annotation_ids": [],
                                                      "dark_request": 'false'},
                                        "features": {"dont_mention_me_view_api_enabled": 'true',
                                                     "interactive_text_enabled": 'true',
                                                     "responsive_web_uc_gql_enabled": 'false',
                                                     "vibe_tweet_context_enabled": 'false',
                                                     "responsive_web_edit_tweet_api_enabled": 'false',
                                                     "standardized_nudges_misinfo": 'false',
                                                     "responsive_web_enhance_cards_enabled": 'false'},
                                        "queryId": "MIGRPGIYo1iAWFy_FXUJUA"})
        Tweet_Send_Text = f'{bcolors.OKGREEN}Tweet has been send [{number_of_tweet}]{bcolors.BOLD}'
        sys.stdout.write('\r' + Tweet_Send_Text + '\n')
        Timer_Countdown = 40
    time.sleep(1)
