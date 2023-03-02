import requests
from bs4 import BeautifulSoup as bs

def get_data():
    cookies = {
        'HINTS_FIO_COOKIE_NAME': '1',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CITY_ID': 'CityCZ_1370',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GUEST_ID': '20332289540',
        'MVID_KLADR_ID': '2600000100000',
        'MVID_REGION_ID': '20',
        'MVID_REGION_SHOP': 'S917',
        'MVID_TIMEZONE_OFFSET': '3',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'searchType2': '1',
        'afUserId': '794cec8b-fd89-47b7-8f25-fc48a14ebfeb-p',
        '_ym_uid': '1648798752782571540',
        'uxs_uid': 'd2d52860-b18e-11ec-8edd-0d8937d9b2d9',
        'wurfl_device_id': 'generic_web_browser',
        'mindboxDeviceUUID': 'dab934d2-6502-42d2-b80c-f6d4ffdbc380',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22dab934d2-6502-42d2-b80c-f6d4ffdbc380%22%7D',
        '__lhash_': '4932d086b946c496b1556d62135c7ae1',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_COOKIE': '2500',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MCLICK_NEW': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_SERVICES': '111',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        '_gid': 'GA1.2.1816821898.1677763508',
        '_sp_ses.d61c': '*',
        '_ym_d': '1677763508',
        '_ym_isad': '1',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'tmr_lvid': '7b0b9a1ffba12350a060192e704a2f75',
        'tmr_lvidTS': '1677763511283',
        'flocktory-uuid': '8b56bdf5-b410-466f-b928-6cce321d5dfc-6',
        'advcake_track_id': '78e67941-3ace-0c3f-cbc0-cafe12a3cf74',
        'advcake_session_id': 'c0764b6f-8ba4-da39-bd21-34465c9d3a65',
        'AF_SYNC': '1677763513107',
        'SL_G_WPT_TO': 'ru',
        'SL_GWPT_Show_Hide_tmp': '1',
        'SL_wptGlobTipTmp': '1',
        'SMSError': '',
        'authError': '',
        '__hash_': 'b5c2cb68ad2be85b667852d3c5e743b3',
        'MVID_VIEWED_PRODUCTS': '',
        'JSESSIONID': '9CNmkQyLMZjfBlMk3sbywNp1PlfCstTHWlNybz9mcLb3sy7J098p!-1256256402',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1929698314.20480.0000',
        'bIPs': '2118529862',
        'MVID_GTM_BROWSER_THEME': '1',
        'BIGipServeratg-ps-prod_tcp80_clone': '1929698314.20480.0000',
        'deviceType': 'tablet',
        'CACHE_INDICATOR': 'true',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UyTgtaImgqO2B/Dzc3VS46bmYJUFJ5fUIVN19OMGELXwhbYSZ/Sy5WRBslJhpQEnU9SnU7GjhmH2RNWyRJWU17FhoXfnIqVQsTXz1BcXobN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueTBCbCNkR1khSV1TdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWyGtg1Q==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UyTgtaImgqO2B/Dzc3VS46bmYJUFJ5fUIVN19OMGELXwhbYSZ/Sy5WRBslJhpQEnU9SnU7GjhmH2RNWyRJWU17FhoXfnIqVQsTXz1BcXobN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueTBCbCNkR1khSV1TdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWyGtg1Q==',
        'cfidsgib-w-mvideo': '0i6fIfZ6yHzhNtdHZRY2dOd2JaVcWTDrho0XKDpY5lUxmwDaoLjYDQfcVsSYaSlH/c4qZvQ8ijG2+NDTtOBYK3C9tRuP18SPDDgVXcA0OuVfVntbrRnaI1avbYHHURnDtwqANr4zbqYDEtzq2ry/zqEVDyWuJQBN2PfYSA==',
        'cfidsgib-w-mvideo': '0i6fIfZ6yHzhNtdHZRY2dOd2JaVcWTDrho0XKDpY5lUxmwDaoLjYDQfcVsSYaSlH/c4qZvQ8ijG2+NDTtOBYK3C9tRuP18SPDDgVXcA0OuVfVntbrRnaI1avbYHHURnDtwqANr4zbqYDEtzq2ry/zqEVDyWuJQBN2PfYSA==',
        'gsscgib-w-mvideo': 'BSGFTQplYzkZPxslc8NdYbkxBddemQQa2aFlPf91L4JM48LvbjwVrzROQEhZbXop4EsG5jDB/kFjknwhjqINTaXfV6OrV7rB5UzqeveEi4iRiWPABVlFTK0fPznG00w7RmeYM6d1BHkuOluZC12BhlQcEP7Bcmn4MXVue4/NtraLnj6k99exMg2z8/XOaS9t8KFqkDNZ3eeqhRP1qyjwTI2ILGOAqwRMBs/eXwXVeSMRgPWEuHaFAghjMflrsQ==',
        'gsscgib-w-mvideo': 'BSGFTQplYzkZPxslc8NdYbkxBddemQQa2aFlPf91L4JM48LvbjwVrzROQEhZbXop4EsG5jDB/kFjknwhjqINTaXfV6OrV7rB5UzqeveEi4iRiWPABVlFTK0fPznG00w7RmeYM6d1BHkuOluZC12BhlQcEP7Bcmn4MXVue4/NtraLnj6k99exMg2z8/XOaS9t8KFqkDNZ3eeqhRP1qyjwTI2ILGOAqwRMBs/eXwXVeSMRgPWEuHaFAghjMflrsQ==',
        'fgsscgib-w-mvideo': 'jzJqd93cd335af0bfca395f0d0a8e81830542398',
        'fgsscgib-w-mvideo': 'jzJqd93cd335af0bfca395f0d0a8e81830542398',
        'cfidsgib-w-mvideo': 'YOgtWRXgIyV0qZ5NST5Um1uwCwtCB6a2n+t6bjkKt5BxaoTkexbSukxyCBSRFW260kSxPcZZXzRam6jmX1oMMwPNhh6UI9i1bAneaeKSV2X5ry/S2VIrb6jRu7rgiSBNOiWPk8RO0yTmzUR/9s+kaLKNMbVRFrRdmKr1TA==',
        '_dc_gtm_UA-1873769-1': '1',
        '_sp_id.d61c': 'edd4b65b-e04c-4121-ad13-8f34ae38f36b.1677763508.1.1677765142..2a1d22cb-bdad-40c5-83f7-d1eee8dc6dda..55753977-6ac8-4d8f-9cb3-9033930c2c1b.1677763508142.90',
        '_ga': 'GA1.2.118058747.1648798750',
        '_dc_gtm_UA-1873769-37': '1',
        'tmr_detect': '1%7C1677765145781',
        'MVID_ENVCLOUD': 'prod2',
        '_ga_CFMZTSS5FM': 'GS1.1.1677763508.6.1.1677765180.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1677763508.6.1.1677765180.18.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=f67532685c094b45a5ac5f8993ef02f1,sentry-sample_rate=0.5',
        # 'cookie': 'HINTS_FIO_COOKIE_NAME=1; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CITY_ID=CityCZ_1370; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GUEST_ID=20332289540; MVID_KLADR_ID=2600000100000; MVID_REGION_ID=20; MVID_REGION_SHOP=S917; MVID_TIMEZONE_OFFSET=3; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=1; afUserId=794cec8b-fd89-47b7-8f25-fc48a14ebfeb-p; _ym_uid=1648798752782571540; uxs_uid=d2d52860-b18e-11ec-8edd-0d8937d9b2d9; wurfl_device_id=generic_web_browser; mindboxDeviceUUID=dab934d2-6502-42d2-b80c-f6d4ffdbc380; directCrm-session=%7B%22deviceGuid%22%3A%22dab934d2-6502-42d2-b80c-f6d4ffdbc380%22%7D; __lhash_=4932d086b946c496b1556d62135c7ae1; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_COOKIE=2500; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_SERVICES=111; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _gid=GA1.2.1816821898.1677763508; _sp_ses.d61c=*; _ym_d=1677763508; _ym_isad=1; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; tmr_lvid=7b0b9a1ffba12350a060192e704a2f75; tmr_lvidTS=1677763511283; flocktory-uuid=8b56bdf5-b410-466f-b928-6cce321d5dfc-6; advcake_track_id=78e67941-3ace-0c3f-cbc0-cafe12a3cf74; advcake_session_id=c0764b6f-8ba4-da39-bd21-34465c9d3a65; AF_SYNC=1677763513107; SL_G_WPT_TO=ru; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; SMSError=; authError=; __hash_=b5c2cb68ad2be85b667852d3c5e743b3; MVID_VIEWED_PRODUCTS=; JSESSIONID=9CNmkQyLMZjfBlMk3sbywNp1PlfCstTHWlNybz9mcLb3sy7J098p!-1256256402; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; flacktory=no; BIGipServeratg-ps-prod_tcp80=1929698314.20480.0000; bIPs=2118529862; MVID_GTM_BROWSER_THEME=1; BIGipServeratg-ps-prod_tcp80_clone=1929698314.20480.0000; deviceType=tablet; CACHE_INDICATOR=true; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UyTgtaImgqO2B/Dzc3VS46bmYJUFJ5fUIVN19OMGELXwhbYSZ/Sy5WRBslJhpQEnU9SnU7GjhmH2RNWyRJWU17FhoXfnIqVQsTXz1BcXobN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueTBCbCNkR1khSV1TdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWyGtg1Q==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UyTgtaImgqO2B/Dzc3VS46bmYJUFJ5fUIVN19OMGELXwhbYSZ/Sy5WRBslJhpQEnU9SnU7GjhmH2RNWyRJWU17FhoXfnIqVQsTXz1BcXobN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueTBCbCNkR1khSV1TdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRIWyGtg1Q==; cfidsgib-w-mvideo=0i6fIfZ6yHzhNtdHZRY2dOd2JaVcWTDrho0XKDpY5lUxmwDaoLjYDQfcVsSYaSlH/c4qZvQ8ijG2+NDTtOBYK3C9tRuP18SPDDgVXcA0OuVfVntbrRnaI1avbYHHURnDtwqANr4zbqYDEtzq2ry/zqEVDyWuJQBN2PfYSA==; cfidsgib-w-mvideo=0i6fIfZ6yHzhNtdHZRY2dOd2JaVcWTDrho0XKDpY5lUxmwDaoLjYDQfcVsSYaSlH/c4qZvQ8ijG2+NDTtOBYK3C9tRuP18SPDDgVXcA0OuVfVntbrRnaI1avbYHHURnDtwqANr4zbqYDEtzq2ry/zqEVDyWuJQBN2PfYSA==; gsscgib-w-mvideo=BSGFTQplYzkZPxslc8NdYbkxBddemQQa2aFlPf91L4JM48LvbjwVrzROQEhZbXop4EsG5jDB/kFjknwhjqINTaXfV6OrV7rB5UzqeveEi4iRiWPABVlFTK0fPznG00w7RmeYM6d1BHkuOluZC12BhlQcEP7Bcmn4MXVue4/NtraLnj6k99exMg2z8/XOaS9t8KFqkDNZ3eeqhRP1qyjwTI2ILGOAqwRMBs/eXwXVeSMRgPWEuHaFAghjMflrsQ==; gsscgib-w-mvideo=BSGFTQplYzkZPxslc8NdYbkxBddemQQa2aFlPf91L4JM48LvbjwVrzROQEhZbXop4EsG5jDB/kFjknwhjqINTaXfV6OrV7rB5UzqeveEi4iRiWPABVlFTK0fPznG00w7RmeYM6d1BHkuOluZC12BhlQcEP7Bcmn4MXVue4/NtraLnj6k99exMg2z8/XOaS9t8KFqkDNZ3eeqhRP1qyjwTI2ILGOAqwRMBs/eXwXVeSMRgPWEuHaFAghjMflrsQ==; fgsscgib-w-mvideo=jzJqd93cd335af0bfca395f0d0a8e81830542398; fgsscgib-w-mvideo=jzJqd93cd335af0bfca395f0d0a8e81830542398; cfidsgib-w-mvideo=YOgtWRXgIyV0qZ5NST5Um1uwCwtCB6a2n+t6bjkKt5BxaoTkexbSukxyCBSRFW260kSxPcZZXzRam6jmX1oMMwPNhh6UI9i1bAneaeKSV2X5ry/S2VIrb6jRu7rgiSBNOiWPk8RO0yTmzUR/9s+kaLKNMbVRFrRdmKr1TA==; _dc_gtm_UA-1873769-1=1; _sp_id.d61c=edd4b65b-e04c-4121-ad13-8f34ae38f36b.1677763508.1.1677765142..2a1d22cb-bdad-40c5-83f7-d1eee8dc6dda..55753977-6ac8-4d8f-9cb3-9033930c2c1b.1677763508142.90; _ga=GA1.2.118058747.1648798750; _dc_gtm_UA-1873769-37=1; tmr_detect=1%7C1677765145781; MVID_ENVCLOUD=prod2; _ga_CFMZTSS5FM=GS1.1.1677763508.6.1.1677765180.0.0.0; _ga_BNX5WPP3YK=GS1.1.1677763508.6.1.1677765180.18.0.0',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'f67532685c094b45a5ac5f8993ef02f1-92f1402dad55b527-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-set-application-id': 'fcc8240d-c5c9-49e6-ae6c-dd623e4a467a',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers)
    print(response)

def main():
    get_data()

if __name__ == '__main__':
    main()