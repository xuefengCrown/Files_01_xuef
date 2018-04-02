package org.smart4j.framework.annotation;

public class Test {
	public static void main(String[] args) {
		System.out.println(Target.class.getAnnotation(Aspect.class).value());
	}
}

@Aspect(Controller.class)
class Target{
	
}