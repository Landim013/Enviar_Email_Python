import win32com.client as win32

# CRIAR A INTEGRAÇÃO COM OUTLOOK
outlook = win32.Dispatch('outlook.application')

# CRIAR UM EMAIL
email = outlook.CreateItem(0)




#CONFIGURAR AS INFORMAÇOES DO SEU E-MAIL


    #destino
email.TO =  'douglas.landim@telefonica.com'                    

    #assunto
email.Subject =  'teste email automatico python'             

    #Corpo do E-mail (f) passar parametros de variaveis {variavel}
email.HTMLBody =  f"""<p>esse é um teste em python</p>
<p>com email automatico </p>




<p>ass, Douglas Landim</p>"""                                             

email.Send()