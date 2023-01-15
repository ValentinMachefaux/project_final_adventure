import time

import sys

from random import randint

from Mappy import *

from Mapped import *

from Save import *

from Character import *



# p à retirer à la fin du test

p = Character(json_class("heros"))

i = "???"

v = Character(json_class("lancer"))

l = "Loic"

t = Character(json_class("warrior"))

k = Character(json_class("priest"))

vill = "Villageois"




# s.print_slow("")

# s.next()

# m = Mapped()

# coordinate = str(dreenshgard.get_x()) + "," + str(dreenshgard.get_y())



token_story = 0

token_event = False





class Story:



    def __init__(self):

        self.is_village_destroyed = True



    # ↓ Tout ce qui est en rapport avec le côté dialogue, écriture...

    def print_slow(self, string):

        for letter in string:

            #        Lecture lente

            sys.stdout.write(letter)

    #        Nettoyer

            sys.stdout.flush()

    # Plus rapide ou plus lent (on le mettra à 0.04)

            time.sleep(0.01)



    def print_very_slow(self, string):

        for letter in string:

            #        Lecture lente

            sys.stdout.write(letter)

    #        Nettoyer

            sys.stdout.flush()

    # Plus rapide ou plus lent (on le mettra à 0.04)

            time.sleep(0.1)



    def print_dialog(self, sujet, text, *person):

        a = ""

        for s in sujet:

            a += s + ""

        if len(person) == 0:

            self.print_slow(f"\n\t{a}: {text}\n")

        else:

            for p in person:

                self.print_slow(f"\n\t{a}: {p} {text}\n")



    def name(self):

        s.print_dialog(f"{l}", " Quel est ton nom ?\n")

        # s.next()

       ## Voir si cette ligne est instructif##

        s.print_slow("Veuillez entrer votre nom : \n")

        n = input()

        while len(n) < 3:

            print("Il faut un pseudo d'au moins 3 caractères !")

            n = input()

        s.print_dialog(f"{i}", "C'est bien cela ?", f"{n}"",")

        s.choice("[1] Oui.", "[2] Non.")

        c = int(input())

        while c != 1 and c != 2:

            s.print_slow("Vous avez fait une erreur")

        if c == 1:

            return p.set_name(n)

        elif c == 2:

            s.name()



    # Nombre variable si le mot-clé n'est pas passé

    def choice(self, *arguments):

        for c in arguments:

            print(c)



    def next(self):

        a = input()

        while a != "":

            a = input()



   # ↓ Tout ce qui est en rapport avec le côté jouable

    def walk(self):

        s.choice(

            "\n[1] - Déplacement\n[2] - Inventaire\n[3] - Map\n[4] - Sauvegarder")

        s.print_slow("Que voulez vous faire ?")

        ch = int(input())

        while ch != 1 and ch != 2 and ch != 3 and ch != 4:

            s.print_slow("Vous avez fait une erreur.")

            ch = int(input())

        # Mais pourquoi ici mais pas ailleurs

        m = Mappy(json_map(str(coordinate)))

    #   if ch == se mouvoir sur la map

        if ch == 1:

            # Ne touche pas au dir =

            dir = s.directory()

            if dir == 5:

                s.walk()

            return dreenshgard.move(dir)



    #   elif ch == ouvrir l'inventaire

        elif ch == 2:

            # s.open_inventory
            print(p.__dict__)
            # return s.open_inventory
            pass

    #   elif ch == ouvrir la map

        elif ch == 3:

            print(coordinate)

            print(m.get_description())

            return dreenshgard.draw_map()

        elif ch == 4:

            data = {
            "coordinate_x":str(dreenshgard.get_x()),
            "coordinate_y":str(dreenshgard.get_y()),
            # "heros":p
            }

            print(data.items())
            Save.save(data)
            return s.walk()
            # pass



    def directory(self):

        s.choice("[1] - Nord", "[2] - Sud", "[3] - Est",

                 "[4] - Ouest", "[5] - Retour")

        dir = int(input())

        while dir != 1 and dir != 2 and dir != 3 and dir != 4 and dir != 5:

            s.print_slow("Vous avez fait une erreur.")

        return dir



    # ↓ Tout ce qui est en rapport avec les fonctionnalités du côté mouvable

    def open_inventory(self, i):

        if i == "i":

           # Inventory()

            pass



    def quest(self):

        print("ici y a une quête")

        # Quest()



    def quit(self, echap):

        if echap == "quit":

            # Qui ramène au menu

            # Quit()

            pass



    def save(self, save):

        if save == "save":

            # Json_write(),

           # s.print_slow("Votre partie a été sauvegarder.")

            pass



    def battle(self):

        #   battle de Chrisline

        battle_round = randint(1, 5)

        if battle_round == 1 or battle_round == 4:

            #   Battle()

            pass



    def battle_fixe(self):

        #   Battle()

        pass





