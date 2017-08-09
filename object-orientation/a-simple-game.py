# 获取输入并解析出输入对应的动作
def get_input():
    command = input(":").split()
    verbo_word = command[0]
    if verbo_word in verb_dict:
        verb = verb_dict[verbo_word]
    else:
        print("Unknown verb {}".format(verbo_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))

# 具体的动作
def say(noun):
    return "You said {}".format(noun)

class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc


# 创建一个继承自游戏对象类的哥布林类
class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)
    
    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off."
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health -= 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
        else:
            msg = "I'm not strong enough, I can only hit goblin."
    else:
        msg = "There is no {} here.".format(noun)
    return msg

goblin = Goblin("Gobbly")

# 具体的动作
def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)


# 将动词和动作对应起来
verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit,
}
while True:
    get_input()
