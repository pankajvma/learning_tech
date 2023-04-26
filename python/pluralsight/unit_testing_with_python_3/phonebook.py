class PhoneBook: 
    
    def __init__(self) -> None: 
        self.numbers = {}
    
    
    def add(self, name, number): 
        self.numbers[name] = number 
    
    
    def lookup(self, name): 
        return self.numbers[name] 
    
    
    def is_consistent(self) : 
        for namel, numberl in self.numbers.items(): 
            for name2, number2 in self.numbers.items(): 
                if namel == name2 : 
                    continue 
                if numberl.startswith(number2): 
                    return False 
        return True 
    
    
    def get_names(self): 
        return self.numbers.keys() 
    
    
    def get_numbers(self):
        return self.numbers.values()