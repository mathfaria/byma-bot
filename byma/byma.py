## coded by matheus comedia <3

while True:
    try:
        from webdriver_manager.firefox import GeckoDriverManager
        from selenium.webdriver.firefox.service import Service
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.support.ui import Select
        from selenium import webdriver
        from statistics import median
        from bs4 import BeautifulSoup
        from random import choice
        from time import sleep
        import configparser
        import requests
        import re

        break

    except Exception as e:
        print("DEPENDENCIAS NAO INSTALADAS")
        exit()

######## reading config file
config = configparser.ConfigParser()
config.read_file(open(r"configuracoes.txt"))

party_url = config.get("BYMABOT", "url")
input_email = config.get("BYMABOT", "email")
input_password = config.get("BYMABOT", "senha")
which_ticket = config.get("BYMABOT", "opcao_ingresso")
min_price = config.get("BYMABOT", "valor_minimo")
max_price = config.get("BYMABOT", "valor_maximo")

if input_email == "":
    print("PREENCHA O CAMPO DE EMAIL / SENHA!!")
    exit()

if which_ticket == "1":
    description = "INGRESSO MAIS BARATO"
elif which_ticket == "2":
    description = "INGRESSO MAIS CARO"
elif which_ticket == "3":
    description = "UM INGRESSO ALEATORIO"
elif which_ticket == "4":
    description = "O INGRESSO DE VALOR MEDIANO"

req = requests.get(party_url)
if req.status_code == 200:
    html_code = req.text
    soup = BeautifulSoup(html_code, "html.parser")
    url_party_name = (soup.find_all("h1")[0].get_text()).upper()
else:
    print("A SUA FESTA NÃO FOI ENCONTRADA")

######################################################################
input(
    """\n\n\n
-------------------------------------------------------------------
   -> CONFIRME SE ESTÁ TUDO CERTO:
 O BOT VAI COMPRAR A FESTA: {}
 NO EMAIL: {}
    SENHA: {}

 COMPRAR O {}; O PAGAMENTO SÓ SERÁ EFETUADO SE O
    INGRESSO ESTIVER ENTRE R$ {} A R$ {}.

    >>>>>>>>> PRESSIONE ENTER PARA CONFIRMAR <<<<<<<<<
    [!!!] CUIDADO PRA NAO COMPRAR NADA POR ENGANO  [!!!]

-------------------------------------------------------------------
""".format(
        url_party_name, input_email, input_password, description, min_price, max_price
    )
)
########################################################################


options = Options()
options.add_argument("--no-sandbox")
#options.add_argument("--headless")


browser = webdriver.Firefox(
    options=options, service=Service(GeckoDriverManager().install())
)


while True:
    try:
        price_dict = {}
        browser.get("https://byma.com.br/login")

        while True:
            sleep(0.05)
            if browser.find_elements_by_xpath(
                "/html/body/div[2]/div[1]/div/form/div[1]/div[2]/input"
            ):
                break

        email = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/form/div[1]/div[2]/input"
        )
        email.send_keys(input_email)

        password = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/form/div[2]/div[2]/input"
        )
        password.send_keys(input_password)

        browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/form/div[3]"
        ).click()

        while True:
            sleep(0.05)
            if browser.find_elements_by_xpath("/html/body/div[2]/div[1]/div[2]"):
                browser.get(party_url)
                break

        buy_button = "/html/body/div[2]/div[1]/div/div[3]/div[2]/div"
        repeat_once = True
        while True:
            sleep(0.05)
            if browser.find_elements_by_xpath(buy_button):
                if (
                    browser.find_element_by_xpath(buy_button).text
                    == "Comprar ingressos"
                ):
                    print(
                        "[ {} ]\n  COMEÇOU A VENDA\nINICIANDO A COMPRA DA FESTA: {}".format(
                            input_email, url_party_name
                        )
                    )
                    browser.find_element_by_xpath(buy_button).click()
                    break

                else:
                    if repeat_once:
                        print("[ %s ]\n  NÃO COMEÇOU A VENDER" % input_email)
                        repeat_once = False

            browser.get(party_url)
            sleep(1)  # taxa de atualização

        class_itens = "tickettype-item"
        num_class_itens = len(browser.find_elements_by_class_name(class_itens))

        while True:
            sleep(0.05)
            if "R$" in (
                browser.find_element_by_xpath(
                    "/html/body/div[4]/div/div/div/div[2]/div[2]/div[1]/span[2]"
                ).text
            ):
                sleep(0.25)
                break

        for i in range(num_class_itens):
            corrected_indc = i + 2
            actual_item = (
                "/html/body/div[4]/div/div/div/div[2]/div[{}]/div[1]/span[2]".format(
                    corrected_indc
                )
            )
            whole_string = str(browser.find_element_by_xpath(actual_item).text)
            processed_string = whole_string.replace("R$ ", "")
            str_price = processed_string[: (processed_string.find(","))]
            price = int(float(str_price))

            if (price > int(min_price)) and (price < int(max_price)):
                price_dict[price] = corrected_indc

        if len(price_dict) <= 0:
            print(
                "TODOS INGRESSOS ESTÃO CUSTANDO MAIS DE %s REAIS, CANCELANDO A COMPRA."
                % max_price
            )
            break

        ## menor preço
        if which_ticket == "1":
            chosen_index = price_dict[min(price_dict)]

        ## maior preço
        if which_ticket == "2":
            chosen_index = price_dict[max(price_dict)]

        ## aleatorio
        if which_ticket == "3":
            chosen_index = choice(list(price_dict.values()))

        ## mais proximo da media
        if which_ticket == "4":
            median_price = median(price_dict)
            closest_value = min(price_dict, key=lambda x: abs(x - median_price))
            chosen_index = price_dict[closest_value]

        select_ticket = Select(
            browser.find_element_by_xpath(
                "/html/body/div[4]/div/div/div/div[2]/div[%s]/div[2]/select"
                % chosen_index
            )
        )
        select_ticket.select_by_value("1")

        buy_button = browser.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div[3]/div[2]"
        ).click()

        checkout_button = (
            "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/form/div/div[2]"
        )
        while True:
            sleep(0.05)
            if browser.find_elements_by_xpath(checkout_button):
                browser.find_element_by_xpath(checkout_button).click()
                break

        while True:
            sleep(0.05)
            if browser.find_elements_by_xpath(
                "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[2]"
            ):
                break

        payment_option = []

        payment_itens = "payment-option"
        num_payment_itens = len(browser.find_elements_by_class_name(payment_itens))

        party_name = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr/td[1]"
        ).text
        party_value = browser.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/table/tbody/tr/td[2]"
        ).text
        print("COMPRADO - {} - {} (sem a taxa do byma)".format(party_name, party_value))

        for i in range(num_payment_itens):
            payment_xpath = (
                "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div[%s]"
                % (i + 1)
            )
            payment_string = str(
                browser.find_element_by_xpath(payment_xpath).text
            ).upper()

            if "****" in payment_string:
                browser.find_element_by_xpath(payment_xpath).click()
                browser.find_element_by_xpath(
                    "/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[3]"
                ).click()

        break

    except Exception:
        print("ALGO DEU ERRADO :(")
