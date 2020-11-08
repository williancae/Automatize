# import os
from random import randint
from instapy import InstaPy
from instapy import smart_run
from os import system
from time import sleep


# login credentials
# insta_username = 'willian.cae'
# insta_password = 'Will84530303'
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
\033[1;31m         █████\033[0;97m         prescione \033[1;91m[S]\033[0;97m para saber mais
\033[1;31m         █▀█▀█        
\033[0;97m                     Prescione \033[1;91m[ENTER]\033[0;97m para continuarmos
\033[0m''')


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
 uso de Banco de Dados.\033[0m''')

user = str(input('Usuario: ')).strip()
password = str(input('Senha: ')).strip()
input('Continuar [ENTER]')


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
    option = str(input('Escolha uma das opções: '))

    if option in '1':
        system('clear')
        while True:
            system('clear')
            print('Exemplo: projeção informatica java php')
            tags = str(input('Digite suas hashtags: ')).split()
            if len(tags) > 0:
                break
            system('clear')
            print('Precisa de pelo menos 1 hashtag, separados por espaços')
        print('~'*40)
        print('~'*40)

        while True:
            system('clear')
            print('Exemplo: muito bom, bacana, gostei disso ai')
            lista_comentarios = str(
                input('Digite de 4 ou mais comentarios: ')).split(',')
            if len(lista_comentarios) >= 4:
                break
            system('clear')
            print('Precisa de pelo menos 4 comentarios, separados por virgulas')
        # ['Muito bom', 'Show de bola', 'Tops!', 'Bacana', 'Muito massa', '👌 Tops!', 'Tops!!', '🤘🤘','Bacana 👍','Interessante 👍', 'legal 👍', '✌️✌️']
        session = InstaPy(username=user,
                        password=password)
        with smart_run(session):
            def commentarios(tags, lista_comentarios):
                # porcentagem de likes que realizara
                session.set_do_comment(True, percentage=100)
                # media='Video' --> define o tipo de post e marca o quem enviou o post
                session.set_comments(lista_comentarios)
                session.like_by_tags(tags, amount=10, media='Photo', skip_top_posts=True,
                                    randomize=True, interact=True)
                session.set_user_interact(amount=1,  # interagir com 1
                                        randomize=True,  # aleatorio
                                        percentage=100,  # porcentagem
                                        media='Photo')  # tipo de midia que sera curtidacommentarios
            commentarios(tags, lista_comentarios)
            system('clear')
            continue
    elif option in '2':
        system('clear')
        while True:
            system('clear')
            print('Exemplo: projeção informatica java php')
            tags = str(input('Digite suas hashtags: ')).split()
            if len(tags) > 0:
                break
            system('clear')
            print('Precisa de pelo menos 1 hashtag, separados por espaços')
        print('~'*40)
        print('~'*40)
        session = InstaPy(username=user,
                        password=password)
        with smart_run(session):
            def likes_option(tags):
                session.like_by_tags(tags, amount=10, media='Photo', skip_top_posts=True,
                                    randomize=True, interact=True)
                session.set_user_interact(amount=1,  # interagir com 1
                                        randomize=True,  # aleatorio
                                        percentage=100,  # porcentagem
                                        media='Photo')  # tipo de midia que sera curtidacommentarios
            likes_option(tags)
    elif option in '3':
        system('clear')
        while True:
            print('Exemplo: projeção informatica java php')
            tags = str(input('Digite suas hashtags: ')).split()
            if len(tags) > 0:
                break
            system('clear')
            print('Precisa de pelo menos 1 hashtag, separados por espaços')
            print('~'*40)
            print('~'*40)
        session = InstaPy(username=user,
                        password=password)
        with smart_run(session):
            def seguir_por_tags(tags): 
                session.follow_by_tags(tags, amount=10)
            seguir_por_tags(tags)
    elif option in '4':	
        system('clear')
        print('Quantos quer deixar de seguir? Obs. campo em branco sera gerado um valor aleatorio.')
        quant = int(input('Digite: '))
        if quant <= 0:
            quant = randint(5,10)
        system('clear')
        session = InstaPy(username=user, password=password)
        with smart_run(session):
            def deixar_de_seguir_all(quant): 
                session.unfollow_users(amount=quant, allFollowing=True,
                style="LIFO", unfollow_after=3*60*60, sleep_delay=450)
            deixar_de_seguir_all(quant)
    elif option in '5':	
        system('clear')
        print('Quantos quer deixar de seguir? Obs. campo em branco sera gerado um valor aleatorio.')
        quant = int(input('Digite: '))
        if quant <= 0:
            quant = randint(5,10)
        system('clear')
        session = InstaPy(username=user, password=password)
        with smart_run(session):
            def deixar_seguir_ingratos(quant): 
                session.unfollow_users(amount=quant, nonFollowers=True, style="FIFO", unfollow_after=42*60*60, sleep_delay=655)
        deixar_seguir_ingratos(quant)
    elif option in '6':
        break        
    elif option in '':
        system('clear')
        print('Escolha um numero de 1 a 6!!\nEm alguns segundos você sera redirecionado ao MENU.')
        for i in range(1,6):
            sleep(0.6)
            print('╚ ', i)
        print() 
        system('clear')
    else:
        system('clear')
        print('Escolha um numero de 1 a 6!!\nEm alguns segundos você sera redirecionado ao MENU.')
        for i in range(1,6):
            sleep(0.6)
            print('╚ ', i)
        print() 
        system('clear')

#         session.unfollow_users(amount=3, allFollowing=True, style="LIFO", unfollow_after=3*60*60, sleep_delay=450)
#         session.follow_by_tags(['fapro', 'uniprojecao'], amount=3)

# session.story_by_tags(['naruto', 'otaku', 'anime', 'itachi'])
# session.set_relationship_bounds(enabled=True,
#                                 potency_ratio=None,
#                                 delimit_by_numbers=True,
#                                 max_followers=10000,
#                                 max_following=3000,
#                                 min_followers=50,
#                                 min_following=25,
#                                 min_posts=4)

# session.set_skip_users(skip_private=True, #pular perfil privado
#                 private_percentage=100, #pular 100% / perfil privado
#                 skip_no_profile_pic=True, #pular perfil sem foto
#                 no_profile_pic_percentage=100, #pular 100% dos perfils sem fot
#                 skip_business=True, #ignorar contas comerciais
#                 business_percentage=100, #ignorar 100% das contas comerciais
#                 skip_business_categories=[], # Categorias de contas comerciais ['Advertising', 'Agency', 'Advertising/Marketing', 'Art', 'Art Gallery', 'Art Museum', 'Artist', 'Arts & Entertainment', 'Arts & Humanities', 'Website', 'Athlete', 'Auto', 'Dealers', 'Business & Utility', 'Services', 'Clothing', 'Store', 'Community', 'Community Organization', 'Company', 'Consulting', 'Agency', 'Content & Apps', 'Creators & Celebrities', 'Education', 'Food & Personal', 'Goods', 'General', 'Interest', 'Graphic', 'Designer', 'Home', 'Goods', 'Stores', 'Home', 'Services', 'Jewelry/Watches', 'Lifestyle', 'Services', 'Local', 'Business', 'Local', 'Events', 'Management', 'Service', 'Media/News', 'Company', 'Non-Profits & Religious', 'Organizations', 'Party', 'Entertainment', 'Service', 'Personal', 'Goods & General', 'Merchandise', 'Stores', 'Photographer', 'Photography', 'Videography', 'Product/Service', 'Professional', 'Service', 'Professional', 'Sports', 'Team', 'Public', 'Figure', 'Public', 'Relations', 'Agency', 'Publishers', 'Restaurants', 'Ski', 'Resort', 'Sport', 'Sports & Recreation', 'Transportation & Accomodation', 'Services', 'Travel', 'Agency', 'Wine/Spirits']
#                 dont_skip_business_categories=[]) #Não seguir uma categoria especifica


# Listas de comentarios
# commentary = [
#     #caso exista uma dessas palavras ('caipira' ou 'fazenda' ou'roça') --> comente isso ....
#     {'mandatory_words': ['caipira','fazenda','roça'], 'comments': ['Muito bom!', 'Haoo trêm bão', 'Muito bom!']},
#     #caso exista uma dessas palavras ('academia' ou ['crossfit' & 'Forte'] ou 'Musculação') --> comente isso ....
#     {'mandatory_words': ['academia',['crossfit', 'Forte'],'Musculação'],'comments': ['Muito bom', 'Tops!', 'Show de bola!']},
#     #Nesta caso todas as palavras precisariam existir ao mesmo tempo
#     {'mandatory_words': [['Cristo', 'espiritosanto','Deus']],'comments': ['Gosto muito...', 'Amem', 'Assim seja']}
# ]


# """
#                         ~~~~~~~~~~~Curtir por TAGs~~~~~~~~~~~~~~~~
#     session.set_do_like(True, percentage=100)
# #Curtir
#     session.like_by_tags(['naruto'],amount=20, media='Photo', randomize=True)

#             ~~~~~~~~~~~~~~~~~~~~Curtir Feed~~~~~~~~~~~~~~~~~~~~~
#     session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
#     session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)
# """


# #Comentar e Curtir
# """
#             ~~~~~~~~~~~~~~~~~~~~~~Comentar & Curtir~~~~~~~~~~~~~~~~~~
#     hashtags= ['reidogado', 'boiada','peao']
#     comments = ['Muito bom', 'Show de bola', 'Tops!', 'Bacana', 'Muito massa', '👌 Tops!', 'Tops!!', '🤘🤘','Bacana 👍','Interessante 👍', 'legal 👍', '✌️✌️']
#     session.set_do_comment(True,percentage=100) # porcentagem de likes que realizara
#     session.set_comments(comments) # media='Video' --> define o tipo de post e marca o quem enviou o post
#     session.like_by_tags(hashtags, amount=20, media='Photo', skip_top_posts=True,
#                         # amount=3, #numero de likes que dara em cada interação
#                         randomize=True, interact=True)
#     session.set_user_interact(amount=2, # interagir com 3
#                             randomize=True, #aleatorio
#                             percentage=100, #porcentagem
#                             media='Photo') #tipo de midia que sera curtida
# """


# #Assistir Story
# """
# ~~~~~~~~~~~~ Ver Storys ~~~~~~~~~~~~~~~
# session.set_do_story(enabled = True, percentage = 100, simulate = True)

# ~~~~~~~~~~~~~~~Tags~~~~~~~~~~~~~~~~~~
# session.story_by_tags(tags=['trump', 'usa'])

# ~~~~~~~~~~~~~~~Usuario~~~~~~~~~~~~~~~~
# session.story_by_users(['user1', 'user2'])

# """


# #Deixar de seguir
# # """
#                 ~~~~~~~~~~~~~~~~ Deixar de Seguir todos ~~~~~~~~~~~~~~
# session.unfollow_users(amount=40, allFollowing=True, style="LIFO", unfollow_after=3*60*60, sleep_delay=450)

#                 ~~~~~~~~~~~ Deixar  de Seguir que nao segue de volta ~~~~~~~~~~~
# session.unfollow_users(amount=4, nonFollowers=True, style="FIFO", unfollow_after=42*60*60, sleep_delay=655)"""

# #Seguir
# """         ~~~~~~~~Seguir por Tag~~~~~~~
# session.follow_by_tags(['tag1', 'tag2'], amount=10)

#             ~~~~~~~~~~Siga os seguidores de outra pessoa~~~~~~~~~~~~~~~
# session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
# session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False, sleep_delay=60, interact=True)

#     ~~~~~~~~~~~~Siga e interaja com os seguidores / seguidores de outra pessoa~~~~~~~~~~~~~~~
# session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
# session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False, interact=True)
# """


# #instapy Pods
# """
#     ~~~~~~~~~~~~~~Instapy Pods~~~~~~~~~~~~~~~~~~
# photo_comments = ['Nice shot! @{}',
#                 'I love your profile! @{}',
#             'Your feed is an inspiration :thumbsup:',
#             'Just incredible :open_mouth:',
#             'What camera did you use @{}?',
#             'Love your posts @{}',
#             'Looks awesome @{}',
#             'Getting inspired by you @{}',
#             ':raised_hands: Yes!',
#             'I can feel your passion @{} :muscle:']

# session = InstaPy()

# with smart_run(session):
#         session.set_comments(photo_comments, media='Photo')
#     session.join_pods()
# """

# #interagir
# """
# ~~~~~~~~~~Interaja com usuários que outra pessoa está seguindo~~~~~~~~~~~~~
# session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
# session.set_do_follow(enabled=False, percentage=70)
# session.set_do_like(enabled=False, percentage=70)
# session.set_comments(["Cool", "Super!"])
# session.set_do_comment(enabled=True, percentage=80)
# session.interact_user_following(['natgeo'], amount=10, randomize=True)

#                 ~~~~~~~~~~~~~~~~ Interagir por comentários ~~~~~~~~~~~~~~~~~~
# Curta comentários em postagens, responda a eles e interaja com os usuários cujo comentário foi curtido na postagem
#                                 ~~~~~~~~~~~~~~~~~~~~~~~~
# session.interact_by_comments(usernames=["somebody", "other buddy"],
#                             posts_amount=10,
#                             comments_per_post=5,
#                             reply=True,
#                             interact=True,
#                             randomize=True,
#                             media="Photo")
# """

# #Idioma
# """
#                 ~~~~~~~~~~ Idioma obrigatorio ~~~~~~~~~~
# session.set_mandatory_language(enabled=True, character_set=['LATIN']) """

# #Ferramenta Simular
# """
#     ~~~~~~~~~~~Simular atividade humana~~~~~~~~~~~~
# session.set_simulation(enabled=True, percentage=66) """

# #configuração de Tempo
# """
# ~~~~~~custumizar delays das atividades~~~~~~~~~~~~
# session.set_action_delays(enabled=True,
#                         like=3,
#                         comment=5,
#                         follow=4.17,
#                         unfollow=28,
#                         story=10)

# ~~~~~~~~~Costumizar valores aleatorios~~~~~~~~~~~~~~
# session.set_action_delays(enabled=True, like=5.2, randomize=True, random_range_from=70, random_range_to=140)
# """


# session.end()
