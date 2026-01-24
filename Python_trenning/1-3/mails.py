mails = ["abc@aa.com","ssss.com","sss@rerrr.com"]
for mail in mails:
    if '@' in mail:
         print(f'{mail} is a valid mail')
    else:
        print(f'{mail} is not a valid mail')