Sourse = "Краб крабу сделал грабли, подарил грабли крабу: «Грабь граблями гравий, краб»."
Sub = "краб"
def SubStrCount(sourse, sub):
    count = 0 
    i = 0 
    while i != -1:
        i = sourse.find(sub, i+1)
        count += 1
    return count
print (f"{SubStrCount(Sourse,Sub)}")