/* Generated By:JJTree: Do not edit this line. ASTNumber.java Version 6.0 */
/* JavaCCOptions:MULTI=true,NODE_USES_PARSER=false,VISITOR=true,TRACK_TOKENS=false,NODE_PREFIX=AST,NODE_EXTENDS=,NODE_FACTORY=,SUPPORT_CLASS_VISIBILITY_PUBLIC=true */
public
class ASTNumber extends SimpleNode {
  public ASTNumber(int id) {
    super(id);
  }

  public ASTNumber(CCALTokeniser p, int id) {
    super(p, id);
  }


  /** Accept the visitor. **/
  public Object jjtAccept(CCALTokeniserVisitor visitor, Object data) {

    return
    visitor.visit(this, data);
  }
}
/* JavaCC - OriginalChecksum=2d3771aa52e20c49da63ce9ba45d2e05 (do not edit this line) */