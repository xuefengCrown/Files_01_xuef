package com.xuef.scm;

/**
 * User-defined procedures are represented as instances of the LambdaProcedure class. 
 * A LambdaProcedure instance has three instance attributes:
 * 	 1. formals is a Scheme list of the formal parameters (symbols) that name the arguments of the procedure.
 *   2. body is a Scheme list of expressions; the body of the procedure.
 *   3. env is the environment in which the procedure was defined.
 * It is "closed" over the environment in which it was created.  
 * To apply the procedure, bind the parameters to the passed in variables, and evaluate the body.
 * @author moveb
 */
public class LambdaProcedure extends Procedure {
	Object formals;
	Object body;
	Frame env;
	
	public LambdaProcedure(Object formals, Object body, Frame env){
		this.name = "lambda_procedure";
		this.formals = formals;
		this.env = env;
		// body 可能是单个form, 也可能是  A begin expression (begin ...)
		// 如果 body是个过程调用，就在前面追加一个 "begin"标记，方便后面的尾递归优化!!!
		this.body = (body instanceof Pair && rest(body) == null) ? first(body) : cons("begin", body);
	}
	
	/**
	 * Call user-defined procedures.
	 * Calling a LambdaProcedure uses lexical scoping: the parent of the new call frame is 
	 * the environment in which the procedure was defined. 
	 */
	@Override
	public Object apply(Scheme interpreter, Object args) {
		// make a new frame, and evaluate this procedure's body in that new frame
		return interpreter.eval(this.body, new Frame(this.formals, args, this.env));
	}
}
