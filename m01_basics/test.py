

class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


class Teglalap:
    def __init__(self, poz, sz, m):
        self.csucs = poz
        self.szelesseg = sz
        self.magassag = m

    def __str__(self):
        return "({0}, {1}, {2})".format(
            self.csucs, self.szelesseg, self.magassag
            )
    
    def noveles(self, delta_szelesseg, delta_magassag):
        self.szelesseg += delta_szelesseg
        self.magassag += delta_magassag
    
    def mozgatas(self, dx, dy):
        self.csucs.x += dx
        self.csucs.y += dy
    
    def terulet(self):
        return(self.szelesseg * self.magassag)

    def kerulet(self):
        return(2 * (self.szelesseg + self.magassag))
    
    def forditas(self):
        (self.szelesseg, self.magassag) = (self.magassag, self.szelesseg)
    
    def tartalmazza_e(self, p1):
        self.x1 = self.csucs.x + self.magassag
        self.y1 = self.csucs.y + self.szelesseg
        s = ((p1.x < self.x1 and p1.x >= self.csucs.x) and 
            (p1.y < self.y1 and p1.y >= self.csucs.y))
        return s

r = Teglalap(Pont(0, 0), 10, 5)
print(r.tartalmazza_e(Pont(0, 0)))

print(r.tartalmazza_e(Pont(3, 3)))

print(not r.tartalmazza_e(Pont(3, 7)))

print(not r.tartalmazza_e(Pont(3, 5)))

print(r.tartalmazza_e(Pont(3, 4.99999)))

print(not r.tartalmazza_e(Pont(-3, -3)))




