import random

def iterative_merge_sort(list):
    rght = 0
    rend = 0
    left = 0
    step = 1
    length = len(list)
    temp = [0] * length

    while(step < length):
        left = 0
        
        while(left + step < length):
            rght = left + step
            rend = rght + step
            
            if(rend > length):
                rend = length
            
            m = left
            i = left
            j = rght

            while(i < rght and j < rend):
                if (list[i] <= list[j]):
                    temp[m] = list[i]
                    i += 1
                else:
                    temp[m] = list[j]
                    j += 1

                m += 1

            while(i < rght):
                temp[m] = list[i]
                i += 1; m += 1
                
            while(j < rend):
                temp[m] = list[j]
                j += 1; m += 1
                
            m = left
            
            while(m < rend):
                list[m] = temp[m]
                m += 1
                
            left += step * 2
        step *= 2

if __name__=="__main__":
    def is_sorted(S):
        for idx in range(len(S)-1):
            if S[idx] > S[idx+1]:
                return False
        return True
        
    x = [11,10,9,8,7,6,5,4,3,2,1]
    #Test using random samples without any duplication
    x = random.sample(range(10000), 1000)
    print(f"Before: {x} is sorted={is_sorted(x)}")
    iterative_merge_sort(x)
    print(f"After:  {x} is sorted={is_sorted(x)}")