import requests
from dotenv import load_dotenv
from requests.exceptions import HTTPError
from urllib.parse import urlparse
import os
import argparse

def shorten_link(headers, long_url):
    params = {
        "long_url": long_url
    }
    response = requests.post("https://api-ssl.bitly.com/v4/shorten/", headers=headers, json=params)
    response.raise_for_status()  
    return response.json()['link']  


def count_clicks(headers,link):
    bit_url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary"  
    response = requests.get(bit_url, headers=headers)
    return response.json()["total_clicks"]


def is_bitlink(headers, url):
    bit_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    response = requests.get(bit_url, headers = headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    headers = {
        "Authorization": f"Bearer {bitly_token}",    
    }
    parser = argparse.ArgumentParser(description='Сокращаем ссылки на bitly')
    parser.add_argument('link', help='Введите ссылку')
    args = parser.parse_args()
    print(args.link)
    
    parsed_url = urlparse(args.link)
    combined_path = f"{parsed_url.netloc}{parsed_url.path}"
    try:
        if is_bitlink(headers, combined_path):
            print(count_clicks(headers, combined_path))
        else:
            print(shorten_link(headers, args.link))
    except HTTPError as error:
        print("Неправильная ссылка", error)


if __name__ == "__main__":
    main()
    