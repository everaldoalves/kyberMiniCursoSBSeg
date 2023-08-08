# testeKyber.py
from kyberMinicursoV2 import Kyber
from sage.modules.free_module_element import vector

# Cria uma instância da classe Kyber com nível de segurança 128
kyber = Kyber(128)

# Gera um par de chaves pública e privada
pk, sk = kyber.keygen()

# Escolhe uma mensagem para criptografar
message = [1, 2, 3, 4]

# Verifica se a mensagem tem a dimensão correta
if len(message) != kyber.params.n:
    # Ajusta a mensagem, se necessário
    message = message + [0] * (kyber.params.n - len(message))
    print("Mensagem formatada", message)

# Encriptação
ciphertext = kyber.encrypt(pk, vector(kyber.F, message), b'randomness')
print("Mensagem encriptada", ciphertext)

# Decriptação
decrypted_message = kyber.decrypt(sk, ciphertext)
print("Mensagem decriptada", decrypted_message)

# Verifica se a mensagem decriptada é igual à mensagem original
assert decrypted_message == vector(kyber.F, message)
