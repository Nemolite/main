##################################

#    Итак, что же такое «декоратор»?

#######################################
def makebold(fn):
    def wrapped():
        return "makebold" + "  "+fn()
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "makeitalic" + "  " + fn()
    return wrapped
 
@makebold
#@makeitalic
def hello():
	return "плюс hello"

tmp1 = hello()
print (tmp1)

######################################

# Функции в Python'e являются объектами

#######################################

word = "да"

print(word.capitalize()) # заглавная буква

def func1(num=21):
	return num

new_obj1 = func1

print(new_obj1(34))

del func1

print(new_obj1(18))


def talk():
    def whisper(word="да"):
        return word.lower()+"...";
    print(whisper())

talk()

######################################

#  Ссылки на функции

print("################################")

def getTalk(type="shout"):
    def shout(word="да"):
        return word.capitalize()+"!"
 
    def whisper(word="да") :
        return word.lower()+"...";
 
    if type == "shout":
        return shout
    else:
        return whisper

talk1 = getTalk()

print("Первый==",talk1)

print("Второй==",talk1())
print("Третий==",getTalk("whisper")())

