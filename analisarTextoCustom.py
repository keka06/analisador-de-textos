from customtkinter import *

def analisar_texto():

    # Entrada do usuario
    texto = botao_texto.get()  # define a caixa de texto

    # variaveis
    if not texto.strip():
        texto_analise.configure(text="Nenhum texto digitado")
        return
    textoSemEspaco = texto.replace(" ", "")
    palavras = texto.split()
    num_palavras = len(palavras)

    diacriticos = texto.count('á'), texto.count('ã'),texto.count('à'), texto.count('é'), texto.count('è'), texto.count('ê'), texto.count('í'), texto.count('ì'), texto.count('ó'), texto.count('ò'), texto.count('ú'), texto.count('Ã'),texto.count('Á'), texto.count('À'), texto.count('É'), texto.count('È'), texto.count('Ê'), texto.count('Í'), texto.count('I'), texto.count('Ó'), texto.count('Ó'), texto.count('Ô'), texto.count('Ú')

    num_diacriticos = sum(diacriticos)

    if (num_diacriticos == 0):
        num_diacriticos = "Não há diacríticos."

    #analise do texto
    analiseDoTexto = f'''
'{texto}'\n
O seu texto possui {len(textoSemEspaco)} letras.\n
Seu texto tem {num_palavras} palavras.\n
Quantidade de Ocorrências (Vírgulas): {texto.count(',')}.\n
Quantidade de Diacríticos: {num_diacriticos}\n
Seu texto todo MAIÚSCULO: {texto.upper()}\n
Seu texto todo minúsculo: {texto.lower()}\n
Seu texto invertido: {texto[::-1]}'''

    texto_analise.configure(text=analiseDoTexto)

#executa a função
def analisar():
    analisar_texto()

#configs iniciais da janela
janela = CTk()
janela.title("Analisador de textos") #titulo do programa
janela.geometry("940x560")
janela.minsize(400,560)
#janela.maxsize(940,560)

#textos iniciais
titulo = CTkLabel(janela, text = "ANALISADOR DE TEXTOS", font=("impact", 40), text_color="lightblue")
texto_1 = CTkLabel(janela, text = "Digite um texto, qualquer um.", font=("calibri", 20))#label: onde vai ser (janela, texto=) exibida // grid: posição(column, row)
texto_2 = CTkLabel(janela, text = "(quantas vezes quiser.)", font=("courirer", 12))
titulo.pack(padx = 0, pady=2)
texto_1.pack(padx=0, pady=0)
texto_2.pack(padx=0, pady=0)

#caixa de texto
botao_texto = CTkEntry(janela, width=200, placeholder_text="Digite aqui", placeholder_text_color="white") #entry: caixa de entrada (janela, resto)
botao_texto.pack(padx=0, pady=10)

#botao pra analisar o texto
botao_analisar = CTkButton(janela,text="Analisar",font=("system", 10),fg_color="green",hover_color="#274e13",command=analisar) #executa o processo de analisar
botao_analisar.pack(padx=0, pady=2)

#analise do texto
texto_analise = CTkLabel(janela, text = "", font=("gadugi", 13))
texto_analise.pack(padx=0, pady=1)

janela.mainloop()
