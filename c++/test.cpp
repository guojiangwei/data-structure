#define CATCH_CONFIG_MAIN
#include <iostream>
#include "catch.hpp"
#include "MyVector.h"



TEST_CASE( "unit test for MyVector", "test" ) {
    MyVector<int> v;
    v.insert(1);
    v.insert(2);
    REQUIRE(v.size()==2);
    REQUIRE(v.capacity()==10);
    for(int i=0;i<10;i++){
        v.insert(i);
    }
    REQUIRE(v.size()==12);
    REQUIRE(v.capacity()==20);
}