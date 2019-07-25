///定义节点初始化宏
#define ListNodePosi(T) ListNode<T> * 
///列表节点模板结构，实现双向列表
template <typename T> struct ListNode
{
    T data;
    ListNodePosi(T) previous;
    ListNodePosi(T) next;
    ///构造函数
    ListNode(){

    }
    ListNode(T e,ListNodePosi(T) p=NULL,ListNodePosi(T) n=NULL):data(e),previous(p),next(n){

    }
    ///操作接口
    ///插入当前节点的前驱节点
    ListNodePosi(T) insertAsPrevious(T const &e);
    ////插入当前节点的后继节点
    ListNodePosi(T) insertAsNext(T const &e);

};
template <typename T> ListNodePosi(T) ListNode<T>::insertAsNext(T const &e){
    ListNodePosi(T) node=new ListNode<T>(e,this,next);
    next->previous=node;
    next=node;
    return node;
}
template <typename T> ListNodePosi(T) ListNode<T>::insertAsPrevious(T const &e){
    ListNodePosi(T) node=new ListNode<T>(e,previous,this);
    previous->next=node;
    previous=node;
    return node;
}
////列表模板类
template <typename T> class List
{
private:
    int _size; //列表所含对象数量
    ListNodePosi(T) header;//头节点
    ListNodePosi(T) trailer;//尾节点
    int SORTMETHOD;//0 bubble sort;1 selectionSort;2 merge sort;3 quicksort;4 heapsort;5 insertsort
protected:
    void init();//初始化列表
    int clear();//清除所有节点
    void copyNodes(ListNodePosi(T),int);///复制列表自指定位置开始的对象
    void merge(ListNodePosi(T)&,int ,List<T>&,ListNodePosi(T),int);//归并
    void mergeSort(ListNodePosi(T)&,int); ///从指定位置开始进行归并排序
    void selectionSort(ListNodePosi(T),int);///从指定位置开始进行选择排序
    void insertionSort(ListNodePosi(T),int);///从指定位置开始进行插入排序
public:
    List(){init()};//default
    List(List<T> const& list);//整体复制列表
    List(List<T> const& list,int start,int n);//复制list ，从start 开始连续复制n个
    List(ListNodePosi(T) p,int n);//复制列表中自位置p起，连续n项
    ~List();//析构函数
    ///返回列表规模
    int size() const{
        return _size;
    }
    //判断列表是否空
    bool empty()const{return  _size<0;}
    //重载[]操作符
    T& operator[](int i)const;
    //获取第一个节点 
    ListNodePosi(T) first()const{return header->next;}
    ///获取最后一个节点
    ListNodePosi(T) last()const{return trailer->previous;}
    //判断节点是否有效
    bool valid(ListNodePosi(T) p){
        return p&&(trailer!=p)&&(header != p);
    }
    //判断列表是否升序
    int disordered()const;
    //无序查找某个元素
    ListNodePosi(T) find(T const& e,int n,ListNodePosi(T) p)const;
    //有序查找某个元素
    ListNodePosi(T) search(T const& e)const{return search(e,_size,trailer);}
    //有序范围查找某个元素
    ListNodePosi(T) search(T const& e,int n,ListNodePosi(T) p)const;
    //返回p节点后的最大值节点
    ListNodePosi(T) selectMax(ListNodePosi(T) p,int n);
    //返回范围最大值
    ListNodePosi(T) selectMax(){return selectMax(header->next,_size);}
    //将插入的节点作为第一个节点
    ListNodePosi(T) insertAsFirst(T const& e);
    //将插入的节点作为最后一个节点
    ListNodePosi(T) insertAsLast(T const& e);
    //在指定节点后插入新节点
    ListNodePosi(T) insertAfter(ListNodePosi(T) p ,T const& e);
    //在指定节点前插入新节点
    ListNodePosi(T) insertBefore(ListNodePosi(T) p, T const& e);
    //移除指定节点
    T remove(ListNodePosi(T) p);
    //交换两个节点
       void swapNode(ListNodePosi(T) p,ListNodePosi(T) q){
           ///交换pq两个节点的位置，需要总共交换八次，分别交换各自后继节点的前驱节点；前驱节点的后继节点；各自的后继节点和前驱节点
        ListNodePosi(T) temp;
        temp=p->next->previous;
        p->next->previous=q->next->previous;
        q->next->previous=temp;

        temp=p->previous->next;
        p->previous->next=q->previous->next;
        q->previous->next=temp;

        temp=p->next;
        p->next=q->next;
        q->next=temp;

        temp=p->previous;
        p->previous=q->previous;
        q->previous=temp;
    }
    ///将一个节点移动到另一个节点后面,需要改变六次指针
    void moveNodeAfter(ListNodePosi(T) position,ListNodePosi(T) target){
        ListNodePosi(T) temp=position->next;
        target->previous->next=target->next;
        target->next->previous=target->previous;

        temp->previous=target;
        target->next=temp;
        position->next=target;
        target->previous=position;
        
    }
    //合并两个list
    void merge(List<T>& list){merge(first(),_size,list,list.size());}
    //将指定元素后n个节点排序
    void sort(ListNodePosi(T) p,int n,int method=5);
    //整个list排序
    void sort(int method=5){sort(first(),_size,method);}
    //无序去除重复节点
    int deduplicate();
    //有序删除重复节点
    int uniquify();
    void reverse();//反转列表
    //遍历列表
    void traverse(void(*)(T &));
    template <typename VST> void traverse(VST&);

};//List
template <typename T> void List<T>::init(){
    header=new ListNode<T>;///创建头结点
    trailer=new ListNode<T>;//创建尾节点
    header->next=trailer; //头结点的后继节点是尾节点
    header->previous=NULL; //头结点的前驱节点是NULL
    trailer->next=NULL;//尾节点的后继节点是NULL
    trailer->previous=header;//尾结点的前驱节点是header
    _size=0;//初始化规模为0
}
///
template <typename T> T& List<T>::operator[](int i)const{
    ListNodePosi(T) p=first();
    while(0<r--){
        p=p->next;
    }
    return p->data;
}
///
template <typename T> ListNodePosi(T) List<T>::find(T const& e,int n,ListNodePosi(T) p)const{
    while(0<n--){
        p=p->previous;
        if((!p)&&e==p->data)return p;
    }
    return NULL;
}
///
template <typename T>  ListNodePosi(T) List<T>::insertAsFirst(T const& e){
    _size++;
    return header->insertAsNext(e);
}
//
template <typename T>  ListNodePosi(T) List<T>::insertAsLast(T const& e){
    _size++;
    return trailer->insertAsPrevious(e);
}
//
template <typename T>  ListNodePosi(T) List<T>::insertBefore(ListNodePosi(T) p,T const& e){
    _size++;
    return p->insertAsPrevious(e);
}

