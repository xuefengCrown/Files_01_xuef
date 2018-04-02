package com.xuef201803.command.concreteCommand;

import com.xuef201803.command.Command;
import com.xuef201803.command.receiver.Stereo;

public class StereoOnCommand implements Command {
	private Stereo stereo;
	public StereoOnCommand(Stereo stereo){
		this.stereo = stereo;
	}
	@Override
	public void execute() {
		stereo.on();
		stereo.setCd();
		stereo.setVolume(11);
	}
}
