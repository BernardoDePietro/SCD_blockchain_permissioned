/*
 * Copyright IBM Corp. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

'use strict';

const { Contract } = require('fabric-contract-api');

class Titolo2 extends Contract {

    async insertTitolo(ctx, new_id_titolo, new_nome_titolo, new_id_studente, new_ipfs_hash) {
        const exists = await this.titoloExists(ctx, new_id_titolo);
        if (exists) {
            throw new Error(`Il titolo ${new_id_titolo} esiste già.`);
        }

        const titolo = {
            nome_titolo: new_nome_titolo,
            id_studente: new_id_studente,
            ipfs_hash: new_ipfs_hash,
        };

        await ctx.stub.putState(new_id_titolo.toString(), Buffer.from(JSON.stringify(titolo)));
        return ctx.stub.getTxID();
    }

    async readTitolo(ctx, id_titolo) {
        const titoloJSON = await ctx.stub.getState(id_titolo);
        if(!titoloJSON || titoloJSON.length === 0) {
            throw new Error(`Il titolo ${id_titolo} non esiste.`);
        }
        return titoloJSON.toString();
    }

    async deleteTitolo(ctx, id_titolo) {
        const exists = await this.titoloExists(ctx, id_titolo);
        if(!exists) {
            throw new Error (`Il titolo ${id_titolo} non esiste`);
        }
        return ctx.stub.deleteState(id_titolo);
    }

    async titoloExists(ctx, id_titolo) {
        const titoloJSON = await ctx.stub.getState(id_titolo);
        return titoloJSON && titoloJSON.length > 0;
    }

    async getAllTitoli(ctx) {
        const allResults = [];
        const iterator = await ctx.stub.getStateByRange('', '');
        let result = await iterator.next();
        while(!result.done) {
            const strValue = Buffer.from(result.value.value.toString()).toString('utf8');
            let record;
            try {
                record = JSON.parse(strValue);
            } catch(err) {
                record = strValue;
            }
            allResults.push(record);
            result = await iterator.next();
        }
        return JSON.stringify(allResults);
    }
}

module.exports = Titolo2;