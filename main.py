import os
import argparse
import requests
from dotenv import load_dotenv


load_dotenv()

def parsing_url():
    parser = argparse.ArgumentParser(
        description='Скрипт сокращает передаваемую в аргументах командной строки ссылку.\
                     При передачи уже сокращенной ссылки, скрипт выводит количество переходов по ссылке.'
    )
    parser.add_argument('link', help='Ссылка для сокращения, либо сокращенная ссылка')
    args = parser.parse_args()

    return args.link

def shorten_link(token, url, long_url):
  headers = {
    'Authorization': 'Bearer {token}'.format(token=token)
  }
  payload = {
    'long_url': long_url
  }

  response = requests.post(url,
                          headers=headers,
                          json=payload)
  response.raise_for_status()

  bitlink = response.json()['link']

  return bitlink

def count_clicks(token, link):
  headers = {
    'Authorization': 'Bearer {token}'.format(token=token)
  }
  payload = {
    'unit': 'day',
    'units': -1
  }

  response = requests.get(link,
                          headers=headers, params=payload)
  response.raise_for_status()

  clicks_count = response.json()['total_clicks']

  return clicks_count

if __name__=='__main__':
  token = os.getenv('BITLY_TOKEN')
  url = 'https://api-ssl.bitly.com/v4/shorten'
  long_url = parsing_url()

  if long_url.startswith('http://bit.ly/') or long_url.startswith('https://bit.ly/') or long_url.startswith('bit.ly/'):
    try:
      bitlink_id = long_url.split('/')[-1]
      link = 'https://api-ssl.bitly.com/v4/bitlinks/bit.ly/{bitlink}/clicks/summary'.format(bitlink=bitlink_id)
      clicks_count = count_clicks(token, link)
      print('По вашей ссылке прошли {} раз(а)'.format(clicks_count))
    except requests.exceptions.HTTPError as Error:
      clicks_count = Error
      print('Ошибка! Перепроверьте ссылку или права доступа\n' + str(Error))

  else:
    try:
      bitlink = shorten_link(token, url, long_url)
      print('Битлинк', bitlink)
    except requests.exceptions.HTTPError as Error:
      bitlink = Error
      print('Ошибка! Перепроверьте ссылку или права доступа\n' + str(Error))