while True:

    s = Story()



    if token_story == 0:

        # LE RÊVE

        # s.print_slow("L'écho d'un combat fait rage. J'entends des cris, mais je n'arrive pas à les discerner.")

        # s.next()



        # s.print_slow("Je n'ai pas le temps de regarder ailleurs, des ennemis arrivent. Des poulpes se jettent sur moi mais je les esquive avec aisance, ma rapidité me permet d'être à l'aise sur l'eau.")

        # s.next()



        # s.print_dialog(f"{i}", "Le Médaillon de L**** fonctionne parfaitement !")

        # s.next()



        # s.print_slow("\nMais en tentant d'esquiver l'un d'eux, je trébuche lamentalement sur un poisson, rendant toutes mes actions précédente inutile.")

        # s.next()



        # s.print_slow("À cet instant, un poulpe m'attrape la jambe et me tire dans les profondeurs des abysses.")

        # s.next()



        # s.print_slow("Avant d'être immerger, je vois au loin une immense silhouette ressemblant à un pouple humanoïde géante.")

        # s.next()



        # s.print_slow("Son cri était tellement puissant que toute la caverne se mit à trembler.")

        # s.next()



        # s.print_very_slow("\n...\n")

        # s.next()



        # DANS L'ECOLE

        # s.print_slow("Je sursaute et manque de tomber de ma chaise. La salle était vide et tous les élèves étaient déjà rentrer.")

        # s.next()



        # s.print_slow("La sonnerie retentit et une voix annonce la fermeture de l'école dans quelques minutes.")

        # s.next()



        # s.print_dialog(f"{i}","Tiens, tu es encore ? Est-ce que tu pourrais ranger ses livres dans la bibliothèque avant de rentrer, s'il te plait ?")

        # s.next()



        # s.print_slow("Sans même me laisser le temps de répondre, le professeur s'en alla. \n")

        # s.next()



        # s.print_slow("Je me lève difficilement après ma sieste cauchemardesque.")

        # s.next()



        # s.print_slow("Le calme de l'école lui donnait un air abandonnée, cependant les quelques cris de la cour me soulager, je n'étais pas seul.")

        # s.next()



        # s.print_slow("Je prends mes affaires et les livres que mon professeur m'a demandé d'apporter.\n")

        # s.next()

        # LE COULOIR

        # s.print_slow("Les couloirs sont vides, la lumière du soleil qui se couche me donne envie de reprendre ma sieste.")

        # s.next()



        # s.print_slow("Je pousse lentement la porte de la bibliothèque et l'odeur du bois me chatouille les narines.")

        # s.next()

        # Bibliothèque

        # s.print_slow("Voyant que la fermeture approche à grand pas, je dépose les livres rapidement et manque le livre qui s'était accroché à ma manche.")

        # s.next()



        # s.print_slow("Le bouquin tombe avec un bruit sourd et s'ouvre, le dessin d'un tétagramme apparaît.\n")

        # s.next()



        # s.print_slow("Voulez-vous ramasser le bouquin?\n")

        # #Essayer de mettre en ralentie(mais fonctionne pas, les s.choice)

        # s.choice(("[1] Oui."), ("[2] Non."))

        # c = int(input())



        # while c != 1 and c != 2:

        #     s.print_slow("Vous avez fait une erreur.")

        #     c = int(input())



        # if c == 1:

        #     s.print_slow("Je tends ma main pour ramasser le bouquin et mes doigts frôlent le tétagramme.")

        #     s.next()

        #     s.print_very_slow("\n...")

        #     s.print_slow("\nSoudainement une lumière blanche envahie la pièce et je ferme mes yeux malgré moi.")

        #     s.next()



        # elif c == 2:

        #     s.print_slow("Je dépose mes derniers livres et me précipite vers la sortie, la sortie annonçant la fermeture de l'établissement retentie.")

        #     s.next()

        #     s.print_very_slow("\n...")

        #     s.next()

        #     s.print_slow("\nSoudainement une lumière blanche envahie la pièce et je ferme mes yeux malgré moi.")

        #     s.next()

        #     s.print_slow("Sans même ouvrir les yeux, je sens que je tombe et me cogne les fesses.\n")

        #     s.next()

        #     #Perte de 10 PV.



        # s.print_very_slow("...\n")

        # s.next()

        # Isekai

        # s.print_slow("Mes yeux me piquent encore à cause de la lumière, j'entends des cris, des pleurs et des rires et même le bruit...")

        # s.next()

        # s.print_dialog(f"{p.get_name()}"," Du feu...?")

        # s.next()

        # s.print_dialog(f"{i}", "ATTENTION !\n")

        # s.next()

        # s.print_slow("Deux bruits de métaux s'entrechoquent juste en face de moi.")

        # s.next()

        # s.print_slow("J'ouvre les yeux et je vois une silhouette qui fait deux têtes de plus que moi, quand mes yeux s'habitue finalement à la lumière tamisée, je peux discener des...oreilles?")

        # s.next()

        # s.print_slow("L'homme tourne sa tête vers moi, je vois sur son visage un groin.")

        # s.next()

        # s.print_dialog(f"{p.get_name()}"," Un cochon ?!")

        # s.next()

        # s.print_dialog(f"{i}"," Dépêche-toi de te lèver.\n")

        # s.next()

        # s.print_slow("J'exécute sans broncher et en reculant, ma main touche quelque chose de doux.")

        # s.next()

        # s.print_slow("Je sursaute.")

        # s.next()

        # s.print_dialog(f"{i}", "Tu m'as l'air bien compétent, tu devrais pouvoir aider, Valentin.\n")

        # s.next()

        # s.print_slow("Je me retourne afin de voir que ce que je viens de toucher était un mélange de ... cheval-lion qui...parle ?")

        # s.next()

        # s.print_dialog(f"{v.get_name()}","Tiens, attrape ça.\n")

        # s.next()

        # s.print_slow("Avant même de pouvoir terminer mon observation de l'incroyable animal, je me retourne pour regarder le dénommé Valentin.")

        # s.next()

        # s.print_slow("Le cochon me lance une épée usée que j'esquive de justesse. La lame se plante dans la terre.")

        # s.next()

        # s.print_slow("Je lève mon regard dans sa direction, choquer par ce qui vient de se passer, mais le cochon était déjà prêt au combat.")

        # s.next()

        # s.print_slow("Il avait raison, un monstre était en train de foncer tout droit sur nous.")



        # AJOUT DU TUTO COMBAT

        # TUTO COMBAT()



        # s.print_very_slow("\n...Quelques heures plus tard...\n")

        # s.next()

        # s.print_slow("Je suis épuiser, je m'assois au sol après toutes les batailles qu'on vient de mener.")

        # s.next()

        # s.print_slow("Tout mon corps me fait mal, mais je relève ma tête pour enfin pouvoir visionner l'endroit dans lequel je suis.")

        # s.next()

        # s.print_slow("C'est un village comme dans les jeux vidéos ou dans les histoires fantastique qu'on trouve dans les bouquins.")

        # s.next()

        # s.print_slow("Toutes les maisons sont faites de bois et ils avaient tous pris feu. Des corps de monstres et d'humains longaient le sol.")

        # s.next()



        # s.print_dialog(f"{i}"," Comment vas-tu ?")

        # s.next()

        # s.choice("[2]- Je vais bien, merci.", "[2]- Comment peux-tu me demander ça ?!")

        # c = int(input())

        # while c != 1 and c != 2:

        #     s.print_slow("Vous avez fait une erreur")

        #     c = int(input())

        # s.print_dialog(f"{v.get_name()}"," Je suis désolé d'interrompre votre discussion, mais Loic, nous avons des gens à sauver.")

        # s.next()

        # s.print_slow("Je pouvais enfin poser un nom sur cette créature mythique, Loic.")

        # s.next()

        # s.print_slow("Il relève la tête vers celui qui vient de l'interpeler et soupir.")

        # s.next()

        # s.print_dialog(f"{l}", " Je sais. Mais tu ne peux pas sauver ce village tout seul.")

        # s.next()

        # s.print_dialog(f"{v.get_name()}", " Que veux-tu dire par là?\n")

        # s.next()

        # s.print_slow("Loic ne répond pas, à la place, il se tourne vers moi.")

        # s.next()

        # s.print_slow("Je sens les ennuies arriver.")

        # s.next()



        # p = s.name()

        # s.print_dialog(f"{i}"," Ravie de te rencontrer, "f"{p.get_name()}")

        # s.next()

        # s.print_dialog(f"{l}", " Je m'appelle Loic et voici mon compagnon de voyage, Valentin.\n")

        # s.next()

        # s.print_slow("Je lance un regard à Valentin, il me met légèrement mal à l'aise, contrairement à Loic qui est beaucoup plus prévenant.")

        # s.next()

        # s.print_dialog(f"{l}", " Je ne vais pas passer par quatre chemins, on a besoin de ton aide.")

        # s.next()

        # s.print_dialog(f"{l}", " Tu es doué au combat. Aide-nous à sauver le village.\n")

        # s.next()

        # s.print_slow("Il avait trop d'informations.")

        # s.next()

        # s.print_slow("Beaucoup trop d'informations.\n")

        # s.next()

        # s.print_slow(

        #     "Soudain, un cri retentit. Je n'avais pas le temps de réfléchir, des gens avaient besoin d'aide.")

        # s.next()

        # s.print_slow("De mon aide.")

        # s.next()

        # s.print_slow(

        #     "Et moi, j'avais aussi besoin d'eux pour comprendre ma situation.")

        # s.next()

        # s.print_dialog(f"{p.get_name()}", " Je vous accompagne.\n")

        # s.next()

        # # s.save()

        token_story += 1



