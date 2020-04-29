import java.util.*;

public class SemanticCheckVisitor implements CCALTokeniserVisitor{

	
	static Hashtable<String, LinkedHashSet<String>> duplicates = new Hashtable<>();
	static HashSet<String> Variables = new HashSet<>();
	static HashSet<String> Functions = new HashSet<>();
	static SymbolTable SymTable;

	static int ErrorCount = 0; 
	static String scope = "global";

	private static ArrayList<String> functionNames;
 	
	public Object visit(SimpleNode node, Object data)
	{
		throw new RuntimeException("Visit SimpleNode"); 
	}


	public Object visit(ASTProgram node, Object data) 
	{
		SymTable = (SymbolTable) data;

		functionNames = SymTable.getFunctions();

		int num = node.jjtGetNumChildren();
		for(int i = 0; i < num; i++) 
		{
			node.jjtGetChild(i).jjtAccept(this, data);
		}

		if(functionNames.size() > 0) {
			for(String functionName : functionNames) {
      			System.out.println("Error found: Function " + functionName + " has not been called");
      			ErrorCount++;
      		}
      	}


		DuplicateDeclarations();
		InvokedFunctions();
		UsedVars();
		if(ErrorCount == 0)
		{
			System.out.println("No errors found");
		}
		else
		{
			System.out.println(ErrorCount + " errors found");
		}
		return data;
	}


	public Object visit(ASTVar node, Object data)
	{ 	
		 
		node.childrenAccept(this, data);
		return data;
	}

	public Object visit(ASTConst node, Object data){
		
		return data;
	}

	public Object visit(ASTFunction node, Object data)
	{
		node.childrenAccept(this, data);
		return data;
	}


	public Object visit(ASTFunctionCall node, Object data)
	{	
		 

		node.childrenAccept(this, data);
		SimpleNode firstChild = (SimpleNode) node.jjtGetChild(0);
		if(SymTable.getFunctions().contains(((String)firstChild.value)))
		{
			if(functionNames.contains((String)firstChild.value))
			{
	    		functionNames.remove((String)firstChild.value);
			}
		}
		return node.value;
	}

	public Object visit(ASTReturn node, Object data)
	{
		node.childrenAccept(this, data);
		return node.value;
	}

	public Object visit(ASTType node, Object data)
	{
		node.childrenAccept(this, data);
		return node.value;
	}

	public Object visit(ASTParam_list node, Object data)
	{
		node.childrenAccept(this, data);
		return data;
	}

	public Object visit(ASTParameters node, Object data)
	{
		node.childrenAccept(this, data);
		return data;
	}

	public Object visit(ASTMain node, Object data)
	{
		
		node.childrenAccept(this, data);
		return data;
	}

	public Object visit(ASTStatement node, Object data)
	{
		node.childrenAccept(this, data);
		SimpleNode id = (SimpleNode) node.jjtGetChild(0);
		if(SymTable.getFunctions().contains((String)id.value)) 
		{
			 Functions.add((String)id.value);
		}


		if(node.jjtGetNumChildren() > 1){

			String child = node.jjtGetChild(1).toString();
			String type = SymTable.getType(child, scope);
			if(type.equals("Integer"))
			{
				Variables.add(child);
			}
		}	


		node.childrenAccept(this, data);
		return data;
	}

	public Object visit(ASTAssign node, Object data)
	{
		 
		node.childrenAccept(this, data);
		return data;
		
	}

	public Object visit(ASTArgList_Assign node, Object data)
	{
		node.childrenAccept(this, data);
		return data;
	}

	public Object visit(ASTPlus node, Object data)
	{

		 
		SimpleNode firstChild = (SimpleNode) node.jjtGetChild(0);
		System.out.println("1: "+firstChild);

		SimpleNode secondChild = (SimpleNode) node.jjtGetChild(1);
		System.out.println("2: "+secondChild);

		DataType firstChildDataType = (DataType) firstChild.jjtAccept(this, data);
		DataType secondChildDataType = (DataType) secondChild.jjtAccept(this, data);
	  	if ((firstChildDataType != secondChildDataType) | firstChildDataType != DataType.Num  | secondChildDataType != DataType.Num ) {
	      	System.out.println("Arithmetic Operator Check Failed: Cannot add '" + firstChildDataType +"' and '" + secondChildDataType + "'");
	      	return DataType.type_unknown;
	  	}

	  return DataType.Num;
	}

	public Object visit(ASTMinus node, Object data)
	{
		SimpleNode firstChild = (SimpleNode) node.jjtGetChild(0);
		SimpleNode secondChild = (SimpleNode) node.jjtGetChild(1);
		DataType firstChildDataType = (DataType) firstChild.jjtAccept(this, data);
		DataType secondChildDataType = (DataType) secondChild.jjtAccept(this, data);
		if(firstChildDataType != DataType.Num | secondChildDataType != DataType.Num)
		{
			System.out.println("Arithmetic Operator Check Failed: Cannot subtract '" + firstChildDataType +"' and '" + secondChildDataType + "'");
		    return DataType.type_unknown;
		}
		return DataType.Num;
	}

	public Object visit(ASTAnd node, Object data)
	{
		DataType child1DataType = (DataType) node.jjtGetChild(0).jjtAccept(this, data);
	    DataType child2DataType = (DataType) node.jjtGetChild(1).jjtAccept(this, data);
	    if(child1DataType != DataType.comp_op || child2DataType != DataType.comp_op) {
	      System.out.println( "Cannot " + node.value + " " + child1DataType + " and " + child2DataType);
	    }
		return data;
	}

