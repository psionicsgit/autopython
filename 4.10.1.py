import copy
import string

def andMyCat(catList):
  if len(catList) >1 :
    for i in range(len(catList)-1):
      catList[i]=catList[i]+","
    catList[-1]="and "+catList[-1]
  return catList

print("Please input name list:")
yourCatList = []
j = 0
while j+1:
    print("Please input name "+str(j+1))
    inputResult= input()
    yourCatList.insert(j,inputResult)
    j += 1
    allName = input ("Is that all (Y/N)")
    if allName=="Y":
        break
yourCatList=copy.copy(andMyCat(yourCatList))
strSeq = " "
print(strSeq.join(tuple(yourCatList)))