#   MOMENT JOUABLE

    coordinate = str(dreenshgard.get_x()) + "," + str(dreenshgard.get_y())

    m = Mappy(json_map(str(coordinate)))

    s.walk()
    if token_event == False:

        print(m.get_description_before())

    if token_event == True:

        print(m.get_description())

    print(coordinate)

    if m == "3,2":

        s.quest()

    if coordinate == "2,4":

        s.quest()

    if coordinate == "1,0" and token_story == 1:

        #   Event à l'église

        s.print_slow(

            "En arrivant devant une bâtisse qui ressemble à une église, on entend une voix rauque s'élever dans le ciel.")

        s.next()

        s.print_dialog(f"{i}", " Dépêches-toi de rentrer dans l'église !")

        s.next()

        s.print_slow(

            "Je ne pouvais pas bien discener la personne vêtue de blanc qui venait de crier.")

        s.next()

        s.print_slow(

            "Mais je pouvais clairement voir une queue apparente. Avec des écailles. Il était entouré de monstres.")

        s.next()

        s.print_slow(

            "En tournant ma tête, vers la direction où l'homme criait, il avait un petit garçon, assit, secouant une femme allongée au sol.")

        s.next()

        s.print_slow("J'en étais certain. Elle était morte.")

        s.next()

        s.print_slow(

            "Un homme le tire pour l'éloigner du corps mort mais le garçon ne voulait pas bouger.")

        s.next()

        s.print_slow(

            "L'homme vêtu de blanc se retourne et je peux voir à son visage que c'est un dragon.")

        s.next()

        s.print_slow(

            "Après avoir vu un cochon et un lion qui parlent, je ne suis plus surpris de grand chose, on dirait...\n")

        s.next()

        s.print_slow(

            "Le dragon se mit aux côtés du garçon qui attirer curieusement les démons. Il contre le coup d'un monstre en grimaçant.")

        s.next()

        s.print_dialog(f"{i}", "Bon, maintenant, tu vas te lever, oui ?!")

        s.next()

        s.print_slow("Hurla le dragon en le prenant par le bras.")

        s.next()

        s.print_slow(

            "L'homme qui tirait le garçon pris la parole avec beaucoup d'inquiétude.")

        s.next()

        s.print_dialog(

            f"{i}", " Thari, il faut qu'on aille à l'église. On reviendra chercher ta maman, c'est promis.")

        s.next()

        s.print_slow("Un frisson parcourut tout mon corps.")

        s.next()

        s.print_dialog(f"{v.get_name()}", " Gamin. C'est à nous de jouer.")

        s.next()

        s.battle_fixe()

        s.print_very_slow("\n...\n")

        s.next()

        s.print_slow(

            "Après avoir décimer tous les monstres. Je regarde autour de moi, le dragon avait disparu.")

        s.next()

        s.print_dialog(f"{v.get_name()}", " Rentrons dans l'église.")

        s.choice("[1] - D'accord", "[2] - Non, je n'ai pas envie")

        c = int(input())

        while c != 1 and c != 2:

            s.print_slow("Vous avez fait une erreur")

            c = int(input)

        if c == 1:

            s.print_dialog(f"{v.get_name()}", " Bien.")

            s.next()

        elif c == 2:

            s.print_slow(

                "En refusant sa demande, Valentin s'approche de moi. Je regrette ma réponse.")

            s.next()

            s.print_slow(

                "Il m'attrape par le col et me tire de force à l'intérieur...")

        s.print_very_slow("\n...\n")

        s.next()

        s.print_slow(

            "J'aurais penser que l'atmosphère serait meilleur l'intérieur mais c'est tout le contraire, les villageois se crient dessus.")

        s.next()

        s.print_dialog(

            f"{vill}", " J'en suis quasiment sûr que c'est de sa faute.")

        s.next()

        s.print_slow(

            "Un homme se lève et pointe du doigt le jeune garçon qu'on venait de voir.")

        s.next()

        s.print_dialog(

            f"{vill}", " Réfléchissez, depuis que lui et sa famille sont ici, les monstres deviennent de plus en plus nombreux.")

        s.next()

        s.print_slow("L'homme commençe son monologue sans jamais s'arrêter.")

        s.next()

        s.print_dialog(f"{i}", " Tais-toi...")

        s.next()

        s.print_slow(

            "Je tourne ma tête vers la petite voix qui se trouvait à ma droite. C'était le dragon de tout à l'heure.")

        s.next()

        s.print_slow(

            "L'homme ne semble pas l'avoir entendu. Le dragon répéta.")

        s.next()

        s.print_slow("Mais l'homme cria de plus en plus fort.")

        s.next()

        s.print_slow(

            "Il se redresse et s'avance avant d'attraper le villageois.")

        s.next()

        s.print_dialog(f"{i}", " Silence.")

        s.next()

        s.print_slow(

            "Sans même devoir ajouter un mot de plus, tout le monde se tue.")

        s.next()

        s.print_dialog(f"{vill}", " Je suis désolé...Mon père Kai.")

        s.next()

        s.print_dialog(f"{k.get_name()}", "Bien pui...")

        s.next()

        s.print_slow(

            "Avant même que le dragon puisse terminer sa phrase, un hurlement se fait retentir dans l'immense salle de l'église.")

        s.next()

        s.print_slow("Des monstres avaient réussi à entrer dans l'église.")

        s.next()

        s.print_slow(

            "Valentin et moi, nous nous débrouillons pour aider le plus de personnes mais ils étaient beaucoup trop nombreux.")

        s.next()

        s.print_slow(

            "Le villageois qui était rempli de confiance tout à l'heure noya son pantalon par la peur.")

        s.next()

        s.print_slow(

            "Un monstre était si proche de lui qu'un coup de griffe pouvait le tuer. Il hurla.")

        s.next()

        s.print_slow(

            "Le monstre salivait, il leva son bras, prêt à le tuer d'un coup mais une petite ombre le sauve in extremis.")

        s.next()

        s.print_slow(

            "Un petit dragon était devant le villeagois et le monstre devant lui était décapité.")

        s.next()

        s.print_slow(

            "En voyant le petit dragon, Thari se mit à hurler, il griffait son corps dans tous les sens.")

        s.next()

        s.print_slow(

            "Dans un hurlement féroce, il repoussa sa tête en arrière, on pouvait à présent voir des petites cornes apparaitrent sur son front.")

        s.next()

        s.print_slow(

            "Le blanc de ses yeux avaient noircit, ses pupilles violettes innoncentes étaient rempli de rage.")

        s.next()

        s.print_slow(

            "Il se jetta un à un sur les monstres et les élimina d'une traite. Laissant derrière lui uniquement des monstres sans vie.")

        s.next()
        s.print_slow("Quand il se redressa, quelque chose de noir avait ronger une partie de son corps gauche, il ressemblait à present à l'un de ses monstres.")
        s.next()
        s.print_dialog(f"{vill}"," Je... je vous l'avais dit !!")
        s.next()
        s.print_slow("Se mit alors à crier le villageois que le petit harcon venait de sauver.")
        s.next()
        s.print_dialog(f"{vill}"," C'est un demon depuis le debut !")
        s.next()
        s.print_slow("En entendant ses paroles, l'homme qui était auprès de l'enfant se lève et l'attrape par le col.")
        s.next()
        s.print_dialog(f"{i}"," Tu n'en as pas marre ?! Laisse mon fils tranquille !\n")
        s.next()
        s.print_slow("Le vieux homme se mit à rire. il venait de dijoncter.")
        s.next()
        s.print_dialog(f"{vill}"," T-Tout s'explique, hahha.. haha... tu es un démon aussi.")    
        s.next()
        s.print_slow("Tout en essayant de se débattre, l'homme attrapa une lame au sol et le plante dans le corps du pere de Thari.")
        s.next()
        s.print_slow("Valentin se précipite pour les séparer mais c'était trop tard. La lame avait toucher un endroit inévitable.")
        s.next()
        s.print_slow("Je pouvais sentir la rage et la haine de Thari montait, j'essaye de me rapprocher de lui le plus rapidement possible mais..")
        s.next()
        s.print_slow("Sans même écouter les gens autour, il tua d'un coup le villageois, laissant du sang coulait le long de son bras.")
        s.next()
        s.print_slow("Tout le monde se mit de nouveau à crier, mais le pretre intervient. Il réussit avec beaucoup de difficulté à faire avaler une fiole qui fit sommeler Thari.")
        s.next()
        s.print_very_slow("\n...\n")
        s.next()
        s.print_slow("Le prêtre Kai a réussit à calmer tout le monde, les monstres ont tous été éliminé par les soldats et par Valentin et moi.")
        s.next()
        s.print_slow("Même si Thari abait sauver des vies, beaucoup de gens ne le voulaient plus dans le village, surtout après sa métamorphose.")
        s.next()
        s.print_slow("Pendant que le dragon soignait nos blessures, il soupira.")
        s.next()
        s.print_dialog(f"{k.get_name()}"," Ton nom est Valentin, c''est bien ça ?")
        s.next()
        s.print_slow("Le dénommé Valentin relève la tête et interroge Kai par un mimique.")
        s.next()
        s.print_dialog(f"{k.get_name()}"," Aussi surprenant soit-il, tu es populaire auprès de l'église de la Lune." )
        s.next()
        s.print_slow("Valentin baisse de nouveau le regard, il se mit de nouveau à essuyer son arme.")
        s.next()
        s.print_dialog(f"{v.get_name()}"," J'ai quitté WaLanTang depuis des années. Ce dojo ne m'appartient plus.")
        s.next()
        s.print_slow("Kai soupira, il avait l'air de connaître le passé de cet homme que je venais de rencontrer.")
        s.next()
        s.print_dialog(f"{l}"," Et si on l'emmener avec nous ?")
        s.next()
        s.print_slow("Une voix s'élève juste derrière moi, je sursaute et brandi t mon arme, ce qui fit rigoler Valentin et Loic.")
        s.next()
        s.print_dialog(f"{l}", " Haha, je suis désolé de t'avoir fait peur.")
        s.next()
        s.print_slow("Je soupire en rangeant mon arme et me décale pour laisser de la place à Loic.")
        s.next()
        s.print_slow("En passant à côté du dragon, je sentis un sentiment de mal-être.")
        s.next()
        s.print_dialog(f"{k.get_name()}"," Je suis prêt à confier Thari à Valentin, mais qui es-tu, toi ?")
        s.next()
        s.print_slow("Son regard était sévère, pour une raison que j'ignore, le Père Kai avait l'air de tenir au petit garçon.")
        s.next()
        s.print_dialog(f"{l}"," Ne soit pas comme ça, si j'étais bon au combat, je vous aurez aider.")
        s.next()
        s.print_slow("Kai continuait à le fixer, puis il tourne son regard vers moi. Après une longue minute de silence et des baisses basses qu'un soldat était venu lui faire, il prit la parole.")
        s.next()
        s.print_dialog(f"{k.get_name()}"," J'aurais besoin de ton aide, Valentin.")
        s.next()
        s.print_slow("Il y a des chances que le monstre qui se trouve dans les ruines après la forêt amplifie les pouvoirs de Thari.")
        s.next()
        s.print_slow("Valentin continue de nettoyer sa lame, ne regardant pas le dragon qui croisait ses bras contre le mur de l'église. Mais on pouvait voir à ses oreilles qu'il était attentif à chaque mot que Kai disait.")
    #s.walk()
        s.print_dialog(f"{k.get_name()}"," Je lui ai apposer mon sceau, grâce à ça, il pourrait tenir le coup pour un moment mais si nous éliminons pas rapidement ce démon, il risque de détruit plus que ce village.")
        s.next()
        s.print_slow("En entendant la fin de sa phrase, l'homme-cochon relève finalement sa tête et plonge son regard dans celui du prêtre.")
        s.next()
        s.print_slow("Il venait de toucher un point sensible.")
        s.next()
        s.print_dialog(f"{v.get_name()}", " De toute façon, je n'ai pas le choix, hein Line ?")
        s.next()
        s.print_slow("fit Valentin en lançant un sourire au dragon, qui le rendit aussitôt.Il se relève, mit son arme sur son dos et se tourne vers moi.")
        s.next()
        s.print_dialog(f"{v.get_name()}"," On y va, gamin ?")

