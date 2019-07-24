#define CATCH_CONFIG_MAIN
#include <iostream>
#include "catch.hpp"
#include "MyVector.h"



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
    REQUIRE(v[v.max()]==99);
    REQUIRE(v.maxSorted()==99); //test-12 max value
     REQUIRE(v[0]==0); /// test -13 min value


}