import requests as rq
import threading as td
import time
import pprint

def cat_facts(api):
    req = rq.get(api)
    if req.status_code == 200:
        pprint.pprint(req.json())
    else:
        pprint.pprint("Error")

def onetoten(n):
    for i in range(1,n+1):
        time.sleep(0.3)
        print('T2 : ',i)

t1 = td.Thread(target=cat_facts,args=('https://cat-fact.herokuapp.com/facts',))
t2 = td.Thread(target=onetoten,args=(15,))

t1.start()
t2.start()
for k in range(10):
    time.sleep(0.3)
    print('AE :',k)
t2.join()
t1.join()