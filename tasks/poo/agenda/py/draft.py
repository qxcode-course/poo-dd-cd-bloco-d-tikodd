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

    def__str__(self):
        fav = "if self.favorite else"
        fones_str = "".join([f]) for i. fone in enumerate(self.fones)
        return f"{fav}{self.name}{fones_str}"

Class Agenda:
    def__init__(self):
        self.contacts: dict[str,  Contact] = {}

        def add_contact(self, name: str, fones: list[Fone]):
            if name not in self.contacts:
                self.contacts[name] = Contact(name)

                



