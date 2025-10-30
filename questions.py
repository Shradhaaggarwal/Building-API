import requests;
import json;

response = requests.get("https://api.stackexchange.com/2.3/answers?order=desc&sort=activity&site=stackoverflow");

print(response); 
print(response.json()); 

for data in response.json()['items']:
    print("account id:", data.get('owner').get('account_id')); 


for data in response.json()['items']:
    if(data.get('owner').get('user_type')=='registered'):
        print("account id: ", data.get('owner').get('account_id')); 
    else:
        print("unregistered user"); 
    # print(); 


for data in response.json()['items']:
    owner = data.get('owner'); 
    acc_type = owner.get('user_type');

    if(acc_type=='registered'):
        print("yes"); 
    else:
        print("no"); 