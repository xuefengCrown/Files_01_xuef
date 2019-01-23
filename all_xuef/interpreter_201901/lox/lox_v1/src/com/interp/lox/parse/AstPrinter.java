package com.interp.lox.parse;

import com.interp.lox.Token;
import com.interp.lox.TokenType;
import com.interp.lox.parse.Expr.Assign;
import com.interp.lox.parse.Expr.Call;
import com.interp.lox.parse.Expr.Logical;
import com.interp.lox.parse.Expr.Variable;

public class AstPrinter implements Expr.Visitor<String> {
	private String parenthesize(String name, Expr... exprs) {
		StringBuilder builder = new StringBuilder();

		builder.append("(").append(name);
		for (Expr expr : exprs) {
			builder.append(" ");
			builder.append(expr.accept(this));
		}
		builder.append(")");

		return builder.toString();
	}

	@Override
	public String visitBinaryExpr(Expr.Binary expr) {
		return parenthesize(expr.operator.lexeme, expr.left, expr.right);
	}

	@Override
	public String visitGroupingExpr(Expr.Grouping expr) {
		return parenthesize("group", expr.expression);
	}

	@Override
	public String visitLiteralExpr(Expr.Literal expr) {
		if (expr.value == null)
			return "nil";
		return expr.value.toString();
	}

	@Override
	public String visitUnaryExpr(Expr.Unary expr) {
		return parenthesize(expr.operator.lexeme, expr.right);
	}

	public String print(Expr expr) {                                            
	    return expr.accept(this);                                          
	}
	public static void main(String[] args) {
		Expr expression = new Expr.Binary(
				new Expr.Unary(                                    
		            new Token(TokenType.MINUS, "-", null, 1),      
		            new Expr.Literal(123)),                        
		        new Token(TokenType.STAR, "*", null, 1),           
		        new Expr.Grouping(                                 
		            new Expr.Literal(45.67)));

		System.out.println(new AstPrinter().print(expression));
	}

	@Override
	public String visitVariableExpr(Variable expr) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String visitAssignExpr(Assign expr) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String visitLogicalExpr(Logical expr) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String visitCallExpr(Call expr) {
		// TODO Auto-generated method stub
		return null;
	}
}
