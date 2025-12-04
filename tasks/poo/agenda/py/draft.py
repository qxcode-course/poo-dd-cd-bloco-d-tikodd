
class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def __eq__(self, other):
        return isinstance(other, Fone) and self.id == other.id and self.number == other.number

    def __str__(self):
        return f"{self.id}:{self.number}"


class Contact:
    def __init__(self, name: str):
        self.name = name
        self.fones: list[Fone] = []
        self.favorite = False

    def add_fone(self, fone: Fone):
        # add only if id not present (avoid duplicate ids)
        for f in self.fones:
            if f.id == fone.id:
                return
        self.fones.append(fone)

    def __str__(self):
        phones = ", ".join(str(f) for f in self.fones)
        return f"{self.name} [{phones}]"


class Agenda:
    def __init__(self):
        self.contacts: dict[str, Contact] = {}

    def add(self, name: str, fones: list[Fone]):
        if name in self.contacts:
            c = self.contacts[name]
            for f in fones:
                c.add_fone(f)
        else:
            c = Contact(name)
            for f in fones:
                c.add_fone(f)
            self.contacts[name] = c

    def rm_fone(self, name: str, index: int) -> bool:
        if name not in self.contacts:
            return False
        c = self.contacts[name]
        if 0 <= index < len(c.fones):
            c.fones.pop(index)
            return True
        return False

    def rm(self, name: str) -> bool:
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def toggle_fav(self, name: str) -> bool:
        if name in self.contacts:
            self.contacts[name].favorite = not self.contacts[name].favorite
            return True
        return False

    def favs(self) -> list[str]:
        lines = []
        for name in sorted(self.contacts.keys()):
            c = self.contacts[name]
            if c.favorite:
                lines.append(f"@ {c}")
        return lines

    def search(self, pattern: str) -> list[str]:
        p = pattern.lower()
        lines = []
        for name in sorted(self.contacts.keys()):
            c = self.contacts[name]
            if p in name.lower():
                lines.append(f"- {c}")
                continue
            for f in c.fones:
                if p in f.id.lower() or p in f.number.lower():
                    lines.append(f"- {c}")
                    break
        return lines

    def show(self) -> list[str]:
        # return list of lines in alphabetical order by name
        lines = []
        for name in sorted(self.contacts.keys()):
            lines.append(f"- {self.contacts[name]}")
        return lines


def parse_fone(token: str) -> Fone:
    # token form id:number
    if ":" not in token:
        return Fone(token, "")
    id, number = token.split(":", 1)
    return Fone(id, number)


def main():
    import sys

    agenda = Agenda()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        cmd = parts[0]
        # echo command prefixed by $
        print(f"${line}")
        if cmd == "end":
            break
        elif cmd == "add":
            # add name fone1 fone2 ...
            if len(parts) >= 2:
                name = parts[1]
                fones = [parse_fone(t) for t in parts[2:]]
                agenda.add(name, fones)
        elif cmd == "show":
            for name in sorted(agenda.contacts.keys()):
                c = agenda.contacts[name]
                prefix = "@ " if c.favorite else "- "
                phones = ", ".join(str(f) for f in c.fones)
                print(f"{prefix}{c.name} [{phones}]")
        elif cmd == "tfav":
            if len(parts) >= 2:
                agenda.toggle_fav(parts[1])
        elif cmd == "favs":
            for l in agenda.favs():
                print(l)
        elif cmd == "search":
            if len(parts) >= 2:
                res = agenda.search(" ".join(parts[1:]))
                for l in res:
                    print(l)
        elif cmd == "rmFone":
            if len(parts) >= 3:
                name = parts[1]
                try:
                    idx = int(parts[2])
                except ValueError:
                    print("fail: indice de telefone invalido")
                    continue
                ok = agenda.rm_fone(name, idx)
                if not ok:
                    print("fail: indice de telefone invalido")
        elif cmd == "rm":
            if len(parts) >= 2:
                agenda.rm(parts[1])


if __name__ == "__main__":
    main()

