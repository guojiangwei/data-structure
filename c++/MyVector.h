template <typename T> class MyVector{
    protected:
    int _size;int _capacity=10; T* _elem;
    float _factor=0.8;
    void copyFrom(T const* A, int low,int high);
    void expand(); //扩展vector
    void shrink();  //收缩vector
    
    int max(int low,int high); //返回最大值位置
    bool bubbleSort(int low,int high);//冒泡排序
    void selectionSort(int low,int high);//选择排序
    void merge(int low,int mid,int high);//归并
    void mergeSort(int low,int high);//归并排序
    int partition(int low,int high);//快速排序的分割点选择
    void quickSort(int low,int high);//快速排序
    void heapSort(int low,int high);//堆排序
    public:
    //构造函数
    MyVector(int c=10,int s=0,T v=0){
        _capacity=c;
        _elem=new T[_capacity];
        for(_size=0;_size<s;_elem[_size++]=v);
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
    MyVector<T> & operator= (MyVector<T> const &);
    //删除第r个元素
    T remove(int r);

    //往第r位置插入元素
    int insert(int r,T const& e);
    //往vector末尾插入元素
    int insert(T const& e){
        return insert(_size,e);
    }
    //范围排序
    void sort(int low,int high);
    //整体排序
    void sort(){
        sort(0,_size);
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
    //遍历vector
    void traverse(void (*) (T&));
    template <typename VST> void traverse(VST&);

};

template <typename T>
int MyVector<T>::insert(int r,T const& e){
    expand();
    for(int i=_size;i>r;i--)_elem[i]=_elem[i-1];
    _elem[_size++]=e;
    return r;
}
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