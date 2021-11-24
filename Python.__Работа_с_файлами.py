def loe_failist(file:str)->str:
    """Loeme tekst failist
    """
    f=open(file,"r")
    stroka=f.read() #str
    #stroka=f.readlines() #list
    f.close()
    return stroka
stroka=loe_failist("Fail.py.txt")
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
spisok=loe_faililst_listisse("Fail.py.txt")
print(spisok)