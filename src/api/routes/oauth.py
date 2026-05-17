from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/oauth/callback", response_class=HTMLResponse)
async def oauth_callback(
    code: str = Query(None),
    error: str = Query(None)
):
    if error:
        return f"""
        <html>
            <body style="font-family: sans-serif; padding: 40px;">
                <h2>OAuth Error</h2>
                <p>{error}</p>
            </body>
        </html>
        """

    if not code:
        return """
        <html>
            <body style="font-family: sans-serif; padding: 40px;">
                <h2>No authorization code received</h2>
            </body>
        </html>
        """

    return f"""
    <html>
        <head>
            <title>OAuth Authorization Code</title>
        </head>

        <body style="
            font-family: sans-serif;
            padding: 40px;
            background: #f5f5f5;
        ">
            <h2>Authorization Code</h2>

            <p>Copy this code and use it to generate your refresh token:</p>

            <textarea
                id="code"
                readonly
                style="
                    width: 100%;
                    height: 120px;
                    font-size: 14px;
                    padding: 10px;
                "
            >{code}</textarea>

            <br /><br />

            <button
                onclick="copyCode()"
                style="
                    padding: 10px 20px;
                    font-size: 14px;
                    cursor: pointer;
                "
            >
                Copy Code
            </button>

            <script>
                function copyCode() {{
                    const textarea = document.getElementById("code");
                    textarea.select();
                    textarea.setSelectionRange(0, 99999);

                    navigator.clipboard.writeText(textarea.value);

                    alert("Code copied!");
                }}
            </script>
        </body>
    </html>
    """