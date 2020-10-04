'''
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
'''
def countingValleys(steps, path):
    count=0
    vally=0
    for s in path:
        if s=="U":
            count+=1
            if count==0:
                vally+=1
        else:
            count-=1
    return vally
print(countingValleys(8,'UDDDUDUU'))