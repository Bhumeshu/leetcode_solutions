# ip = no of copies
# op = total cost price
def overall_cost(ip, dis, cp, sp, ap):
    if ip == 0 or type(ip) != int:
        return "0"
    return [(cp * (1 - dis/100) * ip) + (sp + ((ip-1) * ap))]


app = .75
cpp = 24.95
spp = 3
# mfp = 40
gkp = 50
print(overall_cost(50, gkp, cpp, spp, app))
