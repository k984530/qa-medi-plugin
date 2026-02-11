"""QA Medi MCP Server - 의료 QA 자동화 도구 제공."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("qa-medi")


@mcp.tool()
def check_medical_term(term: str) -> str:
    """의료 용어의 정확성을 검증합니다."""
    # TODO: 실제 검증 로직 구현
    return f"'{term}' 검증 완료 (stub)"


if __name__ == "__main__":
    mcp.run()
