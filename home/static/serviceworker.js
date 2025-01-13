const CACHE_NAME = 'eg-app-cache-v3.1'; // Increment on each update
const urlsToCache = [
  '/', // Cache the homepage
  '/static/style.css?v=3.1', // Versioned CSS URL
  '/static/js/main.js', // JS file (update as needed)
  '/static/icons/icon-192x192.png', // App icon
  '/static/icons/icon-512x512.png'  // App icon
];

// Install the service worker and cache the resources
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(urlsToCache).catch((error) => {
        console.warn('Some assets failed to cache:', error);
      });
    })
  );
});

// Activate the service worker and clean up old caches
self.addEventListener('activate', (event) => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (!cacheWhitelist.includes(cacheName)) {
            return caches.delete(cacheName); // Delete old caches
          }
        })
      );
    })
  );

  // Notify clients (browser windows) that there's a new version
  self.clients.matchAll().then((clients) => {
    clients.forEach((client) => {
      client.postMessage('new-version'); // Send a message to all open pages
    });
  });

  // Ensure the new service worker takes control immediately
  self.clients.claim();
});

