update_version = 5
import json
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


Auto_Login_Email = ''
Auto_Login_PASSWORD = ''
print(f'{bcolors.WARNING}[*] NEW UPDATE{bcolors.BOLD}')
print(f'{bcolors.HEADER}Script version ===> [2.5]{bcolors.BOLD}')
print(
    f'{bcolors.WARNING} لو في اي مشكلة في الاسكريبت ابعت علي جروب احنا شايفنكوا و معاكوا و هنفضل ديما معاكوا [*] {bcolors.BOLD}')
print('[*] لو مش هياخد من وقتك حاجة ف ياريت تستغفر ربنا و لو ينفع ف ممكن تدعيلي و شكرا ليك')
Hashtag = '#قاطع_we'

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
i = 0
while 1:
    a = '.' * i
    try:
        r = session.get('https://twitter.com/i/flow/login')
        print(f'\r{bcolors.OKGREEN}PASSED [1/6]{bcolors.BOLD}')
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

save_string = r.content.decode('UTF-8')

res = save_string[save_string.index('decodeURIComponent("gt=') + 23: save_string.index('Max-Age') - 2]

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs'
                     '%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
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

while 1:
    a = '.' * i
    try:
        j = session.post("https://twitter.com/i/api/1.1/onboarding/task.json?flow_name=login", headers=headers,
                         json=payload_data)
        print(f'\r{bcolors.OKGREEN}PASSED [2/6]{bcolors.BOLD}')
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

save_string = j.content.decode('UTF-8')

id1 = save_string.index("{") - 1
id2 = save_string.index(",")

flow_toke = ''
for i in range(id1 + len("{") + 1, id2):
    flow_toke = flow_toke + save_string[i]

flow_toke = flow_toke[14:-1]

print(f'{bcolors.WARNING}[*] Collect Twitter Data{bcolors.BOLD}')

while 1:
    a = '.' * i
    try:
        init = session.post('https://twitter.com/i/api/1.1/branch/init.json', headers=headers, json={})
        print(f'\r{bcolors.OKGREEN}PASSED [3/6]{bcolors.BOLD}')
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

username = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                        json={"flow_token": flow_toke, "subtask_inputs": [
                            {"subtask_id": "LoginJsInstrumentationSubtask", "js_instrumentation": {
                                "response": "{\"rf\":{"
                                            "\"dd2b19ff23a9840c02d8d2b6fbd4298babb05fe25bfddd1b832cfeb4639860dc\":-1,"
                                            "\"d9bc9e2b84711e7e27f9b9ae56b0d7a5543e884ddfd4e00d9f7d5130a8452e3b\":-1,"
                                            "\"ac5ba49359e48da3a6cd16bd4882ac5b0cfcbfdedc6fd7e30379614f2a808e56\":0,"
                                            "\"dad83ded720ad64cdfb6aeb86a0f4d302344a2fae55dd6afb95996072f0ccdae\":0},"
                                            "\"s"
                                            "\":\"mvesx7UxLAxWAeAHMzwZjK3mUD3vhebrY7JUAPz7wr6T_GXG7E0bj9VLn14h45AZ8niOn5jpNemMNJXdzxTikjvn3o9LOm9GevWFlsqnC1MT4YoLHJbwSBqqV8P6QnNon2y6FIz8ZI31-bJOm50lF8ooGGT_OYwYkxMxu7Yt5ZStunbJswPUnpXyQkUTpfq58Rf-JDPDv-E1W60gqBmcFmGNQeolfkLdcTn1RBaxo7HcI8oUPT5DRoMZR39Dwc13SZhXPaiKDb4KZbwRrgIv9VcN2BSvhSpHxYlmh2vx482-UYQUv78kurtQUHE8YfgoYw6aDboVcSHkDbAkYTZoLwAAAYIUDvko\"}",
                                "link": "next_link"}}]})

print(f'{bcolors.OKGREEN}[*] Data has been Collected{bcolors.BOLD}')

print(f'#####################################')

flow_toke = flow_toke[:-1] + '1'

