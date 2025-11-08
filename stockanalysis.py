import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import matplotlib.dates as mdates
from matplotlib.gridspec import GridSpec
import requests
import json
from urllib.parse import urlencode, unquote
import xml.etree.ElementTree as ET

# 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# API 설정
API_KEY = "365ADE7440DA44D0B6D2AD50B9DC7121F6EDEE01키"
BASE_URL = "https://openapi.krx.co.kr/openapi/service/market/index/price"  # 실제 엔드포인트는 문서에서 확인

def get_krx_data(service_name, params):
    """한국거래소 OpenAPI를 통해 데이터를 가져오는 함수"""
    url = f"{BASE_URL}/{service_name}"
    params['serviceKey'] = API_KEY
    params['resultType'] = 'json'
    
    try:
        response = requests.get(url, params=params)
        print(f"API Response Status: {response.status_code}")
        print(f"API Response Content: {response.text[:200]}")  # 응답 내용의 일부만 출력
        
        if response.status_code == 200:
            data = response.json()
            if 'response' in data and 'body' in data['response']:
                items = data['response']['body'].get('items', {}).get('item', [])
                if items:
                    return pd.DataFrame(items)
        return None
    except Exception as e:
        print(f"데이터 수집 중 오류 발생: {e}")
        return None

def get_securities_index():
    """증권업 지수 데이터 수집"""
    params = {
        'beginBasDt': (datetime.now() - timedelta(days=365)).strftime('%Y%m%d'),
        'endBasDt': datetime.now().strftime('%Y%m%d'),
        'idxNm': '증권업',
        'mrktCls': 'KOSPI'
    }
    return get_krx_data('getStockPriceInfo', params)

def get_kospi_trading_value():
    """KOSPI 거래대금 데이터 수집"""
    params = {
        'beginBasDt': (datetime.now() - timedelta(days=365)).strftime('%Y%m%d'),
        'endBasDt': datetime.now().strftime('%Y%m%d'),
        'mrktCls': 'KOSPI'
    }
    return get_krx_data('getStockTradingValue', params)

def get_kospi_credit_balance():
    """KOSPI 신용잔고 데이터 수집"""
    params = {
        'beginBasDt': (datetime.now() - timedelta(days=365)).strftime('%Y%m%d'),
        'endBasDt': datetime.now().strftime('%Y%m%d'),
        'mrktCls': 'KOSPI'
    }
    return get_krx_data('getStockCreditBalance', params)

# 데이터 수집
print("증권업 지수 데이터 수집 중...")
securities_index = get_securities_index()
print("KOSPI 거래대금 데이터 수집 중...")
trading_value = get_kospi_trading_value()
print("KOSPI 신용잔고 데이터 수집 중...")
credit_balance = get_kospi_credit_balance()

if all(data is not None for data in [securities_index, trading_value, credit_balance]):
    # 날짜 형식 변환
    for df in [securities_index, trading_value, credit_balance]:
        df['basDt'] = pd.to_datetime(df['basDt'])
        df.set_index('basDt', inplace=True)
    
    # 그래프 그리기
    plt.figure(figsize=(15, 10))
    gs = GridSpec(3, 1, height_ratios=[2, 1, 1])
    
    # 증권업 지수 그래프
    ax1 = plt.subplot(gs[0])
    ax1.plot(securities_index.index, securities_index['clpr'], label='증권업 지수', color='blue')
    ax1.set_title('증권업 지수 추이')
    ax1.set_ylabel('지수')
    ax1.legend()
    ax1.grid(True)
    
    # KOSPI 거래대금 그래프
    ax2 = plt.subplot(gs[1], sharex=ax1)
    ax2.plot(trading_value.index, trading_value['trdval'], label='KOSPI 거래대금', color='red')
    ax2.set_title('KOSPI 거래대금 추이')
    ax2.set_ylabel('거래대금 (원)')
    ax2.legend()
    ax2.grid(True)
    
    # KOSPI 신용잔고 그래프
    ax3 = plt.subplot(gs[2], sharex=ax1)
    ax3.plot(credit_balance.index, credit_balance['crdtBalAmt'], label='KOSPI 신용잔고', color='green')
    ax3.set_title('KOSPI 신용잔고 추이')
    ax3.set_ylabel('신용잔고 (원)')
    ax3.legend()
    ax3.grid(True)
    
    # x축 날짜 포맷 설정
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
else:
    print("데이터를 가져오는데 실패했습니다. API 키가 올바르게 설정되었는지 확인해주세요.")

# KRX OpenAPI 엔드포인트 (예시, 실제 명세서에서 확인 필요)
url = "https://krxopenapi.kr/apis/sto/stk_bydd_trd"

headers = {
    "AUTH_KEY": "여기에_발급받은_인증키"
}
params = {
    "basDd": "20240522"  # 기준일자 (YYYYMMDD)
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
