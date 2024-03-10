"""A simple lexical analyzer"""

#standard library

#3rd party library
#Project library
from calculator.token import Token, TokenType

class Lexer:
#-------------------------------------------------------------------------------------------------------------------------------------------------
    def get_number(self, text, pos):
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if not text[pos].isdigit():
            return Token(TokenType.ERROR, lexeme), pos
        
        while pos < length and text[pos].isdigit():
            lexeme += text[pos]
            pos += 1
        return Token(TokenType.NUMBER, lexeme), pos
    
    def get_add_op(self, text, pos):
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        if text[pos] == '+' :
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.ADD_OP, lexeme), pos
        elif text[pos] == '-':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.ADD_OP, lexeme), pos
        else:return Token(TokenType.ERROR, lexeme), pos

    def get_mul_op(self, text, pos):
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        if text[pos] == '*' :
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == '/':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == '%':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.MUL_OP, lexeme), pos
        else:return Token(TokenType.ERROR, lexeme), pos

    def get_power_op(self, text, pos):
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        if text[pos] == '^' :
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.POWER_OP, lexeme), pos
        else:return Token(TokenType.ERROR, lexeme), pos

    def get_fac_op(self, text, pos):
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        if text[pos] == '!' :
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.FAC_OP, lexeme), pos
        else:return Token(TokenType.ERROR, lexeme), pos
        
    def get_L_paren(self, text, pos):
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        if text[pos] == '(':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.LEFT_OP, lexeme), pos
        else:return Token(TokenType.ERROR, lexeme), pos

    def get_R_paren(self, text, pos):
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        if text[pos] == ')':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.RIGHT_OP, lexeme), pos
        else:return Token(TokenType.ERROR, lexeme), pos

#-----------------------------------------------------------------------------------------------------------------------------
    def get_token(self, text, pos):
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        
        if text[pos].isdigit():
            while pos < length and text[pos].isdigit():
                lexeme += text[pos]
                pos += 1
            return Token(TokenType.NUMBER, lexeme), pos
        #add_op
        if text[pos] == '+' :
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.ADD_OP, lexeme), pos
        elif text[pos] == '(':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.LEFT_OP, lexeme), pos
        elif text[pos] == ')':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.RIGHT_OP, lexeme), pos
        elif text[pos] == '-':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.ADD_OP, lexeme), pos
        #mul_op
        elif text[pos] == '*' :
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == '/':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == '%':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.MUL_OP, lexeme), pos
        #power_op
        elif text[pos] == '^' :
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.POWER_OP, lexeme), pos
        #fac_op
        elif text[pos] == '!' :
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.FAC_OP, lexeme), pos
        else:return Token(TokenType.ERROR, lexeme), pos
    

    def skip_white_space(self, text, pos):
        """Skip all white spaces.
       
        Args:
            text (str): Text to be scanned.
            pos (int):  The starting position to scan.
           
        Return:
            new_pos (int)   The position after the last white space
       
        """
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos
        if text[pos] == " ":
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.SPACE, lexeme), pos
        else:return Token(TokenType.ERROR, lexeme), pos
