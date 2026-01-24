

#num_1=10%5
#num_2=10%3
#יש לקלוט מערך --לעבור על כל המספרים במערך ולהדפיס הודעה אם המספר זוגי או לא.
#יש לעבור על מערך, לסכום את המספרים הזוגיים בלבד ולהדפיס את הסכום.ולעבור על המספרים האי  זוגיים ולסכום את סכומם

list_numbers=[11,18,57,29,54,68]
summery=[number%2 for number in list_numbers]

for number in list_numbers:
    if number%2==0:
        print(f'number {number} is even')
    if number%2==0:
        print(summery)

    else:
        print(f'number {number} is odd')
