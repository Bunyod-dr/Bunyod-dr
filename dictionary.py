# car_0 = {'model':'buggati','rang':'sariq'}
# print(car_0['model'])
# print(car_0['rang'])

# talaba_0 = {'ism':'bunyod yuldashev','yosh':15,'t_yil':2009}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")

# talaba_0['kurs'] = 5
# talaba_0['fakultet'] = 'informatika'
# print(talaba_0)

# talaba_1 = {}
# talaba_1['ism'] = 'bunyod yoldoshev'
# talaba_1['kurs'] = 5
# talaba_1['yosh'] = 15
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# talaba_1['kurs'] = 5
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# talaba_0 = {'ism':'bunyod yoldoshev','yosh':15,'t_yil':2009}
# print(talaba_0)
# del talaba_0['yosh'] 
# print(talaba_0)

telefonlar = {
    'behruz':'iphone x',
    'beknazar':'galaxy s9',
    'azamat':'mi 10 pro',
    'laziz':'nokia 7979'
    }

# phone = telefonlar['behruz']
# print(f"behruzning telefoni {phone}")

# phone = telefonlar['beknazar']
# print(f"beknazarning telefoni {phone}")
# phone = telefonlar.get('hasan','Bunday ism mavjud emas')
phone = telefonlar.get('hasan')
print(phone)