if os.path.exists('Twitter_login.txt'):
    file = open('Twitter_login.txt', 'r')
    line = file.readlines()
    print('File Exist')
    if len(line[0]) > 1:
        Auto_Login_Email = line[0].replace('\n', '')
        while 1:
            a = '.' * i
            try:
                j = username_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                               json={"flow_token": flow_toke, "subtask_inputs": [
                                                   {"subtask_id": "LoginEnterUserIdentifierSSO", "settings_list": {
                                                       "setting_responses": [{"key": "user_identifier",
                                                                              "response_data": {
                                                                                  "text_data": {"result": line[0]}}}],
                                                       "link": "next_link"}}]})
                print(f'\r{bcolors.OKGREEN}PASSED [3/6]{bcolors.BOLD}')
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)
        file.close()
    else:
        print("Can't Find Your Twitter ID in file")
        while 1:
            write_user = input('Twitter id: ')
            Auto_Login_Email = write_user
            while 1:
                a = '.' * i
                try:
                    j = username_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json',
                                                   headers=headers,
                                                   json={"flow_token": flow_toke, "subtask_inputs": [
                                                       {"subtask_id": "LoginEnterUserIdentifierSSO", "settings_list": {
                                                           "setting_responses": [{"key": "user_identifier",
                                                                                  "response_data": {
                                                                                      "text_data": {
                                                                                          "result": write_user}}}],
                                                           "link": "next_link"}}]})
                    print(f'\r{bcolors.OKGREEN}PASSED [3/6]{bcolors.BOLD}')
                    break
                except requests.ConnectionError:
                    sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                    sys.stdout.flush()
                    i += 1
                    if i > 3:
                        i = 0
                time.sleep(1)

            if username_ts.status_code == 200:
                file.close()
                break
            print(f'{bcolors.FAIL}Write a correct twitter id{bcolors.BOLD}')
else:
    print('No AutoLogin File Found')
    while 1:
        write_user = input('Twitter id: ')
        Auto_Login_Email = write_user
        while 1:
            a = '.' * i
            try:
                j = username_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                               json={"flow_token": flow_toke, "subtask_inputs": [
                                                   {"subtask_id": "LoginEnterUserIdentifierSSO", "settings_list": {
                                                       "setting_responses": [{"key": "user_identifier",
                                                                              "response_data": {
                                                                                  "text_data": {
                                                                                      "result": write_user}}}],
                                                       "link": "next_link"}}]})
                print(f'\r{bcolors.OKGREEN}PASSED [3/6]{bcolors.BOLD}')
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)
        if username_ts.status_code == 200:
            break
        print(f'{bcolors.FAIL}Write a correct twitter id{bcolors.BOLD}')

print(f'{bcolors.OKGREEN}USER_FIND{bcolors.BOLD}')

flow_toke = flow_toke[:-1] + '5'

if os.path.exists('Twitter_login.txt'):
    file = open('Twitter_login.txt', 'r')
    line = file.readlines()
    try:
        Auto_Login_PASSWORD = line[1]
        while 1:
            a = '.' * i
            try:
                pass_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                       json={"flow_token": flow_toke,
                                             "subtask_inputs": [{"subtask_id": "LoginEnterPassword",
                                                                 "enter_password": {
                                                                     "password": line[1],
                                                                     "link": "next_link"}}]})
                print(f'\r{bcolors.OKGREEN}PASSED [4/6]{bcolors.BOLD}')
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        file.close()
        if pass_ts.status_code != 200:
            print("Password is wrong")
            while 1:
                write_pass = input('Twitter password: ')
                Auto_Login_PASSWORD = write_pass
                while 1:
                    a = '.' * i
                    try:
                        pass_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                               json={"flow_token": flow_toke,
                                                     "subtask_inputs": [{"subtask_id": "LoginEnterPassword",
                                                                         "enter_password": {
                                                                             "password": write_pass,
                                                                             "link": "next_link"}}]})
                        print(f'\r{bcolors.OKGREEN}PASSED [4/6]{bcolors.BOLD}')
                        break
                    except requests.ConnectionError:
                        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                        sys.stdout.flush()
                        i += 1
                        if i > 3:
                            i = 0
                    time.sleep(1)

                if pass_ts.status_code == 200:
                    file.close()
                    break
                print(f'{bcolors.FAIL}Write a correct password{bcolors.BOLD}')
    except:
        print("Can't Find Your Twitter Password in file")
        while 1:
            write_pass = input('Twitter password: ')
            Auto_Login_PASSWORD = write_pass
            while 1:
                a = '.' * i
                try:
                    pass_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                           json={"flow_token": flow_toke,
                                                 "subtask_inputs": [{"subtask_id": "LoginEnterPassword",
                                                                     "enter_password": {
                                                                         "password": write_pass,
                                                                         "link": "next_link"}}]})
                    print(f'\r{bcolors.OKGREEN}PASSED [4/6]{bcolors.BOLD}')
                    break
                except requests.ConnectionError:
                    sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                    sys.stdout.flush()
                    i += 1
                    if i > 3:
                        i = 0
                time.sleep(1)

            if pass_ts.status_code == 200:
                file.close()
                break
            print(f'{bcolors.FAIL}Write a correct password{bcolors.BOLD}')
