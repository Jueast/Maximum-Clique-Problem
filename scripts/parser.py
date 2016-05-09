SOURCE_FILE = "./frb30-15-clq/frb30-15-1.clq"
TARGET_FILE = "./data/graph.clq"

###################################################################
#
# Benchmark data format:
#	
#	c [str]: comment
#	p edge [num of vertexs] [num of edges]: overview information
# 	e [src] [dst]: edge information
#
#
# Output file format:
#
# 	[num of vertexs] [num of edges]
# 	[src] [dst]  
# 	[src] [dst]
# 	....
#
####################################################################

def parse(line, out):
	line = line.strip("\n");
	if line[0] == "c":
		return
	if line[0] == "p":
		tokens = list(filter(lambda x: x != '', line.split(' ')))
		v, e = [int(s) for s in tokens[-2::]] 
		out.write("%d %d\n" % (v, e))
		return
	if line[0] == "e":
		tokens = list(filter(lambda x: x != '', line.split(' ')))
		src, dst = [int(s) for s in tokens[-2::]]
		out.write("%d %d\n" % (src, dst))
		return 

if __name__ == "__main__":
	inFile = open(SOURCE_FILE, "r");
	outFile = open(TARGET_FILE, "w");
	for line in inFile.readlines():
		parse(line, outFile)
	inFile.close()
	outFile.close()
