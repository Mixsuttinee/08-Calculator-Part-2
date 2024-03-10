# simple-calculate
work for 305396 08 Calculator Part 2
There are several tasks for this assignment.

1. Extend your solution from assignment 07 by adding the method get_token() from the attached file.  The method get_token() will replace the methods: get_add_op(), get_mul_op(), get_power_op() and get_fac_op().  This is the result of refactoring the code from assignment 07.  

2. Then implement the method skip_while_space() to skip all white spaces this method accept two parameters (text, pos) like other methods but return only the position after the last white space instead of both token and position.

    def skip_white_space(text, pos):
        """Skip all white spaces.
       
        Args:
            text (str): Text to be scanned.
            pos (int):  The starting position to scan.
           
        Return:
            new_pos (int)   The position after the last white space
       
        """
   
    e.g. skip_white_space(" abc ", 0) ==> 1
         skip_white_space(" xyz ", 0) ==> 1
         skip_white_space(" xyz ", 1) ==> 1
         skip_white_space(" xyz ", 2) ==> 2
         skip_white_space(" xyz ", 3) ==> 3
         skip_white_space(" xyz ", 4) ==> 5
         skip_white_space(" xyz ", 5) ==> 5
         skip_white_space("   pqr", 0) ==> 3
         
3. Then implement the method get_token_list() which scans the entire text and
    produces the list of tokens
   
    def get_token_list(text, pos):
        """
        Extract all tokens from the text.
       
        Args:
            text (str): Text to be scanned.
            pos (int):  The starting position to scan.
           
        Return:
            list_of_tokens   The list of all tokens
       
        """
       
    e.g. get_token_list("123 + (32 / 4)", 0) will return the following list
        [
            Token(TokenType.NUMBER, "123"),
            Token(TokenType.ADD_OP, "+"),
            Token(TokenType.LEFT_PAREN, "("),
            Token(TokenType.NUMBER, "32"),
            Token(TokenType.MUL_OP, "/"),
            Token(TokenType.NUMBER, "4"),
            Token(TokenType.RIGHT_PAREN, ")"),
        ]