else:
    while 1:
        write_pass = input('Twitter password: ')
        Auto_Login_PASSWORD = write_pass
        while 1:
            a = '.' * i
            try:
                pass_ts = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                       json={"flow_token": flow_toke,
                                             "subtask_inputs": [{"subtask_id": "LoginEnterPassword",
                                                                 "enter_password": {
                                                                     "password": write_pass,
                                                                     "link": "next_link"}}]})
                print(f'\r{bcolors.OKGREEN}PASSED [4/6]{bcolors.BOLD}')
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        if pass_ts.status_code == 200:
            break
        print(f'{bcolors.FAIL}Write a correct password{bcolors.BOLD}')

flow_toke = flow_toke[:-1] + '6'

print(f'{bcolors.OKGREEN}Password is correct{bcolors.BOLD}')

file = open('Twitter_login.txt', 'w+')
file.write(f'{Auto_Login_Email}\n{Auto_Login_PASSWORD}')
file.close()
while 1:
    a = '.' * i
    try:
        last_request = session.post('https://twitter.com/i/api/1.1/onboarding/task.json', headers=headers,
                                    json={"flow_token": flow_toke,
                                          "subtask_inputs": [{"subtask_id": "AccountDuplicationCheck",
                                                              "check_logged_in_account": {
                                                                  "link": "AccountDuplicationCheck_false"}}]})
        print(f'\r{bcolors.OKGREEN}PASSED [5/6]{bcolors.BOLD}')
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

print(f'{bcolors.OKCYAN}Almost_Done{bcolors.BOLD}')

while 1:
    a = '.' * i
    try:
        what_is = session.get('https://twitter.com/home?precache=1')
        print(f'\r{bcolors.OKGREEN}PASSED [6/6]{bcolors.BOLD}')
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

value = what_is.cookies.get_dict()
value = value['ct0']

command = 'clear'
if os.name in ('nt', 'dos'):
    command = 'cls'
os.system(command)

print(f'{bcolors.OKGREEN}[*]ALL THINGS IS GOOD ===> SCRIPT WILL START NOW{bcolors.BOLD}')
headers = {
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'accept': 'application/json',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs'
                     '%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'origin': 'https://twitter.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36',
    'x-csrf-token': value,
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'ar'
}

number_of_tweet = 1

choose_random_tweet = random.randint(0, len(arr) - 1)

Tweet_Text = arr[choose_random_tweet] + f"\nللمرة {random.randint(0, 99999999)} دة حقنا"
while 1:
    a = '.' * i
    try:
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
        break
    except requests.ConnectionError:
        sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
        sys.stdout.flush()
        i += 1
        if i > 3:
            i = 0
    time.sleep(1)

Tweet_Send_Text = f'{bcolors.OKGREEN}Tweet has been send [{number_of_tweet}]{bcolors.BOLD}'
sys.stdout.write('\r' + Tweet_Send_Text + '\n')

update_Timer = 121

Timer_Countdown = random.randrange(30, 45)

