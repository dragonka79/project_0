def derekszogu_e(a, b, c ):
     """
     Három paraméterként megadott szám alapján meghatározza, hogy lehetnek-e 
     azok egy háromszög oldalainak mérőszámai és ha igen, akkor azok 
     derékszögű háromszöget alkotnak-e.
     """
     if (a, b, c ) > (0, 0, 0) and (a + b > c and c + a > b and b + c > a):
          n = (a ** 2) + (b ** 2) - c ** 2
          m = (c ** 2) + (a ** 2) - b ** 2
          l = (b ** 2) + (c ** 2) - a ** 2
          t = 0.0000000001
          if n < t or m < t or l < t:
               return True
          return False
     print("Ezek nem lehetnek egy háromszög oldalai.")
     exit() # Block returning the 'None' return value
print(derekszogu_e(13, 12, -5))
