import java.util.*;


public class SymbolTable extends Object {
    

    Hashtable<String, LinkedList<String>> symbolTable;
    Hashtable<String, String> types;
    Hashtable<String, String> values;
    
    
    SymbolTable() {
        this.symbolTable = new Hashtable<>();
        this.types = new Hashtable<>();
        this.values = new Hashtable<>();
        
        symbolTable.put("global", new LinkedList<>());
    }

    public void addToTable(String id, String value, String type, String scope ){
        
        LinkedList<String> CurrentScope = symbolTable.get(scope);
        
        if(CurrentScope == null){
            CurrentScope = new LinkedList<>();
            CurrentScope.add(id);
            symbolTable.put(scope,CurrentScope);
        } 
        else{
            CurrentScope.addFirst(id);
        }
        values.put(id+scope, value);
        types.put(id+scope, type);
    }   

    public void PrintTable(){
        String scope;
        Enumeration table = symbolTable.keys();
        
        while (table.hasMoreElements()){
            scope = (String) table.nextElement();
            System.out.println("\nScope: "+scope);
            LinkedList<String> ID_List = symbolTable.get(scope);
            for (String id : ID_List) {
                String val = values.get(id + scope);
                String type = types.get(id + scope);
                System.out.print(val + " " + id + " " + type + "\n");
            }
        }
    }


    public String getType(String id, String scope) 
    {
        String type = types.get(id + scope);
        if(type != null) 
        {
            return type;
        }
        else 
        {
            type = types.get(id+"global");
            if(type != null) 
            {
                return type;
            }
        }
        return null;
    }



    public LinkedList<String> getScopeTable(String scope) 
    {
        return symbolTable.get(scope);
    }


    public ArrayList<String> getFunctions() {
        LinkedList<String> list = symbolTable.get("global");
        ArrayList<String> functionNames = new ArrayList<String>();
        for (String func : list){
            if(values.get(func + "global") != null){
                String functionName = values.get(func + "global");
                if(functionName.equals("Function")){
                    functionNames.add(func);
                }
            }
        }
        return functionNames;
    }

    public Hashtable<String,  ArrayList<String>> getDupsInScopes(){
        Set<String>keys = symbolTable.keySet();
        Hashtable<String, ArrayList<String>> dupsTable = new Hashtable<String, ArrayList<String>>();
        
        for(String key : keys) {
            LinkedList<String> tmpList = symbolTable.get(key);
            
            ArrayList<String> dups = new ArrayList<String>();
            while(0 < tmpList.size() -1){
                Collections.sort(tmpList);
                if (tmpList.size() > 0) {
                    String checker = tmpList.pop();
                    if(tmpList.contains(checker)){
                        dups.add(checker);
                    }
                }
            }
            dupsTable.put(key, dups);
        }
        
        return dupsTable;
    }

public ArrayList<String> getVars() 
    {
        ArrayList<String> vars = new ArrayList<String>();
        Enumeration enumm = symbolTable.keys();
        while(enumm.hasMoreElements()) 
        {
            String scope = (String) enumm.nextElement();
            LinkedList<String> scopeList = symbolTable.get(scope);
            for(int i = 0; i < scopeList.size(); i++) 
            {
                String description = types.get(scopeList.get(i)+scope);
                if(description.equals("Var"))
                {
                    vars.add(scopeList.get(i));
                }
            }
        }
        return vars;
    }
    
       
}

