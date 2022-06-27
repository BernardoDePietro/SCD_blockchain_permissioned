import subprocess, os
import json

from python_shell import Shell

my_env = dict(os.environ)

class Blockchain():
    def __init__(self, promotore):
        my_env['PATH'] = "/home/bernardo/go/src/github.com/BernardoDePietro/fabric-samples/unime/api/../../bin:$PATH"
        my_env['FABRIC_CFG_PATH'] = "/home/bernardo/go/src/github.com/BernardoDePietro/fabric-samples/unime/api/../../config/"
        my_env['CORE_PEER_TLS_ENABLED'] = "true"
        if(promotore == 1):
            my_env['CORE_PEER_LOCALMSPID'] = "Org2MSP"
            my_env['CORE_PEER_TLS_ROOTCERT_FILE'] = "/home/bernardo/go/src/github.com/BernardoDePietro/fabric-samples/unime/api/../organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt"
            my_env['CORE_PEER_MSPCONFIGPATH'] = "/home/bernardo/go/src/github.com/BernardoDePietro/fabric-samples/unime/api/../organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp"
            my_env['CORE_PEER_ADDRESS'] = "localhost:9051"
            canale = "canale1"
        else:
            my_env['CORE_PEER_LOCALMSPID'] = "Org3MSP"
            my_env['CORE_PEER_TLS_ROOTCERT_FILE'] = "/home/bernardo/go/src/github.com/BernardoDePietro/fabric-samples/unime/api/../organizations/peerOrganizations/org3.example.com/peers/peer0.org3.example.com/tls/ca.crt"
            my_env['CORE_PEER_MSPCONFIGPATH'] = "/home/bernardo/go/src/github.com/BernardoDePietro/fabric-samples/unime/api/../organizations/peerOrganizations/org3.example.com/users/Admin@org3.example.com/msp"
            my_env['CORE_PEER_ADDRESS'] = "localhost:11051"
            canale = "canale2"

    def insertTitolo(self, id_titolo, nome_titolo, id_studente, ipfs_hash):
        if(my_env["CORE_PEER_LOCALMSPID"] == "Org2MSP"):
            create_request = "peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/../organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C canale1 -n titolo --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/../organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/../organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt --peerAddresses localhost:11051 --tlsRootCertFiles ${PWD}/../organizations/peerOrganizations/org3.example.com/peers/peer0.org3.example.com/tls/ca.crt -c '{\"function\":\"insertTitolo\",\"Args\":[\"" + str(id_titolo) + "\", \"" + str(nome_titolo) + "\", \"" + str(id_studente) + "\", \"" + str(ipfs_hash) + "\"]}'"
            #create_request = "peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/../organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C canale1 -n titolo --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/../organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles ${PWD}/../organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{\"function\":\"insertTitolo\",\"Args\":[\"" + str(id_titolo) + "\", \"" + str(nome_titolo) + "\", \"" + str(id_studente) + "\", \"" + str(ipfs_hash) + "\"]}'"
        else:
            create_request = "peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile ${PWD}/../organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C canale2 -n titolo2 --peerAddresses localhost:7051 --tlsRootCertFiles ${PWD}/../organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:11051 --tlsRootCertFiles ${PWD}/../organizations/peerOrganizations/org3.example.com/peers/peer0.org3.example.com/tls/ca.crt -c '{\"function\":\"insertTitolo\",\"Args\":[\"" + str(id_titolo) + "\", \"" + str(nome_titolo) + "\", \"" + str(id_studente) + "\", \"" + str(ipfs_hash) + "\"]}'"
        output = subprocess.run(create_request, shell=True, env=my_env, capture_output=True)
        #status, payload = self.getResponse(output.stderr.decode("utf-8"))
        #if(status == '200'):
        #    return payload
        #return status

    def getTitolo(self, id_titolo):
        read_request = "peer chaincode query -C " + str(self.canale) + " -n titolo -c '{\"Args\":[\"readTitolo\", \"" + str(id_titolo) + "\"]}'"
        titolo = subprocess.run(read_request, shell=True, env=my_env, capture_output=True)
        return json.loads(titolo.stderr.decode('utf-8'))

    def deleteTitolo(self, id_titolo):
        delete_request = "peer chaincode query -C " + str(self.canale) + " -n titolo -c '{\"Args\":[\"deleteTitolo\", \"" + str(id_titolo) + "\"]}'"
        titolo = subprocess.run(delete_request, shell=True, env=my_env, capture_output=True)
        return json.loads(titolo.stderr.decode('utf-8'))

    def getAllTitoli(self):
        read_request = "peer chaincode query -C " + str(self.canale) + " -n titolo -c '{\"Args\":[\"getAllTitoli\"]}'"
        titoli = subprocess.run(read_request, shell=True, env=my_env, capture_output=True)
        return json.loads(titoli.stderr.decode('utf-8'))

    def getResponse(input):
        temp = ''
        status = ''
        payload = ''
        for char in input:
            char = str(char)
            if(temp.startswith('status:')):
                if(char.isdigit()):
                    status += char

            if(temp.startswith('payload:\"')):
                if(char != '\"'):
                    payload += char
            
            if(char != ' '):
                temp += char
            else:
                temp = ''
        return status, payload