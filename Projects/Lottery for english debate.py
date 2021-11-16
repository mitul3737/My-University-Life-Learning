List_0 = ["Supporter", "Opposer", "Supporter", "Opposer"]
import random
def Lotter_for_debate(l):

    var = random.choice(l)
    return var


List_1=[0,1,2,3]
name_list=['Abira','Noved','Mitul','Arefin']
for i in name_list:
    x=Lotter_for_debate(List_1)
    print(f"Hurray! {i} is a/an {List_0[x]}")
    List_1.remove(x)


