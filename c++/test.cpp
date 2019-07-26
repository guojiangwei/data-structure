#define CATCH_CONFIG_MAIN
#include <iostream>
#include "catch.hpp"
#include "MyVector.h"
#include "List.h"



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
