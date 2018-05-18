package books.concurrency_practice.chap2;

import java.math.BigInteger;
/**
 * 提供因式分解服务的 Servlet
 * @author moveb
 */
// Not Thread Safe
public class UnsafeCountingFactorier implements Servlet {
	private long count = 0;
	public long getCount() {
		return count;
	}
	public void service(ServletRequest req, ServletResponse resp){
		// 得到要分解的数
		BigInteger i = extractFromRequest(req);
		// 因式分解
		BigInteger[] factors = factor(i);
		++count;
		// 响应给客户端
		encodeIntoResponse(resp, factors);
	}
	private void encodeIntoResponse(ServletResponse resp, BigInteger[] factors) {
		// TODO Auto-generated method stub
		
	}
	private BigInteger[] factor(BigInteger i) {
		// TODO Auto-generated method stub
		return null;
	}
	private BigInteger extractFromRequest(ServletRequest req) {
		// TODO Auto-generated method stub
		return null;
	}
}
