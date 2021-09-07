# SUBBOT É UM PROGRAMA LIVRE
#         passo-a-passo da legenda como transcrição automática:
# 1. Upar vídeo no YT, esperar sair legendas automáticas.
# 2. Editar as legendas online, e salvá-las na mesma plataforma (não é preciso editar realmente), esse processo evita overlapping.
# 3. Salvar uma cópia em UTF-16 para permitir a visualização de caracteres especiais.
# 4. Substituir caracteres ",NUMERO" por ":NUMERO", se .SRT
# 5. IMPORTAR NO PROGRAMA
# 6. MELHOR CENÁRIO: Fazer o programa criar markers nos momentos da fala
# PRÓXIMOS PASSOS:
# CADASTRAR TRANSCRIÇÃO, FAZER ARTICULAÇÃO COM LEGENDA DE ALGUMA MANEIRA
# CRIAR INTERFACE COM KIVY(?)

# Para você que está abrindo isso agora e importando no seu projeto, lembre-se que deve adaptar os nomes de personagens para o seu workflow. 
# No caso desta versão do programa, o arquivo usado refere-se aos personagens das produções da COALA FILMES, com entrevistas e gravações realizadas entre 2006 e 2017, a serem usadas em DOCUMENTÁRIOS ANIMADOS.


