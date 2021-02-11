def get_max(a,compare):
    largest=a[0]
    for item in a[1:]:
        if compare(item,largest):
            largest=item
    return largest

def bubblesort(a,compare):
    for item in range(len(a)-1,0,-1):
        for items in range(item):
            if compare(a[items],a[items+1]):
                a[items],a[items+1]=a[items+1],a[items]
    return a

   