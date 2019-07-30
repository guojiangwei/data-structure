#define CATCH_CONFIG_MAIN
#include <iostream>
#include "catch.hpp"
// #include "MyVector.h"
#include "List.h"
#include "Stack.h"



TEST_CASE( "unit test for MyVector", "test" ) {
    MyVector<int> v;
    v.insert(1);
    v.insert(2);
    v.insert(3);
    REQUIRE(v.size()==3);//1
    REQUIRE(v.capacity()==10);//2
    for(int i=0;i<100;i++){
        v.insert(i);
    }
    for(int i=0;i<100;i++){
        v.insert(i);
    }
    REQUIRE(v.size()==203);//3
    REQUIRE(v.capacity()==320);//4
    v.unsort();
    // v.remove(1);
    REQUIRE(v.size()==203);//5
    // REQUIRE(v.find(99)==1);
    REQUIRE(v.deduplicate()==103);//--test-6
    REQUIRE(v.size()==100);//test-7
    REQUIRE(v.capacity()==160);//test-8
    REQUIRE(v[v.max()]==99);///test-9 max
    v.sort();
    REQUIRE(v.maxSorted()==99); ////test -10 max sorted
    REQUIRE(v[0]==0);  ///test -11 min 
    v.unsort();   
    v.sort(2); ///test  mergesort
    REQUIRE(v[v.max()]==99); //test - 12  verify max
    REQUIRE(v.maxSorted()==99); //test-13 sorted max value
     REQUIRE(v[0]==0); /// test -14 min value
}


TEST_CASE( "unit test for List", "test list" ) {
    List<int>  list;
    REQUIRE(list.size()==0);  //test  15 list size 
    for(int i=0;i<100;i++)list.insertAsFirst(i);
    REQUIRE(list.first()->data==99); //test 16
    REQUIRE(list.last()->data==0); //test 17
    REQUIRE(list.size()==100); // test 18 list insert list size
    for(int i=0;i<10;i++)list.remove(i);
    REQUIRE(list.size()==90);   //test 19 list remove and size
    REQUIRE(list.selectMax()->data==98);  ///test 20 list max
    REQUIRE(list.selectMax()->data==98); ///test 21 list max
    REQUIRE(list.first()->data==98); ///test 22 list max
    REQUIRE(list.last()->data==0); ///test 23 list max
    list.unsort();
    // REQUIRE(list.first()->data==98); ///test 20 list max
    // REQUIRE(list.last()->data==0);
    REQUIRE(list.size()==90);
    list.sort(); ///test sort
    REQUIRE(list.size()==90);
    REQUIRE(list.first()->data==0); //test sort result min
    REQUIRE(list.last()->data==98);//test sort result max
    for(int i=0;i<100;i++)list.insertAsFirst(i);
    REQUIRE(list.size()==190);
    list.deduplicate();
    REQUIRE(list.size()==100);
    list.sort(1);////test selectionsort
    REQUIRE(list.last()->data==99);
    REQUIRE(list.first()->data==0);
    for(int i=0;i<200;i++)list.insertAsFirst(i);
    REQUIRE(list.size()==300);
    list.sort();
    REQUIRE(list.size()==300);
    list.uniquify();
    REQUIRE(list.size()==200);
    REQUIRE(list.last()->data==199);
    REQUIRE(list.first()->data==0);

    
    // list.traverse

    // list.find()

}

TEST_CASE( "unit test for Stack", "test stack" ) {
    Stack<int> stack;
    for(int i=0;i<10 ;i++){
stack.push(i);
    }
    REQUIRE(stack.top()==9);
    REQUIRE(stack.pop()==9);
    REQUIRE(stack.size()==9);
    REQUIRE(stack.pop()==8);
    REQUIRE(stack.size()==8);
    REQUIRE(stack.pop()==7);
    REQUIRE(stack.size()==7);
    REQUIRE(stack.pop()==6);
    REQUIRE(stack.size()==6);
    REQUIRE(stack.pop()==5);
    REQUIRE(stack.size()==5);
    REQUIRE(stack.pop()==4);
    REQUIRE(stack.size()==4);
    REQUIRE(stack.pop()==3);
    REQUIRE(stack.size()==3);
    REQUIRE(stack.pop()==2);
    REQUIRE(stack.size()==2);
    REQUIRE(stack.pop()==1);
    REQUIRE(stack.size()==1);
    REQUIRE(stack.top()==0);
    REQUIRE(stack.pop()==0);
    //  REQUIRE(stack.top()==0);  ///边界测试没做好
    REQUIRE(stack.size()==0);
    /////test digit to bin or oct or hex
    Stack<char> result;
    char  result2[4]={'1','0','1','0'};
     printf("\nstart:%d",result.size());
     convertTo(result,10,DIGITSYSTEM::BIN);
      printf("\nend:%d",result.size());
    for(int i=0;i<4;i++){
        // printf("\nresult:%c   %d",result.top(),result.top());
        // printf("\npop:%c",result.pop());
        REQUIRE(result.pop()==result2[i]);
    }
    //将其他进制转换为10进制
    char bin[]="1010";
    int dig=convertFrom(bin,DIGITSYSTEM::BIN);
    printf("\ndig=%d",dig);

    

}