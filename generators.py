import random
import re

from colorama import Fore
from Provinces_Codes import *

const = '00'

number_code = random.randint(10, 99)
ID_code = random.randint(1000000, 9999999)

def generate_BI_Number():
    try:
        value = list(province_code.values())
        for values in value:
            code = "".join(random.sample(value, 1))
        BI_generated = f'{const}{ID_code}{code}{const[0:1]}{number_code}'    
        return BI_generated
    except:
        print('Aconteceu um erro não programável! Tente Novamente. [!]')

def province_choosed(code: int):
    try:
        provinces = list(province_code.items())
        return provinces[code][0]
    except:
        print('Aconteceu um erro não programável! Tente Novamente. [!]')



def generate_per_province(code: int):
    try:
        keys = list(province_code.items())
        for count in range(18):
            if province_choosed(code) in keys[count][0]:
                Province_code = keys[count][1]
                BI_generated = f'{const}{ID_code}{Province_code}{const[0:1]}{number_code}'    
                print(BI_generated)      
    except:
        print('Aconteceu um erro não programável! Tente Novamente. [!]')


def validator(BI: str):
    try:
        BI_pattern = re.compile(r'^\d{9}[A-Z]{2}\d{3}$')
        search_pattern = BI_pattern.search(BI)

        if search_pattern:
            print(f'{Fore.GREEN}[!] BI VÁLIDO [!]')
        else:
            print(f'{Fore.RED}[!] BI INVÁLIDO [!]')
    except:
        print("[!] Aconteceu um erro não programável! Tente Novamente.")
