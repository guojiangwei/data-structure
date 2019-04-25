package com.gjw.test;

import static org.junit.Assert.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.gjw.datastructure.AVLTree;
import com.gjw.datastructure.BinarySearchTree;
import com.gjw.datastructure.MyLinkedList;

class Mytest2 {

	@BeforeEach
	void setUp() throws Exception {
	}

	@Test
	void test() {
		BinarySearchTree<String> b=new BinarySearchTree<String>();
		////test isEmpty
		assertEquals(b.isEmpty(),true);
		//insert data
		b.insert("g");
		b.insert("c");
		b.insert("a");
		b.insert("z");
		b.insert("f");
		b.insert("b");
		
		////test findMax()
		assertEquals(b.findMax(),"z");
		//test findMin()
		assertEquals(b.findMin(),"a");
	////test isEmpty
		assertEquals(b.isEmpty(),false);
	////test remove()
		b.remove("z");
		assertEquals(b.findMax(),"g");
	}

@Test
void testAVL() {
	
	AVLTree<Integer> avl=new AVLTree<Integer>();
	int[] test= {7,4,8,3,5,6};
	Integer[] val= {3,4,5,6,7,8};
	for(int i=0;i<test.length;i++) {
		avl.insert(test[i]);
	}
	assertEquals(avl.findMax(),new Integer(8));
	assertEquals(avl.findMin(),new Integer(3));
	MyLinkedList<Integer> list=avl.scanTreeMid();
	for(int i=0;i<test.length;i++) {
		System.out.println(list.get(i));
		assertEquals(val[i],list.get(i));
	}
	
}
	
	@Test
	void testLinkedList() {
		MyLinkedList<Integer> list=new MyLinkedList<Integer>();
		assertEquals(list.isEmpty(),true);
		Integer[] val= {3,4,5,6,7,8};
		list.add(1);
	}
}
