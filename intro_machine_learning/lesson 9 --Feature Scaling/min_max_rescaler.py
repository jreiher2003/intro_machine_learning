""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    re_scale = []
    if all(x == arr[0] for x in arr):
        return 0.5
    for i in arr:
        re_scale.append((i - min(arr)) / float(max(arr) - min(arr))) 
    return re_scale

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
data1 = [10,10,10]
print featureScaling(data)
print featureScaling(data1)
