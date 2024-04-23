import pyautogui
def iniciar_gravador():
    
    return None

#Iniciar gravador
def atuar_sobre_o_gravador(acao, objeto, parametros_de_atuacao):
    if acao in(["ligar"]) and objeto == "gravador":

        print("Iniciando gravador")
        pyautogui.hotkey('winleft', 'alt', 'r')
        
#Parar gravador

    elif(acao in ["desligar"]) and objeto == "gravador":
        print("Encerrando gravação! ")
        
        pyautogui.hotkey('winleft', 'alt', 'r')