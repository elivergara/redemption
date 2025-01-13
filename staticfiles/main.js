if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/serviceworker.js')  // Correct path
      .then((registration) => {
        console.log('Service Worker registered with scope:', registration.scope);
      })
      .catch((error) => {
        console.log('Service Worker registration failed:', error);
      });
  });

  // Listen for a message from the service worker
  navigator.serviceWorker.addEventListener('message', (event) => {
    if (event.data === 'new-version') {
      // Notify the user that a new version is available
      if (confirm('A new version is available. Do you want to refresh and update?')) {
        window.location.reload(); // Refresh the page to get the new version
      }
    }
  });
}

