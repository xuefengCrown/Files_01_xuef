package com.xuef201803.command.concreteCommand;

import com.xuef201803.command.Command;
import com.xuef201803.command.receiver.Light;

public class LightOffCommand implements Command {
	private Light light;
	public LightOffCommand(Light light){
		this.light = light;
	}
	@Override
	public void execute() {
		light.off();
	}
	
}
