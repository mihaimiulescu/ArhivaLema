def PercentValueCustomScale(value, minVal1, maxVal1, minVal2, maxVal2):
    value = float(( (value-minVal1) * (maxVal2-minVal2) + minVal2 * maxVal1 - minVal1 * minVal2)/(maxVal1 - minVal1))
    return "{0:.2f}".format(round(value,2))