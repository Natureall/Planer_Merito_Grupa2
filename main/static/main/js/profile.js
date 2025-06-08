document.addEventListener('DOMContentLoaded', function() {
  const btnProfile = document.getElementById('btn-profile');
  if (!btnProfile) return;
  btnProfile.addEventListener('click', function(e) {
    e.preventDefault();
    fetch('/ajax/profil/')
      .then(res => res.text())
      .then(html => {
        document.getElementById('content').innerHTML = html;
      })
      .catch(() => alert('Błąd ładowania profilu.'));
  });
});
