import crcmod
import qrcode

def gerarQRCode(valor):
    chave = '+5521990935252'
    nome = 'Bar do Malhado'
    cidade = 'Rio de Janeiro'
    precrc = f'00020126360014BR.GOV.BCB.PIX0114{chave}52040000530398654{len(valor):02}{valor}5802BR59{len(nome)}{nome}60{len(cidade)}{cidade}62070503***6304'
    crc = crcmod.mkCrcFun(0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0)
    crc = hex(crc(str(precrc).encode('utf-8'))).replace('0x', '').upper()

    codigo = f'{precrc}{crc}'

    qr = qrcode.make(codigo)
    return qr.save('./static/img/pagamento.png')