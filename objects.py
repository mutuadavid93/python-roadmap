# Objects are a result on instantiating a class.

class Duck:
    sound = 'Quaack!'

    def speak(self):
        print(self.sound)

def main():
    duckduckgo = Duck()   # class instantiation
    duckduckgo.speak()

# Define entry point into program
if __name__ == '__main__': main()