FIRSTCOMMAND = input("INSIRA UMA PERSONAGEM: ")
while True:
    if FIRSTCOMMAND == 'angeli':
        ATK01_DIA01 = open("ATK01_DIA01_SUB.txt")
        textATK01D01 = ATK01_DIA01.read().lower().strip().split('\n\n')
        ATK01_DIA01.close()
        ATK01_DIA02 = open("ATK01_DIA02_SUB.txt")
        textATK01D02 = ATK01_DIA02.read().lower().strip().split('\n\n')
        ATK01_DIA02.close()
        ATK01_DIA03 = open("ATK01_DIA03_SUB.txt")
        textATK01D03 = ATK01_DIA03.read().lower().strip().split('\n\n')
        ATK01_DIA03.close()
        ATK01_DIA04 = open("ATK01_DIA04_SUB.txt")
        textATK01D04 = ATK01_DIA04.read().lower().strip().split('\n\n')
        ATK01_DIA04.close()
        ATK02_DIA01 = open("ATK02_DIA01_SUB.txt")
        textATK02D01 = ATK02_DIA01.read().lower().strip().split('\n\n')
        ATK02_DIA01.close()
        ATK02_DIA02 = open("ATK02_DIA02_SUB.txt")
        textATK02D02 = ATK02_DIA02.read().lower().strip().split('\n\n')
        ATK02_DIA02.close()
        ATK02_DIA03 = open("ATK02_DIA03_SUB.txt")
        textATK02D03 = ATK02_DIA03.read().lower().strip().split('\n\n')
        ATK02_DIA03.close()
        BOB_DIA01 = open("ETV_BOBCUSPE_DIA01_SUB.txt")
        textBOBDIA01 = BOB_DIA01.read().lower().strip().split('\n\n')
        BOB_DIA01.close()
        BOB_DIA02 = open("ETV_BOBCUSPE_DIA02_SUB.txt")
        textBOBDIA02 = BOB_DIA02.read().lower().strip().split('\n\n')
        BOB_DIA02.close()
        DOSSIE = open("DOSSIE_ANGELI.txt")
        textDOSSIE = DOSSIE.read().lower().strip().split('\n\n')
        DOSSIE.close()
        OCUPACAO = open("ETV_OCUPACAO_SUB.txt")
        textOCUPACAO = OCUPACAO.read().lower().strip().split('\n\n')
        OCUPACAO.close()
        while True:
            USERENTRY = input("------------------------------------------------------------\nINSIRA UM TEXTO: ") #Takes input of a string from user
            BADLIST = []
            CHECKATK01DIA01 = [i for i in textATK01D01 if USERENTRY in i]
            CHECKATK01DIA02 = [i for i in textATK01D02 if USERENTRY in i]
            CHECKATK01DIA03 = [i for i in textATK01D03 if USERENTRY in i]
            CHECKATK01DIA04 = [i for i in textATK01D04 if USERENTRY in i]
            CHECKATK02DIA01 = [i for i in textATK02D01 if USERENTRY in i]
            CHECKATK02DIA02 = [i for i in textATK02D02 if USERENTRY in i]
            CHECKATK02DIA03 = [i for i in textATK02D03 if USERENTRY in i]
            CHECKBOBDIA01 = [i for i in textBOBDIA01 if USERENTRY in i]
            CHECKBOBDIA02 = [i for i in textBOBDIA02 if USERENTRY in i]
            CHECKOCUPACAO = [i for i in textOCUPACAO if USERENTRY in i]
            CHECKDOSSIE = [i for i in textDOSSIE if USERENTRY in i]
            if USERENTRY == "": #if no value is entered for the string
                continue
            if USERENTRY == "9outof10":
                FIRSTCOMMAND = 'x'
                break
            if USERENTRY == "VOLTAR":
                FIRSTCOMMAND = 'VOLTAR'
                break
            if CHECKATK01DIA01 == []:
                BADLIST.append('S01D01')
            else:
                #for TCATK01DIA01 in CHECKATK01DIA01:
                #    TCATK01DIA01[] = CHECKATK01DIA01[].split('-->')
                #print(TCATK01DIA01)
                print("\nATK 01 DIA 01:\n"), print(*CHECKATK01DIA01, sep = "\n", end = '\n\n')
            if CHECKATK01DIA02 == []:
                BADLIST.append('S01D02')
            else:
                print("\nATK 01 DIA 02:\n"), print(*CHECKATK01DIA02, sep = "\n", end = '\n\n')
            if CHECKATK01DIA03 == []:
                BADLIST.append('S01D03')
            else:
                print("\nATK 01 DIA 03:\n"), print(*CHECKATK01DIA03, sep = "\n", end = '\n\n')
            if CHECKATK01DIA04 == []:
                BADLIST.append('S01D04')
            else:
                print("\nATK 01 DIA 04:\n"), print(*CHECKATK01DIA04, sep = "\n", end = '\n\n')
            if CHECKATK02DIA01 == []:
                BADLIST.append('S02D01')
            else:
                print("\nATK 02 DIA 01:\n"), print(*CHECKATK02DIA01, sep = "\n", end = '\n\n')
            if CHECKATK02DIA02 == []:
                BADLIST.append('S02D02')
            else:
                print("\nATK 02 DIA 02:\n"), print(*CHECKATK02DIA02, sep = "\n", end = '\n\n')
            if CHECKATK02DIA03 == []:
                BADLIST.append('S02D03')
            else:
                print("\nATK 02 DIA 03:\n"), print(*CHECKATK02DIA03, sep = "\n", end = '\n\n')
            if CHECKBOBDIA01 == []:
                BADLIST.append('BOBD01')
            else:
                print("\nBOB DIA 01:\n"), print(*CHECKBOBDIA01, sep = "\n", end = '\n\n')
            if CHECKBOBDIA02 == []:
                BADLIST.append('BOBD02')
            else:
                print("\nBOB DIA 02:\n"), print(*CHECKBOBDIA02, sep = "\n", end = '\n\n')
            if CHECKDOSSIE == []:
                BADLIST.append('DOSSIE')
            else:
                print("\nDOSSIE:\n"), print(*CHECKDOSSIE, sep = "\n", end = '\n\n')
            if CHECKOCUPACAO == []:
                BADLIST.append('OCUPACAO')
            else:
                print("\nOCUPACAO:\n"), print(*CHECKOCUPACAO, sep = "\n", end = '\n\n')
            if BADLIST == ['S01D01', 'S01D02', 'S01D03', 'S01D04', 'S02D01', 'S02D02', 'S02D03', 'BOBD01', 'BOBD02', 'DOSSIE', 'OCUPACAO']:
                print("\nO texto inserido não se encontra nas legendas da personagem. \n->'VOLTAR' para voltar à lista de personagens<-\n->'9outof10' para sair<-\n")
            else: continue
    if FIRSTCOMMAND == 'bibelo':
        ATK01_BIBELO = open("BIBELO_ATK01.txt")
        textATK01BIBELO = ATK01_BIBELO.read().lower().strip().split('\n\n')
        ATK01_BIBELO.close()
        ATK02_BIBELO = open("BIBELO_ATK02.txt")
        textATK02BIBELO = ATK02_BIBELO.read().lower().strip().split('\n\n')
        ATK02_BIBELO.close()
        while True:
            USERENTRY = input("------------------------------------------------------------\nINSIRA UM TEXTO: ") #Takes input of a string from user
            BADLIST = []
            CHECKATK01BIBELO = [i for i in textATK01BIBELO if USERENTRY in i]
            CHECKATK02BIBELO = [i for i in textATK02BIBELO if USERENTRY in i]
            if USERENTRY == "": #if no value is entered for the string
                continue
            if USERENTRY == "9outof10":
                FIRSTCOMMAND = 'x'
                break
            if USERENTRY == "VOLTAR":
                FIRSTCOMMAND = 'VOLTAR'
                break
            if CHECKATK01BIBELO == []:
                BADLIST.append('S01BIBELO')
            else:
                print("\nBIBELO ATK01:\n"), print(*CHECKATK01BIBELO, sep = "\n", end = '\n\n')
            if CHECKATK02BIBELO == []:
                BADLIST.append('S02BIBELO')
            else:
                print("\nBIBELO ATK02:\n"), print(*CHECKATK02BIBELO, sep = "\n", end = '\n\n')
            if BADLIST == ['S01BIBELO', 'S02BIBELO']:
                print("\nO texto inserido não se encontra nas legendas da personagem. \n->'VOLTAR' para voltar à lista de personagens<-\n->'9outof10' para sair<-\n")
            else: continue
    if FIRSTCOMMAND == 'woodstock':
        ATK01_WOODSTOCK = open("WOODSTOCK_ATK01.txt")
        textATK01WOODSTOCK = ATK01_WOODSTOCK.read().lower().strip().split('\n\n')
        ATK01_WOODSTOCK.close()
        ATK02_WOODSTOCK = open("WOODSTOCK_ATK02.txt")
        textATK02WOODSTOCK = ATK02_WOODSTOCK.read().lower().strip().split('\n\n')
        ATK02_WOODSTOCK.close()
        while True:
            USERENTRY = input("------------------------------------------------------------\nINSIRA UM TEXTO: ") #Takes input of a string from user
            BADLIST = []
            CHECKATK01WOODSTOCK = [i for i in textATK01WOODSTOCK if USERENTRY in i]
            CHECKATK02WOODSTOCK = [i for i in textATK02WOODSTOCK if USERENTRY in i]
            if USERENTRY == "": #if no value is entered for the string
                continue
            if USERENTRY == "9outof10":
                FIRSTCOMMAND = 'x'
                break
            if USERENTRY == "VOLTAR":
                FIRSTCOMMAND = 'VOLTAR'
                break
            if CHECKATK01WOODSTOCK == []:
                BADLIST.append('S01WOODSTOCK')
            else:
                print("\nWOODSTOCK ATK01:\n"), print(*CHECKATK01WOODSTOCK, sep = "\n", end = '\n\n')
            if CHECKATK02WOODSTOCK == []:
                BADLIST.append('S02WOODSTOCK')
            else:
                print("\nWOODSTOCK ATK02:\n"), print(*CHECKATK02WOODSTOCK, sep = "\n", end = '\n\n')
            if BADLIST == ['S01WOODSTOCK', 'S02WOODSTOCK']:
                print("\nO texto inserido não se encontra nas legendas da personagem. \n->'VOLTAR' para voltar à lista de personagens<-\n->'9outof10' para sair<-\n")
            else: continue
    if FIRSTCOMMAND == 'rebordosa':
        ATK01_REBORDOSA = open("GRACE_ATK01.txt")
        textATK01REBORDOSA = ATK01_REBORDOSA.read().lower().strip().split('\n\n')
        ATK01_REBORDOSA.close()
        ATK02_REBORDOSA = open("GRACE_ATK02.txt")
        textATK02REBORDOSA = ATK02_REBORDOSA.read().lower().strip().split('\n\n')
        ATK02_REBORDOSA.close()
        BCNNGG_REBORDOSA = open("GRACE_BCNNGG.txt")
        textBCNNGGREBORDOSA = BCNNGG_REBORDOSA.read().lower().strip().split('\n\n')
        BCNNGG_REBORDOSA.close()
        while True:
            USERENTRY = input("------------------------------------------------------------\nINSIRA UM TEXTO: ") #Takes input of a string from user
            BADLIST = []
            CHECKATK01REBORDOSA = [i for i in textATK01REBORDOSA if USERENTRY in i]
            CHECKATK02REBORDOSA = [i for i in textATK02REBORDOSA if USERENTRY in i]
            CHECKBCNNGGREBORDOSA = [i for i in textBCNNGGREBORDOSA if USERENTRY in i]
            if USERENTRY == "": #if no value is entered for the string
                continue
            if USERENTRY == "9outof10":
                FIRSTCOMMAND = 'x'
                break
            if USERENTRY == "VOLTAR":
                FIRSTCOMMAND = 'VOLTAR'
                break
            if CHECKATK01REBORDOSA == []:
                BADLIST.append('S01REBORDOSA')
            else:
                print("\nRE BORDOSA ATK01:\n"), print(*CHECKATK01REBORDOSA, sep = "\n", end = '\n\n')
            if CHECKATK02REBORDOSA == []:
                BADLIST.append('S02REBORDOSA')
            else:
                print("\nRE BORDOSA ATK02:\n"), print(*CHECKATK02REBORDOSA, sep = "\n", end = '\n\n')
            if CHECKBCNNGGREBORDOSA == []:
                BADLIST.append('BCNNGGREBORDOSA')
            else:
                print("\nRE BORDOSA BCNNGG:\n"), print(*CHECKBCNNGGREBORDOSA, sep = "\n", end = '\n\n')
            if BADLIST == ['S01REBORDOSA', 'S02REBORDOSA', 'BCNNGGREBORDOSA']:
                print("\nO texto inserido não se encontra nas legendas da personagem. \n->'VOLTAR' para voltar à lista de personagens<-\n->'9outof10' para sair<-\n")
            else: continue
    if FIRSTCOMMAND == 'x':
        break
    if FIRSTCOMMAND == 'VOLTAR':
        FIRSTCOMMAND = input("Insira um personagem: ")
        continue
    else:
        print("\nEste personagem não existe no banco de dados.\nInsira 'x' para encerrar o programa.\n")
        FIRSTCOMMAND = input("Insira um personagem: ")
        continue
