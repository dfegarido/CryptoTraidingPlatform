import requests as r
import json, ast
import pandas as pd
from time import time as ts
from datetime import datetime
import os
from bs4 import BeautifulSoup



class CoinMarkeCap:

    def __init__(self):
        self.url = "https://coinmarketcap.com"
        self.path =  'coinmarketcap'
        self.historical = 'historycal_data'
        
    def save_to_xls(self, result):
        path = self.path
        time = datetime.fromtimestamp(ts()).strftime('%m-%d-%Y_%H-%M-%S') 
        try:
            os.mkdir(path)
            os.mkdir(path + "/" + self.historical)
        except:
            pass
        save_to = str(path +"/"+ time)
        cols = ['rank', 'id', 'name', 'symbol',  'price_usd', 'price_btc', 'volume_usd_24h', 'market_cap_usd', 'available_supply', 'total_supply', 'max_supply', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'last_updated','graph(7d)']
        df = pd.DataFrame(columns=cols)
        df = df.append(result, ignore_index=False)
        df.to_excel('{}.xls'.format(save_to), index=False)

    def historical_data(self, stock_name):
        historical_file = self.path + "/historycal_data"
        try:
            os.mkdir(self.path)
            os.mkdir(historical_file)
        except:
            pass
        hist_data = "https://coinmarketcap.com/currencies/{}/historical-data/?start=20130428&end=20171230".format(stock_name)
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        sess = r.Session()
        sess = sess.get(hist_data, headers=headers).text
        soup = BeautifulSoup(sess, 'lxml')
        try:
            table = soup.find_all("table",{"class":"table"})[0]
            cols = ["Date","Open","High","Low","Close","Volume", "Market Cap"]
            df = pd.DataFrame(columns=cols)
            datasets = []
            for tr in table.find_all("tr")[1:]:
                hdata = tr.text.split("\n")[1:-1]
                keys = {}
                for i in range(len(cols)):
                    keys.update({cols[i]:hdata[i]})   
                datasets.append(keys)
            save_to = "{}/{}".format(historical_file, stock_name)
            df = df.append(datasets, ignore_index=False)
            df.to_excel('{}.xls'.format(save_to), index=False)   
        except:
            pass
        return datasets

    def page_crawler(self):
        url = self.url
        i = 1
        headers = {
            'cookie':'__cfduid=d610dedd6d49197dab76835d46e85e23d1514802696; gtm_session_first=Mon%20Jan%2001%202018%2013:31:39%20GMT+0300%20(Arab%20Standard%20Time); _ga=GA1.2.1827791076.1514802700; _gid=GA1.2.546089261.1514802700; __gads=ID=2d4c2935567363ae:T=1514802701:S=ALNI_MZsp5Hpj_qVfD7D8G2lW3cTTqhr8A; gtm_session_last=Mon%20Jan%2001%202018%2014:16:52%20GMT+0300%20(Arab%20Standard%20Time)',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            }
        status = True
        datasets = []
        img = []
        cols = ['No#','Name','Market','Market Cap','Price','Volume(24h)','Circulating Supply','Change(24h)','Price Graph(7d)']
        while status:
            page_url = "{}/{}".format(url, i)
            sess = r.Session()
            sess = sess.get(page_url, headers=headers)
            if sess.status_code == 200: 
                soup =  BeautifulSoup(sess.text, 'lxml')
                tbody = soup.find_all("tbody")
                for tr in tbody[0].find_all("tr"):
                    td = tr.find_all('td')
                    sets = {}
                    sets.update({
                        cols[0]:td[0].text.strip(),
                        cols[1]:td[1].text.strip().split("\n")[1],
                        cols[2]:td[1].text.strip().split("\n")[0],
                        cols[3]:td[2].text.strip(),
                        cols[4]:td[3].text.strip(),
                        cols[5]:td[4].text.strip(),
                        cols[6]:td[5].text.strip(),
                        cols[7]:td[6].text.strip(),
                        cols[8]:td[7].img['src'],
                        })
                    img.append(td[7].img['src'])
                    datasets.append(sets)
                    i += 1
            else:
                status = False
        time = datetime.fromtimestamp(ts()).strftime('%m-%d-%Y_%H-%M-%S')
        try:
            os.mkdir("file")
        except:
            pass
        df = pd.DataFrame(columns=cols)
        df = df.append(datasets, ignore_index=False)
        df.to_excel("file/" + time + ".xls", index=False)
        return img

    def save_to_database(self):
        url = "https://api.coinmarketcap.com/v1/ticker/"
        sess = r.Session()
        sess = sess.get(url).json()
        img = self.page_crawler()
        i = 0
        for ses in sess:
            ses.update({'graph(7d)':img[i]})
            ses.update({'RSI_1d':''})
            ses.update({'Stoch_RSI_1d':''})
            ses.update({'Vol_1d':''})
            ses.update({'RSI_1h':''})
            ses.update({'Stoch_RSI_1h':''})
            ses.update({'Vol_1h':''})
            ses.update({'Vol_1mo':''})
            ses.update({'Vol_1w':''})
            ses.update({'RSI_30min':''})
            ses.update({'Stoch_RSI_30min':''})
            ses.update({'Vol_30min':''})
            ses.update({'RSI_5min':''})
            ses.update({'Stoch_RSI_5min':''})
            ses.update({'Vol_5min':''})
            ses.update({'Avg_Day':''})
            ses.update({'Avg_Hour':''})
            ses.update({'Avg_Month':''})
            ses.update({'Avg_Week':''})
            ses.update({'Coin_Day':''})
            ses.update({'Day_High':''})
            ses.update({'Day_Low':''})
            ses.update({'Last_30_Days':''})
            ses.update({'Market':''})
            ses.update({'Market_Cap':''})
            ses.update({'Market_Vol':''})
            ses.update({'Month':''})
            ses.update({'Month_High':''})
            ses.update({'Month_Low':''})
            ses.update({'Site':''})
            ses.update({'Supply_Week':''})
            ses.update({'Week_High':''})
            ses.update({'Week_Low':''})
            dic_to_str = json.dumps(str(self.historical_data(ses['id'])))
            ses.update({'history':dic_to_str})
            i += 1
