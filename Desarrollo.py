#Investigue, y en python int ya permite trabajar con numeros enormes
def tam(n):
    #retorna el tamaño, convertido en string, y por si fuese negativo, lo convierte en su absoluto
    return len(str(abs(n)))

def mult(u,v):
    #numeros chicos
    n = max(tam(u),tam(v))
    if n <=2:
        return u * v
    else:
        #numeros grandes
        s = n//2
        p = 10**s
        
        w = u//p
        x = u % p
        y = v // p
        z = v % p
        return mult(w,y)*(10**(2*s))+(mult(w,z)+mult(x,y))*(10**s)+mult(x,z)
    
u = 12345678910541
v = 51548768468468

res = mult(u,v)
print(f"El resultado es: {res}")