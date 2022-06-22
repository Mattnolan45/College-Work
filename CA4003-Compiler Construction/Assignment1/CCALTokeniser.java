/* CCALTokeniser.java */
/* Generated By:JavaCC: Do not edit this line. CCALTokeniser.java */
public class CCALTokeniser implements CCALTokeniserConstants {
        public static void main(String args[])
        {
                CCALTokeniser tokeniser;
                if (args.length == 0)
                {
                        System.out.println("Reading from standard input . . .");
                        tokeniser = new CCALTokeniser(System.in);
                }
                else if (args.length == 1)
                {
                        try
                        {
                                tokeniser = new CCALTokeniser(new java.io.FileInputStream(args[0]));
                        }
                        catch (java.io.FileNotFoundException e)
                        {
                                System.err.println("File " + args[0] + " not found.");
                                return;
                        }
                }
                else
                {
                        System.out.println("SLP Tokeniser: Usage is one of:");
                        System.out.println(" java CCALTokeniser < inputfile");
                        System.out.println("OR");
                        System.out.println(" java CCALTokeniser inputfile");
                        return;
                }


                try {
            tokeniser.program();
            System.out.println("Parse successful");
        } catch (ParseException e) {
            System.out.println(e.getMessage());
            System.out.println("Parse failure");
        }


        }

/***********************************
***** SECTION 4 - THE GRAMMAR *****
***********************************/
  static final public 

void program() throws ParseException {
    decl_list();
    function_list();
    main();
  }

