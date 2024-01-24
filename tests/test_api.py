import requests
import allure
import pytest_check as check
import time
import json


@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Получение главной страницы методом GET")
@allure.tag("API", "GET")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Tatsiana Malahova")
@allure.link("https://zalando.pl/", name="Zalando")
def test_get_main_page():
    url = "https://zalando.pl/"

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    time_start = time.time()

    response = requests.request("GET", url, headers=headers, data=payload)

    time_end = time.time()
    time_loud = time_end - time_start

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200, 'Неверый статус код')

    with allure.step('Проверка времени ответа страницы'):
        check.greater_equal(time_loud, 0, 'Время ответа страницы меньше нуля')

    with allure.step('Проверка наличия Content-Type в headers'):
        check.is_in(response.headers["Content-Type"], "text/html; charset=utf-8")

    with allure.step('Проверка,что метод GET'):
        print(response.request.method)
        check.equal(response.request.method, 'GET')


@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Добавление отсутствуеющего продукта в корзину методом POST")
@allure.tag("API", "POST")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Tatsiana Malahova")
@allure.link("https://zalando.pl/", name="Zalando")
def test_add_to_cart():
    url = "https://www.zalando.pl/api/graphql/add-to-cart/"

    payload = json.dumps([
        {
            "id": "wrong_id",
            "variables": {
                "addToCartInput": {
                    "productId": "wrong_id",
                    "clientMutationId": "addToCartMutation"
                }
            }
        }
    ])

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200, 'Неверный статус код')

    with allure.step('Проверка параметра errors'):
        res = response.json()
        check.equal(res[0]["errors"][0]["message"], 'Persisted Query "wrong_id" NOT FOUND')


@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Авторизация методом POST")
@allure.tag("API", "POST")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Tatsiana Malahova")
@allure.link("https://zalando.pl/", name="Zalando")
def test_authorization():
    url = "https://accounts.zalando.com/api/login"

    payload = json.dumps({
        "email": "spgwwnlsdcwzayrvof@cwmxc.com",
        "secret": "3bbe38c9-32b8-404f-a71d-d780af48e787",
        "request": {
            "redirect_uri": "https://www.zalando.pl/sso/callback",
            "client_id": "fashion-store-web",
            "response_type": "code",
            "scope": "openid",
            "request_id": "huxhXKGKfRBlvUAc:105aaa5e-545c-459b-9206-9f47e66f8aab:huxhXKGKfRBlvUAc",
            "nonce": "3bbe38c9-32b8-404f-a71d-d780af48e787",
            "state": "eyJvcmlnaW5hbF9yZXF1ZXN0X3VyaSI6Ii8iLCJ0cyI6IjIwMjQtMDEtMjRUMTk6MTg6NDZaIn0=",
            "ui_locales": "pl-PL",
            "zalando_client_id": "105aaa5e-545c-459b-9206-9f47e66f8aab",
            "sales_channel": "ca9d5f22-2a1b-4799-b3b7-83f47c191489",
            "client_country": "PL",
            "client_category": "fs"
        }
    })
    headers = {
        'authority': 'accounts.zalando.com',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://accounts.zalando.com',
        'referer': 'https://accounts.zalando.com/authenticate?redirect_uri=https://www.zalando.pl/sso/callback&client_id=fashion-store-web&response_type=code&scope=openid&request_id=huxhXKGKfRBlvUAc:105aaa5e-545c-459b-9206-9f47e66f8aab:huxhXKGKfRBlvUAc&nonce=3bbe38c9-32b8-404f-a71d-d780af48e787&state=eyJvcmlnaW5hbF9yZXF1ZXN0X3VyaSI6Ii8iLCJ0cyI6IjIwMjQtMDEtMjRUMTk6MTg6NDZaIn0=&ui_locales=pl-PL&zalando_client_id=105aaa5e-545c-459b-9206-9f47e66f8aab&sales_channel=ca9d5f22-2a1b-4799-b3b7-83f47c191489&client_country=PL&client_category=fs',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-csrf-token': '3d8f5854-012d-4e4c-bdf8-ab9dbb10bf87',
        'x-flow-id': 'bj7zu0nuv5hgWwxu',
        'x-zalando-username': 'spgwwnlsdcwzayrvof@cwmxc.com'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 403, 'Неверный статус код')


@allure.suite("Test API")
@allure.story("Test API")
@allure.description("Подписка на новости методом POST")
@allure.tag("API", "POST")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Tatsiana Malahova")
@allure.link("https://zalando.pl/", name="Zalando")
def test_newsletter():
    url = "https://www.zalando.pl/api/graphql/"

    payload = json.dumps([
        {
            "id": "06fe5b50b4218612aa3fa8494df326aef7ff35a75a8563b3455bb53c15168872",
            "variables": {
                "input": {
                    "email": "spgwwnlsdcwzayrvof@cwmxc.com",
                    "preference": {
                        "category": "WOMEN",
                        "topics": [
                            {
                                "id": "item_alerts",
                                "isEnabled": True
                            },
                            {
                                "id": "recommendations",
                                "isEnabled": True
                            },
                            {
                                "id": "follow_brand",
                                "isEnabled": True
                            },
                            {
                                "id": "subscription_confirmations",
                                "isEnabled": True
                            },
                            {
                                "id": "stories",
                                "isEnabled": True
                            },
                            {
                                "id": "offers_sales",
                                "isEnabled": True
                            },
                            {
                                "id": "fashion_fix",
                                "isEnabled": True
                            },
                            {
                                "id": "survey",
                                "isEnabled": True
                            }
                        ]
                    },
                    "referrer": "nl_subscription_banner_one_click",
                    "clientMutationId": "1706125274340"
                }
            }
        }
    ])
    headers = {
        'content-type': 'application/json',
        'origin': 'https://www.zalando.pl',
        'referer': 'https://www.zalando.pl/faq/Wysylka-i-dostawa/Czy-dostawa-i-zwrot-cos-kosztuja.html',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    with allure.step('Проверка статус кода'):
        check.equal(response.status_code, 200, 'Неверный статус код')
    with allure.step("Проверка подтверждения подписки"):
        res = response.json()
        email = res[0]["data"]["subscribeToNewsletter"]["email"]
        isEmailVerificationRequired = res[0]["data"]["subscribeToNewsletter"]["isEmailVerificationRequired"]

        check.equal(email, "spgwwnlsdcwzayrvof@cwmxc.com", 'Неверный email')
        check.equal(isEmailVerificationRequired, True, 'Неверное значение isEmailVerificationRequired')