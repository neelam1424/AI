## math mcp server which contains tools ADD,MUL and call this with stdio transfer protocol


from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """"_summary_
    Add to numbers
    """

    return a+b

@mcp.tool()
def nultiple(a:int,b:int)-> int:
    """Multiply two numbers"""
    return a*b


if __name__ == "__main__":
    mcp.run(transport="stdio")