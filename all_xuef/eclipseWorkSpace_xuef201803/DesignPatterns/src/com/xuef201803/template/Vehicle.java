package com.xuef201803.template;

public abstract class Vehicle {
	// Ä£°å·½·¨
	public final void drive(){
		startTheEngine();
		putIntoGear();
		looseHandBrake();
		stepOnTheGasAndGo();
	}
	protected abstract void putIntoGear();
	private void stepOnTheGasAndGo() {
		
	}

	private void looseHandBrake() {
		
	}

	private void startTheEngine() {
		
	}
}
