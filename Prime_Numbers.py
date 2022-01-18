prime_number = []
    
for i in range(1, 100):
    counter = 0
    for ii in range(1, (i + 1)):
        if i % ii == 0:
            counter += 1
    if counter == 2:
            
        prime_number.append(ii)
        
print(prime_number)

