# import os
from random import randint
from types import coroutine
from instapy import InstaPy
from instapy import smart_run
from os import system
from time import sleep


system('clear')
system('clear')
print('''\033[1;33m
 █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ ██████╗ ████████╗██╗███████╗███████╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔═══██╗╚══██╔══╝██║╚══███╔╝██╔════╝
███████║██║   ██║   ██║   ██║   ██║██╔████╔██║██║   ██║   ██║   ██║  ███╔╝ █████╗
██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██║   ██║   ██║   ██║ ███╔╝  ██╔══╝
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║╚██████╔╝   ██║   ██║███████╗███████╗
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝
\033[1;31m    ▄█▀ ▄▄▄▄▄▄▄ ▀█▄
\033[1;31m    ▀████████████▀\033[0;97m   Automatizando tarefas \033[1;93mINSTAGRAM\033[1;33m...
\033[1;31m        █▄███▄█\033[0;97m      \033[1;93mLIKE, Comments, Follows, Unfollows
\033[1;31m         █████\033[0;97m
\033[1;31m         █▀█▀█\033[0;97m      Prescione \033[1;91m[ENTER]\033[0;97m para continuarmos
\033[0m''')
input()
system('clear')
print(f'''
                  \033[1;33mSobre o AUTOMATIZE!\033[0m
\033[0;93m╔════════════════════════════════════════════════════╗
\033[0;93m║                    \033[1;31mAtenção!\033[0m                        ║
\033[0;93m║  \033[0;97mA ferramenta evitara o maximo Possivel atividades \033[0;93m║
\033[0;93m║ \033[0;97mnão humanizadas exceder limites de Likes ou de     \033[0;93m║
\033[0;93m║ \033[0;97mcomentarios pode ser um risco para sua conta para  \033[0;93m║
\033[0;93m║ \033[0;97msua conta não venha ser BLOQUEADA fizemos com que  \033[0;93m║
\033[0;93m║ \033[0;97mtivesse intervalos de tempo sobre cada atividade.  \033[0;93m║
\033[0;93m║                                                    \033[0;93m║
\033[0;93m║                 \033[1;92mDesenvolvimento\033[0m                    \033[0;93m║
\033[0;93m║   \033[0;97mNão foi criada interface grafica devido que a    \033[0;93m║
\033[0;93m║ \033[0;97mferramenta rodara 100% em segundo plano, e nem     \033[0;93m║
\033[0;93m║ \033[0;97mutilizado banco de dados pois não havera armazena- \033[0;93m║
\033[0;93m║ \033[0;97mmento de qualuer informação. Porem existe a possi- \033[0;93m║
\033[0;93m║ \033[0;97mbilidade de um possivel integração com o banco e   \033[0;93m║
\033[0;93m║ \033[0;97mcom uma interface mais amigavel.                   \033[0;93m║
\033[0;93m║                                                    ║
\033[0;93m╚════════════════════════════════════════════════════╝
\033[1;92m              [Enter] para continuar \033[0m''')

input()
system('clear')

print('''\033[1;33m
    ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
    ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
    ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
    ██║     ██║   ██║██║   ██║██║██║╚██╗██║
    ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
╔════════════════════════════════════════════╗
║\033[1;97m    Usuario e Senha de Acesso - INSTAGRAM   \033[1;33m║
║\033[1;96m       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       \033[1;33m║
║\033[1;97m          SEUS DADOS ESTÃO SEGUROS          \033[1;33m║
╚════════════════════════════════════════════╝
\033[1;92m Observações:\033[0;97m Não guardaremos nenhuma de suas
 Credenciais o Bot - AUTOMOTIZE trabalha sem
 uso de Banco de Dados.\033[0m
''')

while True:
    user = str(input('\033[1;33mUsuario: \033[1;97m')).strip()
    if user is None or user == '': print()
    else: break
while True:
    password = str(input('\033[1;33mSenha: \033[1;97m')).strip()
    if password is None or password == '': print()
    else: break
input('\033[1;33mContinuar \033[1;31m[ENTER]\033[1;97m')


system('clear')

while True:

    print('''\033[1;33m
        ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
        ████╗ ████║██╔════╝████╗  ██║██║   ██║
        ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
        ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
        ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
        ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝
    ╔════════════════════════════════════════════╗
    ║\033[1;31m               Bot Instagram\033[1;33m                ║
    ║\033[1;36m        Centro Universitario Projeção\033[1;33m       ║
    ╚════════════════════════════════════════════╝
                \033[1;32mMenu de Fucionalidades:\033[1;33m
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ╚ 1 \033[1;97mComentararios e Likes\033[1;33m
    ╚ 2 \033[1;97mLikes\033[1;33m
    ╚ 3 \033[1;97mSeguir "Hashtags"\033[1;33m
    ╚ 4 \033[1;97mDeixar de Seguir [Sem Restrições]\033[1;33m
    ╚ 5 \033[1;97mDeixar de Seguir [Os que não seguem de volta]\033[1;33m
    ╚ 6 \033[1;31mSair\033[0m
    ''')
    option = input('\033[1;33mEscolha uma das opções: \033[1;97m').strip()
    if option not in '123456' or option is None or option == '':
        system('clear')
        print('''\033[1;31m
    ╔════════════════════════════════════════════╗
    ║          Escolha uma opção valida          ║
    ╚════════════════════════════════════════════╝\033[0m''')
    else: break

