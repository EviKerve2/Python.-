def loe_failist(file:str)->str:
    """Loeme tekst failist
    """
    f=open(file,"r")
    stroka=f.read() #str
    #stroka=f.readlines() #list
    f.close()
    return stroka
stroka=loe_failist("File.py.txt")
print(stroka)
def loe_faililst_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjedisse
    """
    f=open(file,"r")
    list_=[]
    for stroka in f:
        list_append(stroka.strip())
    f.close 
    return list_
spisok=loe_faililst_listisse("File.py.txt")
print(spisok)

def salvesta_failisse(file:str):
    f=open(file,"a")
    text=input("Sisesta tekst: ")
    f.write(text+"\n")
    f.close()

for i in range(10):
    salvesta_failisse("Loetelu.txt")

def faili_sisu_umberkirjutamine(file:str):
    text=input("Sisesta uus tekst: ")
    with open(file,"w") as f:
        f.write(text+"\n")

faili_sisu_umberkirjutamine(input("Faili nimetus: ")+".txt")