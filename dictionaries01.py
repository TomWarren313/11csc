#dictionary
haircut = {}

#get data
for i in range(5):
    key = input('Please enter the students name: ').title()
    ans = input('Does this student need a haircut? (Y/N) ').upper()
    if ans == 'Y':
        value = True
    elif ans == 'N':
        value = False
    else:
        value = None
    
    haircut[key] = value

#printing k
for key,value in haircut.items():
    print((key), 'has', len(key), 'characters')