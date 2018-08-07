from django.shortcuts import render, HttpResponse
from .script.scrap import CoinMarkeCap, Spirai
import requests as r
from .models import Post
import json, time


#/
def home(request):
    head = 'https://api2.spir.ai/home/header'
    data = r.get(head).json()['coins'][:6]
    update = time.strftime('%H') == '24'
    return render(request, 'home.html', {"data":data,'update':update})


#/<u_id>/
def chart(request, u_id=None):
    post = Post.objects.filter(u_id=u_id)
    l = len(post)
    post = post[int(l-1)]

    post.price = format(float(post.price), '.10f')
    post.diff_percent = format(float(post.diff_percent), ".3f")
    
    return render(request, "chart_page.html", {"name":u_id, "post":post})
##    return HttpResponse(post, content_type="text/json")

#/json/<u_id>
def json_page(request, u_id=None):
    post = Post.objects.filter(u_id=u_id)
    l = len(post)
    post = post[int(l-1)]
    history = Spirai().history(post.u_id)
                
    data = []
    for datas in history:
        date = int(datas['date'])*1000
        o = datas['open']
        h = datas['high']
        l = datas['low']
        c = datas['close']
        vol = datas['volume']        
        data.append([date,o,h,l,c,vol])
        
    data =  json.dumps(data[:])
    return HttpResponse(data, content_type="text/json")

#/datatable/
def datatable(request):
    return render(request, "datatable.html")


#/table_api
def table_api(request):
    post = Spirai().api()[:330]
    data = {"data":[]}
    
    for item in post:
        p = []
        p.append("<a href='../" + str(item["id"]) + "' ><b>" + str(item["id"]) + "</b></a>")
        p.append("<a href='../" + str(item["id"]) + "' ><b>" + str(item['name']) + "</b></a>")
        p.append("<a href='../" + str(item["id"]) + "' ><b>" + str(item['market']) + "</b></a>")
        p.append("<a href='../" + str(item["id"]) + "' ><b><img src= '" + str(item['image_1d_url']) + "' class='img-thumbnail ' />" + "</b></a>")
        p.append(item['price'])
#        p.append(item['price'])
        p.append(item['volume_day'])
        p.append(item['market_cap'])
#        p.append(item['available_supply'])
        p.append(item['market_volume'])
        p.append(item['coin_volume'])
        p.append(item['diff_percent'])
        p.append(item['week_diff_percent'])
        p.append(item['month_diff_percent'])
#        p.append(item['last_updated'] )
        data["data"].append(p)
        
    return HttpResponse(json.dumps(data, indent=2) , content_type="text/html")




#/savedata/
def savedata(request):
        
    data = Spirai().run()

    for datasets in data['coins']:
        
        p = Post(u_id = datasets["id"],
                 site = datasets["site"],
                 market = datasets["market"],
                 coin = datasets["coin"],
                 name = datasets["name"],
                 price = datasets["price"],
                 market_volume = datasets["market_volume"],
                 coin_volume = datasets["coin_volume"],
                 price_quality = datasets["price_quality"],
                 volume_quality = datasets["volume_quality"],
                 volume_quality_value = datasets["volume_quality_value"],
                 price_quality_value = datasets["price_quality_value"],
                 pivot_quality = datasets["pivot_quality"],
                 market_cap = datasets["market_cap"],
                 available_supply = datasets["available_supply"],
                 total_supply = datasets["total_supply"],
                 coin_url = datasets["coin_url"],
                 balance = datasets["balance"],
                 usd_balance = datasets["usd_balance"],
                 favorite = datasets["favorite"],
                 usd_price = datasets["usd_price"],
                 usd_volume = datasets["usd_volume"],
                 logo_url = datasets["logo_url"],
                 description = datasets["description"],
                 history = datasets["history"],
                 image_1h_url = datasets["image_1h_url"],
                 image_5m_url = datasets["image_5m_url"],
                 image_30m_url = datasets["image_30m_url"],
                 image_1d_url = datasets["image_1d_url"],
                 website_image_url = datasets["website_image_url"],
                 market_standard = datasets["market_standard"],
                 all_time_high = datasets["all_time_high"],
                 all_time_low = datasets["all_time_low"],
                 atl_diff = datasets["atl_diff"],
                 ath_diff = datasets["ath_diff"],
                 diff_percent = datasets["diff_percent"],
                 avg_diff_percent = datasets["avg_diff_percent"],
                 low_diff_percent = datasets["low_diff_percent"],
                 high_diff_percent = datasets["high_diff_percent"],
                 week_diff_percent = datasets["week_diff_percent"],
                 avg_week_diff_percent = datasets["avg_week_diff_percent"],
                 week_low_diff_percent = datasets["week_low_diff_percent"],
                 week_high_diff_percent = datasets["week_high_diff_percent"],
                 month_diff_percent = datasets["month_diff_percent"],
                 avg_month_diff_percent = datasets["avg_month_diff_percent"],
                 month_low_diff_percent = datasets["month_low_diff_percent"],
                 month_high_diff_percent = datasets["month_high_diff_percent"],
                 hour_diff_percent = datasets["hour_diff_percent"],
                 avg_hour_diff_percent = datasets["avg_hour_diff_percent"],
                 five_rsi = datasets["five_rsi"],
                 five_stoch_rsi = datasets["five_stoch_rsi"],
                 thirty_rsi = datasets["thirty_rsi"],
                 thirty_stoch_rsi = datasets["thirty_stoch_rsi"],
                 sixty_rsi = datasets["sixty_rsi"],
                 sixty_stoch_rsi = datasets["sixty_stoch_rsi"],
                 day_rsi = datasets["day_rsi"],
                 day_stoch_rsi = datasets["day_stoch_rsi"],
                 five_rsi_text = datasets["five_rsi_text"],
                 five_stoch_rsi_text = datasets["five_stoch_rsi_text"],
                 thirty_rsi_text = datasets["thirty_rsi_text"],
                 thirty_stoch_rsi_text = datasets["thirty_stoch_rsi_text"],
                 sixty_rsi_text = datasets["sixty_rsi_text"],
                 sixty_stoch_rsi_text = datasets["sixty_stoch_rsi_text"],
                 day_rsi_text = datasets["day_rsi_text"],
                 day_stoch_rsi_text = datasets["day_stoch_rsi_text"],
                 volume_five = datasets["volume_five"],
                 volume_thirty = datasets["volume_thirty"],
                 volume_sixty = datasets["volume_sixty"],
                 volume_day = datasets["volume_day"],
                 volume_week = datasets["volume_week"],
                 volume_month = datasets["volume_month"],
                 five_macd = datasets["five_macd"],
                 five_macd_text = datasets["five_macd_text"],
                 thirty_macd = datasets["thirty_macd"],
                 thirty_macd_text = datasets["thirty_macd_text"],
                 sixty_macd = datasets["sixty_macd"],
                 sixty_macd_text = datasets["sixty_macd_text"],
                 day_macd = datasets["day_macd"],
                 day_macd_text = datasets["day_macd_text"])
        p.save()
        
       
    
       
##    return render(request, "loader.html", {"data":data['coins'][0]})
    return HttpResponse(json.dumps(data['coins']), content_type="text/json")
    

