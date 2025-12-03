Class Fone:
    def__init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def__str__(self):
        return f"{self.id}:{self.number}"

Class Contact:
    def__init__(self, name: str):
        self.name = name
        self.fones: list[Fone] = []
        self.favorite = False

    def add_fone(self, fone: Fone):
        self.fones.append(fone)

    def remove_fone(self, index: int):
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
        else:
            print("fail: indice de telefone invalido")

    def matches(self, pattern: str):
        if pattern.lower() in self.name.lower():
            return True
        for f in self.fones:
            if pattern.lower() in f.id.lower() or patter.lower() in f.number.lower():
                return True
        return False
 Class Fone:
    def __init__(self. id: str =",number: str ="):
        self.__id:str = id;
        self.__number: str = number;

def __str__(Self) -> str:
    return f"{self.getld()}:{self.getNumber()}";

def getld(self) -> str:
    return self.__id;

def getNumber(self) -> str:
    return self.__id;

def getNumber(self) -> str:
    return self.number;

def isValid(self):
    allowedCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","(,)"];
    fone = list(self.getNumber());

    for char in fone:
        if char not in allowedCharacters: 

fdfsgsdf
sdfsdsdffsd
lkljnnjhjnhqwabcdefghijklmnopqrstuvwxyz
abcdefghijklmnopqrstuvwxyz
abcdefghijklmnopqrstuvwxyz
jhbjhkjhjj
kikikkkhhnbhnhjjhnbhuoih[[0´999999095636.+.,kmnhb
kikikkkhhnbhnhjjhnbhuoih
]]
jhjjhjkkJDKSJKJK
IJFSFJDF
SJDJASKJD
askdjaskdj
kjsdasiiwofhs
sdjhsjjhaswiuasdiasjdajs
aajshdahsjahajh
asdhasdaksjkj

