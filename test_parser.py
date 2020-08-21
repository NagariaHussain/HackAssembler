from unittest import TestCase, main
from hack_parser import parser, code

# Test clean function
class ParserCleanTest(TestCase):
    def test_clean_newline(self):
        self.assertEqual(parser.clean("\n"), "")

    def test_clean_comment(self):
        self.assertEqual(parser.clean("// Hello world"), "")
    
    def test_clean_inline_comment(self):
        self.assertEqual(parser.clean("MD=D+1;JMP // A comment"), "MD=D+1;JMP")
    
    def test_clean_whitespaces(self):
        self.assertEqual(parser.clean("    M= D+ 1 "), "M=D+1")

# Test select function 
class ParserSelectTest(TestCase):
    def test_select_valid_a(self):
        self.assertTrue(parser.select("@786"))

    def test_select_valid_label(self):
        self.assertTrue(parser.select("(END)"))

    def test_select_valid_c(self):
        self.assertTrue(parser.select("A=D+M"))
    
    def test_unselect_empty_string(self):
        self.assertFalse(parser.select(""))

    def test_unselect_comments(self):
        self.assertFalse(parser.select("// This is a comment"))


# Test instruction translation
class CodeTranslationText(TestCase):
    def test_a_100_instruction(self):
        c = code.Code()
        self.assertEqual(c.handle_a_ins("100"), "0000000001100100")
    
    def test_a_0_instruction(self):
        c = code.Code()
        self.assertEqual(c.handle_a_ins("0"), "0000000000000000")

    def test_c_0_instruction(self):
        c = code.Code()
        self.assertEqual(c.handle_c_instruction("0", "D", "JGT"), "1110101010010001")

    def test_c_instruction_without_dest(self):
        c = code.Code()
        self.assertEqual(c.handle_c_instruction("D", None, "JMP"), "1110001100000111")
    
    def test_c_instruction_without_jump(self):
        c = code.Code()
        self.assertEqual(c.handle_c_instruction("A-D", "M", None), "1110000111001000")
    

if __name__ == '__main__':
    # Running the test suite
    main()