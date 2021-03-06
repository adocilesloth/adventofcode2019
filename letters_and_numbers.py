import numpy as np
#from sys import stdout

class characters():
    '''Creates letters  and  number with
       5 pix width and 6 pix height
       Can try to find  letters in image'''
    
    def __init__(self):
        self.char = {}

        self.char['A'] = np.array([[0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,1,1,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0]])

        self.char['B'] = np.array([[1,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,1,1,0,0]])

        self.char['C'] = np.array([[0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,0,0],
                                   [1,0,0,0,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0]])

        self.char['D'] = np.array([[1,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,1,1,0,0]])

        self.char['E'] = np.array([[1,1,1,1,0],
                                   [1,0,0,0,0],
                                   [1,1,1,0,0],
                                   [1,0,0,0,0],
                                   [1,0,0,0,0],
                                   [1,1,1,1,0]])

        self.char['F'] = np.array([[1,1,1,1,0],
                                   [1,0,0,0,0],
                                   [1,1,1,0,0],
                                   [1,0,0,0,0],
                                   [1,0,0,0,0],
                                   [1,0,0,0,0]])

        self.char['G'] = np.array([[0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,0,0],
                                   [1,0,1,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,1,0]])

        self.char['H'] = np.array([[1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,1,1,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0]])

        self.char['I'] = np.array([[1,1,1,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0],
                                   [1,1,1,0,0]])

        self.char['J'] = np.array([[0,0,1,1,0],
                                   [0,0,0,1,0],
                                   [0,0,0,1,0],
                                   [0,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0]])

        self.char['K'] = np.array([[1,0,0,1,0],
                                   [1,0,1,0,0],
                                   [1,1,0,0,0],
                                   [1,0,1,0,0],
                                   [1,0,1,0,0],
                                   [1,0,0,1,0]])

        self.char['L'] = np.array([[1,0,0,0,0],
                                   [1,0,0,0,0],
                                   [1,0,0,0,0],
                                   [1,0,0,0,0],
                                   [1,0,0,0,0],
                                   [1,1,1,1,0]])

        self.char['M'] = np.array([[1,0,0,1,0],
                                   [1,1,1,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0]])

        self.char['N'] = np.array([[1,0,0,1,0],
                                   [1,1,0,1,0],
                                   [1,0,1,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0]])

        self.char['O'] = np.array([[0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0]])

        self.char['P'] = np.array([[1,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,1,1,0,0],
                                   [1,0,0,0,0],
                                   [1,0,0,0,0]])

        self.char['Q'] = np.array([[0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,1,0,0],
                                   [0,1,0,1,0]])

        self.char['R'] = np.array([[1,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,1,1,0,0],
                                   [1,0,1,0,0],
                                   [1,0,0,1,0]])

        self.char['S'] = np.array([[0,1,1,1,0],
                                   [1,0,0,0,0],
                                   [0,1,1,0,0],
                                   [0,0,0,1,0],
                                   [0,0,0,1,0],
                                   [1,1,1,0,0]])

        self.char['T'] = np.array([[1,1,1,1,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0]])

        self.char['U'] = np.array([[1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0]])

        self.char['V'] = np.array([[1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,0,1,0],
                                   [0,0,1,0,0]])

        self.char['W'] = np.array([[1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,1,1,1,0],
                                   [1,0,0,1,0]])

        self.char['X'] = np.array([[1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0]])

        self.char['Y'] = np.array([[1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,0,1,0],
                                   [0,0,1,0,0],
                                   [0,0,1,0,0],
                                   [0,0,1,0,0]])

        self.char['Z'] = np.array([[1,1,1,0,0],
                                   [0,0,1,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0],
                                   [1,0,0,0,0],
                                   [1,1,1,0,0]])
        
        self.char['0'] = np.array([[0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,1,1,0],
                                   [1,1,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0]])
        
        self.char['1'] = np.array([[0,1,0,0,0],
                                   [1,1,0,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0],
                                   [1,1,1,0,0]])
        
        self.char['2'] = np.array([[0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [0,0,0,1,0],
                                   [0,1,1,0,0],
                                   [1,0,0,0,0],
                                   [1,1,1,1,0]])
        
        self.char['3'] = np.array([[0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [0,0,1,0,0],
                                   [0,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0]])
        
        self.char['4'] = np.array([[0,0,1,0,0],
                                   [0,1,1,0,0],
                                   [1,0,1,0,0],
                                   [1,1,1,1,0],
                                   [0,0,1,0,0],
                                   [0,0,1,0,0]])
        
        self.char['5'] = np.array([[1,1,1,1,0],
                                   [1,0,0,0,0],
                                   [1,1,1,0,0],
                                   [0,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0]])
        
        self.char['6'] = np.array([[0,1,1,0,0],
                                   [1,0,0,0,0],
                                   [1,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0]])
        
        self.char['7'] = np.array([[1,1,1,1,0],
                                   [0,0,0,1,0],
                                   [0,0,1,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0],
                                   [0,1,0,0,0]])
        
        self.char['8'] = np.array([[0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,0,0]])
        
        self.char['9'] = np.array([[0,1,1,0,0],
                                   [1,0,0,1,0],
                                   [1,0,0,1,0],
                                   [0,1,1,1,0],
                                   [0,0,0,1,0],
                                   [0,1,1,0,0]])
        return
        
    def get_character(self, character):
        '''Returns the array for character'''
        
        if type(character) == int:
            character = str(character)
        
        return self.char[character]
        
    def find_characters(self, image, x_offset=0, y_offset=0):
        '''Finds the characters in an  image
           Assumes text starts top left and characters
           are 5 pixels wide and 6 pixels high'''
        height = len(image)//6
        width = len(image[0])//5
        
        found_char = ""
        
        if (height*6)+y_offset < len(image):
            print('WARNING: Height is not a multiple of 6. Clipping')
        if (width*5)+x_offset < len(image[0]):
            print('WARNING: Width is not a multiple of 5. Clipping')
            
        for h in range(0, height):
            for w in range(0, width):
                target = image[(h*6)+y_offset:((h+1)*6)+y_offset,(w*5)+x_offset:((w+1)*5)+x_offset]
                for key in self.char.keys():
                    if np.array_equal(target, self.char[key]):
                        #stdout.write(key)
                        found_char += key
                        break
            #stdout.write('\n')
            found_char += "\n"
            
        return found_char