package com.xuef201803.command.concreteCommand;

import com.xuef201803.command.Command;
import com.xuef201803.command.receiver.Stereo;

public class StereoOffCommand implements Command {
	private Stereo stereo;
	public StereoOffCommand(Stereo stereo){
		this.stereo = stereo;
	}
	@Override
	public void execute() {
		stereo.off();
	}

}
