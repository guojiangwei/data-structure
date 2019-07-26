#include "MyVector.h"
template <typename T> class Stack:public MyVector<T>{
    public:
    void push(T e){insert(size(),e);}
    T pop(){return remove(size()-1);}
    T & top(){return (*this)[size()-1];}
}