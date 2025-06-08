document.addEventListener('DOMContentLoaded', function() {
  const btnNotif = document.getElementById('btn-notifications');
  if (!btnNotif) return;
  btnNotif.addEventListener('click', function(e) {
    e.preventDefault();
    fetch('/ajax/notifications/')
      .then(res => res.text())
      .then(html => {
        document.getElementById('content').innerHTML = html;
      })
      .catch(() => alert('Błąd ładowania powiadomień.'));
  });
});
