import sys

class log:

    def info(self, end = "\n"):
        sys.stderr.write("[INFO] " + self + end);

    def ok(self, end = "\n"):
        sys.stderr.write("[ \x1b[0;32mOK\x1b[1;0m ] " + self + end);

    def warn(self, end = "\n"):
        sys.stderr.write("[\x1b[0;93mWARN\x1b[1;0m] " + self + end);

    def fail(self, end = "\n"):
        sys.stderr.write("[\x1b[1;31mFAIL\x1b[1;0m] " + self + end);
    
    def print(self, end = "\n"):
        sys.stderr.write("       " + self + end);

    def tree(self, start = True, end = True, tree = 0):

        i=0;
        
        for line in self:
            symbol = "├╴";

            if i == 0 and start:
                symbol = "╭╴"
            if i == (len(self)-1) and end:
                symbol = "╰╴"

            
            i2 = 0;
            spacing = "";
            while i2 < tree:
                spacing += "│  ";
                i2=i2+1;

            if isinstance(line, list):
                log.tree(line, False, True, tree+1)
            else:
                log.print(spacing + symbol + line);

            i=i+1;
        if tree > 0:
            log.print(spacing)