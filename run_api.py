import requests

def run_api(url: str, params: dict):
    """APIのresponseをjsonで返す"""
    res = requests.get(url, params)
    return res.json()