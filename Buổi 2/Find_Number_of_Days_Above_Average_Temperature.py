from array import *
def dayAboveAverageTemperature():
    # print(f"How many day's temperature? ")
    n = int(input(f"How many day's temperature? "))
    allTemperatureDay =  array('i')
    for i in range(1,1+n):
        k = int(input(f"Day {i}'s high temp: "))
        allTemperatureDay.append(k)
    numberOfDay =0
    for i in range(len(allTemperatureDay)):
        averageTemperature = sum(allTemperatureDay)/n
        if allTemperatureDay[i]> averageTemperature:
            numberOfDay+=1
    print(f"Average = {averageTemperature}\n{numberOfDay} day(s) above average")
dayAboveAverageTemperature()