//
template <typename T>  ListNodePosi(T) List<T>::insertAfter(ListNodePosi(T) p,T const& e){
    _size++;
    return p->insertAsNext(e);
}
//
template <typename T> void List<T>::copyNodes(ListNodePosi(T) p,int n){
    init();
    while((!p)&&n--){
        insertAsLast(p->data);
        p=p->next;   
    }
}
//
template <typename T> List<T>::List(ListNodePosi(T) p,int n){copyNodes(p,n);}
//
template <typename T>  List<T>::List(List<T> const& list){copyNodes(list.first(),list.size());}
template <typename T>  List<T>::List(List<T> const& list ,int start,int n){
    copyNodes(list[start],n);
    }
template <typename T>  T List<T>::remove(ListNodePosi(T) p)
{
    T e=p->data;
    p->previous->next=p->next;
    p->next->previous=p->previous;
    delete p;
    _size--;
    return e;
}
template <typename T> List<T>::~List(){
    clear();
    delete header;
    delete trailer;
}
//
template <typename T> int List<T>::clear(){
    int oldSize=_size;
    while(0<_size){
        remove(header->next);
    }
    return oldSize;
}
///
template <typename T> int List<T>::deduplicate(){
    ListNodePosi(T) p= header->next;
    int oldSize=_size;
    int r=_size;
    while(!p){
        find(p->data,r--,trailer->previous)?remove(p):p=p->next;
    }
    return oldSize-_size;
}
///遍历list
template <typename T>  void List<T>::traverse(void (*visit) (T&)){
    for(ListNodePosi(T) p=header->next;p!=trailer;p=p->next) visit(p->data);
}
/// 遍历list
template <typename T>  template <typename VST> void List<T>::traverse(VST & visit){
    for(ListNodePosi(T) p=header->next;p!=trailer;p=p->next)visit(p->data);
}
///有序唯一化
template <typename T> int List<T>::uniquify(){
    int oldSize=_size;
    ListNodePosi(T) p=header->next;
    ListNodePosi(T) q;
    while ((q=p->next)!=trailer)
    {
        p->data==q->data?remove(q):p=q;
    }
    return oldSize-_size;
}
///
template <typename T> ListNodePosi(T) List<T>::search(T const& e,int n,ListNodePosi(T) p)const{
    ListNodePosi(T)  q;
    while ((q=p->previous)!=header&&0<n--)
    {
        if(q->data<=e)return q;
        else
        {
            p=q
        }
    }
    return q;
}
///sort 
template <typename T> void List<T>::sort(ListNodePosi(T) p,int n,int method){
    switch (method)
    {
    case 5:
       insertionSort(p,n);
        break;
    
    default:
        break;
    }
}
template <typename T> void List<T>::insertionSort(ListNodePosi(T) p,int n){
    ListNodePosi(T) q,r;
    for (int i = 0; i < n; i++)
    {
        insertAfter(search(p->data,i,p),p->data);
        p=p->next;
        remove(p->previous);//删除加入到有序序列中的节点

    }
    ////不用删除或者新加节点，通过变更节点previous和next指针来进行排序
    // while ((q=p->next)!=trailer)
    // {
    //     while ((r=q->previous)!=header)
    //     {
    //         if(q->data>=r->data){
    //             moveNodeAfter(r,q);
    //             break;
    //             }
    //             q=r;
    //     }
    //     p=q;
    // }

}

template <typename T> ListNodePosi(T) List<T>::selectMax(ListNodePosi(T) p,int n){
    ListNodePosi(T) max=p;
    while((p=p->next)!=trailer&&0<n--){
        if(max->data<p->data)max=p;
    }
    return max;
}
//selection sort
template <typename T> void List<T>::selectionSort(ListNodePosi(T) p,int n){
    ListNodePosi(T)  tail=p,selectMax;
    for(int i=0;i<n;i++)tail=tail->next; //找到排序的尾节点

    while(1<n--){
        selectMax=selectMax(p,n);
        insertBefore(tail,remove(selectMax));
        tail=tail->previous;
    }


}