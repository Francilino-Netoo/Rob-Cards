from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pyautogui
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

chrome_options = Options()
# chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options=chrome_options)
# nav.get('https://blaze.com/pt/games/double')


bot = telebot.TeleBot('Token') #Aqui você vai adicinar o token gerado quando você cria um bot do telegram
user_id = -0000000000 # Você deve usar o ID do seu canal do telegram

nav.get('https://m.b1.bet/#/auth/login')

time.sleep(3)
usuario_text = nav.find_element(By.XPATH, '/html/body/app/div/ng-component/div[3]/form[1]/input[1]')
time.sleep(2)
usuario_text.send_keys('Robo') # O usuário na hora de fazer o login
time.sleep(1)
text_senha = nav.find_element(By.XPATH, '/html/body/app/div/ng-component/div[3]/form[1]/input[2]')
time.sleep(2)
text_senha.send_keys('Robozin 123') # Sua senha para efetuar o login
time.sleep(1)
pyautogui.press('enter')
# time.sleep(5)
# pyautogui.moveTo(938, 703)
# pyautogui.click()
# time.sleep(1)
# pyautogui.click()

# cassino_ao = nav.find_element(By.XPATH, '/html/body/app/div/ng-component/content/div/div[3]/ul/li[3]/div').click()
# time.sleep(2)
# evolution = nav.find_element(By.XPATH, '/html/body/app/div/ng-component/div/div[1]/div[2]/div/i').click()
# time.sleep(2)
# pyautogui.moveTo(938, 703)
# pyautogui.click()
# time.sleep(2)
# pyautogui.click()
# time.sleep(2)
# pyautogui.click()
# time.sleep(2)

# pyautogui.moveTo(171, 785)
# pyautogui.click()


time.sleep(60)


def BUTTON_LINK():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(text='🤑👉❗APOSTE AQUI❗👈🤑',url='https://dpg.evo-games.com/frontend/evo/r3/#provider=evolution&vt_id=p4giis2jqyeabxao&ua_launch_id=1720ce4fe9d0f3cbf3717926&table_id=TopCard000000001&game=topcard'))
    return markup


def tempo():
    time.sleep(12)

def tempo1():
    time.sleep(4)

#elif nav.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[10]/div[2]') == True:
#nav.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[10]/div[1]/button')


def pegar_numero_cor(na):
    while True:
        time.sleep(1)
        na = na
        c = na.page_source
        soup = BeautifulSoup(c, 'html.parser')
        dat = soup.find('div', class_="gameResult--982ee")
        valor = dat.text.split()
        if valor == ['CASA']:
            return valor
        elif valor == ['VISITANTE']:
            return valor
        elif valor == ['EMPATE']:
            return valor


