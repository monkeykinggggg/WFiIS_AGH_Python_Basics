#!/usr/bin/env python3.12
'''
Moduł do wyliczania poprawności numeru karty kredytowej oraz numeru PESEL oraz funkcję do wyliczania średniej wieku osób z pliku.
'''
from datetime import date
import datetime
import logging
import numpy as np

logging.basicConfig(filename = 'modul.log', filemode = 'w', format = '%(asctime)s %(message)s', level = logging.INFO)
logger = logging.getLogger()


def check_card_number(card_number):
    '''
    params:
    card_number: str consisting of digits
    returns:
    bool stating whether card number is correct or not in accordance with Luhn algorithm
    '''
    logger.info(f'Wywołanie funkcji check_card_number na numerze: {card_number}')
    if card_number.isdigit() and len(card_number)==16:
        suma = sum(int(el) if not idx%2 else (2*int(el) if 2*int(el)<10 else 2*int(el)-9) for idx,el in zip(range(15,-1,-1),card_number))
        logger.info(f'Wyliczono sumę kontrolną z karty: {suma}')
        return suma%10==0
    else:
        logger.error(f'Niepoprawny podany numer karty: {card_number}')
        raise ValueError('Niepoprawny numer karty: musi być string o długości 16')
   
def check_pesel(pesel, data_urodzenia, plec):
    '''
    params:
    pesel: str consisting of digits
    data_urodzenia: datetime.date type object
    plec: 'M' or 'F' string
    returns:
    bool stating whether pesel is correct or not
    '''
    logger.info(f'Wywołanie funkcji check_pesel na numerze: {pesel}')
    if not pesel.isdigit() or len(pesel)!=11:
        logger.error(f'Niepoprawny podany numer PESEL: {pesel}')
        raise ValueError('Niepoprawny numer PESEL: musi być string o długości 11')
    
    year_from_pesel = int(pesel[:2]) 
    month_from_pesel = int(pesel[2:4])
    day_from_pesel = int(pesel[4:6])
    
    if month_from_pesel>=1 and month_from_pesel<=12:
        century = 1900
    elif month_from_pesel>=21 and month_from_pesel<=32:
        century = 2000
        month_from_pesel -= 20
    elif month_from_pesel>=41 and month_from_pesel<=52:
        century = 2100
        month_from_pesel -= 40
    elif month_from_pesel>=61 and month_from_pesel<=72:
        century = 2200
        month_from_pesel -= 60
    elif month_from_pesel>=81 and month_from_pesel<=92:
        century = 1800
        month_from_pesel -= 80
    else:
        logger.error(f'Niepoprawnie zakodowany miesiac w PESELu')
        raise ValueError('Niepoprawnie zakodowany miesiac w PESELu')
    
    if date(century+year_from_pesel, month_from_pesel, day_from_pesel) == data_urodzenia:
        gender_digit = int(pesel[9])
        if (plec == 'F' and gender_digit%2==0) or (plec == 'M' and gender_digit%2==1):
            wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            check_sum_assessed = (10-sum(w*int(el) for w, el in zip(wagi,pesel))%10)%10
            if check_sum_assessed == int(pesel[10]):
                logger.info(f'Pesel {pesel} przeszedł weryfikację')
                return True      

    logger.info(f'Pesel {pesel} nie przeszedł weryfikacji')
    return False

def czy_rok_przestepny(rok):
    return (rok%4 == 0 and rok%100!=0) or (rok%400==0)
    

def get_average_from_file(filename, mode = 'liberalny'):
    '''
    Pobiera nazwe pliku, na podstawie którego chcemy wyciągnąć średnią wieku i dodatkowo tryb przeszukiwania wartości
    Zwraca średnią wieku osób z pliku w formie ilości dni
    '''
    logger.info(f'Wywołanie funkcji get_average_from_file na pliku: {filename}')
    today = datetime.date.today()
    ages = []
    
    with open(filename) as f:
        lines = f.readlines()   # D M Y
        if mode == 'liberalny':
            dates = [line.split() for line in lines if len(line.split()) == 3]
            for i, data in enumerate(dates):
                try:
                    day = int(data[0])
                    month = int(data[1])
                    year = int(data[2])
                    
                    if not (day>=1 and day<=31 and month>=1 and month<=12 and year>=1900 and year<=today.year):
                        logger.info(f'Zignorowano datę niepoprawną: {data}')
                        continue
                        
                    if month == 2:
                        if (czy_rok_przestepny(year) and day>29) or (not czy_rok_przestepny(year) and day>28):
                            logger.info(f'Zignorowano datę niepoprawną: {data}')
                            continue

                    if month in [4, 6, 9, 11] and day>30:
                        logger.info(f'Zignorowano datę niepoprawną: {data}')
                        continue    
                        
                    ages.append((today - datetime.date(year, month, day)).days)  
                      
                except Exception as e:
                    print(f'{e}')
                
            return round(np.average(ages)/365)
        
        elif mode  == 'restrykcyjny':
            dates = []
            for line in f.readlines():
                if len(line.split())!=3:
                    raise ValueError(f'Niepoprawny format daty, linijka: {line}')
                dates.append(line.split())
            for i, data in enumerate(dates):
                # tutaj nie uzywamy try, chcemy żeby wyjątki się wyrzuciły
                day = int(data[0])
                month = int(data[1])
                year = int(data[2])
                
                if not (day>=1 and day<=31 and month>=1 and month<=12 and year>=1900 and year<=today.year):
                    raise ValueError(f'Bląd w linijce {i}, niepoprawna data: {data}')
                    
                if month == 2:
                    if (czy_rok_przestepny(year) and day>29) or (not czy_rok_przestepny(year) and day>28):
                        raise ValueError(f'Bląd w linijce {i}, niepoprawna data: {data}')

                if month in [4, 6, 9, 11] and day>30:
                    raise ValueError(f'Bląd w linijce {i}, niepoprawna data: {data}')
                    
                ages.append((today - datetime.date(year, month, day)).days)  
                
            if not ages:  
                raise ValueError('Lista lat jest pusta')  
            else:
                return round(np.average(ages)/365)
                    
        else:
            logger.error(f'Niepoprawny tryb działania. Podano: {mode}')
            raise ValueError('Podano niepoprawny tryb działania. Do wyboru: restrykcyjny, liberalny')
        
       
        
if __name__=='__main__':
    pass