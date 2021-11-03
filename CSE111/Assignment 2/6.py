mit_0=input("").strip(")(").split(",")
str_3=mit_0[0]

def vowel_count(name):
    list_0=['a','e','i','o','u']
    str_0=""
    count_0=0
    for i in name.lower():
        if  i in list_0:
            count_0+=1
            str_0+=i+", "

    if count_0>0:
        print(f"Vowels: {str_0[:-2]}.Total number of vowels: {count_0}")
    else:
        print("No vowels in the name")



vowel_count(str_3)
