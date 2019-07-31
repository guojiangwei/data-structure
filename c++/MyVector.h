template <typename T> class MyVector{
    protected:
    int _size;int _capacity; T* _elem;
    int SORTMETHOD;//0 bubble sort;1 selectionSort;2 merge sort;3 quicksort;4 heapsort
    int SEARCHMETHOD; //1 binsearch   2 binsearch2
    float _factor=0.8;
    void copyFrom(T const* A, int low,int high);
    void expand(); //扩展vector
    void shrink();  //收缩vector
    
    int max(int low,int high); //返回最大值位置
    T maxSorted(int low,int high); //返回最大值位置
    void bubbleSort(int low,int high);//冒泡排序
    void selectionSort(int low,int high);//选择排序
    void merge(int low,int mid,int high);//归并
    void mergeSort(int low,int high);//归并排序
    int partition(int low,int high);//快速排序的分割点选择
    void quickSort(int low,int high);//快速排序
    void heapSort(int low,int high);//堆排序
    void swap(T * e1,T * e2){
        T e=*e1;
        *e1=*e2;
        *e2=e;
    }
    public:
    //构造函数
    MyVector(){
        // _capacity=c;
        _capacity=10;
        _size=0;
        _elem=new T[_capacity];
        // for(_size=0;_size<s;_elem[_size++]=v);
    }
    MyVector(T const* A,int n){
        copyFrom(A,0,n);
    }
    MyVector(T const* A,int low,int high){
        copyFrom(A,low,high);
    }
    MyVector(MyVector<T> const& v,int n){
        copyFrom(v,0,v._size);
    }
    MyVector(MyVector<T> const& v,int low,int high){
        copyFrom(v,low,high);
    }
    //析构函数
    ~MyVector(){
        delete [] _elem;
    }

    ///返回vector含有的元素数量
    int size() const{
        return _size;
    } 
    //
    int capacity()const{
        return _capacity;
    }
    //判断vector是否空
    bool empty() const{
        return !_size;
    }
    //
    int max(){
        return max(0,_size);

    }
    T maxSorted(){
        return maxSorted(0,_size);
    }
    //判断是否无序
    int disordered()const;
    //无序vector整体查找
    int find(T const& e)const{
        return find(e,0,_size);
    }
    //无序vector范围查找
    int find(T const& e,int low,int high)const;
    //有序vector整体查找
    int search(T const& e)const{
        return (0>=_size)?-1:search(e,0,_size);
    }
    //有序vector范围查找
    int search(T const& e,int low,int high)const;
    //重载[]操作符
    T& operator[] (int r) const;
    //重载=操作符
    MyVector<T> & operator= (MyVector<T> const &v);
    //删除第r个元素
    T remove(int r);
    ///
    int remove(int low,int high);

    //往第r位置插入元素
    int insert(int r,T const& e);
    //往vector末尾插入元素
    int insert(T const& e){
        return insert(_size,e);
    }
    //范围排序
    void sort(int low,int high,int m=0);
    //整体排序
    void sort(int m=0){
        sort(0,_size,m);
    }
    //范围打乱
    void unsort(int low,int high);
    //整体打乱
    void unsort(){
        unsort(0,_size);
    }
    //无序去除重复元素
    int deduplicate();
    //有序去除重复
    int uniquify();
    //有序去除重复,optimize
    int uniquifyOpt1();
    //遍历vector
    void traverse(void (*) (T&));
    template <typename VST> void traverse(VST&);

};

template <typename T> void MyVector<T>::copyFrom(T const* A, int low,int high){
_capacity=high/low*2;
_elem=new T[_capacity];
_size=0;
while(low<high){
    _elem[_size++]=A[low++];
}
}

template <typename T>
int MyVector<T>::insert(int r,T const& e){
    expand();
    for(int i=_size;i>r;i--)_elem[i]=_elem[i-1];
    _elem[_size++]=e;
    return r;
}
//
template <typename T> void MyVector<T>::shrink(){
  if(_size!=0&&_size/(_capacity/2)<0.6){
      T * oldElem=_elem;
      _capacity=_capacity>>1;
      _elem=new T[_capacity];
      for(int i=0;i<_size;i++) _elem[i]=oldElem[i];
      delete[] oldElem;

  }
}

///

template <typename T>
void MyVector<T>::expand(){
    if(_size/_capacity>_factor){
        T* oldElem=_elem;
        _capacity=_capacity<<1;
        _elem=new T[_capacity];
        for(int i=0;i<_size;i++){
            _elem[i]=oldElem[i];
        }
        delete[] oldElem;
    }
}
///
template <typename T> int MyVector<T>::max(int low,int high){
    T temp=_elem[low++];
    int index=0;
    while(low<high){
        if(_elem[low]>temp) {
            temp=_elem[low];
            index=low;
    }
    // printf("\n----max=%d--temp=%d--low=%d---index=%d",_elem[low],temp,low,index);
    low++;
    }

    return index;
}

///
template <typename T> T MyVector<T>::maxSorted(int low,int high){
    return _elem[high-1];
}
///
template <typename T> int MyVector<T>::disordered()const{
    int n=0;
    for(int i=1;i<_size;i++){
        if(_elem[i-1]>_elem[i])n++;
    }
    n++;
    return n;
}

///
// template <typename T> int MyVector<T>::find(T const& e,int low,int high)const{
//     for(int i=low;i++;i<high){
//         if(_elem[i]==e)return i;
//     }
//     return -1;
// }

template <typename T> int MyVector<T>::search(T const& e,int low,int high)const{
return 1;
}