def estrategia(nu):
    possivel_sn = [['p', 'p', 'p', 'p'], ['v', 'v', 'v', 'v'], ['p', 'v', 'p'], ['v', 'p', 'v']]
    for i in possivel_sn:
        if nu == i:
            return 'sinal'

    ##############  PRETA ################
    preta = [['v', 'v', 'v', 'v', 'v'], ['p', 'v', 'p', 'v']]
    for i in preta:
        if nu == i:
            return 'preta'

    # /............gale preta.......................

    gale1_preta = [['v', 'v', 'v', 'v', 'v', 'v'], ['p', 'v', 'p', 'v', 'v']]
    for i in gale1_preta:
        if nu == i:
            return 'gale1_preta'

    gale2_preta = [['v', 'v', 'v', 'v', 'v', 'v', 'v'], ['p', 'v', 'p', 'v', 'v', 'v']]
    for i in gale2_preta:
        if nu == i:
            return 'gale2_preta'

    # /...................... GREEN PRETO#########################

    gren_preto = [['v', 'v', 'v', 'v', 'v', 'p'], ['p', 'v', 'p', 'v', 'p']]
    for i in gren_preto:
        if nu == i:
            return 'green_preto'

    gren_preto = [['v', 'v', 'v', 'v', 'v', 'v', 'v', 'p'],['p', 'v', 'p', 'v', 'v', 'p'], ['p', 'v', 'p', 'v', 'v', 'v', 'p']]
    for i in gren_preto:
        if nu == i:
            return 'green_preto1'

    gren_preto = [['v', 'v', 'v', 'v', 'v', 'v', 'v', 'p'], ['p', 'v', 'p', 'v', 'v', 'v', 'v', 'p']]
    for i in gren_preto:
        if nu == i:
            return 'green_preto2'

    vermelha = [['p', 'p', 'p', 'p', 'p'], ['v', 'p', 'v', 'p']]
    for i in vermelha:
        if nu == i:
            return 'vermelha'

    # /............gale vermelhor.......................

    gale1_vermelha = [['p', 'p', 'p', 'p', 'p', 'p'], ['v', 'p', 'v', 'p', 'p']]
    for i in gale1_vermelha:
        if nu == i:
            return 'gale1_vermelha'

    gale2_vermelha = [['p', 'p', 'p', 'p', 'p', 'p', 'p'], ['v', 'p', 'v', 'p', 'p', 'p']]
    for i in gale2_vermelha:
        if nu == i:
            return 'gale2_vermelha'

    # /...................... GREEN vermelho

    green_vermelho = [['p', 'p', 'p', 'p', 'p', 'v'], ['v', 'p', 'v', 'p', 'v']]
    for i in green_vermelho:
        if nu == i:
            return 'green_vermelho'

    green_vermelho = [['p', 'p', 'p', 'p', 'p', 'p', 'v'], ['v', 'p', 'v', 'p', 'p', 'v']]
    for i in green_vermelho:
        if nu == i:
            return 'green_vermelho1'

    green_vermelho = [['p', 'p', 'p', 'p', 'p', 'p', 'p', 'v'], ['v', 'p', 'v', 'p', 'p', 'p', 'v']]
    for i in green_vermelho:
        if nu == i:
            return 'green_vermelho2'

    ############### nova estrategia #############3

    branca = [['v', 'v', 'v', 'v', 'v', 'b'], ['p', 'v', 'p', 'v', 'b'], ['v', 'v', 'v', 'v', 'v', 'v', 'v', 'b'],
              ['p', 'v', 'p', 'v', 'v', 'v', 'b'], ['v', 'v', 'v', 'v', 'v', 'v', 'v', 'b'],
              ['p', 'v', 'p', 'v', 'v', 'v', 'v', 'b'], ['p', 'p', 'p', 'p', 'p', 'b'], ['v', 'p', 'v', 'p', 'b'],
              ['p', 'p', 'p', 'p', 'p', 'p', 'b'], ['v', 'p', 'v', 'p', 'p', 'b'],
              ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'], ['v', 'p', 'v', 'p', 'p', 'p', 'b']]
    for i in branca:
        if nu == i:
            return 'branco_green'

    # /............... limpeza
    red = [['v', 'v', 'v', 'v', 'v', 'v', 'v', 'v'], ['p', 'v', 'p', 'v', 'v', 'v', 'v'],
           ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], ['v', 'p', 'v', 'p', 'p', 'p', 'p']]
    for i in red:
        if nu == i:
            return 'red'

    limm = [['v', 'v', 'b'], ['p', 'p', 'b'], ['v', 'v', 'p', 'b'], ['v', 'b'], ['p', 'b'], ['b'],
            ['v', 'p', 'p', 'p', 'b'], ['v', 'p', 'p', 'b'], ['v', 'v', 'b'], ['p', 'v', 'v', 'b'],
            ['v', 'v', 'v', 'v', 'v', 'v', 'p', 'b'], ['v', 'p', 'v', 'b'], ['v', 'p', 'b'], ['v', 'v', 'v', 'b'],
            ['p', 'p', 'b'], ['p', 'v', 'b'], ['p', 'p', 'p', 'b'], ['v', 'b'], ['p', 'b'], ['b'], ['v', 'v', 'v', 'b'],
            ['p', 'v', 'p', 'b'], ['v', 'v', 'v', 'v', 'b'], ['p', 'v', 'p', 'v', 'b'], ['v', 'p', 'v', 'p', 'b'],
            ['p', 'p', 'p', 'p', 'b'], ['v', 'v', 'v', 'v', 'v', 'b'], ['v', 'p', 'v', 'p', 'v', 'b'],
            ['p', 'p', 'p', 'p', 'p', 'b'], ['p', 'v', 'p', 'v', 'p', 'b'], ['v', 'v', 'v', 'v', 'v', 'v', 'b'],
            ['v', 'p', 'v', 'p', 'v', 'v', 'b'], ['v', 'v', 'v', 'v', 'v', 'v', 'v', 'b'],
            ['v', 'p', 'v', 'p', 'v', 'v', 'v', 'b'], ['v', 'v', 'v', 'v', 'v', 'v', 'v', 'v', 'b'],
            ['v', 'p', 'v', 'p', 'v', 'v', 'v', 'v', 'b'], ['p', 'p', 'p', 'p', 'p', 'b'],
            ['p', 'v', 'p', 'v', 'p', 'b'], ['p', 'p', 'p', 'p', 'p', 'p', 'b'], ['p', 'v', 'p', 'v', 'p', 'p', 'b'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'], ['p', 'v', 'p', 'v', 'p', 'p', 'p', 'b'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'], ['p', 'v', 'p', 'v', 'p', 'p', 'p', 'p', 'b']]
    for i in limm:
        if nu == i:
            return ('limpar')

    if len(nu) > 9:
        return ('limpar')

    # /.............  limpeza parcial

    l0 = [['p', 'p', 'p', 'p', 'v'],['v', 'v', 'v', 'v', 'p'], ['p', 'v', 'p', 'p'], ['v', 'p', 'v', 'v']]
    for i in l0:
        if nu == i:
            msg = f'''❗❗❗NÃO CONFIRMOU❗❗❗'''
            message_ids = bot.send_message(user_id, msg).message_id
            tempo()
            bot.delete_message(user_id, message_ids, timeout=8000)
            del (lista_cor[0:2])

    l0 = [['p', 'p', 'p','p', 'b'], ['v', 'v', 'v', 'v','b'], ['p', 'v', 'p', 'b'], ['v', 'p', 'v', 'b']]
    for i in l0:
        if nu == i:
            msg = f'''❗❗❗NÃO CONFIRMOU❗❗❗\n'''
            message_ids = bot.send_message(user_id, msg).message_id
            tempo()
            bot.delete_message(user_id, message_ids, timeout=8000)
            lista_cor.clear()

    l0 = [['p', 'p', 'p', 'p', 'v', 'v'], ['p', 'p', 'p', 'p', 'v', 'p'], ['v', 'v', 'v', 'v', 'p', 'v'],['v', 'v', 'v', 'v', 'p', 'p'], ['p', 'v', 'p', 'v', 'v', 'v'], ['p', 'v', 'p', 'v', 'v', 'p'],['v', 'p', 'v', 'p', 'p', 'v'], ['v', 'p', 'v', 'p', 'p', 'p']]
    for i in l0:
        if nu == i:
            return 3

    l1 = [['v', 'v', 'v', 'p'],['p', 'p', 'p', 'v']]
    for i in l1:
        if nu == i:
            return 2

    l1 = [['v', 'v', 'p'], ['p', 'p', 'v'], ['v', 'p', 'p'], ['p', 'v', 'v']]
    for i in l1:
        if nu == i:
            return 1

    l4 = [['v', 'v', 'v', 'v', 'p'], ['p', 'p', 'p', 'p', 'v'], ['v', 'p', 'v', 'p', 'v'], ['p', 'v', 'p', 'v', 'p']]
    for i in l4:
        if nu == i:
            return 3

    l5 = [['v', 'v', 'v', 'v', 'v', 'p'], ['p', 'p', 'p', 'p', 'p', 'p', 'v'], ['p', 'p', 'p', 'p', 'p', 'v'],['v', 'p', 'v', 'p', 'v', 'p']]
    for i in l5:
        if nu == i:
            return 4

    l6 = [['v', 'v', 'v', 'v', 'v', 'v', 'p'], ['v', 'p', 'v', 'p', 'v', 'v', 'p'], ['p', 'p', 'p', 'p', 'p', 'p', 'v'],['v', 'p', 'v', 'p', 'v', 'v', 'p'], ['p', 'v', 'p', 'v', 'p', 'p', 'v'], ['v', 'v', 'v', 'v', 'v', 'v', 'p']]
    for i in l6:
        if nu == i:
            return 5

    l8 = [['v', 'p', 'v', 'p', 'v', 'v', 'v', 'p'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'v'],['v', 'p', 'v', 'p', 'v', 'v', 'v', 'p'], ['v', 'v', 'v', 'v', 'v', 'v', 'v', 'p']]
    for i in l8:
        if nu == i:
            return 6


