from BATO_RESULT import BatoResult
import asyncio

def download_image(link: str, filepath: str, filename: str, file_format: str):
    return download_image_from_link(link, filepath, filename, file_format)



def download_image_from_link(link: str, filepath: str, filename: str, file_format: str):
    import requests

    r = requests.get(link)

    if r.status_code != 200:
        return False
    if r.content == b'':
        return False
    
    with open(f"{filepath}/{filename}.{file_format}", 'wb') as f:
        f.write(r.content)
    
    return True