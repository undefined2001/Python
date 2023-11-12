inp = input("Enter Your Space Separated Value: ")

arr = inp.split(" ")

int_arr = [0]*len(arr)





#Looping till the end of the array
for i in range(len(arr)):
    #assigning value inside the array
    int_arr[i] = int(arr[i])

#for loop
#which value is even and which value is odd

#hints if-else, string formatting 

print("int_arr", int_arr)

print("arr", arr)
