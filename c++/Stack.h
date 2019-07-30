#include "MyVector.h"
template <typename T> class Stack:public MyVector<T>{
    public:
    void push(T const & e){
        
        this->insert(MyVector<T>::size(),e);
        }
    T pop(){
        int size=MyVector<T>::size();
        return this->remove(size-1);}
    T & top(){return (*this)[this->size()-1];}
    };
    enum class DIGITSYSTEM:int {BIN=2,OCT=8,DIGIT=10,HEX=16};
    ////将10进制转换为其他进制
     void convertTo(Stack<char> & result,int src,DIGITSYSTEM ba){
         printf("\nbase;%d",ba);
         static char  digit[]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
        int base=(int)ba;
        int mod;
        // char * result;
        while(src){
            mod=src%base;
             printf("\nmod;%c",digit[mod]);
            result.push(digit[mod]);
            src=src/base;
        }
    }
    //将其他进制转换为10进制
    int convertFrom(char * src,DIGITSYSTEM ba){
        static char  digit[]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
        // MyVector<char> * v=new MyVector<char>(digit,16);
        // int base=(int)ba;
        // while(src!='\0'){
        //     printf("\nsrc=%c",src);
        //     src=src+1;
        // }
    }
    ///根据表达式计算机值
    /////////////加，减，乘，除，乘方，阶乘，左括号，右括号，结束和起始符
    typedef enum{ADD,SUB,MUL,DIV,POW,FAC,L_P,R_P,EOE} Operator;
    int calculator(char * exp){
    const char pri[9][9]={//运算符优先级，[栈顶] [当前]
           // 当前运算符
           //         +   -   *   /  ^    !   (   )  \0
            /*-- + */">",">","<","<","<","<","<",">",">",
            /*|  - */">",">","<","<","<","<","<",">",">",
            /*栈 * */">",">",">",">","<","<","<",">","<",
            /*顶 / */">",">",">",">","<","<","<",">","<",
            /*运 ^ */">",">",">",">","<","<","<",">",">",
            /*算 ! */">",">",">",">","<","<","<",">",">",
            /*符 ( */"<","<","<","<","<","<","<","=","",
            /*|  ) */" "," "," "," "," "," "," "," "," ",
            /*--\0 */"=","=","=","=","=","=","=","=","="
                    };

    }