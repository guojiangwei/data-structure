#include "MyBinTreeNode.h"
template <typename T> class MyBinTree
{
protected:
///规模和根节点
    int _size;MyBinTreeNodePosi(T) _root;
    ////更新节点高度
    virtual int updateHeight(MyBinTreeNodePosi(T) x);
    //更新节点及其祖先的高度
    void updateHeightAbove(MyBinTreeNodePosi(T) x);
public:
    MyBinTree(/* args */):_size(0),_root(NULL){}
    ~MyBinTree(){
        if(0<_size )remove(_root);
    }
    int size(){return _size;}
    bool empty(){return !_root;}
    MyBinTreeNodePosi(T) root(){return _root;}
    ///插入根节点
    MyBinTreeNodePosi(T) insertAsRoot(T const & e);
    //将e作为x的左孩子插入
    MyBinTreeNodePosi(T) insertAsLChild(MyBinTreeNodePosi(T) x,T const & e);
    //将e作为x的右孩子插入
    MyBinTreeNodePosi(T) insertAsRChild(MyBinTreeNodePosi(T) x,T const & e);
    //将t作为x的左孩子接入
    MyBinTreeNodePosi(T) attachAsLChild(MyBinTreeNodePosi(T) x,MyBinTree<T> * &t);
    //将t作为x的右孩子接入
    MyBinTreeNodePosi(T) attachAsRChild(MyBinTreeNodePosi(T) x,MyBinTree<T> * &t);
    //删除以节点x为根的子树，并返回移除的子树的规模
    int remove(MyBinTreeNodePosi(T) x);
    //将子树x从当前树种移除作为一个单独的树
    MyBinTree<T> * secede(MyBinTreeNodePosi(T) x);
    ////遍历
    template <typename VST> void travLevel(VST& visit){ if (_root) _root->travLevel(visit); }
    template <typename VST> void travPre(VST& visit){if (_root) _root->travPre(visit);}
    template <typename VST> void travIn(VST& visit){ if (_root)  _root->travIn(visit); }  
    template <typename VST> void travPost(VST& visit){if (_root)   _root->travPost(visit);}

    ///比较器
    bool operator<(MyBinTree<T> const & t){
        return _root && t._root && lt(_root,t._root);
    }

    bool operator== (MyBinTree<T> const & t){
        return _root && t._root && (_root==t._root);
    }
};

///更新高度
template <typename T> int MyBinTree<T>::updateHeight(MyBinTreeNodePosi(T) x){
    return x->height=1+max(stature(x->lc),stature(x->rc));
}


///更新所有祖先节点高度
template <typename T> int MyBinTree<T>::updateHeight(MyBinTreeNodePosi(T) x){
    while (x)
    {
       updateHeight(x);
       x=x->parent;
    }
    
}
template <typename T> MyBinTreeNodePosi(T) MyBinTree<T>::insertAsRoot(T const & e){
    _size=1;
    return _root=new MyBinTreeNode<T>(e);
}
template <typename T> MyBinTreeNodePosi(T) MyBinTree<T>::insertAsLChild(MyBinTreeNodePosi(T) x,T const& e){
    x->insertAsLc(e);
    _size++;
    updateHeightAbove(x);
    return x->lc;
}

template <typename T> MyBinTreeNodePosi(T) MyBinTree<T>::insertAsRChild(MyBinTreeNodePosi(T) x,T const& e){
    x->insertAsRc(e);
    _size++;
    updateHeightAbove(x);
    return x->rc;
}

template <typename T> MyBinTreeNodePosi(T) MyBinTree<T>::attachAsLChild(MyBinTreeNodePosi(T) x,MyBinTree<T> * &t){
    if (x->lc=t->_root) x->lc->parent=x; ///将树t的根节点接到x的左边，并更改父节点指向
    _size=_size+t->_size;
    updateHeightAbove(x);
    t->_root=NULL;
    t->_size=0;
    release(t);
    t=NULL;
    return x;
}

template <typename T> MyBinTreeNodePosi(T) MyBinTree<T>::attachAsRChild(MyBinTreeNodePosi(T) x,MyBinTree<T> * &t){
    if (x->rc=t->_root) x->rc->parent=x; ///将树t的根节点接到x的又边，并更改父节点指向
    _size=_size+t->_size;
    updateHeightAbove(x);
    t->_root=NULL;
    t->_size=0;
    release(t);
    t=NULL;
    return x;
}