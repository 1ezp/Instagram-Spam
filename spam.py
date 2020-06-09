import requests
import uuid
import time

uid = str(uuid.uuid4())


class appp:
    def __init__(self, **kwargs):
        self.data = kwargs
        self.username = self.data["username"]
        self.password = self.data["password"]
        self.target = self.data["target"]
        self.sleep = self.data["sleep"]
        self.r =requests.session()

        self.BASE_URL = 'https://instagram.com/'
        self.USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\Chrome/59.0.3071.115 Safari/537.36'


    def loginn(self):
        headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi;1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com'
                   }
        url = "https://i.instagram.com/api/v1/accounts/login/"
        cr = {
            'uuid': uid,
            'password': self.password,
            'username': self.username,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_count': '0'
        }
        self.login = self.r.post(url, data=cr, headers=headers).text
        if ('"logged_in_user"') in self.login:
            print('Logged in As @{}'.format(self.username))
            return True
        elif ("Incorrect Username") in self.login:
            print(
                "The username you entered doesn't appear to belong to an account. Please check your username and try again.")
        elif ('Incorrect password') in self.login:
            print("The password you entered is incorrect. Please try again.")
        elif ('"inactive user"') in self.login:
            print(
                'Your account has been disabled for violating our terms. Learn how you may be able to restore your account.')
        elif ('checkpoint_challenge_required') in self.login:
            print('Secure !')
        else:
            print(self.login)
    def id_graber(self):
        headers = {
            'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
        }



        a_url = f"https://www.instagram.com/web/search/topsearch/?context=blended&query={self.username}&rank_token=0.3953592318270893&count=1"
        #?__a = 1

        self.id1 = requests.get(a_url)
        data = self.id1.json()
        try:
            self.id = str(data['users'][0].get("user").get("pk"))
        except:
            return "Unexpected error"
        #self.id = data["graphql"]["user"]["id"]




    def spam(self):
        done = 0
        false = 0


        target_url = f"https://instagram.com/{self.target}/"

        req = self.r.get(target_url)
        if req.status_code == 404:
            print("user not found")
            exit()
        headers= {
                "Host": "www.instagram.com",
                'User-Agent': "mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
                "Accept": "*/*",
                "Accept-Language": "ar,en-US;q=0.7,en;q=0.3",
                "Accept-Encoding": "gzip, deflate,br",
                "X-IG-WWW-Claim": "hmac.AR37f7MiwKJBWEmpZHU89vwM-ADEoozmKdmgsiRo6BgoTgfo",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest",
                "Content-Length": '37',
                "Origin": "https://www.instagram.com",
                "Connection": "keep-alive",
                "Referer": target_url,
        }
        self.r.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
        while True:

            sp_url = f"{self.BASE_URL}users/{self.id}/report/"
            sp_data = {
                "source_name": "profile",
                "reason_id": '1'
                }
            #sp_get = self.r.get(sp_url)
            sp_req = self.r.post(sp_url,data=sp_data,headers=headers)
            if sp_req.status_code == 200:
                done +=1
                print(f"spam >>{done}")
                print(sp_req.json())
            else:
                print(sp_req.reason)

            time.sleep(self.sleep)

            
        


def main():
    
    username = input("username :>> \u001b[34m")
    password = input("\u001b[0mPassword :>> \u001b[31m")
    target = input("\u001b[0mTarget :>> \u001b[31m")
    sleep = int(input("\u001b[0msleep :>> \u001b[31m"))
    app = appp(username=username,password=password,target=target,sleep=sleep)
    app.loginn()
    app.id_graber()
    app.spam()
main()
