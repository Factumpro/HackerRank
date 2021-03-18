'''
Day 0: Mean, Median, and Mode

  https://www.hackerrank.com/challenges/s10-basic-statistics/problem

    ! in Python for mode use:
       max(sorted(x), key=x.count)
      Also in Python 3x we have Statistics Module:
        import statistics
        
        statistics.harmonic_mean()	Calculates the harmonic mean (central location) of the given data
        statistics.mean()	Calculates the mean (average) of the given data
        statistics.median()	Calculates the median (middle value) of the given data
        statistics.median_grouped()	Calculates the median of grouped continuous data
        statistics.median_high()	Calculates the high median of the given data
        statistics.median_low()	Calculates the low median of the given data
        statistics.mode()	Calculates the mode (central tendency) of the given numeric or nominal data
        statistics.pstdev()	Calculates the standard deviation from an entire population
        statistics.stdev()	Calculates the standard deviation from a sample of data
        statistics.pvariance()	Calculates the variance of an entire population
        statistics.variance()	Calculates the variance from a sample of data
'''

def meann(x_list_int):
    return sum(x_list_int) / len(x_list_int)

def mediann(x_list_int):
    i = len(x_list_int)
    if i % 2 == 0: 
        median1 = x_list_int[i//2]      #if i= 10, [i//2] = 6
        median2 = x_list_int[i//2 - 1]  #if i= 10, [i//2 -1] = 5
        median  = (median1 + median2) /2
    else: 
        median  = x_list_int[i//2] 
    return median

def modde_min(x_list_int):
        _counter = []
        _index = 0
        for i in range(0,len(x_list_int)):          
            for j in range(i,len(x_list_int)):   
                #print(i,j,x_list_int[i],x_list_int[j])                        
                if x_list_int[j] == x_list_int[i]:
                    _index +=1
            if _index != 0:
                _counter.append(_index) 
                _index = 0
        _index = _counter.index(max(_counter))
        if max(_counter) == 1:
            return min(x_list_int)
        else:
            return x_list_int[_index]

if __name__ == '__main__':
    N = int(input())
    x_list = input().strip().split()       
    x_list_int = list(map(int,x_list))
    x_list_int.sort()
          
    mean     = meann(x_list_int)      #mean
    median   = mediann(x_list_int)    #median
    mode_min = modde_min(x_list_int)  #mode
    #mode = max(x_list_int, key=x_list_int.count)

    print(round(  mean,1))    
    print(round(median,1))    
    print(mode_min)
    #print(mode)