if option in '1':
    system('clear')
    while True:
        system('clear')
        print('\033[1;33mExemplo: \033[1;92m#projeção #informatica #java #php')
        tags = str(input('\033[1;33mDigite suas hashtags: \033[1;97m').replace('#','')).split()
        if len(tags) > 0:
            break
        system('clear')
        print('\033[1;33mPrecisa de \033[1;31mpelo menos 1 hashtag, separados por espaços')
    print('~'*40)
    print('~'*40)

    while True:
        system('clear')
        print('\033[1;33mExemplo: \033[1;92mmuito bom, bacana, gostei disso ai, interessante')
        lista_comentarios = str(
            input('\033[1;33mDigite de 4 ou mais comentarios: \033[1;97m')).split(',')
        if len(lista_comentarios) >= 4:
            break
        system('clear')
        print('\033[1;33mPrecisa de \033[1;31mpelo menos 4 comentarios, separados por virgulas')
    # ['Muito bom', 'Show de bola', 'Tops!', 'Bacana', 'Muito massa', '👌 Tops!', 'Tops!!', '🤘🤘','Bacana 👍','Interessante 👍', 'legal 👍', '✌️✌️']
    session = InstaPy(username=user,
                        password=password,headless_browser=False)
    with smart_run(session):
        
        def commentarios(tags, lista_comentarios):
            # porcentagem de likes que realizara
            session.set_do_comment(True, percentage=100)
            # media='Video' --> define o tipo de post e marca o quem enviou o post
            session.set_comments(lista_comentarios)
            session.like_by_tags(tags, amount=5, media='Photo', skip_top_posts=True,
                                    randomize=True, interact=True)
            session.set_user_interact(amount=1,  # interagir com 1
                                        randomize=True,  # aleatorio
                                        percentage=100,  # porcentagem
                                        media='Photo')  # tipo de midia que sera curtidacommentarios
        commentarios(tags, lista_comentarios)
        system('clear')
elif option in '2':
    system('clear')
    while True:
        system('clear')
        print('\033[1;33mExemplo: \033[1;92m#projeção #informatica #java #php')
        tags = str(input('\033[1;33mDigite suas hashtags: \033[1;97m').replace('#','')).split()
        if len(tags) > 0:
            break
        system('clear')
        print('\033[1;31mPrecisa de pelo menos 1 hashtag, separados por espaços')
    print('~'*40)
    print('~'*40)
    print('\033[1;97m')
    session = InstaPy(username=user,
                        password=password,headless_browser=False)
    with smart_run(session):
        def likes_option(tags):
            session.like_by_tags(tags, amount=5, media='Photo', skip_top_posts=True,
                                    randomize=True, interact=True)
            session.set_user_interact(amount=1,  # interagir com 1
                                        randomize=True,  # aleatorio
                                        percentage=100,  # porcentagem
                                        media='Photo')  # tipo de midia que sera curtidacommentarios
        likes_option(tags)
elif option in '3':
    system('clear')
    while True:
        print('\033[1;33mExemplo: \033[1;92m#projeção #informatica #java #php')
        tags = str(input('\033[1;33mDigite suas hashtags: \033[1;97m')).split()
        if len(tags) > 0:
            break
        system('clear')
        print('\033[1;33mPrecisa de \033[1;31mpelo menos 1 hashtag, separados por espaços\033[1;97m')
        print('~'*40)
        print('~'*40)
    session = InstaPy(username=user,
                        password=password,headless_browser=False)
    with smart_run(session):
        def seguir_por_tags(tags):
            session.follow_by_tags(tags, amount=5)
        seguir_por_tags(tags)
elif option in '4':
    system('clear')
    print('\033[1;33mQuantos quer deixar de seguir?')
    quant = int(input('\033[1;33mDigite: \033[1;97m'))
    
    system('clear')
    session = InstaPy(username=user,
                        password=password,headless_browser=False)
    with smart_run(session):
        def deixar_de_seguir_all(quant):
            session.unfollow_users(amount=quant, allFollowing=True,
                                    style="LIFO", unfollow_after=3*60*60, sleep_delay=300)
        deixar_de_seguir_all(quant)
elif option in '5':
    system('clear')
    print('\033[1;33mQuantos quer deixar de seguir?')
    quant = int(input('\033[1;33mDigite: \033[1;97m'))
    system('clear')
    session = InstaPy(username=user,
                        password=password,headless_browser=False)
    with smart_run(session):
        def deixar_seguir_ingratos(quant):
            session.unfollow_users(amount=quant, nonFollowers=True,
                                    style="FIFO", unfollow_after=42*60*60, sleep_delay=350)
    deixar_seguir_ingratos(quant)
elif option in '6':
    system('clear')
    print('\033[1;31mObrigador por utilizar nossa ferramenta!') 
    for i in range(5):
        print(f'\033[1;33m╚ {i+1}')
        sleep(0.5)
    print('\033[1;33mBye, bye !!')
    system('clear')
    quit()
    