from generators import *
from colorama import *
init(autoreset=True)


print(f"""{Fore.GREEN}
        ----------------------------
        |  BI NUMBER GENERATOR 1.0 |
        ----------------------------
        |           MENU           |
        ----------------------------
        | [0] - GERAR BI ALEATÓRIO |
        | [1] - GERAR POR PROVÍN.  |
        | [2] - SAIR               |
        ----------------------------
    """)

choose = int(input('> '))

if(choose == 0):
    try:
        while True:
            print(f'BI NUMBER: {generate_BI_Number()}')
            print('|----------------------|')
            print('|DESEJA CONTINUAR? [S/N]:')
            print('|----------------------|')
            answer = str(input('>: ')).strip()[0].upper()
            if answer != 'S':
                break
    except:
        print('Aconteceu um erro não programável! Tente Novamente [!]')
if(choose == 1):
    print("""
    
    -------------------------------
    |CHOOSE A PROVINCE TO GENERATE|
    -------------------------------
    |[0]| - Luanda
    |[1]|- Bengo
    |[2]| - Kwanza-Norte
    |[3]|- Kwanza-Sul
    |[4]| - Uíge
    |[5]| - Zaíre
    |[6]| - Malanje
    |[7]| - Lunda-Sul
    |[8]| - Lunda-Norte
    |[9]| - Moxico
    |[10| - Kuando Kubango
    |[11| - Cunene
    |[12| - Huíla
    |[13| - Huambo
    |[14| - Benguela
    |[15| - Namibe
    |[16| - Bié
    |[17| - Cabinda
    """)
    Code_Province = int(input('>: '))
    generate_per_province(Code_Province)
if(choose == 2):
    print(f'{Fore.BLUE}By: Sílvio Silva [!]')