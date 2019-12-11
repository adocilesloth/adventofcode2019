import numpy as np

class intcode_computer():
    
    def  __init__(self, in_put=None):
        '''inits  intcode_computer
           loads whatever in_put is'''
        if in_put is not None:
            self.load_program(in_put)
        else:
            self.program = None
            self.day = None
        self.pointer = 0
        self.complete = False
        self.relative_base = 0
        return
        
    def load_program(self, in_put):
        '''Loads the program or program from day'''
        if in_put is None:
            raise Exception('No program or day passed')
            return
        
        #If program is passed directly
        elif type(in_put) == np.ndarray:
            self.program = in_put.to_list()
            self.day = None
        elif type(in_put) == list:
            self.program = in_put
            self.day = None
            
        #If program is to be loaded from file
        else:
            self.day = in_put
            self.program = np.genfromtxt('day'+str(self.day)+'_input.txt', dtype=np.int64, delimiter=',').tolist()
            
        self.pointer = 0
        self.complete = False
        self.relative_base = 0
        return
        
    def reset_memory(self, in_put=None):
        '''Reloads program'''
        if self.day is None and in_put is None:
            raise Exception('No program loaded')
            
        elif in_put is not None:
            self.load_program(in_put)
            
        else:
            self.load_program(self.day)
        return
            
    def edit_memory(self, pointer, value):
        '''Edits program value at position'''
        #position and value are lists
        if (type(pointer) == np.ndarray or type(pointer) == list) and\
           (type(value) == np.ndarray or type(value) == list):
            if len(pointer) != len(value):
                raise Exception('Unequal list lengths')
                return
            for i in range(0, len(pointer)):
                self.program[pointer[i]] = value[i]
                
        #position is list and value is int
        elif type(pointer) == np.ndarray or type(pointer) == list:
            for i in position:
                self.program[i] = value
                
        #position and value are both int
        else:
            self.program[pointer] = value
        return
    
    def get_memory(self,  pointer):
        return self.program[pointer]
            
    def set_pointer(self, pointer):
        '''Sets pointer position'''
        self.pointer = pointer
        
    def get_complete(self):
        return self.complete
    
    def pad_memory(self, idx):
        '''Expands memory'''
        while len(self.program) <=  idx:
            self.program.append(0)
            
    def run_program(self, param_in=None, pointer=None, pause_on_out=False, verbose=True):
        '''Function to run the program
           Steps along until 99 is reached
           fctn: 1 == +, 2 == *, 3 == input, 4 == output,
                 5 == jump-if-true, 6 == jump-if-false,
                 7 == <, 8 == ==,
                 99 == STOP
           mode: 0 == position, 1 == immediate
           ABCDE: DE - fctn (with leading 0 if < 10)
                  C  - mode of param1
                  B  - mode of param2
                  A  - mode of param3'''
        if pointer is not None:
            self.pointer = pointer
        i = self.pointer

        state = 0
        param_out = []
        while i < len(self.program):
            fctn = self.program[i]
            #ABCDE
            
            #Break function down from ABCDE into A B C DE
            instruction = np.zeros(5, dtype=np.int)
            for j in range(4, -1, -1):
                instruction[4-j] = fctn // pow(10, j)
                fctn = int(fctn % pow(10, j))
            fctn = 10*instruction[3] + instruction[4] #DE

            #fctn that perform operations or comparisons
            if fctn == 1 or fctn == 2 or (fctn >= 5 and fctn <= 8):
                #If parameter 1 is relative to base...
                if instruction[2] == 2: #C
                    address = self.relative_base+self.program[i+1]
                #...is in place...
                elif instruction[2] == 1:
                    address = i+1
                #...or from memory
                else:
                    address = self.program[i+1]
                if address >= len(self.program):
                    self.pad_memory(address)
                param1 = self.program[address]

                #If parameter 1 is relative to base...
                if instruction[1] == 2: #B
                    address = self.relative_base+self.program[i+2]
                #...is in place...
                elif instruction[1] == 1:
                    address = i+2
                #...or from memory
                else:
                    address = self.program[i+2]
                if address >= len(self.program):
                    self.pad_memory(address)
                param2 = self.program[address]

                #If parameter 3 is relative to base...
                if instruction[0] == 2: #A
                    param3 = self.relative_base+self.program[i+3]
                #...is in place...
                elif instruction[0] == 1:
                    param3 = i+3
                #...or from memory
                else:
                    param3 = self.program[i+3]
                if param3 >= len(self.program):
                    self.pad_memory(param3)

                #fctn that output to param3
                if fctn == 1 or fctn == 2 or fctn == 7 or fctn == 8:
                    #Sum
                    if fctn == 1:
                        result = param1+param2

                    #Multiply
                    elif fctn == 2:
                        result = param1*param2

                    #less-than
                    elif fctn == 7:
                        if param1 < param2:
                            result = 1
                        else:
                            result = 0

                    #equal-to
                    elif fctn == 8:
                        if param1 == param2:
                            result = 1
                        else:
                            result = 0

                    self.program[param3] = result                
                    i += 4

                #fctn that jump
                elif fctn == 5 or fctn == 6:
                    #   jump-if-true                   jump-if-false
                    if (fctn == 5 and param1 != 0) or (fctn == 6 and param1 == 0):
                        i = param2
                    else:
                        i += 3

            #I/O functions
            #Get input
            elif fctn == 3:
                #print('Input:')
                if param_in is None:
                    print('Input:')
                    param0 = int(input())
                elif type(param_in) == np.ndarray or type(param_in) == list:
                    param0 = param_in[state]
                    if verbose:
                        print('Input:', param0)
                    
                    state += 1
                    if state >= len(param_in):
                        state = 0
                else:
                    param0 = param_in
                    if verbose:
                        print('Input:', param0)

                #Save input relative to base...
                if instruction[2] == 2:
                    address = self.relative_base+self.program[i+1]
                #...in place...
                elif instruction[2] == 1:
                    address = i+1
                #...or to memory
                else:
                    address = self.program[i+1]
                if address >= len(self.program):
                    self.pad_memory(address)
                self.program[address] = param0
                i += 2

            #Print output
            elif fctn == 4:
                #Output relative to base...
                if instruction[2] == 2:
                    address = self.relative_base+self.program[i+1]
                #...in place...
                elif instruction[2] == 1:
                    address = i+1
                #...or from memory
                else:
                    address = self.program[i+1]
                if address >= len(self.program):
                    self.pad_memory(address)
                paramN = self.program[address]
                param_out.append(paramN)
                i += 2

                #Print output
                if verbose:
                    print('Output:', paramN)

                #If  using output as input for another program, this program can pause            
                if pause_on_out:
                    self.pointer = i
                    return np.array(param_out)
                
            #Change relative base
            elif fctn == 9:
                #If parameter 1 is relative to base...
                if instruction[2] == 2: #C
                    address = self.relative_base+self.program[i+1]
                #...is in place...
                elif instruction[2] == 1:
                    address = i+1
                #...or from memory
                else:
                    address = self.program[i+1]
                if address >= len(self.program):
                    self.pad_memory(address)
                param1 = self.program[address]
                self.relative_base += param1
                i += 2

            #End program
            elif fctn == 99:
                self.complete = True
                break

            #Error handling
            else:
                self.pointer = i
                raise Exception('i:', i, 'fctn:', fctn, 'instruction:', instruction)
                break
                
            #print(self.program)

        self.pointer = i
        return np.array(param_out)