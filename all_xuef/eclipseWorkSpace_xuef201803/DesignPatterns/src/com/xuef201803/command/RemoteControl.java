package com.xuef201803.command;

import java.util.Arrays;

/**
 * 遥控器
 * @author moveb
 */
public class RemoteControl {
	// 遥控器要处理7个开与关的命令
	Command[] onCommands;
	Command[] offCommands;
	
	public RemoteControl(){
		onCommands = new Command[7];
		offCommands = new Command[7];
		Command noCommand = new NoCommand();
		for(int i=0; i<7; i++){
			onCommands[i] = noCommand;
			offCommands[i] = noCommand;
		}
	}
	
	public void setCommand(int slot, 
			Command onCommand, 
			Command offCommand){
		onCommands[slot] = onCommand;
		offCommands[slot] = offCommand;
	}
	
	public void onBtnPressed(int slot){
		onCommands[slot].execute();
	}
	
	public void offBtnPressed(int slot){
		offCommands[slot].execute();
	}

	@Override
	public String toString() {
		return "RemoteControl [onCommands=" + Arrays.toString(onCommands)
				+ ", offCommands=" + Arrays.toString(offCommands) + "]";
	}
	
}
