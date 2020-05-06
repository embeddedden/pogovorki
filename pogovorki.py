#!/usr/bin/env python3

"""
Created on Wed May  6 00:57:54 2020

@author: embden
"""

import random
POGOVORKI = [
    "Алмаз остается алмазом, даже если бросить его в грязь. Татарская поговорка",
    "Батыр без ран не бывает. Башкирская поговорка",
    "Будет прибыль, будут и издержки. Калмыцкая поговорка",
    "Будешь злым — повесят, будешь мягким — раздавят. Татарская поговорка",
    "Будешь сиять тихо — узнаешь много. Татарская поговорка",
    "Вернуться с полпути — тоже смелость. Татарская поговорка",
    "Видел раз — знакомый; видел два — товарищ; видел три — друг. Башкирская поговорка",
    "Все собаки сильны у себя во дворе. Абхазская поговорка",
    "Где дыра — там ветер, где лодырь — там и разговоры. Башкирская поговорка",
    "Голова одинока, зато душа спокойна. Татарская поговорка",
    "Даже красавице ум не помеха. Татарская поговорка",
    "Делай для другого, учись для себя. Абхазская поговорка",
    "Дитя унимай смолоду, жену — с первого раза. Башкирская поговорка",
    "Для океана и капля — прибавление. Калмыцкая поговорка",
    "Дурного не спрашивай: сам скажет. Калмыцкая поговорка",
    "Если все твердят: «Ты крив»- закрой глаз. Осетинская поговорка",
    "Если дал другу коня, не проси беречь его. Башкирская поговорка",
    "Если за сдай не наелся, облизывая посуду не насытишься. Татарская поговорка",
    "Если мир затопит вода, разве утка станет горевать? Татарская поговорка",
    "Если крикнешь в кувшин, то и кувшин на тебя крикнет. Абхазская поговорка",
    "Если умер отец — не забывай его друга. Башкирская поговорка",
    "Есть душа — есть и надежда. Татарская поговорка",
    "Жадный взбесится — в колодце рыбу удит, лентяй взбесится — в праздник работает. Башкирская поговорка",
    "И врага своего корми до смерти! Абхазская поговорка",
    "Из одного полена костра не сложишь. Осетинская поговорка",
    "И ты мулла, и я мулла, кто же коням сена даст? Башкирская поговорка",
    "К любому замку ключ подобрать можно. Татарская поговорка",
    "Как бы далеко ни было, иди дорогою; как бы стар ни был, бери девушку. Калмыцкая поговорка",
    "Как лягушка ни прыгает, а все в своей луже. Калмыцкая поговорка",
    "Как ни зол лебедь — и он своих яиц не бьет. Калмыцкая поговорка",
    "Как подумаешь, так увидишь. Башкирская поговорка",
    "Какова земля, таковы и родники. Татарская поговорка",
    "К кому привыкли, к тому нет уважения. Абхазская поговорка",
    "Ключ подбирают к замку, а не замок к ключу. Осетинская поговорка",
    "Коварная жена — плетка шайтана. Татарская поговорка",
    "Когда бой кончился, появляется много батыров. Татарская поговорка",
    "Кому не повезло утром — не повезет и вечером, кому не повезло вечером — не повезет никогда. Татарская поговорка",
    "Коня за месяц испытаешь, человека — за год. Башкирская поговорка",
    "Красота нужна только на свадьбе, ум — каждый день. Татарская поговорка",
    "Красоту в миску не положишь. Татарская поговорка",
    "Кроме смерти, все, что быстро, хорошо. Калмыцкая поговорка",
    "Куда достанет ногой — ударит, куда дотянет шею — укусит. Калмыцкая поговорка",
    "Лучшую пищу давай другому, лучшую одежду надевай на себя. Калмыцкая поговорка",
    "Мешок котомке не пара. Осетинская поговорка",
    "Мыслями — на троне, задницей — в грязи. Калмыцкая поговорка",
    "Мышь сама себе кошку ищет. Осетинская поговорка",
    "Не лезь своим куском в чужую похлебку. Осетинская поговорка",
    "Не каждый раз на удочке рыбка. Татарская поговорка",
    "Не клади свою ложку туда, где нет твоей миски. Абхазская поговорка",
    "Не поседеет борода — не поумнеет голова. Башкирская поговорка",
    "Не ройся не дне мешка (т. е. не вспоминай прежних обид). Татарская поговорка",
    "Не умеющий плясать музыки не любит. Башкирская поговорка",
    "Не успеет споткнуться, как уже падает. Татарская поговорка",
    "Нечего учить есть зубастого. Осетинская поговорка",
    "Небо украшают звезды, мужчин — борода, женщин — волосы. Татарская поговорка",
    "Незнание — не порок, нежелание знать — большой порок. Башкирская поговорка",
    "Нелюбимый всегда лишний. Башкирская поговорка",
    "Ни о ком не будешь думать — тебя никто не вспомнит. Осетинская поговорка",
    "Одел бедняк — откуда взял? Одел бай — носи на здоровье! Татарская поговорка",
    "Один раз не сумеешь, во второй — научишься. Татарская поговорка",
    "Одним ударом дерева не срубишь. Татарская поговорка",
    "Опасен на сильный, а мстительный. Башкирская поговорка",
    "Подать надежду легко, исполнить — трудно. Осетинская поговорка",
    "Пока есть силы — работай, пока есть зубы — кусай. Татарская поговорка",
    "Пока красавица прихорашивается, свадьба кончается. Татарская поговорка",
    "Понадеявшись на многое, не потеряй малого. Башкирская поговорка",
    "Прежде чем войти, подумай, как выйти. Башкирская поговорка",
    "Приходит без дела — мешает работе, приходит с делом — увеличивает заботу. Татарская поговорка",
    "Про женщину спроси у женщины. Абхазская поговорка",
    "Просьба учит просить. Осетинская поговорка",
    "Река прокладывает не одно русло. Осетинская поговорка",
    "Ростом вышел, а умом нет. Татарская поговорка",
    "С дураком вместе ничего не находи и не теряй. Татарская поговорка",
    "Самое толстое бревно еще не дом. Башкирская поговорка",
    "Светильник, прежде чем потухнуть, вспыхивает. Калмыцкая поговорка",
    "Свинья не видит неба. Калмыцкая поговорка",
    "Себя не возвеличивай, других не унижай. Башкирская поговорка",
    "Сердце девушки — кипящий котел, ни с чем не считается. Татарская поговорка",
    "Сильный победит одного, знающий — тысячу. Башкирская поговорка",
    "Сильный рычит, бессильный — визжит. Калмыцкая поговорка",
    "Сколько бы ни бодался баран, горы не разрушит. Татарская поговорка",
    "Слабый поневоле добр. Абхазская поговорка",
    "Слепой курице — все пшеница. Татарская поговорка",
    "Слово мужчины — всегда одно. Татарская поговорка",
    "Собаки не порычав не подружатся. Татарская поговорка",
    "Собственный запах человеку неизвестен. Калмыцкая поговорка",
    "Снег красив, да ноги стынут. Осетинская поговорка",
    "Солнце тоже далеко, а греет. Осетинская поговорка",
    "Стащив цыпленка, ястреб вернется за вторым. Осетинская поговорка",
    "Стремись завоевать не мир, а его знание. Осетинская поговорка",
    "Сперва напои, потом спрашивай, зачем приехали. Калмыцкая поговорка",
    "Спотыкайся ногами, но не спотыкайся языком. Татарская поговорка",
    "Стреляет криво, а попадает прямо. ( о речи хитреца) Татарская поговорка",
    "У кого ничего нет, тому нечего бояться. Татарская поговорка",
    "У лгуна дом сгорел — никто не поверил. Татарская поговорка",
    "У палки два конца. Калмыцкая поговорка",
    "Умный понимает, глупый слушает. Татарская поговорка",
    "Умный хвалит коня, полоумный — жену, а глупец — сам себя. Башкирская поговорка",
    "Умный сам замечает свою ошибку. Осетинская поговорка",
    "Учить дурака — оживлять мертвеца. Татарская поговорка",
    "Хочешь яблока — ухаживай за яблоней. Татарская поговорка",
    "Что в лесу крикнешь, то и в ответ услышишь. Татарская поговорка",
    "Чужой не простит, свой не убьет. Башкирская поговорка",
    "Щеголь не мерзнет, но дрожит. Татарская поговорка",
    "Ястреб ловит — коршун отнимает. Абхазская поговорка"]

class Pogovorka:
    def __init__(self):
        self.current_position = 0

    def read_pogovorka(self):

        if self.current_position < len(POGOVORKI) and self.current_position >= 0:
            return POGOVORKI[self.current_position]
        else:
            return 'none'

    def read_next_pogovorka(self):

        if self.current_position < len(POGOVORKI):
            self.current_position += 1
        if self.current_position < len(POGOVORKI):
            return POGOVORKI[self.current_position]
        else:
            return 'none'

    def read_prev_pogovorka(self):

        if self.current_position > -1:
            self.current_position -= 1
        if self.current_position >= 0:
            return POGOVORKI[self.current_position]
        else:
            return 'none'

    def read_random_pogovorka(self):

        self.current_position = random.randint(0, len(POGOVORKI)-1)
        if self.current_position >= 0:
            return POGOVORKI[self.current_position]
        else:
            return 'none'
