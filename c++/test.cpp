#define CATCH_CONFIG_MAIN
#include <iostream>
#include "catch.hpp"
#include "MyVector.h"



TEST_CASE( "unit test for MyVector", "test" ) {
    MyVector<int> v;
    v.insert(1);
    v.insert(2);
    v.insert(3);
    REQUIRE(v.size()==3);
    REQUIRE(v.capacity()==10);
    for(int i=0;i<100;i++){
        v.insert(i);
    }
    for(int i=0;i<100;i++){
        v.insert(i);
    }
    REQUIRE(v.size()==203);
    REQUIRE(v.capacity()==320);
    v.unsort();
    REQUIRE(v.size()==203);
    
    
}