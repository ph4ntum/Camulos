import jwt
from datetime import datetime

def show_banner():
    print(r"""
     ██████╗ █████╗ ███╗   ███╗██╗   ██╗██╗      ██████╗ ███████╗
    ██╔════╝██╔══██╗████╗ ████║██║   ██║██║     ██╔═══██╗██╔════╝
    ██║     ███████║██╔████╔██║██║   ██║██║     ██║   ██║███████╗
    ██║     ██╔══██║██║╚██╔╝██║██║   ██║██║     ██║   ██║╚════██║
    ╚██████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝███████╗╚██████╔╝███████║
     ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝
    ------------------------------------------------------------
                  >> JWT Decoder by ph4ntum <<
    ------------------------------------------------------------
    """)

def decode_jwt(token: str) -> dict:
    """Decodifica un token JWT sin verificar la firma."""
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
        if "exp" in payload:
            payload["exp_date"] = datetime.fromtimestamp(payload["exp"]).strftime('%Y-%m-%d %H:%M:%S')
        return payload
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    show_banner()
    token = input("Ingrese el token JWT: ")
    result = decode_jwt(token)
    print("\n🔍 Resultado:")
    print(result)