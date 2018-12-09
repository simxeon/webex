class Snake:
    def __init__ (self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name


python = Snake("idle")
anaconda = Snake("boost")


print (python.name)
python.change_name("Xu mai")
print (anaconda.name)
print (python.name)