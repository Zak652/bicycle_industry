# Test file for classes

class musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
class guitarist(object):
    def __init__(self):
        self.sounds = ['boink', 'bow', 'boom']
        
    def solo(self, lenght):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
    def tune(self):
        print('be with you in a moment')
        print("Twoning, sproing, splang")