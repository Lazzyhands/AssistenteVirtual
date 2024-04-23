import pyautogui


def iniciar_steam():

    return None


def atuar_sobre_a_steam(acao, objeto, parametro_de_atuacao):
    if acao == "iniciar" and objeto == "steam":
        print("abrindo steam")
        pyautogui.press('winleft')
        pyautogui.write('Steam')
        pyautogui.press('enter')

    elif acao == "fechar" and objeto == "steam":
        print("Fechando Steam")
        pyautogui.hotkey('alt', 'f4')
