from vk_clients import *

get_user = GettingID('boriska24')
user = get_user.execute()
user_id = user.get('id')

get_friends = GettingFriends(user_id)
friends = get_friends.execute()

age_list = [0 for i in range(120)]
today = datetime.now()

print(user.get('last_name'), user.get('first_name'), sep=' ')

for f in friends:
    bdate_str = f.get('bdate')
    try:
        bdate = datetime.strptime(bdate_str, '%d.%m.%Y')
        days = (today-bdate).days
        age = days // 365
        age_list[age] += 1
    except:
         pass
for i in range(120):
    if age_list[i]>0:
        print(i,': ','#'*age_list[i])