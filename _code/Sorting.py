import copy
class Sorting:

    def __init__(self,arr:list):
        self.__list=arr
    

    def insertionSort(self)->list:
        tmp=copy.deepcopy(self.__list) # 깊은 복사

        for i in range(1,len(tmp)):
            for j in range(i,0,-1): #i를 기준으로 왼쪽으로 가며 i가 들어갈 자리를 찾는다. 
                if(tmp[j]>=tmp[j-1]): # 왼쪽에 있는 값이 작거나 같으면 넘어감 
                    continue
                self.swap(tmp,j,j-1) #왼쪽에 값이 클 때 스왑
    
        return tmp
    

    def bubbleSort(self)->list:
        #가장 큰 것을 오른쪽 끝으로 계속 밈
        tmp=copy.deepcopy(self.__list)
        
        for i in range(0,len(tmp)):
            for j in range(0,len(tmp)-1-i):#가장 큰겂을 (오른쪽)끝까지 미루기 때문에 미룬 횟수만큼 오른쪽 끝 위치를 왼쪽으로 당김
                if(tmp[j]<=tmp[j+1]):
                    continue
                self.swap(tmp,j,j+1)
        
        return tmp
    
    def selectionSort(self)->list:
        tmp=copy.deepcopy(self.__list)

        for i in range(0,len(tmp)-1): #현재 값
            currIdx:int=i
            for j in range(len(tmp)-1,i,-1): #끝 부분 부터 i앞 까지
                if(tmp[j]<tmp[currIdx]): #현재 가르키는 값이 더크면 바꿈 
                    currIdx=j
            
            self.swap(tmp,i,currIdx) #가장 작은놈을 가르치는 인덱스와 현재 인덱스랑 변경
        
        return tmp

    
    def shellSort(self):
        tmp=copy.deepcopy(self.__list)

        sub_list_gap=len(tmp)//2
        #서브 리스트 길이

        '''
        Pass1
        ▪ 위치가 n/2만큼 떨어진 값을 2개씩 묶어 n/2개의 서브리스트를 생성
        • 예) n = 16이면, 8개의 서브리스트 생성: (0,8), (1,9), ..., (7, 15) ▪ 각 서브리스트를 Insertion Sort로 정렬
        ● Pass2
        ▪ 위치가 n/4만큼 떨어진 값을 4개씩 묶어 n/4개의 서브리스트를 생성
        • 예) n = 16이면,4개의 서브리스트 생성: (0,4,8,12), (1,5,9,13), ... ▪ 각 서브리스트를 Insertion Sort로 정렬
        '''

        while(sub_list_gap>2):
            for j in range(0,sub_list_gap):
                self.insertionSort2(tmp,j,sub_list_gap)
            
            self.insertionSort2(tmp,0,1)
            sub_list_gap=sub_list_gap//2
    
        return tmp

    
    def insertionSort2(self,arr:list,start:int,incr:int):
        
        for i in range(start+incr,len(arr),incr):
            for j in range(i,0,-incr):
                if(arr[j]>=arr[j-incr]):
                    continue
                self.swap(arr,j,j-incr) 


    def view(self):
        print(self.__list)
    
    def swap(self,arr:list,i:int,j:int):
        tmp=arr[i]
        arr[i]=arr[j]
        arr[j]=tmp
    