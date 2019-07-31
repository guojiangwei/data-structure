#include "MyList.h"
template <typename T> class MyQueue:public MyList<T>
{

public:
void enqueue(T const& e){this->insertAsLast(e);}
T dequeue(){
    T e;
    // if (this->size()==0)
    // {
    //    return e;
    // }
    
    
    return this->remove(this->first());
    }
T & front(){return this->first()->data;}
};

///顾客类：顾客所属的窗口，排队时长
struct Customer
{
   int window;unsigned int time; 
};

/////选取当前窗口排队最少的人
int bestWindow(MyQueue<Customer>* windows,int nWin){
    int count=windows[0].size();
    int index=0;
    while (--nWin)
    {
        if (count<windows[nWin].size())
        {
            index=nWin;
            count=windows[nWin].size();
        }
        
    }
    return nWin;
    
}
///模拟银行业务，nWin窗口数量，serveTime 银行营业时间
void simulateBank(int nWin,int serveTime){
    MyQueue<Customer>* windows=new MyQueue<Customer>[nWin];
    for (int i = 0; i < serveTime; i++)
    {
        Customer c;
        c.window=bestWindow(windows,nWin);
        c.time=10+rand()%98;
        windows[c.window].enqueue(c);
        for (int j = 0; i < nWin; i++)
        {
            
            if (windows[i].size()>0&&--(windows[i].front().time)<=0)
            {
                windows[i].dequeue();
            }
            
        }
        
    }
    
    for (int i = 0; i < 10000; i++)
    {
        Customer c;
        c.window=bestWindow(windows,nWin);
        c.time=10+rand()%98;
        windows[c.window].enqueue(c);
    }

    
}
