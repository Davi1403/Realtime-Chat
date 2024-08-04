#  1 - Página incial 
        # Nome
        # Entrar -->2
#  2 - PopUp
    # Bem vindo 
    # Insira seu nome
    # Entrar no chat -->3
#  3 - Chat -->Limpar página inicial
    # (USER) entro na  conversa
    # Escreva sua mensagem
    # Botão enviar
# Criar o tunel de comunicação

import flet as ft

def main (page):

    # Config da Página

    page.title ='BudCHAT'
    
    page.vertical_aligment = ft.MainAxisAlignment.CENTER

    # 4 -  Criar o tunel de comunicação

    def tunel (mensagem):
        chat.controls.append (mensagem)
        page.update()

    page.pubsub.subscribe (tunel)

    #  1 - Página incial

    #Criar os elementos 

    pi_titulo = ft.Text('BudCHAT')

    def abrir_popup (evento):
        page.dialog = popup
        popup.open = True
        page.update()

    pi_botao = ft.ElevatedButton('Iniciar chat', on_click=abrir_popup)
    linha1 = ft.Row([pi_titulo],alignment=ft.MainAxisAlignment.CENTER)
    linha2 = ft.Row([pi_botao],alignment=ft.MainAxisAlignment.CENTER)
    
    page.add (linha1)
    page.add (linha2)

    #  2 - PopUp

    pu_titulo = ft.Text('BEM VINDO AO BudCHAT') 
     
                                               
    def abrir_chat (evento):
        
        # Limpar página inical
        page.remove (linha1)
        page.remove (linha2)
        popup.open = False

        # Abrir chat
        page.add (chat)
        page.add (chat_linha)

        entrou_chat = f'{pu_box.value} entrou no chat'
        page.pubsub.send_all (ft.Text(entrou_chat, italic= True ,color= ft.colors.YELLOW , size= 12))

        page.update()

    pu_box = ft.TextField(label='Escreve seu nome', on_submit=abrir_chat, autofocus=True)
    pu_botao = ft.ElevatedButton('Iniciar chat',on_click=abrir_chat)
    popup = ft.AlertDialog (title=pu_titulo,content=pu_box, actions=[pu_botao])  # Criar popup

    #  3 - Chat 
    
    chat = ft.ListView(
        expand=True, # Aumenta a listViesw
        spacing=10, # Espaço entre uma linha e outra
        auto_scroll = True # Permite dar scroll na página 
    )

    def enviar_mensagem(evento):
        mensagem = f'{pu_box.value} : {chat_box.value}'
        if chat_box.value != '':
            page.pubsub.send_all (ft.Text(mensagem))
        chat_box.value = ''
        chat_box.focus()
        page.update()
       

    chat_box = ft.TextField(label='Escreva sua mensagem', on_submit= enviar_mensagem, autofocus=True)
    chat_botao = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    chat_linha = ft.Row ([chat_box,chat_botao])


ft.app (target=main, view=ft.WEB_BROWSER)