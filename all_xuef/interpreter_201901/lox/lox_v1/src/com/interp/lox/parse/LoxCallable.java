package com.interp.lox.parse;

import java.util.List;

/**
 * The Java representation of any Lox object that can be called 
 * like a function will implement this interface. 
 * 
 * That includes user-defined functions, naturally, but also 
 * class objects since classes are ��called�� to construct new instances.
 * python�пɵ��ö���������:
 * 1. procedure
 * 2. �� [A()]
 * 3. ʵ���� __call__()�������� ��ʵ��
 * @author moveb
 *
 */
public interface LoxCallable {
	//We pass it the interpreter in case the class implementing call() needs it. 
	//We also give it the list of evaluated argument values. 
	//The implementer��s job is then to return the value that the call expression produces.
	Object call(Interpreter interpreter, List<Object> arguments);
}