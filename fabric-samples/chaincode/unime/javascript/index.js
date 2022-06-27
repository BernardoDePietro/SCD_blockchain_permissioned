/*
 * Copyright IBM Corp. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

'use strict';

const Titolo = require('./lib/titolo');
const Titolo2 = require('./lib/titolo2');

module.exports.Titolo2 = Titolo2;
module.exports.contracts = [ Titolo2 ];

module.exports.Titolo = Titolo;
module.exports.contracts = [ Titolo ];