options = 0
while 1:
    update_Timer -= 1

    options = random.randrange(3)

    if update_Timer == 0:
        print('check for updates')

        url = 'https://raw.githubusercontent.com/AbdelrhmanX7/test-send/main/Hash_Twitter.py'

        while 1:
            a = '.' * i
            try:
                check_updates = requests.get(url, allow_redirects=True)
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        LOC = check_updates.content.decode('UTF-8')

        if update_version < int(LOC[LOC.index('=') + 2: LOC.index('\n')]):
            exec(LOC)

        print(f"{bcolors.WARNING}There's no update right now{bcolors.BOLD}")

        update_Timer = 120

    Timer_Countdown = Timer_Countdown - 1

    b = f"{bcolors.OKCYAN}TWEET_WILL_SEND_AFTER ==> [{Timer_Countdown}]{bcolors.BOLD}"

    sys.stdout.write('\r' + b)

    if Timer_Countdown == 0 and options == 0:

        number_of_tweet += 1

        choose_random_tweet = random.randint(0, len(arr) - 1)

        Tweet_Text = arr[choose_random_tweet] + f"\nللمرة {random.randint(0, 99999999)} دة حقنا"

        while 1:
            a = '.' * i
            try:
                SEND_TWEET = session.post('https://twitter.com/i/api/graphql/MIGRPGIYo1iAWFy_FXUJUA/CreateTweet',
                                          headers=headers,
                                          json={"variables": {"tweet_text": Tweet_Text,
                                                              "media": {"media_entities": [],
                                                                        "possibly_sensitive": 'false'},
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
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        Tweet_Send_Text = f'{bcolors.OKGREEN}\rTweet has been send [{number_of_tweet}]{bcolors.BOLD}\n'

        sys.stdout.write(Tweet_Send_Text)

        Timer_Countdown = random.randint(30, 40)

    elif Timer_Countdown == 0 and options == 1:
        url = 'https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q=%23%D8%B9%D8%A7%D9%8A%D8%B2%D9%8A%D9%86_%D8%A7%D9%86%D8%AA%D8%B1%D9%86%D8%AA_%D8%BA%D9%8A%D8%B1_%D9%85%D8%AD%D8%AF%D9%88%D8%AF&tweet_search_mode=live&count=20&query_source=typed_query&pc=1&spelling_corrections=1&include_ext_edit_control=false&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2Ccollab_control '

        while 1:
            a = '.' * i
            try:
                get_trend_tweets = session.get(url, headers=headers)
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)
        decode_trend_tweet = json.loads(get_trend_tweets.content.decode('UTF-8'))

        save_decode = decode_trend_tweet['globalObjects']['tweets']

        tweet_trend_id = list(save_decode.keys())[random.randrange(len(list(save_decode.keys())))]

        if random.randint(1, 2) == 1:
            while 1:
                a = '.' * i
                try:
                    send_love = session.post('https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet',
                                             headers=headers,
                                             json={"variables": {"tweet_id": tweet_trend_id},
                                                   "queryId": "lI07N6Otwv1PhnEgXILM7A"})
                    break
                except requests.ConnectionError:
                    sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                    sys.stdout.flush()
                    i += 1
                    if i > 3:
                        i = 0
                time.sleep(1)
            print(f'{bcolors.OKGREEN}\rYOU_SEND_LOVE_ON_A_TWEET{bcolors.BOLD}\n')

            Timer_Countdown = random.randint(10, 20)

        else:

            while 1:
                a = '.' * i
                try:
                    get_trend_tweets = session.get(url, headers=headers)
                    break
                except requests.ConnectionError:
                    sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                    sys.stdout.flush()
                    i += 1
                    if i > 3:
                        i = 0
                time.sleep(1)

            user_id_str = save_decode[tweet_trend_id]['user_id_str']

            quote_user = decode_trend_tweet['globalObjects']['users'][user_id_str]['screen_name']

            quote_url = f'https://twitter.com/{quote_user}/status/{tweet_trend_id}'
            
            Tweet_Text = arr[choose_random_tweet]
            
            while 1:
                a = '.' * i
                try:
                    SEND_Quote = session.post('https://twitter.com/i/api/graphql/Mvpg1U7PrmuHeYdY_83kLw/CreateTweet',
                                              headers=headers,
                                              json={"variables": {"tweet_text": Tweet_Text, "attachment_url": quote_url,
                                                                  "media": {"media_entities": [],
                                                                            "possibly_sensitive": 'false'},
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
                                                                 "vibe_api_enabled": 'false',
                                                                 "responsive_web_edit_tweet_api_enabled": 'false',
                                                                 "standardized_nudges_misinfo": 'true',
                                                                 "responsive_web_enhance_cards_enabled": 'false'},
                                                    "queryId": "hC1nuE-2d1NX5LYBuuAvtQ"})
                    break
                except requests.ConnectionError:
                    sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                    sys.stdout.flush()
                    i += 1
                    if i > 3:
                        i = 0
                time.sleep(1)

            print(f'{bcolors.OKGREEN}\rYOU_SEND_QUOTE_TWEET_ON_A_TWEET{bcolors.BOLD}\n')

            number_of_tweet += 1

            Timer_Countdown = random.randint(30, 40)

    elif Timer_Countdown == 0 and options == 2:

        headers = {
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs'
                             '%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'origin': 'https://twitter.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                          'Safari/537.36',
            'x-csrf-token': value,
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'ar'
        }
        
        Tweet_Text = arr[choose_random_tweet]

        img_url = ["https://i.postimg.cc/pVYQv688/Compressed-img-32.jpg", "https://i.postimg.cc/C5RGhPSp/Compressed-img-14.jpg",
           "https://i.postimg.cc/vBH7j8KB/Compressed-img-15.jpg", "https://i.postimg.cc/sxbpvYgQ/Compressed-img-16.jpg",
           "https://i.postimg.cc/ydbRbm9Q/Compressed-img-17.jpg", "https://i.postimg.cc/nhb4xGWN/Compressed-img-18.jpg",
           "https://i.postimg.cc/8PrRx0Zh/Compressed-img-19.jpg", "https://i.postimg.cc/Bv5NkVQh/Compressed-img-2.jpg",
           "https://i.postimg.cc/L4WkCp39/Compressed-img-20.jpg", "https://i.postimg.cc/htL9t7Wv/Compressed-img-21.jpg",
           "https://i.postimg.cc/cJdfg40m/Compressed-img-22.jpg", "https://i.postimg.cc/q7Qy8V7d/Compressed-img-23.jpg",
           "https://i.postimg.cc/LXXfDCqg/Compressed-img-24.jpg", "https://i.postimg.cc/wMRN81Q6/Compressed-img-25.jpg",
           "https://i.postimg.cc/MZn3KtsG/Compressed-img-26.jpg", "https://i.postimg.cc/QVLTXjfc/Compressed-img-27.jpg",
           "https://i.postimg.cc/BZRY8DyB/Compressed-img-28.jpg", "https://i.postimg.cc/VLM7XvPQ/Compressed-Img-29.jpg",
           "https://i.postimg.cc/hjSMB1XK/Compressed-img-3.jpg", "https://i.postimg.cc/JzLpx8Ry/Compressed-img-30.jpg",
           "https://i.postimg.cc/BnBMwzvm/Compressed-img-31.jpg", "https://i.postimg.cc/ZqfjJyp3/Compressed-img-35.jpg",
           "https://i.postimg.cc/cJGXDSZg/Compressed-img-4.jpg", "https://i.postimg.cc/D00gWfQD/Compressed-img-5.jpg",
           "https://i.postimg.cc/QCzqcL0M/Compressed-img-6.jpg", "https://i.postimg.cc/DyW6nZw4/Compressed-img-7.jpg",
           "https://i.postimg.cc/nz02c9mB/Compressed-img-8.jpg", "https://i.postimg.cc/fWqCGXDh/Compressed-img-9.jpg",
           "https://i.postimg.cc/vm1x61C5/Compressed-img-34.jpg", "https://i.postimg.cc/7ZB912h6/Compressed-Img-1.jpg",
           "https://i.postimg.cc/Yqzb9VwQ/Compressed-img-10.jpg", "https://i.postimg.cc/K8cQgNZw/Compressed-img-11.jpg",
           "https://i.postimg.cc/qMT1prWk/Compressed-img-12.jpg", "https://i.postimg.cc/90zk3HMd/Compressed-img-13.jpg",
           "https://i.postimg.cc/L6cbW7MP/Compressed-img-36.jpg", "https://i.postimg.cc/v8SjrTq3/Compressed-img-37.jpg",
           "https://i.postimg.cc/yx5bspgw/Compressed-img-38.jpg", "https://i.postimg.cc/T3n4v9R4/Compressed-img-39.jpg",
           "https://i.postimg.cc/kX6HfCL9/Compressed-img-40.jpg", "https://i.postimg.cc/Xv3DjCq7/Compressed-img-41.jpg",
           "https://i.postimg.cc/Xv81pYBK/Compressed-img-42.jpg", "https://i.postimg.cc/bJwCbf17/Compressed-img-43.jpg",
           "https://i.postimg.cc/PxV6QV4P/Compressed-img-44.jpg", "https://i.postimg.cc/T1yt7j7Q/Compressed-img-45.jpg",
           "https://i.postimg.cc/pVYQv688/Compressed-img-32.jpg", "https://i.postimg.cc/Y2xLvRgY/Compressed-img-46.jpg",
           "https://i.postimg.cc/SRVnHQqD/Compressed-img-47.jpg", "https://i.postimg.cc/MpLQWGBL/Compressed-img-48.jpg",
           "https://i.postimg.cc/bJxDHH5X/Compressed-img-49.jpg", "https://i.postimg.cc/9M5w7NJt/Compressed-img-50.jpg",
           "https://i.postimg.cc/d3J7WZMh/Compressed-img-51.jpg", "https://i.postimg.cc/KYgg4yr8/Compressed-img-52.jpg"]

        while 1:
            a = '.' * i
            try:
                res_data = requests.get(img_url[random.randint(0, len(img_url) - 1)])
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        resource_url = 'https://upload.twitter.com/1.1/media/upload.json'

        upload_image = {
            'media': res_data.content,
            'media_category': 'tweet_image'}

        while 1:
            a = '.' * i
            try:
                media_id = session.post(resource_url, headers=headers, files=upload_image)
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        x = json.loads(media_id.content.decode('UTF-8'))
        save_id = x['media_id']

        while 1:
            a = '.' * i
            try:
                SEND_IMG = session.post('https://twitter.com/i/api/graphql/Mvpg1U7PrmuHeYdY_83kLw/CreateTweet',
                                        headers=headers,
                                        json={"variables": {"tweet_text": Tweet_Text, "media": {
                                            "media_entities": [{"media_id": save_id, "tagged_users": []}],
                                            "possibly_sensitive": 'false'}, "withDownvotePerspective": 'false',
                                                            "withReactionsMetadata": 'false',
                                                            "withReactionsPerspective": 'false',
                                                            "withSuperFollowsTweetFields": 'true',
                                                            "withSuperFollowsUserFields": 'true',
                                                            "semantic_annotation_ids": [],
                                                            "dark_request": 'false'},
                                              "features": {"dont_mention_me_view_api_enabled": 'true',
                                                           "interactive_text_enabled": 'true',
                                                           "responsive_web_uc_gql_enabled": 'false',
                                                           "vibe_api_enabled": 'false',
                                                           "responsive_web_edit_tweet_api_enabled": 'false',
                                                           "standardized_nudges_misinfo": 'true',
                                                           "responsive_web_enhance_cards_enabled": 'false'},
                                              "queryId": "hC1nuE-2d1NX5LYBuuAvtQ"})
                break
            except requests.ConnectionError:
                sys.stdout.write(f"\r{bcolors.FAIL}Reconnecting{a}{bcolors.BOLD}")
                sys.stdout.flush()
                i += 1
                if i > 3:
                    i = 0
            time.sleep(1)

        print(f'{bcolors.OKGREEN}\rTWEET_WITH_IMG_SEND{bcolors.BOLD}\n')

        number_of_tweet += 1

        Timer_Countdown = random.randint(30, 40)

    time.sleep(1)
