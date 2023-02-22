file_name = r'C:\Users\facto\Desktop\KBTU\pp2\pp2-23B050002\tsis4\sample_data.json'

my_file = open(file_name, 'r')

data = my_file.read()
my_file.close()
print('''=======================================================================================
DN                                                 Description           Speed    MTU 
-------------------------------------------------- --------------------  ------  ------''')
dn, mtu, description, speed = "", "", "", ""

for i, k in data['imdata'][0]['l1PhysIf']['attributes'].items():
    if i == 'dn':
        print(k, end="                          ")
    if i == "speed":
        print(k, end="                                         ")
    if i == "mtu":
        print(k, end="                   ")

