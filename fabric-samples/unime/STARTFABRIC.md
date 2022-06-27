## Starting utils
starting ipfs
```bash
ipfs daemon
```

starting postman
```bash
cd Postman
./Postman_Agent
```

starting xampp
```bash
cd ../..
cd opt/lampp
sudo ./xampp start
```

starting server flask
```bash
cd go/src/github.com/BernardoDePietro/fabric-samples/unime/api/
python3 app.py
```

## Inizializzazione e comandi per fabric - unime

Il primo comando da eseguire per inizializzare ed eseguire, la blockchain di fabric e simultaneamente crea anche il canale che mette in comunicazione org1 e org2, è:

```bash
cd go/src/github.com/BernardoDePietro/fabric-samples/unime/
./network.sh up createChannel
```


## Installazione del chaincode

Successivamente si può installare il chaincode sulla blockchain:

```bash
./network.sh deployCC -c canale1 -ccn titolo -ccp ../chaincode/unime/javascript -ccl javascript
```

Con questo comando viene installato sulla blockchain il chaincode che prende il nome di titolo ed è scritto in javascript.


## Impostazione delle variabili d'ambiente

Per andare ad effettuare le operazioni sulla blockchain si devono settare le variabili d'ambiente in base all'organizzazione che deve effettuare le operazioni. A questo proposito ho preparato tre file chiamati setOrg1Env, setOrg2Env e setOrg3Env. Basta eseguire uno dei seguenti comandi per operare come una delle relative organizzazioni:

```bash
source ./setOrg1Env.sh # Utilizzato per operare come org1.

source ./setOrg2Env.sh # Utilizzato per operare come org2.

source ./setOrg3Env.sh # Utilizzato per operare come org3, in questo esempio non viene creato il canale che comunica org3 ad altre organizzazioni, di conseguenza il successivo comando produrrà un errore se viene eseguito come org3.
```

## Inserimento di un titolo nella blockchain

Dopo aver impostato le variabili d'ambiente è possibili inserire elementi all'interno della blockchain. Il seguente comando utilizza la funzione "createTitolo" presente nel chaincode Titolo per inserire un titolo formato da quattro attributi:

```bash
peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n titolo --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"function":"insertTitolo","Args":["1", "titolo1", "1", "hash1"]}'
```

