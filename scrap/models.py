from django.db import models

class Post(models.Model):

    u_id = models.TextField(null=True, blank=True)
    site = models.TextField(null=True, blank=True)
    market = models.TextField(null=True, blank=True)
    coin = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    market_volume = models.TextField(null=True, blank=True)
    coin_volume = models.TextField(null=True, blank=True)
    price_quality = models.TextField(null=True, blank=True)
    volume_quality = models.TextField(null=True, blank=True)
    volume_quality_value = models.TextField(null=True, blank=True)
    price_quality_value = models.TextField(null=True, blank=True)
    pivot_quality = models.TextField(null=True, blank=True)
    market_cap = models.TextField(null=True, blank=True)
    available_supply = models.TextField(null=True, blank=True)
    total_supply = models.TextField(null=True, blank=True)
    coin_url = models.TextField(null=True, blank=True)
    balance = models.TextField(null=True, blank=True)
    usd_balance = models.TextField(null=True, blank=True)
    favorite = models.TextField(null=True, blank=True)
    usd_price = models.TextField(null=True, blank=True)
    usd_volume = models.TextField(null=True, blank=True)
    logo_url = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    history = models.TextField(null=True, blank=True)
    image_1h_url = models.TextField(null=True, blank=True)
    image_5m_url = models.TextField(null=True, blank=True)
    image_30m_url = models.TextField(null=True, blank=True)
    image_1d_url = models.TextField(null=True, blank=True)
    website_image_url = models.TextField(null=True, blank=True)
    market_standard = models.TextField(null=True, blank=True)
    all_time_high = models.TextField(null=True, blank=True)
    all_time_low = models.TextField(null=True, blank=True)
    atl_diff = models.TextField(null=True, blank=True)
    ath_diff = models.TextField(null=True, blank=True)
    diff_percent = models.TextField(null=True, blank=True)
    avg_diff_percent = models.TextField(null=True, blank=True)
    low_diff_percent = models.TextField(null=True, blank=True)
    high_diff_percent = models.TextField(null=True, blank=True)
    week_diff_percent = models.TextField(null=True, blank=True)
    avg_week_diff_percent = models.TextField(null=True, blank=True)
    week_low_diff_percent = models.TextField(null=True, blank=True)
    week_high_diff_percent = models.TextField(null=True, blank=True)
    month_diff_percent = models.TextField(null=True, blank=True)
    avg_month_diff_percent = models.TextField(null=True, blank=True)
    month_low_diff_percent = models.TextField(null=True, blank=True)
    month_high_diff_percent = models.TextField(null=True, blank=True)
    hour_diff_percent = models.TextField(null=True, blank=True)
    avg_hour_diff_percent = models.TextField(null=True, blank=True)
    five_rsi = models.TextField(null=True, blank=True)
    five_stoch_rsi = models.TextField(null=True, blank=True)
    thirty_rsi = models.TextField(null=True, blank=True)
    thirty_stoch_rsi = models.TextField(null=True, blank=True)
    sixty_rsi = models.TextField(null=True, blank=True)
    sixty_stoch_rsi = models.TextField(null=True, blank=True)
    day_rsi = models.TextField(null=True, blank=True)
    day_stoch_rsi = models.TextField(null=True, blank=True)
    five_rsi_text = models.TextField(null=True, blank=True)
    five_stoch_rsi_text = models.TextField(null=True, blank=True)
    thirty_rsi_text = models.TextField(null=True, blank=True)
    thirty_stoch_rsi_text = models.TextField(null=True, blank=True)
    sixty_rsi_text = models.TextField(null=True, blank=True)
    sixty_stoch_rsi_text = models.TextField(null=True, blank=True)
    day_rsi_text = models.TextField(null=True, blank=True)
    day_stoch_rsi_text = models.TextField(null=True, blank=True)
    volume_five = models.TextField(null=True, blank=True)
    volume_thirty = models.TextField(null=True, blank=True)
    volume_sixty = models.TextField(null=True, blank=True)
    volume_day = models.TextField(null=True, blank=True)
    volume_week = models.TextField(null=True, blank=True)
    volume_month = models.TextField(null=True, blank=True)
    five_macd = models.TextField(null=True, blank=True)
    five_macd_text = models.TextField(null=True, blank=True)
    thirty_macd = models.TextField(null=True, blank=True)
    thirty_macd_text = models.TextField(null=True, blank=True)
    sixty_macd = models.TextField(null=True, blank=True)
    sixty_macd_text = models.TextField(null=True, blank=True)
    day_macd = models.TextField(null=True, blank=True)
    day_macd_text = models.TextField(null=True, blank=True)
    five_uo = models.TextField(null=True, blank=True)
    thirty_uo = models.TextField(null=True, blank=True)
    sixty_uo = models.TextField(null=True, blank=True)
    day_uo = models.TextField(null=True, blank=True)
    five_uo_text = models.TextField(null=True, blank=True)
    sixty_uo_text = models.TextField(null=True, blank=True)
    thirty_uo_text = models.TextField(null=True, blank=True)
    day_uo_text = models.TextField(null=True, blank=True)
    five_ichimoku = models.TextField(null=True, blank=True)
    five_ichimoku_text = models.TextField(null=True, blank=True)
    five_reg_ichimoku = models.TextField(null=True, blank=True)
    five_reg_ichimoku_text = models.TextField(null=True, blank=True)
    thirty_ichimoku = models.TextField(null=True, blank=True)
    thirty_ichimoku_text = models.TextField(null=True, blank=True)
    thirty_reg_ichimoku = models.TextField(null=True, blank=True)
    thirty_reg_ichimoku_text = models.TextField(null=True, blank=True)
    sixty_ichimoku = models.TextField(null=True, blank=True)
    sixty_ichimoku_text = models.TextField(null=True, blank=True)
    sixty_reg_ichimoku = models.TextField(null=True, blank=True)
    sixty_reg_ichimoku_text = models.TextField(null=True, blank=True)
    day_ichimoku = models.TextField(null=True, blank=True)
    day_ichimoku_text = models.TextField(null=True, blank=True)
    day_reg_ichimoku = models.TextField(null=True, blank=True)
    day_reg_ichimoku_text = models.TextField(null=True, blank=True)
    five_tenken = models.TextField(null=True, blank=True)
    five_reg_tenken = models.TextField(null=True, blank=True)
    five_tenken_cloud = models.TextField(null=True, blank=True)
    five_reg_tenken_cloud = models.TextField(null=True, blank=True)
    thirty_tenken = models.TextField(null=True, blank=True)
    thirty_reg_tenken = models.TextField(null=True, blank=True)
    thirty_tenken_cloud = models.TextField(null=True, blank=True)
    thirty_reg_tenken_cloud = models.TextField(null=True, blank=True)
    sixty_tenken = models.TextField(null=True, blank=True)
    sixty_reg_tenken = models.TextField(null=True, blank=True)
    sixty_tenken_cloud = models.TextField(null=True, blank=True)
    sixty_reg_tenken_cloud = models.TextField(null=True, blank=True)
    day_tenken = models.TextField(null=True, blank=True)
    day_reg_tenken = models.TextField(null=True, blank=True)
    day_tenken_cloud = models.TextField(null=True, blank=True)
    day_reg_tenken_cloud = models.TextField(null=True, blank=True)
 

    def __str__(self):
        return self.name

##1d RSI
##1d Stoch RSI
##1d Vol %
##1h RSI
##1h Stoch RSI
##1h Vol %
##1mo Vol %
##1w Vol %
##30min RSI
##30min Stoch RSI
##30min Vol %
##5min RSI
##5min Stoch RSI
##5min Vol %
##Available Supply
##Avg Day %
##Avg Hour %
##Avg Month %
##Avg Week %
##Coin Day %
##Day High %
##Day Low %
##Hour %
##Last 30 Days
##Market
##Market Cap
##Market Vol
##Month %
##Month High %
##Month Low %
##Name
##Price
##Site
##Status
##Total
##Supply Week %
##Week High %
##Week Low %
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##

























