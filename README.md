<h1>Sistema di certificazione digitale basato su blockchain permissioned in ambito accademico</h1>
<p>Il lavoro mira allo sviluppo di un sistema di certificazione digitale che sfrutti le potenzialità della tecnologia blockchain. In particolar modo, la scelta per il tipo di blockchain ricade sul modello permissioned, poiché il sistema deve permettere l'accesso esclusivamente a partecipanti verificati e conosciuti. Il sistema dovrà inoltre consentire agli stessi di caricare documenti che certificano l'assegnazione o l'aquasizione di titoli (per esempio attestati, diplomi, ecc.). Data la scelta di una soluzione blockchain permissioned, i documenti caricati su di esse sono verificati da tutti i partecipanti alla rete.</p>
<p>Al fine di raggiungere un certo livello di completezza, verranno approfondite e applicate diverse tecnologie, tra cui:</p>
<ul>
  <li>Hyperledger Fabric: una piattaforma DLT (Distributed Ledger Technology) open-source che offre alcune chiavi di differenziazione rispetto ad altri progetti blockchain</li>
  <li>IPFS (InterPlanetary File System): un sistema distribuito per l’archiviazione e l’accesso a file, siti Web, applicazioni e dati. Poiché all’interno della blockchain non è consentito l’inserimento di file, questi verranno caricati su IPFS, che produrrà un valore hash. Tale valore hash, al momento della scrittura, sarà
inserito sulla blockchain all’interno della transazione;</li>
  <li>Flask: un micro-framework Python capace di creare un’API per comunicare
con il database, Fabric e IPFS.</li>
</ul>

<h2>Tecnologie principali</h2>
