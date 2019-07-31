#include "MyVector.h"
#include <cmath>
template <typename T> class MyStack:public MyVector<T>{
    public:
    void push(T const & e){
        // printf("\ntttt=%f",e);
        this->insert(MyVector<T>::size(),e);
        }
    T pop(){
        int size=MyVector<T>::size();
        return this->remove(size-1);}
    T & top(){return (*this)[this->size()-1];}
    };
    enum class DIGITSYSTEM:int {BIN=2,OCT=8,DIGIT=10,HEX=16};
    ////将10进制转换为其他进制
     void convertTo(MyStack<char> & result,int src,DIGITSYSTEM ba){
        //  printf("\nbase=%d",ba);
         static char  digit[]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
        int base=(int)ba;
        int mod;
        // char * result;
        while(src){
            mod=src%base;
            //  printf("\nmod;%c",digit[mod]);
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
        return 1;
    }
    ///根据表达式计算机值
    /////////////加，减，乘，除，乘方，阶乘，左括号，右括号，结束和起始符
    typedef enum{ADD,SUB,MUL,DIV,POW,FAC,L_P,R_P,EOE} Operator;
    int isNumber(char * str){
        //  printf("\nstart number=%d %c",*str,*str);
        return 0<=(*str)-48&&(*str)-48<10;////ascii(0)=48  ascii(9)=57
    }
    double readNumber(char ** str){
        
        double value=**str-48;
       
        // char * temp= *str+1;
        int i=isNumber((*str)+1);
        // printf("\nstart valuef=%f",value);
        while(i){
            (*str)++;
            // printf("\n inumber=%d",i);
            value=value*10.0+(**str-48.0);
            i=isNumber((*str)+1);
            
        }
        // printf("\nend valuef=%f   %c",value,**str);
        return value;
    }
    Operator operatorIndex(char op){
        switch (op)
        {
        case '+':return Operator::ADD;
        case '-':return Operator::SUB;
        case '*':return Operator::MUL;
        case '/':return Operator::DIV;
        case '^': return Operator::POW;
        case '!':return Operator::FAC;
        case '(': return Operator::L_P;
        case ')':return Operator::R_P;
        case '\0': return Operator::EOE;
        default:
            break;
        }
    }
    double calculator(char * exp){
    const char pri[9][9]={//运算符优先级，[栈顶] [当前]
           // 当前运算符
           //         +   -   *   /  ^    !   (   )  \0
            /*-- + */'>','>','<','<','<','<','<','>','>',
            /*|  - */'>','>','<','<','<','<','<','>','>',
            /*栈 * */'>','>','>','>','<','<','<','>','>',
            /*顶 / */'>','>','>','>','<','<','<','>','>',
            /*运 ^ */'>','>','>','>','<','<','<','>','>',
            /*算 ! */'>','>','>','>','<','<','<','>','>',
            /*符 ( */'<','<','<','<','<','<','<','=',' ',
            /*|  ) */' ',' ',' ',' ',' ',' ',' ',' ',' ',
            /*--\0 */'<','<','<','<','<','<','<','<','='
                    };
    MyStack<char> opt;
    opt.push('\0');// eof
    double p1,p2;
    MyStack<double> optNumber;
    char priSybol;
    char optor;
    while (opt.size()) ////end loop when pop eof 
    {
        // printf("\nexp=%d",*exp);
        if(isNumber(exp)){////ascii(0)=48  ascii(9)=57
         optNumber.push(readNumber(&exp));
        //  printf("\nstart-optNumber=%f",optNumber.top());

        }else{
                optor=opt.top();
                priSybol=pri[operatorIndex(optor)][operatorIndex(*exp)];
                if(priSybol=='>'){
                    switch (operatorIndex(optor))
                    {
                    case Operator::ADD :
                        optNumber.push(optNumber.pop()+optNumber.pop());
                        opt.pop();
                        opt.push(*exp);
                        break;
                    case Operator::SUB :
                    optNumber.push(-optNumber.pop()+optNumber.pop());
                        opt.pop();
                        opt.push(*exp);
                    break;
                    case Operator::MUL :
                    optNumber.push(optNumber.pop()*optNumber.pop());
                        opt.pop();
                        opt.push(*exp);
                    break;
                    case Operator::DIV :
                        optNumber.push(1/optNumber.pop()*optNumber.pop());
                        opt.pop();
                        opt.push(*exp);
                    break;
                    case Operator::POW :
                    p1=optNumber.pop();
                    p2=optNumber.pop();
                    optNumber.push(pow(p2,p1));
                    opt.pop();
                    opt.push(*exp);
                    break;
                    case Operator::FAC :
                    p2=1;
                    p1=optNumber.pop();
                    while(p1>0){
                        p2=p1*p2;
                        p1--;
                    }
                    optNumber.push(p2);
                    opt.pop();
                    opt.push(*exp);
                    break;
                    case Operator::L_P :
                    p2=1;
                    p1=optNumber.pop();
                    while(p1>0){
                        p2=p1*p2;
                        p1--;
                    }
                    optNumber.push(p1);
                    opt.pop();
                    opt.push(*exp);
                    break;
                    default:
                        break;
                    }
                    if(opt.top()==')' || opt.top()=='\0'){
                        opt.pop();
                        // printf("\noptNumber=%f",optNumber.top());
                        continue;
                    }

                }else if (priSybol=='<')
                {
                    opt.push(*exp);
                    
                }else if (priSybol=='=')
                {
                    opt.pop();
                }
            // printf("\nopt=%c",opt.top());
        }
        // printf("\noptNumber=%f",optNumber.top());
        exp++;
    }
    return optNumber.pop();
    }