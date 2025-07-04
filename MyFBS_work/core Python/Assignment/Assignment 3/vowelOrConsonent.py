#Write a program to input any alphabet and check whether it is vowel or consonant.


alpha = input("enter a alphabet :")
if alpha =='a' or alpha =='A' or alpha =='E' or alpha =='e' or alpha =='I' or alpha =='i' or alpha =='o' or alpha =='O' or alpha =='u' or alpha =='U' :
    print(f'{alpha} is Vowel')
# # elif alpha =='e' :
# #     print(f'{alpha} is Vowel')
# elif alpha =='i' :
#     print(f'{alpha} is Vowel')
# elif alpha =='o' :
#     print(f'{alpha} is Vowel')
# elif alpha =='u' :
#     print(f'{alpha} is Vowel')

else:
    print(f'{alpha} is consonant')