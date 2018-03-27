package ex03.pyrmont.startup;

import ex03.pyrmont.connector.http.HttpConnector;

public final class Bootstrap {
  public static void main(String[] args) {
	// 创建连接器实例，它会另起一个线程来运行
    HttpConnector connector = new HttpConnector();
    connector.start();
  }
}