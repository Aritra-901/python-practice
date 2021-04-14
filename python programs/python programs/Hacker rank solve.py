#sample input - 5
#               23665
#sample output - 5
#Explanation -  given list is [2,3,6,6,5].the maximum score is 6. second maximum is 5.hence we print 5 as a runner up score.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = set(arr)
    list.remove(max(list))
    print(max(list))