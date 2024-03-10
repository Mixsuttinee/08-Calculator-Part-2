#standard library

#3rd party library
import pytest
#Project library
from calculator.token import Token, TokenType
from calculator.lexer import Lexer

@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.NUMBER,"456"),3),
        ("705", 1, Token(TokenType.NUMBER,"05"),3),
        ("+", 0, Token(TokenType.ERROR,""),0),
    ]
)
def test_get_number(text, pos, expected_token, expected_pos):
    #arange
    lexer = Lexer()
    #act
    token, new_pos = lexer.get_number(text, pos)
    #assert
    assert token == expected_token
    assert new_pos == expected_pos


@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR,""),0),
        ("705", 1, Token(TokenType.ERROR,""),1),
        ("+", 0, Token(TokenType.ADD_OP,"+"),1),
        ("+-", 1, Token(TokenType.ADD_OP,"-"),2),
    ]
)
def test_get_add_op(text, pos, expected_token, expected_pos):
    #arange
    lexer = Lexer()
    #act
    token, new_pos = lexer.get_add_op(text, pos)
    #assert
    assert token == expected_token
    assert new_pos == expected_pos

@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR,""),0),
        ("705", 1, Token(TokenType.ERROR,""),1),
        ("+", 0, Token(TokenType.ERROR,""),0),
        ("+-", 1, Token(TokenType.ERROR,""),1),
        ("*/%", 1, Token(TokenType.MUL_OP,"/"),2),
        ("*", 0, Token(TokenType.MUL_OP,"*"),1),
        ("*/%", 2, Token(TokenType.MUL_OP,"%"),3),
    ]
)
def test_get_mul_op(text, pos, expected_token, expected_pos):
    #arange
    lexer = Lexer()
    #act
    token, new_pos = lexer.get_mul_op(text, pos)
    #assert
    assert token == expected_token
    assert new_pos == expected_pos

@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR,""),0),
        ("705", 1, Token(TokenType.ERROR,""),1),
        ("+", 0, Token(TokenType.ERROR,""),0),
        ("+-", 1, Token(TokenType.ERROR,""),1),
        ("*/%", 1, Token(TokenType.ERROR,""),1),
        ("^", 0, Token(TokenType.POWER_OP,"^"),1),
        ("*/^", 2, Token(TokenType.POWER_OP,"^"),3),
    ]
)
def test_get_power_op(text, pos, expected_token, expected_pos):
    #arange
    lexer = Lexer()
    #act
    token, new_pos = lexer.get_power_op(text, pos)
    #assert
    assert token == expected_token
    assert new_pos == expected_pos

@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR,""),0),
        ("705", 1, Token(TokenType.ERROR,""),1),
        ("+", 0, Token(TokenType.ERROR,""),0),
        ("3!", 1, Token(TokenType.FAC_OP,"!"),2),
        ("/*!", 2, Token(TokenType.FAC_OP,"!"),3),
        ("3*3!", 3, Token(TokenType.FAC_OP,"!"),4),
        ("*3!", 0, Token(TokenType.ERROR,""),0),
    ]
)
def test_get_fac_op(text, pos, expected_token, expected_pos):
    #arange
    lexer = Lexer()
    #act
    token, new_pos = lexer.get_fac_op(text, pos)
    #assert
    assert token == expected_token
    assert new_pos == expected_pos


@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR,""),0),
        ("(7)", 2, Token(TokenType.RIGHT_OP,")" ),3),
        ("*()", 2, Token(TokenType.RIGHT_OP,")" ),3),
    ]
)
def test_get_R_paren(text, pos, expected_token, expected_pos):
    #arange
    lexer = Lexer()
    #act
    token, new_pos = lexer.get_R_paren(text, pos)
    #assert
    assert token == expected_token
    assert new_pos == expected_pos

@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR,""),0),
        ("(7)", 0, Token(TokenType.LEFT_OP,"(" ),1),
        ("*(", 1, Token(TokenType.LEFT_OP,"(" ),2),
    ]
)
def test_get_L_paren(text, pos, expected_token, expected_pos):
    #arange
    lexer = Lexer()
    #act
    token, new_pos = lexer.get_L_paren(text, pos)
    #assert
    assert token == expected_token
    assert new_pos == expected_pos

@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        (" 456", 0, Token(TokenType.SPACE," "),1),
        (" abc", 0, Token(TokenType.SPACE," "),1),
        (" xyz ", 0, Token(TokenType.SPACE," "),1),
        (" xyz ", 1, Token(TokenType.ERROR,""),1),
        (" xyz ", 2, Token(TokenType.ERROR,""),2),
        (" xyz ", 3, Token(TokenType.ERROR,""),3),
        (" xyz ", 4, Token(TokenType.SPACE," "),5),
    ]
)
def test_space(text, pos, expected_token, expected_pos):
    #arange
    lexer = Lexer()
    #act
    token, new_pos = lexer.skip_white_space(text, pos)
    #assert
    assert token == expected_token
    assert new_pos == expected_pos

@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("123+(32/4)",0,Token(TokenType.NUMBER,"123"),3),
        ("123+(32/4)",3,Token(TokenType.ADD_OP,"+"),4),
        ("123+(32/4)",4,Token(TokenType.LEFT_OP,"("),5),
        ("123+(32/4)",5,Token(TokenType.NUMBER,"32"),7),
        ("123+(32/4)",7,Token(TokenType.MUL_OP,"/"),8),
        ("123+(32/4)",8,Token(TokenType.NUMBER,"4"),9),
        ("123+(32/4)",9,Token(TokenType.RIGHT_OP,")"),10),
    ]
)
def test_all_token(text, pos, expected_token, expected_pos):
    #arange
    lexer = Lexer()
    #act
    token, new_pos = lexer.get_token(text, pos)
    #assert
    assert token == expected_token
    assert new_pos == expected_pos