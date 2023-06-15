
def cal_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total

ram_exp=[12000,5500,2500,750]
shyam_exp=[7500,8000,8000,550]

ram_total=cal_total(ram_exp)
shyam_total=cal_total(shyam_exp)
print("The Total expenses spend by ram is :",ram_total)
print("The Total expenses spend by shyam is ",shyam_total)

