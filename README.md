# OAI-PMH Harvester
Script python per l'export nel formato CSV dei metadati descrittivi esposti tramite protocollo OAI-PMH. I metadati vengono estratti e salvati secondo lo standard Dublin Core. 


## Installazione ##
Per l'utilizzo degli scripts è necessario aver scaricato `Python 3.8+` sul proprio dispositivo, per installare Python seguire le istruzioni riportate al seguente [link](https://www.python.org/downloads/).

Una volta eseguito il download è possibile verificare le versioni di `Python` e `pip` tramite i comandi:

```
python --version
```
```
pip --version
```

### Ambiente virtuale ###
Per non compromettere l'installazione di Python e le relative librerie è consigliabile creare un ambiente virtuale indipendente dal proprio sistema; per la creazione di un ambiente virtuale procedere come segue:

Creare l'ambiente virtuale
```
python -m venv pyenv
```

Attivare l'ambiente virtuale:
```
source pyenv/bin/activate
```

### Librerie ###
Una volta attivato l'ambiente virtuale è possibile procedere con l'installazione delle librerie necessarie

```
pip install -r requirements.txt
```


## Utilizzo ##
Una volta scaricato il repository e scaricate le librerie necessarie, per avviare lo script sarà sufficiente eseguire il comando:
```
python oaiClient.py
```
Verrà quindi chiesto di inserire, a riga di comando, l'URL da cui effettuare l'estrazione.

Una volta lanciato lo script comincerà a scrivere all'interno di una file CSV, denominato con la data corrente, i metadati esposti.

Ad ogni colonna è assegnato un campo Dublin Core, per il campo `\\dc:subjects` viene creata una colonna aggiuntiva, alla fine, per ogni valore