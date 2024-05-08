def catAndMouse(catA, catB, mosC):
    A = abs(catA - mosC)
    B = abs(catB - mosC)

    if A < B:
        return "Cat A"  
    elif B < A:
        return "Cat B" 
    else:
         A==B
         return "Mouse C"  

# Test Case 1
Test_Case_1= catAndMouse(16, 24, 15)
print(Test_Case_1) 

# Test Case 2
Test_Case_2 = catAndMouse(mosC=15, catB=24, catA=16)
print(Test_Case_2)  
#test case 3
Test_Case_3 = catAndMouse (catA=0, catB=0, mosC=0)
print(Test_Case_3)  


