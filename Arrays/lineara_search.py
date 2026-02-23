def linear_search(a,key):
    for i in range(0,len(a)):
        if a[i] == key:
            return i
    return -1

def main():
    a = [10,20,34,45,56]
    key = 34
    res = linear_search(a,key)
    print(res)

if __name__ == '__main__':
    main()
    
    