##        for sets in sess:
####            print("saving datasets")
##            post_datas(sets)  
##        for ses in sess:
##            ses.pop("history")
##        self.save_to_xls(sess)
        return sess

    def get_api(self):

        url = "https://api.coinmarketcap.com/v1/ticker/"
        sess = r.Session()
        sess = sess.get(url).json()
        img = self.page_crawler()
        for i in range(len(sess)):
            sess[i].update({"graph": img[i]})
        return sess
    
    def get_json(self):
        
        file = "api.json"
        with open(file,"r") as f:
            api = json.load(f)   
        return api

    def run(self):
        api = self.get_api()
        return api
            
            


class Spirai():

    def __init__(self):
        pass

    def spirai_api(self):
        session, result = self.auth()
        print("Authentication Status : " + str(result.status_code))
        path = 'api'
        try:
            os.mkdir(path)
        except:
            pass
        url = "https://api2.spir.ai/exchange?sites=Bittrex,Poloniex,Kraken,Bitfinex"
        sess = session.post(url)
        data = sess.json()
        for i in range(len(data['coins'])):
            try:
                l = ast.literal_eval(data['coins'][i]['history'])
            except:
                continue        
            data['coins'][i]['history'] = l
        time = datetime.fromtimestamp(ts()).strftime('%m-%d-%Y_%H-%M-%S')
        with open("{}/{}.json".format(path, time), 'w') as file:
            json.dump(data, file, indent=2)

        return data    

    def auth(self):
        username = "agapito"
        password = "P@$$word"
        headers = {
            'authorization':'Basic YWdhcGl0bzpQQCQkd29yZA==',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        }
        payload = (username, password)
        url = "https://api2.spir.ai/userAuth"
        sess = r.Session()
        sess.auth = payload
        sess.headers.update(headers)
        result = sess.post(url)
        return sess, result
    
    def history(self, u_id):
        url = "https://api2.spir.ai/exchange/{}?interval=1d".format(u_id)
        api = r.get(url).json()["candleData"]
        return api

    def api(self):
        url = "https://api2.spir.ai/exchange?sites=Bittrex,Poloniex,Kraken,Bitfinex,Binance"
##        head = 'https://api2.spir.ai/home/header'
        header = {
            'accept':'application/json',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9',
            'authorization':'Basic null',
            'content-length':'17',
            'content-type':'application/json',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        api = r.post(url, headers=header, data={"columns":False}).json()["coins"]
##        head_api = r.get(head).json()['coins'][:6]
        return api
    
    def run(self):
        data = self.spirai_api()
        return data


    
      
       
if __name__ == "__main__":
###    try:
###        x = cols_spi()
###    except Exception as e:
###        print(e)
####    x, y = cols_spi()
##    x = CoinMarkeCap().page_crawler() 
##    x = CoinMarkeCap().historical_data('ethereum') # then run this historical data 
##    x = CoinMarkeCap().save_to_database()  #run this first 
####    x = spirai_data()
##    x = spirai_api_2()
##    result = get_api()
##    soup = historical_data("ethereum")
    s = Spirai()
    api = s.api()

    


    
