my_student = {
    'name':'santi',
    'grades':[50, 80, 90, 100]
}

media = lambda x : sum(x)/len(x)

print(media(my_student['grades']))