  static final public void decl_list() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case VARIABLE:
    case CONSTANT:{
      decl();
      jj_consume_token(SEMICOLON);
      decl_list();
      break;
      }
    default:
      jj_la1[0] = jj_gen;
      ;
    }
  }

  static final public void decl() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case VARIABLE:{
      var_decl();
      break;
      }
    case CONSTANT:{
      const_decl();
      break;
      }
    default:
      jj_la1[1] = jj_gen;
      jj_consume_token(-1);
      throw new ParseException();
    }
  }

  static final public void var_decl() throws ParseException {
    jj_consume_token(VARIABLE);
    jj_consume_token(ID);
    jj_consume_token(COLON);
    type();
  }

  static final public void const_decl() throws ParseException {
    jj_consume_token(CONSTANT);
    jj_consume_token(ID);
    jj_consume_token(COLON);
    type();
    jj_consume_token(ASSIGNMENT);
    expression();
  }

  static final public void function_list() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case INTEGER:
    case BOOLEAN:
    case VOID:{
      function();
      function_list();
      break;
      }
    default:
      jj_la1[2] = jj_gen;
      ;
    }
  }

  static final public void function() throws ParseException {
    type();
    jj_consume_token(ID);
    jj_consume_token(LBRACKET);
    parameter_list();
    jj_consume_token(RBRACKET);
    jj_consume_token(LBRACE);
    decl_list();
    statement_block();
    jj_consume_token(RETURN);
    jj_consume_token(LBRACKET);
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case TRUE:
    case FALSE:
    case LBRACKET:
    case MINUS:
    case NUM:
    case ID:{
      expression();
      break;
      }
    default:
      jj_la1[3] = jj_gen;
      ;
    }
    jj_consume_token(RBRACKET);
    jj_consume_token(SEMICOLON);
    jj_consume_token(RBRACE);
  }

  static final public void type() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case INTEGER:{
      jj_consume_token(INTEGER);
      break;
      }
    case BOOLEAN:{
      jj_consume_token(BOOLEAN);
      break;
      }
    case VOID:{
      jj_consume_token(VOID);
      break;
      }
    default:
      jj_la1[4] = jj_gen;
      jj_consume_token(-1);
      throw new ParseException();
    }
  }

  static final public void parameter_list() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case ID:{
      nemp_parameter_list();
      break;
      }
    default:
      jj_la1[5] = jj_gen;
      ;
    }
  }

  static final public void nemp_parameter_list() throws ParseException {
    jj_consume_token(ID);
    jj_consume_token(COLON);
    type();
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case COMMA:{
      jj_consume_token(COMMA);
      nemp_parameter_list();
      break;
      }
    default:
      jj_la1[6] = jj_gen;
      ;
    }
  }

  static final public void main() throws ParseException {
    jj_consume_token(MAIN);
    jj_consume_token(LBRACE);
    decl_list();
    statement_block();
    jj_consume_token(RBRACE);
  }

  static final public void statement_block() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case IF:
    case WHILE:
    case SKIPTOKEN:
    case LBRACE:
    case ID:{
      statement();
      statement_block();
      break;
      }
    default:
      jj_la1[7] = jj_gen;
      ;
    }
  }

  static final public void statement() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case ID:{
      jj_consume_token(ID);
      choice_statement();
      break;
      }
    case LBRACE:{
      jj_consume_token(LBRACE);
      statement_block();
      jj_consume_token(RBRACE);
      break;
      }
    case IF:{
      jj_consume_token(IF);
      condition();
      jj_consume_token(LBRACE);
      statement_block();
      jj_consume_token(RBRACE);
      jj_consume_token(ELSE);
      jj_consume_token(LBRACE);
      statement_block();
      jj_consume_token(RBRACE);
      break;
      }
    case WHILE:{
      jj_consume_token(WHILE);
      condition();
      jj_consume_token(LBRACE);
      statement_block();
      jj_consume_token(RBRACE);
      break;
      }
    case SKIPTOKEN:{
      jj_consume_token(SKIPTOKEN);
      jj_consume_token(SEMICOLON);
      break;
      }
    default:
      jj_la1[8] = jj_gen;
      jj_consume_token(-1);
      throw new ParseException();
    }
  }

  static final public void choice_statement() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case ASSIGNMENT:{
      jj_consume_token(ASSIGNMENT);
      expression();
      jj_consume_token(SEMICOLON);
      break;
      }
    case LBRACKET:{
      jj_consume_token(LBRACKET);
      arg_list();
      jj_consume_token(RBRACKET);
      jj_consume_token(SEMICOLON);
      break;
      }
    default:
      jj_la1[9] = jj_gen;
      jj_consume_token(-1);
      throw new ParseException();
    }
  }

  static final public void expression() throws ParseException {
    choice_expression();
    expression_arith();
  }

  static final public void choice_expression() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case MINUS:
    case ID:{
      switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
      case MINUS:{
        jj_consume_token(MINUS);
        break;
        }
      default:
        jj_la1[10] = jj_gen;
        ;
      }
      jj_consume_token(ID);
      switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
      case LBRACKET:{
        jj_consume_token(LBRACKET);
        arg_list();
        jj_consume_token(RBRACKET);
        break;
        }
      default:
        jj_la1[11] = jj_gen;
        ;
      }
      break;
      }
    case NUM:{
      jj_consume_token(NUM);
      break;
      }
    case TRUE:{
      jj_consume_token(TRUE);
      break;
      }
    case FALSE:{
      jj_consume_token(FALSE);
      break;
      }
    case LBRACKET:{
      jj_consume_token(LBRACKET);
      expression();
      jj_consume_token(RBRACKET);
      break;
      }
    default:
      jj_la1[12] = jj_gen;
      jj_consume_token(-1);
      throw new ParseException();
    }
  }

  static final public void expression_arith() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case PLUS:
    case MINUS:{
      binary_arith_op();
      expression();
      break;
      }
    default:
      jj_la1[13] = jj_gen;

    }
  }

  static final public void fragment() throws ParseException {
    expression();
  }

  static final public void binary_arith_op() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case PLUS:{
      jj_consume_token(PLUS);
      break;
      }
    case MINUS:{
      jj_consume_token(MINUS);
      break;
      }
    default:
      jj_la1[14] = jj_gen;
      jj_consume_token(-1);
      throw new ParseException();
    }
  }

  static final public void condition() throws ParseException {
    choice_condition();
    condition_simple();
  }

  static final public void choice_condition() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case AND:{
      jj_consume_token(AND);
      condition();
      break;
      }
    case OR:{
      jj_consume_token(OR);
      condition();
      break;
      }
    default:
      jj_la1[15] = jj_gen;

    }
  }

  static final public void condition_simple() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case TILDE:{
      jj_consume_token(TILDE);
      condition();
      break;
      }
    case LBRACKET:{
      jj_consume_token(LBRACKET);
      condition();
      jj_consume_token(RBRACKET);
      break;
      }
    case TRUE:
    case FALSE:
    case MINUS:
    case NUM:
    case ID:{
      expression();
      comp_op();
      expression();
      break;
      }
    default:
      jj_la1[16] = jj_gen;
      jj_consume_token(-1);
      throw new ParseException();
    }
  }

  static final public void comp_op() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case EQUALS:{
      jj_consume_token(EQUALS);
      break;
      }
    case NOTEQUALS:{
      jj_consume_token(NOTEQUALS);
      break;
      }
    case LT:{
      jj_consume_token(LT);
      break;
      }
    case LE:{
      jj_consume_token(LE);
      break;
      }
    case GT:{
      jj_consume_token(GT);
      break;
      }
    case GE:{
      jj_consume_token(GE);
      break;
      }
    default:
      jj_la1[17] = jj_gen;
      jj_consume_token(-1);
      throw new ParseException();
    }
  }

  static final public void arg_list() throws ParseException {
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case ID:{
      nemp_arg_list();
      break;
      }
    default:
      jj_la1[18] = jj_gen;
      ;
    }
  }

  static final public void nemp_arg_list() throws ParseException {
    jj_consume_token(ID);
    switch ((jj_ntk==-1)?jj_ntk_f():jj_ntk) {
    case COMMA:{
      jj_consume_token(COMMA);
      nemp_arg_list();
      break;
      }
    default:
      jj_la1[19] = jj_gen;
      ;
    }
  }

  static private boolean jj_initialized_once = false;
  /** Generated Token Manager. */
  static public CCALTokeniserTokenManager token_source;
  static JavaCharStream jj_input_stream;
  /** Current token. */
  static public Token token;
  /** Next token. */
  static public Token jj_nt;
  static private int jj_ntk;
  static private int jj_gen;
  static final private int[] jj_la1 = new int[20];
  static private int[] jj_la1_0;
  static private int[] jj_la1_1;
  static {
      jj_la1_init_0();
      jj_la1_init_1();
   }
   private static void jj_la1_init_0() {
      jj_la1_0 = new int[] {0x1800,0x1800,0x1c000,0x40300000,0x1c000,0x0,0x1000000,0x10c40000,0x10c40000,0x48000000,0x0,0x40000000,0x40300000,0x0,0x0,0x0,0x40300000,0x0,0x0,0x1000000,};
   }
   private static void jj_la1_init_1() {
      jj_la1_1 = new int[] {0x0,0x0,0x0,0x2802,0x0,0x2000,0x0,0x2000,0x2000,0x0,0x2,0x0,0x2802,0x3,0x3,0x18,0x2806,0x7e0,0x2000,0x0,};
   }

  /** Constructor with InputStream. */
  public CCALTokeniser(java.io.InputStream stream) {
     this(stream, null);
  }
  /** Constructor with InputStream and supplied encoding */
  public CCALTokeniser(java.io.InputStream stream, String encoding) {
    if (jj_initialized_once) {
      System.out.println("ERROR: Second call to constructor of static parser.  ");
      System.out.println("       You must either use ReInit() or set the JavaCC option STATIC to false");
      System.out.println("       during parser generation.");
      throw new Error();
    }
    jj_initialized_once = true;
    try { jj_input_stream = new JavaCharStream(stream, encoding, 1, 1); } catch(java.io.UnsupportedEncodingException e) { throw new RuntimeException(e); }
    token_source = new CCALTokeniserTokenManager(jj_input_stream);
    token = new Token();
    jj_ntk = -1;
    jj_gen = 0;
    for (int i = 0; i < 20; i++) jj_la1[i] = -1;
  }

  /** Reinitialise. */
  static public void ReInit(java.io.InputStream stream) {
     ReInit(stream, null);
  }
  /** Reinitialise. */
  static public void ReInit(java.io.InputStream stream, String encoding) {
    try { jj_input_stream.ReInit(stream, encoding, 1, 1); } catch(java.io.UnsupportedEncodingException e) { throw new RuntimeException(e); }
    token_source.ReInit(jj_input_stream);
    token = new Token();
    jj_ntk = -1;
    jj_gen = 0;
    for (int i = 0; i < 20; i++) jj_la1[i] = -1;
  }

  /** Constructor. */
  public CCALTokeniser(java.io.Reader stream) {
    if (jj_initialized_once) {
      System.out.println("ERROR: Second call to constructor of static parser. ");
      System.out.println("       You must either use ReInit() or set the JavaCC option STATIC to false");
      System.out.println("       during parser generation.");
      throw new Error();
    }
    jj_initialized_once = true;
    jj_input_stream = new JavaCharStream(stream, 1, 1);
    token_source = new CCALTokeniserTokenManager(jj_input_stream);
    token = new Token();
    jj_ntk = -1;
    jj_gen = 0;
    for (int i = 0; i < 20; i++) jj_la1[i] = -1;
  }

  /** Reinitialise. */
  static public void ReInit(java.io.Reader stream) {
    jj_input_stream.ReInit(stream, 1, 1);
    token_source.ReInit(jj_input_stream);
    token = new Token();
    jj_ntk = -1;
    jj_gen = 0;
    for (int i = 0; i < 20; i++) jj_la1[i] = -1;
  }

  /** Constructor with generated Token Manager. */
  public CCALTokeniser(CCALTokeniserTokenManager tm) {
    if (jj_initialized_once) {
      System.out.println("ERROR: Second call to constructor of static parser. ");
      System.out.println("       You must either use ReInit() or set the JavaCC option STATIC to false");
      System.out.println("       during parser generation.");
      throw new Error();
    }
    jj_initialized_once = true;
    token_source = tm;
    token = new Token();
    jj_ntk = -1;
    jj_gen = 0;
    for (int i = 0; i < 20; i++) jj_la1[i] = -1;
  }

  /** Reinitialise. */
  public void ReInit(CCALTokeniserTokenManager tm) {
    token_source = tm;
    token = new Token();
    jj_ntk = -1;
    jj_gen = 0;
    for (int i = 0; i < 20; i++) jj_la1[i] = -1;
  }

  static private Token jj_consume_token(int kind) throws ParseException {
    Token oldToken;
    if ((oldToken = token).next != null) token = token.next;
    else token = token.next = token_source.getNextToken();
    jj_ntk = -1;
    if (token.kind == kind) {
      jj_gen++;
      return token;
    }
    token = oldToken;
    jj_kind = kind;
    throw generateParseException();
  }


