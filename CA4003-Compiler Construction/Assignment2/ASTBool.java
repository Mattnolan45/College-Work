/* Generated By:JJTree: Do not edit this line. ASTBool.java Version 6.0 */
/* JavaCCOptions:MULTI=true,NODE_USES_PARSER=false,VISITOR=true,TRACK_TOKENS=false,NODE_PREFIX=AST,NODE_EXTENDS=,NODE_FACTORY=,SUPPORT_CLASS_VISIBILITY_PUBLIC=true */
public
class ASTBool extends SimpleNode {
  public ASTBool(int id) {
    super(id);
  }

  public ASTBool(CCALTokeniser p, int id) {
    super(p, id);
  }


  /** Accept the visitor. **/
  public Object jjtAccept(CCALTokeniserVisitor visitor, Object data) {

    return
    visitor.visit(this, data);
  }
}
/* JavaCC - OriginalChecksum=3955b2b93d1f577229544527bfc41b34 (do not edit this line) */