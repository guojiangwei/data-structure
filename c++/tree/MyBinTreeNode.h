#define MyBinTreeNode(T) MyBinTreeNodePosi<T> *
typedef enum {RB_RED,RB_BLACK} RBColor;
template <typename T> struct MyBinTreeNode //
{
    //
    T data;
    MyBinTreeNode(T) parent;MyBinTreeNode(T) lc;MyBinTreeNode(T) rc;
    int height;
    //
    int npl; 
    //R
    RBColor color;
    

};
