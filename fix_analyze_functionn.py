import ast

def find_try_without_except_or_finally(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()
    try:
        tree = ast.parse(code, filename=filename)
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
        return

    class TryVisitor(ast.NodeVisitor):
        def visit_Try(self, node):
            if not node.handlers and not node.finalbody:
                print(f"Try без except или finally в строке {node.lineno}")
            self.generic_visit(node)

    visitor = TryVisitor()
    visitor.visit(tree)

# Использование:
find_try_without_except_or_finally('rita_main.py')
