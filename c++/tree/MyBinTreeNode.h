#define MyBinTreeNodePosi(T) MyBinTreeNode<T> *
///空树高度为-1
#define stature(p) ((p)?(p)->height:-1)
/********************************************
 * 与节点状态相关的宏
**********************************************/
#define lsRoot(x) (!((x)->parent))
#define lsLChild(x) (!lsRoot(x)&&(&(x)==(x)->prarent->lc))
#define lsRChild(x) (!lsRoot(x)&&(&(x)==(x)->prarent->rc))
#define hasParent(x) (!lsRoot(x))
#define hasLChild(x) ((x)->lc)
#define hasRChild(x) ((x)->rc)
///至少有一个孩子
#define hasChild(x) (hasLChild(x) || hasRChild(x))
///同时有两个孩子
#define hasBothChild(x) (hasLChild(x) && hasRChild(x))
#define lsLeaf(x) (!hasChild(x))
///获取兄弟节点
#define sibling(p) (lsLChild(p)?(p)->parent->rc:(p)->parent->lc)
//获取叔叔节点
#define uncle(x) (lsLChild(x->parent)?(x)->parent->parent->rc:(x)->parent->parent->lc)
typedef enum {RB_RED,RB_BLACK} RBColor;
//二叉树节点数据结构
template <typename T> struct MyBinTreeNode 
{
    //节点数据
    T data;
    //每个二叉树节点有三个指针，分别指向父亲，左孩子，右孩子
    MyBinTreeNode(T) parent;MyBinTreeNode(T) lc;MyBinTreeNode(T) rc;
    //节点在二叉树中的高度，方便以后实现AVL等二叉树
    int height;
    //NULL Path Length (左式堆空路径长度，也可以用height代替)
    int npl; 
    //节点颜色，方便后面实现红黑树
    RBColor color;
    //构造函数
    MyBinTreeNode():
    parent(NULL),lc(NULL),rc(NULL),height(0),npl(1),color(RB_RED){}
    MyBinTreeNode(T e,MyBinTreeNodePosi(T) p=NULL,MyBinTreeNodePosi(T) lc=NULL,MyBinTreeNodePosi(T) rc=NULL,int h=0,int l=1,RBColor c=RB_RED ):
    data(e),parent(p),lc(lc),rc(rc),height(h),npl(l),color(c){}
    //操作接口
    ///统计当前节点后代总数，即以当前节点为根的树的规模
    int size();
    //作为当前节点的左孩子插入新节点
    MyBinTreeNodePosi(T) insertAsLc(T const&);
    //作为当前节点的右孩子插入新节点
    MyBinTreeNodePosi(T) insertAsRc(T const&);
    //取当前节点的下一个,中序遍历序列的后一个元素
    MyBinTreeNodePosi(T) next();
    //子树层次遍历
    template <typename VST> void travLevel(VST&);
    //子树先序遍历
    template <typename VST> void travPre(VST&);
    //子树中序遍历
    template <typename VST> void travIn(VST&);
    //子树后序遍历
    template <typename VST> void travPost(VST&);
    //重载小于操作符
    bool operator<(MyBinTreeNode const& bn){return data<bn.data;}
    //重载==操作符
    bool operator== (MyBinTreeNode const& bn){return data==bn.data;}

};

template <typename T> MyBinTreeNodePosi(T) MyBinTreeNode<T>::insertAsLc(const T & e){
    return lc=new MyBinTreeNode(e,this);
}
template <typename T> MyBinTreeNodePosi(T) MyBinTreeNode<T>::insertAsRc(const T &e){
    return rc=new MyBinTreeNode(e,this);
}