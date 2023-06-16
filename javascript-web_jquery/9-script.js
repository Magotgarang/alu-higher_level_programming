#!/usr/bin/node

$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  datatype: 'json',
  sucesss: (json) => {
    &('div#hello').text(json);
  }
});
