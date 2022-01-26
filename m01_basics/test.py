# from math import sqrt

# class Pont:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y

#     def kor_kozeppontja(p1, p2, p3, p4):
#         m1 = int((p2.y - p1.y) / (p2.x - p1.x))
#         c1 = int(((p1.y * p2.x) - (p2.y * p1.x)) / (p2.x - p1.x))
#         m2 = int((p4.y - p3.y) / (p4.x - p3.x))
#         c2 = int(((p3.y * p4.x) - (p4.y * p3.x)) / (p4.x - p3.x))
#         u = int((c2 - c1) / (m1 - m2))
#         v = int((c2 * m1 - c1 *m2) / (m1 - m2))
#         return (u,v)


# p1 = Pont(0, 1 + sqrt(5))
# p2 = Pont(1, 1 + (2 * sqrt(2)))
# p3 = Pont(-1, 1)
# p4 = Pont(2, 4)

# print(Pont.kor_kozeppontja(p1, p2, p3, p4))


from math import sqrt

class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def felezopont(p1, p2):
        fx = int((p1.x + p2.x) / 2)
        fy = int((p1.y + p2.y) / 2)
        return (fx, fy)

    def normalvektor(p1, p2):
        n2 = int(p2.x - p1.x)
        n1 = int(-p2.y + p1.y)
        return int(n1 / n2)
    
    def egyenes(p1, p2):
        m = -1 * Pont.normalvektor(p1, p2)
        c = (Pont.normalvektor(p1, p2) * Pont.felezopont(p1, p2)[0] + 
            Pont.felezopont(p1, p2)[1])
        return (m, c)

    def kor_kozeppontja(p1, p2, p3, p4):
        m1 = int((p2.y - p1.y) / (p2.x - p1.x))
        c1 = int(((p1.y * p2.x) - (p2.y * p1.x)) / (p2.x - p1.x))
        m2 = int((p4.y - p3.y) / (p4.x - p3.x))
        c2 = int(((p3.y * p4.x) - (p4.y * p3.x)) / (p4.x - p3.x))
        # u = int((c2 - c1) / (m1 - m2))
        u = int(Pont.egyenes(p3, p4)[1] - Pont.egyenes(p1, p2)[1] / 
                Pont.egyenes(p1, p2)[0] - Pont.egyenes(p3, p4)[0])
        # v = int((c2 * m1 - c1 *m2) / (m1 - m2))
        v = int((Pont.egyenes(p3, p4)[1] * Pont.egyenes(p1, p2)[0] - 
                Pont.egyenes(p1, p2)[1] * Pont.egyenes(p3, p4)[0]) / 
                Pont.egyenes(p1, p2)[0] - Pont.egyenes(p3, p4)[0])
        return (u,v)


# p1 = Pont(3, -3)
# p2 = Pont(1, 1)
# p3 = Pont(-1, 1)
# p4 = Pont(2, 4)

p1 = Pont(0, 1 + sqrt(5))
p2 = Pont(-1, 1)
p3 = Pont(1, 1 + (2 * sqrt(2)))
p4 = Pont(2, 4)

# print(Pont.felezopont(p1, p2))
# print(Pont.normalvektor(p1, p2))
# print(Pont.egyenes(p1, p2))
print(Pont.kor_kozeppontja(p1, p2, p3, p4))