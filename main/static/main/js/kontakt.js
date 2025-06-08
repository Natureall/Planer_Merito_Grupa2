document.addEventListener('DOMContentLoaded', () => {
  function getCookie(name) {
    let v = null;
    if (document.cookie && document.cookie !== '') {
      document.cookie.split(';').forEach(c => {
        const [k, val] = c.trim().split('=');
        if (k === name) v = decodeURIComponent(val);
      });
    }
    return v;
  }
  const csrftoken = getCookie('csrftoken');

  const btn = document.getElementById('btn-kontakt');
  if (!btn) return;

  function bindForm() {
    const form = document.getElementById('kontakt-form');
    if (!form) return;
    form.addEventListener('submit', e => {
      e.preventDefault();
      const data = new FormData(form);
      fetch('/ajax/kontakt/', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { 'X-CSRFToken': csrftoken },
        body: data
      })
      .then(res => {
        console.log('Fetch /ajax/kontakt/ status:', res.status);
        console.log('Request headers sent:', res.headers);
        if (!res.ok) return res.text().then(text => { throw new Error(text) });
        return res.json();
      })
      .then(json => {
        document.getElementById('content').innerHTML =
          `<p style="color:green;">${json.success ? 'Wysłano wiadomość!' : 'Coś poszło nie tak.'}</p>`;
      })
      .catch(err => {
        console.error('Error submitting form:', err);
        alert('Błąd wysyłania formularza: ' + err.message);
      });
    });
  }

  btn.addEventListener('click', e => {
    e.preventDefault();
    fetch('/ajax/kontakt/', { credentials: 'same-origin' })
      .then(r => r.text())
      .then(html => {
        document.getElementById('content').innerHTML = html;
        bindForm();
      })
      .catch(() => alert('Błąd ładowania formularza.'));
  });
});