#!/usr/bin/node
const Squared = require('./5-sqaure');

module.exports = class Sqaure extends Sqaured {
  charprint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
	s += c;
      }
      console.log(s);
    }
  }
};
