package com.xuef201803.book_dp.maze;

/**
 * 创建迷宫
 * @author moveb
 *
 */
public class MazeGame {
	// 硬编码，很难用不同的组件去创建迷宫
	public static Maze createMaze(){
		Maze aMaze = new Maze();
		Room r1 = new Room(1);
		Room r2 = new Room(2);
		
		Door theDoor = new Door(r1, r2);
		
		aMaze.addRoom(r1);
		aMaze.addRoom(r2);
		
		r1.setSide(Direction.NORTH, new Wall());
		r1.setSide(Direction.EAST, theDoor);
		r1.setSide(Direction.SOUTH, new Wall());
		r1.setSide(Direction.WEST, new Wall());
		
		r2.setSide(Direction.NORTH, new Wall());
		r2.setSide(Direction.EAST, new Wall());
		r2.setSide(Direction.SOUTH, new Wall());
		r2.setSide(Direction.WEST, theDoor);
		
		return aMaze;
	}
}