	public Object visit(ASTOr node, Object data)
	{
		DataType child1DataType = (DataType) node.jjtGetChild(0).jjtAccept(this, data);
	    DataType child2DataType = (DataType) node.jjtGetChild(1).jjtAccept(this, data);
	    if(child1DataType != DataType.comp_op || child2DataType != DataType.comp_op) {
	      System.out.println( "Cannot " + node.value + " " + child1DataType + " and " + child2DataType);
	    }
		return data;
	}

	public Object visit(ASTComp node, Object data)
	{
		DataType child1DataType = (DataType) node.jjtGetChild(0).jjtAccept(this, data);
	    DataType child2DataType = (DataType) node.jjtGetChild(1).jjtAccept(this, data);
	    if(child1DataType != DataType.comp_op || child2DataType != DataType.comp_op) {
	      System.out.println( "Cannot " + node.value + " " + child1DataType + " and " + child2DataType);
	    }
		return data;
	}

	public Object visit(ASTequals node, Object data)
	{
		DataType child1DataType = (DataType) node.jjtGetChild(0).jjtAccept(this, data);
	    DataType child2DataType = (DataType) node.jjtGetChild(1).jjtAccept(this, data);
	    if(child1DataType != DataType.comp_op || child2DataType != DataType.comp_op) {
	      System.out.println( "Cannot " + node.value + " " + child1DataType + " and " + child2DataType);
	    }
		return data;
	}

	public Object visit(ASTnotEquals node, Object data)
	{
		DataType child1DataType = (DataType) node.jjtGetChild(0).jjtAccept(this, data);
	    DataType child2DataType = (DataType) node.jjtGetChild(1).jjtAccept(this, data);
	    if(child1DataType != DataType.comp_op || child2DataType != DataType.comp_op) {
	      System.out.println( "Cannot " + node.value + " " + child1DataType + " and " + child2DataType);
	    }
		return data;
	}

	public Object visit(ASTLT node, Object data)
	{
		DataType child1DataType = (DataType) node.jjtGetChild(0).jjtAccept(this, data);
	    DataType child2DataType = (DataType) node.jjtGetChild(1).jjtAccept(this, data);
	    if(child1DataType != DataType.comp_op || child2DataType != DataType.comp_op) {
	      System.out.println( "Cannot " + node.value + " " + child1DataType + " and " + child2DataType);
	    }
		return data;
	}

	public Object visit(ASTLE node, Object data)
	{
		DataType child1DataType = (DataType) node.jjtGetChild(0).jjtAccept(this, data);
	    DataType child2DataType = (DataType) node.jjtGetChild(1).jjtAccept(this, data);
	    if(child1DataType != DataType.comp_op || child2DataType != DataType.comp_op) {
	      System.out.println( "Cannot " + node.value + " " + child1DataType + " and " + child2DataType);
	    }
		return data;
	}

	public Object visit(ASTGT node, Object data)
	{
		DataType child1DataType = (DataType) node.jjtGetChild(0).jjtAccept(this, data);
	    DataType child2DataType = (DataType) node.jjtGetChild(1).jjtAccept(this, data);
	    if(child1DataType != DataType.comp_op || child2DataType != DataType.comp_op) {
	      System.out.println( "Cannot " + node.value + " " + child1DataType + " and " + child2DataType);
	    }
		return data;
	}

	public Object visit(ASTGE node, Object data)
	{
		DataType child1DataType = (DataType) node.jjtGetChild(0).jjtAccept(this, data);
	    DataType child2DataType = (DataType) node.jjtGetChild(1).jjtAccept(this, data);
	    if(child1DataType != DataType.comp_op || child2DataType != DataType.comp_op) {
	      System.out.println( "Cannot " + node.value + " " + child1DataType + " and " + child2DataType);
	    }
		return data;
	} 

	public Object visit(ASTID node, Object data)
	{
		 
		node.childrenAccept(this, data);
		return node.value;
	}

	public Object visit(ASTNumber node, Object data)
	{
		 
		node.childrenAccept(this, data);
		return node.value;
	}

	public Object visit(ASTBool node, Object data)
	{
		node.childrenAccept(this, data);
		return node.value;
	}
	
	public Object visit(ASTSkip node, Object data)
	{
		node.childrenAccept(this, data);
		return node.value;
	}


	public Object visit(ASTExpression node, Object data)
	{
		node.childrenAccept(this, data);
		return node.value;
	} 


	public static void DuplicateDeclarations()
	{
		Hashtable<String, ArrayList<String>> duplicate = SymTable.getDupsInScopes();
		if (duplicate.size() > 0) {
			Enumeration enumm = duplicate.keys();
	   	while(enumm.hasMoreElements()) 
	   	{
	   		String scope = (String) enumm.nextElement();
	   	 	ArrayList<String> dups = new ArrayList<String>(duplicate.get(scope));
	   	 	Set<String> dupSet = new LinkedHashSet<String>(dups);
	   	 	Iterator<String> it = dupSet.iterator();
	   	 	
	   	 	
	   	 	while(it.hasNext()) 
	   	 	{
	   	 		System.out.println("Error found: Multiple declarations found for: " + it.next() );
				ErrorCount++;
			}
		}
		}

	} 

	public void InvokedFunctions(){

		ArrayList<String> functions = SymTable.getFunctions();
		for(int i = 0; i < functions.size(); i++) 
		{
			if(!Functions.contains(functions.get(i))) 
			{
				System.out.println("Error found: " + functions.get(i) + " is declared but never used");
				ErrorCount ++;
			}
		}
	}

	public static void UsedVars()
	{
		ArrayList<String> vars = SymTable.getVars();
		for(int i = 0; i < vars.size(); i++) 
		{
			if(!Variables.contains(vars.get(i))) 
			{
				System.out.println("Error found: " + vars.get(i) + " is declared but never used");
				ErrorCount ++;
			}
		}
	}
 

}