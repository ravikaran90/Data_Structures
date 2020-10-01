#!/usr/bin/python3

class Sort:
    def bubble_sort(self,listing):
        for h in range(len(listing)-1):
            for i in range(len(listing)-1): 
                if listing[i]>listing[i+1]:
                    listing[i],listing[i+1]=listing[i+1],listing[i]
                else:
                    pass
            print(listing)

def main():
    obj=Sort()
    obj.bubble_sort([100,30,70,40,90,60,20,50,10,80])

if __name__=='__main__':
    main()