template <typename T> T& MyVector<T>::operator[] (int r) const{
    // if(r>=_size) r=_size-1;
    // if(r<0)return ;
return _elem[r];
}

template <typename T> MyVector<T> & MyVector<T>::operator= (MyVector<T> const &v){
  copyFrom(v,0,v.size());
  return *this;
}


template <typename T> T MyVector<T>::remove(int r){
    T e;
    if (r>=_size or r<0) return e;
    e=_elem[r];
    r++;
    while(r<_size){
        _elem[r-1]=_elem[r];
        r++;
       
    }
    _size--;
    shrink();
    return e;
}
template <typename T> int MyVector<T>::remove(int low,int high){
    if(low<0 ) low=0;
    if(high>size) high=_size;
    if(low==high) return 0;
    while(high<_size){
        _elem[low++]=_elem[high++];
    }
    _size=low;
    shrink();
    return high-low;
}

template <typename T> void MyVector<T>::unsort(int low,int high){
    int ind;
    for(int i=high-low;i>0;i--){
        ind=rand()%i;
        swap(_elem+low+i-1,_elem+ind);
    }
}
template <typename T> int MyVector<T>::find(T const& e,int low,int high)const{
    while(low<high--&&_elem[high]!=e);
    return high;
}
template <typename T> int MyVector<T>::deduplicate(){
    int oldSize=_size;
    int inx;
    for(int i=0;i<_size;){
        inx=find(_elem[i],i+1,_size);
        inx>=i+1?remove(inx):i++;
    }
    return oldSize-_size;
}
template <typename T>  int MyVector<T>::uniquify(){
    int oldSize=_size;
    int i=1;
    while(i<_size){
        _elem[i-1]==_elem[i]?remove(i):i++;
    }
    return oldSize-_size;
}
/////
template <typename T>  int MyVector<T>::uniquifyOpt1(){
    int i=0,j=0;
    while(++j<_size){
        if(_elem[i]!=_elem[j]){
            _elem[++i]=_elem[j];
        }
    }
    _size=++i;
    shrink();
    return j-i;
}

///ordered search algorithm
template <typename T> static int binSearch(T * A,T & e,int low,int high){
    int mid;
    while(low<high){
        mid=(low+high)>>1;
        if(e<A[mid]) high=mid;
        else if(A[mid]<e)low=mid+1;
        else return mid;
    }
    return -1;
}

///ordered search algorithm return the max index of the equal item,if failed return the position
template <typename T> static int binSearch2(T * A,T & e,int low,int high){
    int mid;
    while(low<high){
        mid=(low+high)>>1;
        e<A[mid]? high=mid:low=mid+1;
    }
    return --low;
}

// ///
// template <typename T>  int MyVector<T>::search(T const& e,int low,int high)const{
//     return bin_search(_elem,e,low,high);
// }

///
template <typename T> void MyVector<T>::sort(int low,int high,int m){
    switch (m)
    {
    case 0:
        bubbleSort(low,high);
        break;
    case 1:
        selectionSort(low,high);
        break;
    case 2:
        mergeSort(low,high);
        break;
    case 3:
        quickSort(low,high);
        break;
    case 4:
        heapSort(low,high);
        break;
    default:
        break;
    }
}
//冒泡排序
template <typename T> void MyVector<T>::bubbleSort(int low,int high){
    // printf("test bubbleDSort");
    int lastSwap=0;
    bool sorted=true;
    while(low<high){
        sorted=true;
        for( int j=low+1;j<high;j++){
            if(_elem[j-1]>_elem[j]){
                swap(_elem+j-1,_elem+j);
                lastSwap=j;
                sorted=false;
                }
        }
        // printf("\n----elem=%d---",_elem[high-low-1]);
        if(sorted)break;
        high=lastSwap;
    }

}
//选择排序
template <typename T> void MyVector<T>::selectionSort(int low,int high){

}
//归并
template <typename T> void MyVector<T>::merge(int low,int mid,int high){
    int lowLen=mid-low;T * lowElem=_elem+low;
    int highLen=high-mid;T * highElem=_elem+mid;
    
    T* tempElem=new T[lowLen];
    for(int i=0;i<lowLen;i++)tempElem[i]=lowElem[i]; ///copy low to temp array
    
    for(int i=0,j=0,k=0;(i<lowLen)||(j<highLen);){
        if(j<highLen && (!(i<lowLen)||highElem[j]<tempElem[i]) ){
            lowElem[k]=highElem[j];
            k++;
            j++;
        }
        if(i<lowLen&&(!(j<highLen)||tempElem[i]<=highElem[j])){
            lowElem[k]=tempElem[i];
            k++;
            i++;
        }
    }
    // printf("\n-tempElem=%d--low=%d--%d---mid=%d--%d---high=%d--%d--",tempElem[0],low,_elem[low],mid,_elem[mid],high,_elem[high-1]);
    delete [] tempElem;
}
//归并排序
template <typename T> void MyVector<T>::mergeSort(int low,int high){
    if(high-low<2)return;
    int mid=(low+high)/2;
    // printf("\n---test-----merge");
    mergeSort(low,mid);
    mergeSort(mid,high);
    merge(low,mid,high);
    // printf("\n---test--merge--end--");

}
//快速排序的分割点选择
template <typename T> int MyVector<T>::partition(int low,int high){

}
//快速排序
template <typename T> void MyVector<T>::quickSort(int low,int high){

}
//堆排序
template <typename T> void MyVector<T>::heapSort(int low,int high){

}