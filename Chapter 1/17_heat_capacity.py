mass = int(input("Enter the mass of water (grams): "))
temp = int(input("Enter the change in material temperature (celcius): "))
sp_water = 4.186
kwh_con = 2.77778e-7
cost_con = 8.9

def specific_heat(mass, temp):
    q = mass*sp_water*temp
    return q

def cost(q, kwh_con, cost_con):
    cost = q * kwh_con * cost_con
    return cost

print(specific_heat(mass, temp))

q = specific_heat(mass, temp)
print(cost(q, kwh_con, cost_con))