#!/usr/bin/node
let callCount = 0;

exports.logMe = function (item) {
  console.log('&{callCount}: &{item}');
  callCountn =+ 1;
};
