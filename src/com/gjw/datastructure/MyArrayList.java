package com.gjw.datastructure;

import java.util.Iterator;

public class MyArrayList<E> implements Iterable<E> {
	private int DEFAULT_CAPACITY=10;
	private int size=0;
	private E [] items;

	
	
	
	public void clear() {
		this.size=0;
		ensureCapacity(DEFAULT_CAPACITY);
	}
	///
	public boolean isEmpty() {
		return this.getSize()==0;
	}
	// get a item from the specified position
	public E get(int i) {
		if(i<0||i>=this.getSize()) throw new ArrayIndexOutOfBoundsException();
		return items[i];
	}
	///replace the element at the specified position  from this list with the specified item
	public E set(int i,E newItem) {
		if(i<0||i>=this.getSize()) throw new ArrayIndexOutOfBoundsException();
		items[i]=newItem;
		return items[i];
	}
	///insert the specified item to the specified position ,while shift the current item and subsequent items to the right
	public E add(int i,E newItem) {
		if(i<0||i>=this.getSize()) throw new ArrayIndexOutOfBoundsException();
		if(this.getSize()+1>=this.items.length)ensureCapacity(this.size*2+1);
		for(int j=this.getSize();j>=i;j--) {
			items[j]=items[j-1];
		}
		items[i]=newItem;
		this.size++;
		return items[i];
	}
	///delete the specified item while shift the subsequent items to left;
	public E remove(int i) {
		if(i<0||i>=this.getSize()) throw new ArrayIndexOutOfBoundsException();
		E item=items[i];
		for(int j=i;j<this.getSize()-1;j++) {
			items[i]=items[i+1];
		}
		this.size--;
		return item;
	}

	
	public int getSize() {
		return this.size;
	}
	
	public void ensureCapacity(int newCapacity) {
		if(newCapacity<=this.size) return;
		E [] old=items;
		E[] items = (E[])new Object[newCapacity];
		System.arraycopy(old, 0, items, this.size-1, this.size);
		
	}
	
  public Iterator<E> iterator(){
	  return new ArrayListIterator();
  }
	 private class ArrayListIterator implements java.util.Iterator<E>{
private int current=0;
		@Override
		public boolean hasNext() {
			
			return current<getSize();
		}

		@Override
		public E next() {
			if(!hasNext())throw new java.util.NoSuchElementException();
			return items[current++];
		}

		@Override
		public void remove() {
			MyArrayList.this.remove(--current);
			
		}
		 
	 }
}
