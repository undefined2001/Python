class HashTable:
    def __init__(self):
        self.arr = [0]*9

    def hash(self, new_str):
        number = "0123456789"
        vowel = "AEIOU"
        con_count = 0
        digit_sum = 0
        for i in new_str:
            if i not in vowel and i not in number:
                con_count += 1
            elif i in number:
                digit_sum += int(i)
        return (con_count*24+(digit_sum))%9

    def insert(self, new_str):
        hash_index = self.hash(new_str)
        while self.arr[hash_index] != 0:
            hash_index = (hash_index + 1) % 9
        self.arr[hash_index] = new_str
        
    def search(self, new_str):
        hash_index = self.hash(new_str)
        
        while self.arr[hash_index] != new_str:
            if self.arr[hash_index] == 0:
                return False
            hash_index = (hash_index + 1) % 9
        return self.arr[hash_index] == new_str
        
        
    def delete(self, new_str):
        hash_index = self.hash(new_str)
        while self.arr[hash_index] != new_str:
            hash_index = (hash_index + 1) % 9
            
        self.arr[hash_index] = 0;
            
        

        
    
    


myarr = ["ST1E89B8A35", "SZ9E89B5A32", "SL5E69B8A21", "ST2H99B3A32", "ST1E22B8A32"]
new_hash = HashTable()
for new_str in myarr:
    #Inserting a item in Hash Table
    new_hash.insert(new_str)
    
print("Before Delete: ")
print(new_hash.arr)
    
#Deleting item from a Hash Table
print("After Delete: ")
new_hash.delete("SZ9E89B5A32")
print(new_hash.arr)

#Searching a value inside a Hash Table
print("Is Exists: ", new_hash.search("ST1E89B8A35"))

