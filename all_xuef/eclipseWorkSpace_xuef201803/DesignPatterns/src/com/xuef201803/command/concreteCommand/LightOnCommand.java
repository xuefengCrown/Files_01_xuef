package com.xuef201803.command.concreteCommand;

import com.xuef201803.command.Command;
import com.xuef201803.command.receiver.Light;

public class LightOnCommand implements Command {
	private Light light;
	public LightOnCommand(Light light){
		this.light = light;
	}
	@Override
	public void execute() {
		light.on();
	}
	
}
