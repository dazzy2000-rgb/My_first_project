

class utils_jb61:
    def age_calculator(self,age,ref_age=18):
        if age>ref_age:
            print(f'age is greater than {ref_age}')
            age_new=age+5
        else:
            print(f'age is less than {ref_age}')
            age_new=age-5
        return age_new

    def email_validator(self,email):
        if '@'and'.' in email:
            print(f'email {email} is valid')
        else:
            print(f'email {email} is not valid')

    def digits_sum(self,num):
        l=len(str(num))
        sum=0
        if (l==3):
            for i in range(l):
                digit=str(num)[i]
                sum=sum+int(digit)
            print(f'sum is {sum}')
        return sum

if __name__ == "__main__":
    u = utils_jb61()
    u.digits_sum(123)