/** Get the next Token. */
  static final public Token getNextToken() {
    if (token.next != null) token = token.next;
    else token = token.next = token_source.getNextToken();
    jj_ntk = -1;
    jj_gen++;
    return token;
  }

/** Get the specific Token. */
  static final public Token getToken(int index) {
    Token t = token;
    for (int i = 0; i < index; i++) {
      if (t.next != null) t = t.next;
      else t = t.next = token_source.getNextToken();
    }
    return t;
  }

  static private int jj_ntk_f() {
    if ((jj_nt=token.next) == null)
      return (jj_ntk = (token.next=token_source.getNextToken()).kind);
    else
      return (jj_ntk = jj_nt.kind);
  }

  static private java.util.List<int[]> jj_expentries = new java.util.ArrayList<int[]>();
  static private int[] jj_expentry;
  static private int jj_kind = -1;

  /** Generate ParseException. */
  static public ParseException generateParseException() {
    jj_expentries.clear();
    boolean[] la1tokens = new boolean[48];
    if (jj_kind >= 0) {
      la1tokens[jj_kind] = true;
      jj_kind = -1;
    }
    for (int i = 0; i < 20; i++) {
      if (jj_la1[i] == jj_gen) {
        for (int j = 0; j < 32; j++) {
          if ((jj_la1_0[i] & (1<<j)) != 0) {
            la1tokens[j] = true;
          }
          if ((jj_la1_1[i] & (1<<j)) != 0) {
            la1tokens[32+j] = true;
          }
        }
      }
    }
    for (int i = 0; i < 48; i++) {
      if (la1tokens[i]) {
        jj_expentry = new int[1];
        jj_expentry[0] = i;
        jj_expentries.add(jj_expentry);
      }
    }
    int[][] exptokseq = new int[jj_expentries.size()][];
    for (int i = 0; i < jj_expentries.size(); i++) {
      exptokseq[i] = jj_expentries.get(i);
    }
    return new ParseException(token, exptokseq, tokenImage);
  }

  /** Enable tracing. */
  static final public void enable_tracing() {
  }

  /** Disable tracing. */
  static final public void disable_tracing() {
  }

}