
#
# Catware Insult Generator
#
# Просьба: не тестировать на слабонервных быках
#

from random import choice, randint
import markovify

insults = "бык,мефедрон,снюс,ворон,мусор,понос,помой,карась,хуй,таракан,урод,шпорк,баклажан,овощ,фрукт,сахарок,барсик,пупс,неосарт,линуксоид,виндузятник,маковод,туалет,толкан,толчок,пепел,краб,макинтош,дельфин,трюфель,бсдшник,цыган,чмо,пидор,задрот,кисель,ботан,гандонео,пушок,зефир,негативчик,быдлан,третьеклассник,газ,еблан,уёбок,пидорас,гандон,педик,презик,волос,негр,убунтовод,арчегомосек,шоколад,козёл,бычара,козлище,козён,обама,навальнёнок,говноед,трамп,гей,гомосек,свин,кобель,хохол,сатана".split(",")
adjectives = "ебаный,обоссаный,поднадусёровый,слабонервный,жирный,вонючий,кастрированный,ебучий,невменяемый,блядский,черномазый,оттраханный,обдроченный".split(",")
geninsult_first = "блядо,члено,говно,хуе,желто,черно,много,верто,мало,швайно,глино,гнидо,писько,сопле,криво,пидо,пердо,срало,срано,порно,без".split(",")
geninsult_second = "рылый,жопый,ротый,ебливый,ссущий,срущий,ухий,клювый,зубый,хвостый,бля".split(",")
geninsult_endings = "лёт,ед,блюй,рот,член,мес,пидор,поезд,танк,дроч,скотч,крейсер,дрочер,дорас".split(",")
abusives = "блять,сука,ебать,пиздец,нахуй".split(",")
dick_adjectives = "трахо,ебо,сексо,порно,конче,негро".split(",")
dicks = "член,штырь,штепсель,кол,баклажан,трон,дик,ствол,крючок,питон,пайтон,шланг,кол".split(",")
demonstrative_verbs = "иди,пиздуй,шуруй,вали,ебись".split(",")
verbs = "ебал,насиловал,трахал,пиздил,ножом резал,на хую вертел,на хуе до 12000 об/с разгонял,оплодотворял".split(",")
relatives_impad = "мать,бабушку,сестру,бабку,мамку,тёщу,сноху,дочь,дочку".split(",")
places = "нахуй,в пизду,отсюда,к хуям,вон туда,сосать".split(",")
whose = "мамкин,папкин,сосалкин,шалавкин,плюшкин".split(",")
fem_insults = "шалава,макака,обезьяна,шлюха,сосалка,дура,проститутка,пизда,махнатка,дырка,дыра,вонючка,конча,пылинка,хохлинка,корова,бабка,уродина,фиона,пепеляшка,акула,курица".split(",")
fem_adjectives = "ебаная,обоссаная,поднадусёровая,слабонервная,жирная,вонючая,кастрированная,ебучая,невменяемая,блядская,черномазая,оттраханая,обдроченная,конченая".split(",")
item_adjectives_fem = "широкая,огромная,мелкая,выебанная,гигантская,обдолбанная".split(",")
smileys = list("😆🤣😡🤬😈👿👺👹🤡🖕🏻🤘🏻😏🧠")

insult = "Оскорбление не придумал"

def genlaugh():
        lg = ""
        parts = "Ах,АХ,ах,аХ,Аъ,пх,Пх,ПХ,пХ,аЪ,пз,".split(",")
        for x in range(randint(1, 20)):
                lg += choice(parts)
        return lg

def writeTo(text, target):
        file = open(target, "a", encoding="utf-8")
        file.write(text + "\n")
        file.close()

def genscob():
        sc = ""
        scobs = "),0,-,_".split(",")
        for x in range(randint(1, 20)):
                sc += choice(scobs)
        return sc

def genins():
        way = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        if way == 1:
                insult = f"{choice(demonstrative_verbs)} {choice(places)}, {choice(insults)} {choice(adjectives)}"
        if way == 2:
                insult = f"{genlaugh()} {choice(abusives)} ты {choice(insults)} {choice(whose)}{genscob()}"
        if way == 3:
                insult = f"пососи мой {choice(dick_adjectives)}{choice(dicks)}, {choice(adjectives)} {choice(whose)}"
        if way == 4:
                insult = f"{choice(abusives)} ты {choice(geninsult_first)}{choice(geninsult_second)}"
        if way == 5:
                insult = f"{choice(abusives)} ты {choice(geninsult_first)}{choice(geninsult_endings)}"
        if way == 6:
                insult = f"{choice(demonstrative_verbs)} {choice(places)}, {choice(fem_insults)} {choice(fem_adjectives)}"
        if way == 7:
                insult = f"{genlaugh()} {choice(abusives)} ты {choice(fem_insults)} {choice(whose)}{genscob()}"
        if way == 8:
                insult = f"{genlaugh()} {choice(abusives)} у тебя {choice(fem_insults)} {choice(item_adjectives_fem)}"
        if way == 9:
                insult = f"{choice(abusives)} ты {choice(geninsult_first)}{choice(geninsult_second)}"
        if way == 10:
                insult = f"{choice(abusives)} ты {choice(geninsult_first)}{choice(geninsult_endings)}"
        if way == 11:
                insult = f"да я твою {choice(relatives_impad)} {choice(verbs)}{genscob()} понимаешь???{genscob()}"
        if way == 12:
                insult = f"я тебе щас {choice(insults)} в рот засуну, {choice(insults)} ты {choice(adjectives)}{genlaugh()}"
        insult = insult.upper()
        insult += choice(smileys) * randint(0, 5)
        if choice([True, False]):
                insult += f" {choice(demonstrative_verbs)} {choice(places)}".upper() + choice(smileys) * randint(0, 6)
                if choice([True, False]):
                        insult += f" {choice(insults)} {choice(adjectives)} {genlaugh()}".upper()
        return insult

print("Готов к работе. Нажмите Enter, чтобы сгенерировать переполняющее негативом гавно")

while True:
        input()
        print("================================================================================")
        a = genins()
        print(a)
