import sys
import builtins

if not hasattr(builtins, 'exit'):
    builtins.exit = sys.exit

if not hasattr(builtins, 'quit'):
    builtins.quit = sys.exit