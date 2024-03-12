from glob import glob
from zipfile import ZipFile
import os
import sys
import patoolib


def unzip(pasta):
    zipStored = True
    while zipStored:
        zipStored = [filename for filename in (glob(pasta + '\\*.zip') or glob(pasta + '\\*.rar'))]
        i = 0
        for arquivo in zipStored:
            i = arquivo[-16:-4]
            if arquivo.endswith('.zip'):
                if not os.path.isdir(pasta + destino):
                    os.mkdir(pasta + destino)
                print(i)
                zf = ZipFile(arquivo, 'r')
                zf.extractall(pasta + destino)
                zf.close()
                os.rename(pasta + destino + "\\resumo.txt", pasta + destino +"\\"+ i + ".txt")
            
            elif arquivo.endswith('.rar'):
                if not os.path.isdir(pasta + destino):
                    os.mkdir(pasta + destino)
                patoolib.extract_archive(arquivo, outdir=pasta + destino)
        break


pasta = "C:\\Users\\roger\\proj\\pythonando\\pasta_teste" 
destino = "\\pasta_destino"


unzip(pasta)