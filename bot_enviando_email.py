import smtplib
import email.message

#Dados
nome = 'Aluno'
n_de_inscricao = 1000
usuario = 'usuario_teste'
senha = 'Senh@Test3'

#Mensagem
mensagem = f"""
<h1>Olá, {nome}!</h1>

<h4>Segue abaixo os dados para acesso a competição:</h4>

<h4>Nº de inscrição: {n_de_inscricao} <br>
Usuário: {usuario} <br>
Senha: {senha}</h4>

<p style="color: #808080;">---</p>

<p style="color: #808080;"><i>Esta é uma mensagem automática enviada através de um robô.</i></p>
<p style="color: #808080;"><i>Por favor, não responda.</i></p>
<p style="color: #808080;"><i>Atenciosamente, Bot.</i></p> <br>

"""

#Configuração da mensagem
msg = email.message.Message()
msg['Subject'] = "Teste - Envio de Email (Bot)"
msg['From'] = 'seuemail@temp.com.br'
msg['To'] = 'emailremetente@temp.com.br'
password = 'SUA_SENHA'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(mensagem)

# Configuração SMTP do servidor Gmail
s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

# Credenciais de login para enviar o e-mail
s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('Email enviado')