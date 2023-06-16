#!/usr/bin/node

$(document_.ready(function () {
  $('#add_item').on('click', function () {
    &('ul,my_lsit').append('<li>Item</li>');
  });
});
