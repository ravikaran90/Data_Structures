#!/usr/bin/python3

class Sorting:
    def bubble_sort(self,listing,i,j):
        if i==len(listing):
            exit()
        else:
            if j==len(listing)-1:
                return listing
            if listing[j]<listing[j+1]:
                pass
            elif listing[j]>listing[j+1]:
                listing[j],listing[j+1]=listing[j+1],listing[j]
            print(listing)
            self.bubble_sort(listing,i,j+1)
        self.bubble_sort(listing,i+1,0)

def main():
    obj=Sorting()
    obj.bubble_sort([100,90,80,70,60,50,40,30,20,10],0,0)

if __name__=='__main__':
    main()
