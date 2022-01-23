# {
#     "workbench.colorTheme": "Dark-Dracula",
#     "explorer.confirmDragAndDrop": false,
#     "explorer.confirmDelete": false,
#     "workbench.sideBar.location": "right",
#     "git.confirmSync": false,
#     "terminal.integrated.scrollback": 100000,
#     "workbench.colorCustomizations": {
#         "tab.activeBackground": "#008080",
#     },
#     "editor.minimap.enabled": false,
#     "editor.rename.enablePreview": false,
#     "editor.rulers": [80]
# }





class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def sulypont_szamitas(self, masik_pont):
        """ A súlypontom a másik ponttal. """
        mx = (self.x + masik_pont.x) / 2
        my = (self.y + masik_pont.y) / 2
        return (mx, my)

p = Pont(3, 4)
q = Pont(5, 12)
r = p.sulypont_szamitas(q)
print(r)

# Ua mint két sorral fentebb, csak beszédesebb kimenettel
print(f"A két pont súlypontja: {Pont(3, 4).sulypont_szamitas(Pont(5, 12))}")

