import pytest_check as check
import time
import allure
import requests
import json


@allure.story('Проверка статус кода')
@allure.feature('Проверка статус кода "onliner.by" ')
def test_api_1():
    url = "https://www.onliner.by/"

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'stid=f86992f5d1b167df80a0863689bf4951b2c0fe81f7437d4a7d372b6b6e635444; ouid=snyBDGWBx51rsDz+OhvhAg==; ADC_REQ_2E94AF76E7=679A40EEE4EFD533A5FFF5FE8A4D841CC5A50786EEBCD0B5E158E8231462D4C2E44407BE2561A8E8; stid=728c1659389c85b65aa171d5347b0f1dd36d87ae57d8cf3bdd59a0a1bec83829; ADC_REQ_2E94AF76E7=99C0A5134D9CD09D5B6243AA8FCB0A740C43CF51F591B71ABD6326CC286325A95EFAD33AA77B27C3; ouid=snyBDmWB085mX0LrOmfIAg==',
        'Referer': 'https://www.onliner.by/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    time_start = time.time()

    response = requests.request("GET", url, headers=headers, data=payload, timeout=10)
    time_end = time.time()
    time_loud = time_end - time_start
    print(f"The loading time for the website {url} is {time_loud} seconds")
    with allure.step("Проверка времени"):
        check.greater_equal(1, time_loud)

    assert response.status_code == 200

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200, 'Неверный статус код')

    with allure.step('Проверка времени ответа страницы'):
        check.greater_equal(time_loud, 0, 'Неверный статус код')

    with allure.step('Проверка времени ответа страницы'):
        check.is_in(response.headers["Content-Type"], "text/html; charset=utf-8")

    print(response.headers.values())
    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'

    with allure.step('Добавить attuch'):
        allure.attach('Remove error', response.text, attachment_type=allure.attachment_type.TEXT)

    with allure.step('Проверка, что метод GET'):
        print(response.request.method)
        check.not_equal(response.request.method, 'POST')

    # with allure.step('Проверка, ):


@allure.story('Проверка статус кода')
@allure.feature('Проверка статус кода "onliner.by" ')
def test_api_2():
    url = "https://catalog.onliner.by/api/seo"

    payload = json.dumps({
        "url": "https://catalog.onliner.by/headphones?shops%5B0%5D=20693&shops%5Boperation%5D=union"
    })
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'stid=f86992f5d1b167df80a0863689bf4951b2c0fe81f7437d4a7d372b6b6e635444; ouid=snyBDGT94pQNtfv+ElNmAg==; catalog_session=JLdTBd0w0OGZzV66U9oMLXsfd5mRdPXUjElpVCkf; ADC_REQ_2E94AF76E7=1F55A1EFAA6B3733FB0781F10A022EC1EEF32C1D5A1120C9DECF60878B51F471330B156818B2A2C7; stid=728c1659389c85b65aa171d5347b0f1dd36d87ae57d8cf3bdd59a0a1bec83829',
        'Origin': 'https://catalog.onliner.by',
        'Referer': 'https://catalog.onliner.by/headphones?shops%5B0%5D=20693&shops%5Boperation%5D=union',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.post(url, headers=headers, data=payload, timeout=10)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200, 'Неверный статус код')

    with allure.step('Проверка параметра errors'):
        print(response.text)
        a = (response.text)
        b = a.find('Unprocessable Content')
        check.not_equal(b, 36)