def cores(cor):
    numero_cor = cor

    if numero_cor == ['CASA']:
        return ('p')  # c

    elif numero_cor == ['VISITANTE']:
        return ('v')  # v

    elif numero_cor == ['EMPATE']:
        return ('b')  # E


lista_cor = []
greenn = 0
brancoo = 0
redd = 0
consecutivas = 0
assertividade = 0
cont_placar = 0
while True:

    # /............. pegar o numero da roleta
    num = pegar_numero_cor(nav)
    # /............. pegar a cor da roleta

    cor = cores(num)
    # /............. adiciona as cores na lista cor
    if cor == 'p':
        lista_cor.append(cor)
        tempo1()
        pyautogui.moveTo(477, 510)
        pyautogui.click()

    elif cor == 'v':
        lista_cor.append(cor)
        tempo1()
        pyautogui.moveTo(477, 510)
        pyautogui.click()

    elif cor == 'b':
        lista_cor.append(cor)
        tempo1()
        pyautogui.moveTo(477, 510)
        pyautogui.click()


    # /............. retorna a Estratégia
    estrategi = estrategia(lista_cor)
    # /............. mostra a  numero e cor da roleta

    print(lista_cor)

    if estrategi == 'limpar':
        lista_cor.clear()
    # /.............. limpeza parcial

    elif estrategi == 0:
        del (lista_cor[0:estrategi])

    elif estrategi == 1:
        del (lista_cor[0:estrategi])

    elif estrategi == 2:
        del (lista_cor[0:estrategi])

    elif estrategi == 3:
        del (lista_cor[0:estrategi])

    elif estrategi == 0:
        del (lista_cor[0:estrategi])

    elif estrategi == 4:
        del (lista_cor[0:estrategi])

    elif estrategi == 5:
        del (lista_cor[0:estrategi])

    if estrategia(lista_cor) == 'sinal':

        msg = f'''🤓💻❗❗❗ATENÇÃO❗❗❗💻🤓\n\n🤑ANALISANDO POSSIVÉL SINAL🤑'''
        message_ids = bot.send_message(user_id, msg).message_id
        tempo()
        bot.delete_message(user_id, message_ids, timeout=8000)


    elif estrategia(lista_cor) == 'preta':

        msg = f'''APOSTAR NO 👉 🔴🔴🔴\nPROTEÇÃO NO 🟠 É OPCIONAL\n❗❗❗REALIZAR 2 GALES❗❗❗'''
        bot.send_message(user_id, msg, reply_markup=BUTTON_LINK())

        ########################## GREEN PRETA & VERMELHA ########

    elif estrategia(lista_cor) == 'green_preto':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = f'''✅✅✅GREEN✅✅✅'''
        bot.send_message(user_id, msg)
        del (lista_cor[0:4])


    elif estrategia(lista_cor) == 'green_preto1':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = f'''✅✅✅GREEN✅✅✅'''
        bot.send_message(user_id, msg)
        del (lista_cor[0:5])

    elif estrategia(lista_cor) == 'green_preto2':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = f'''✅✅✅GREEN✅✅✅'''
        bot.send_message(user_id, msg)
        del (lista_cor[0:6])

    elif estrategia(lista_cor) == 'green_preto3':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = f'''✅✅✅GREEN✅✅✅'''
        bot.send_message(user_id, msg)
        del (lista_cor[0:7])


    elif estrategia(lista_cor) == 'green_vermelho':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = f'''✅✅✅GREEN✅✅✅'''
        bot.send_message(user_id, msg)
        del (lista_cor[0:4])

    elif estrategia(lista_cor) == 'green_vermelho1':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = f'''✅✅✅GREEN✅✅✅'''
        bot.send_message(user_id, msg)
        del (lista_cor[0:5])

    elif estrategia(lista_cor) == 'green_vermelho2':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = f'''✅✅✅GREEN✅✅✅'''

        bot.send_message(user_id, msg)
        del (lista_cor[0:6])

    elif estrategia(lista_cor) == 'green_vermelho3':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = f'''✅✅✅GREEN✅✅✅'''
        bot.send_message(user_id, msg)
        del (lista_cor[0:7])


    ########################## GREEN PRETA & VERMELHA ########

    elif estrategia(lista_cor) == 'branco_green':

        brancoo += 1
        cont_placar += 1
        consecutivas += 1

        msg = f'''✅🟠🟠✅GREEN✅🟠🟠✅'''
        bot.send_message(user_id, msg)
        lista_cor.clear()

        ############################################

    elif estrategia(lista_cor) == 'green1_preta':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = '''✅✅Grenn Gale 1✅✅'''
        bot.send_message(user_id, msg)

    elif estrategia(lista_cor) == 'gale1_preta':

        msg = '''1ª TENTATIVA'''
        message_ids = bot.send_message(user_id, msg).message_id
        tempo()
        bot.delete_message(user_id, message_ids, timeout=8000)
        #############################################


    elif estrategia(lista_cor) == 'green2_preta':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = '''✅✅Grenn Gale 2✅✅'''
        bot.send_message(user_id, msg)


    elif estrategia(lista_cor) == 'gale2_preta':

        msg = '''2ª TENTATIVA'''
        message_ids = bot.send_message(user_id, msg).message_id
        tempo()
        bot.delete_message(user_id, message_ids, timeout=8000)

        #############################################


    elif estrategia(lista_cor) == 'green3_preta':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = '''✅✅Grenn Gale 3✅✅'''
        bot.send_message(user_id, msg)


    elif estrategia(lista_cor) == 'gale3_preta':

        msg = '''3ª TENTATIVA'''
        message_ids = bot.send_message(user_id, msg).message_id
        tempo()
        bot.delete_message(user_id, message_ids, timeout=8000)


    ################# fim preta ###############################

    elif estrategia(lista_cor) == 'vermelha':

        msg = f'''APOSTAR NO 👉🔵🔵🔵\nPROTEÇÃO NO EMPATE 🟠 É OPCIONAL\n❗❗❗REALIZAR 2 GALES❗❗❗'''
        bot.send_message(user_id, msg, reply_markup=BUTTON_LINK())

        #############################################


    elif estrategia(lista_cor) == 'green1_vermelha':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = '''✅✅Grenn Gale 1✅✅'''
        bot.send_message(user_id, msg)

    elif estrategia(lista_cor) == 'gale1_vermelha':

        msg = '''1ª TENTATIVA'''
        message_ids = bot.send_message(user_id, msg).message_id
        tempo()
        bot.delete_message(user_id, message_ids, timeout=8000)

        #############################################

    elif estrategia(lista_cor) == 'green2_vermelha':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = '''✅✅Grenn Gale 2✅✅'''
        bot.send_message(user_id, msg)


    elif estrategia(lista_cor) == 'gale2_vermelha':

        msg = '''2ª TENTATIVA'''
        message_ids = bot.send_message(user_id, msg).message_id
        tempo()
        bot.delete_message(user_id, message_ids, timeout=8000)

        #############################################

    elif estrategia(lista_cor) == 'green3_vermelha':
        greenn += 1
        cont_placar += 1
        consecutivas += 1

        msg = '''✅✅Grenn Gale 3✅✅'''
        bot.send_message(user_id, msg)

    elif estrategia(lista_cor) == 'gale3_vermelha':

        msg = '''3ª TENTATIVA'''
        message_ids = bot.send_message(user_id, msg).message_id
        tempo()
        bot.delete_message(user_id, message_ids, timeout=8000)



    elif estrategia(lista_cor) == 'red':
        redd += 1
        cont_placar += 1
        consecutivas = 0
        msg = f'''❌❌💔 RED 💔❌❌\n\n😮‍💨RESPIRA FUNDO😮‍💨\n\n🤗ESPERE O PRÓXIMO SINAL🤗\n\n❗NÃO FIQUE DESESPERADO❗'''
        bot.send_message(user_id, msg)
        lista_cor.clear()


    if cont_placar > 0:
        g = greenn + brancoo
        t = greenn + brancoo + redd
        asserti = (g / t) * 100

        asserti = f'{asserti:.2f}'
        msg = f'''Relatório atual:\n\n✅Greens: {greenn}\n🟠Empates: {brancoo}\n❌ Reds: {redd}\n\n📈Consecutivas:  {consecutivas}\n\n🎯 Assertividade: {asserti}% '''
        bot.send_message(user_id, msg)
        cont_placar = 0


