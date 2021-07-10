def palin(str):

    # this makes all the characters in the string lower class
    str = str.lower()

    # first make it all 1 string:
    str = str.strip()
    str = str.replace(" ", "")
    str = list(str)

    x = list(dict.fromkeys(str))

    i = []
    for k in x:
        i.append((str.count(k)%2))


    if i.count(1) > 1:
        return "FUCCCCCK"
    else:
        return "GET IN"

#print(palin("taco cta"))
#print(palin("Jonathan Jonathan"))

##########
# TEST
##########

data1111 = ['Tact Coa',
            'jhsabckuj ahjsbckj',
            'Able was I ere I saw Elba',
            'So patient a nurse to nurse a patient so',
            'Random Words',
            'Not a Palindrome',
            'no x in nixon',
            'azAZ']

for k in data1111:
    print(palin(k))

data = [('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]
