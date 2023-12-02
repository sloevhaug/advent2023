import regex as re

file = open('1-input.txt')
document = file.readlines()

number_pattern = re.compile(r'one|two|three|four|five|six|seven|eight|nine|\d+')
number_pattern_digit_only = re.compile(r'\d+')

total1 = 0
total2 = 0

numbdic = {
    'one': '1', 
    'two': '2', 
    'three': '3', 
    'four': '4', 
    'five': '5', 
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9'    
}

numbdic2 = {
    'one': 'o1e', 
    'two': 't2o', 
    'three': 't3e', 
    'four': 'f4r', 
    'five': 'f5e', 
    'six': 's6x', 
    'seven': 's7n', 
    'eight': 'e8t', 
    'nine': 'n9e'    
}

for line in document:
    
    line = line.replace('\n', '')
    line2 = '' + line

    print('------------------------------')
    print('input: ', line)
    # Find all numbers text and digit
    for repl in numbdic2:
        line2 = line2.replace(repl, numbdic2[repl])

    #numbers1 = number_pattern.findall(line, overlapped = True) 
    numbers1 = number_pattern.findall(line) 
    numbers2 = number_pattern_digit_only.findall(line2) 
    
    print('numbers: ', numbers1)
    print('numbers: ', numbers2)
    
    first1 = numbers1[0]
    last1 = numbers1[-1]

    first2 = numbers2[0]
    last2 = numbers2[-1]

    # Replace text with digits
    if(numbers1[0] in numbdic): 
        first1 = numbers1[0].replace(numbers1[0], numbdic[numbers1[0]])
    else:
        first1 = numbers1[0]

    if(numbers1[-1] in numbdic): 
        last1 = numbers1[-1].replace(numbers1[-1], numbdic[numbers1[-1]])
    else:
        last1 = numbers1[-1]

    print('first1: ', numbers1[0])
    print('last1: ', numbers1[-1])

    print('first2: ', numbers2[0])
    print('last2: ', numbers2[-1])


    combined1 = first1[0] + last1[-1]
    combined2 = first2[0] + last2[-1]

    if(combined1 != combined2):
        print('----------------- ERROR! ---------------------')
        print('----------------- ERROR! ---------------------')
        print('----------------- ERROR! ---------------------')
        print('----------------- ERROR! ---------------------')
        print('----------------- ERROR! ---------------------')
        print('----------------- ERROR! ---------------------')
        print('input: ', line)
    
    print('combined1', combined1)
    print('combined2', combined2)
    print('total1 before: ', total1)
    print('total2 before: ', total2)
    total1 += int(combined1)
    total2 += int(combined2)
    print('total1 after: ', total1)
    print('total2 after: ', total2)

print(total1)
print(total2)